import os
APPNAME = "script.module.pycountry"
VERSION = "17.1.8"

out = "build"


def configure(ctx):
    ctx.check_waf_version(mini='1.9.7')


def build(bld):
    streamlink_src = bld.path.make_node("pycountry/src/")
    bld(rule='cp -r ${SRC} ${TGT}',
        source=streamlink_src.make_node("pycountry/"),
        target=bld.path.get_bld().make_node("lib/pycountry/"))

    bld(features="subst", source="addon.xml.in", target="addon.xml",
        APPNAME=APPNAME, VERSION=VERSION)

    for f in ['LICENSE', 'changelog.txt', 'icon.png']:
        bld(rule='cp -r ${SRC} ${TGT}', source=bld.path.make_node(f), target=bld.path.get_bld().make_node(f))


def dist(ctx):
    ctx.algo = "zip"
    ctx.base_path = ctx.path.make_node(out)
    ctx.base_name = APPNAME  # set the base directory for the archive
    ctx.files = ctx.path.ant_glob(
        "build/**.xml build/**.md build/**.png build/LICENSE build/**.py build/lib/**/* build/lib/*"
        "build/resources/*.py  build/**/*.xml")
    ctx.arch_name = "{0}-{1}.{2}".format(APPNAME, VERSION, ctx.ext_algo.get(ctx.algo, ctx.algo))
