from winshell import recycle_bin

bin = recycle_bin()
bin.empty(confirm=False, show_progress=False, sound=False)
