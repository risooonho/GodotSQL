
def can_build(plat):
	return plat == "android"

def configure(env):
	if env["platform"] == "android":
		env.android_add_java_dir("android");
		env.android_add_to_manifest("android/AndroidManifestChunk.xml")
