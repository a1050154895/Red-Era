
# game/audio.rpy

# ==========================================
# 音频定义 (Audio Definitions)
# ==========================================

# 音乐 (Music)
# ------------------------------------------
# 历史线 BGM
define audio.bgm_history_epic = "audio/music/history_epic.wav" # 宏大叙事
define audio.bgm_history_sad = "audio/music/history_sad.wav"   # 悲壮
define audio.bgm_history_tension = "audio/music/history_tension.wav" # 紧张

# 蓝线 BGM (Cyberpunk / Neon)
define audio.bgm_blue_cyber = "audio/music/blue_cyber.wav"
define audio.bgm_blue_glitch = "audio/music/blue_glitch.wav"

# 赤色线 BGM (Soviet / Industrial)
define audio.bgm_red_march = "audio/music/red_march.wav"
define audio.bgm_red_space = "audio/music/red_space.wav"

# 音效 (SFX)
# ------------------------------------------
define audio.sfx_typewriter = "audio/sfx/typewriter.wav"
define audio.sfx_explosion = "audio/sfx/explosion.wav"
define audio.sfx_rain = "audio/sfx/rain.wav"
define audio.sfx_glitch = "audio/sfx/glitch.wav"
define audio.sfx_crowd = "audio/sfx/crowd.wav"

# ==========================================
# 音频函数 (Audio Functions)
# ==========================================
init python:
    def play_music(music_file, fade=1.0):
        renpy.music.play(music_file, fadeout=fade, fadein=fade, loop=True)

    def play_sfx(sfx_file):
        renpy.sound.play(sfx_file)
