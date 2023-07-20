import os
import random
import moviepy.editor as mp


def get_random_video_file(folder):
    """
    Выбирает случайный видеофайл из указанной папки.

    Параметры:
        folder (str): Путь к папке с видеофайлами.

    Возвращает:
        str: Полный путь к случайно выбранному видеофайлу.
    """
    video_files = [f for f in os.listdir(folder) if f.endswith(".mp4")]
    if not video_files:
        raise ValueError(f"No video files found in folder: {folder}")
    return os.path.join(folder, random.choice(video_files))


def trim_video(file_path, duration):
    """
    Обрезает видеофайл до указанной длительности.

    Параметры:
        file_path (str): Путь к видеофайлу, который нужно обрезать.
        duration (float): Желаемая длительность обрезанного видео в секундах.

    Возвращает:
        moviepy.editor.VideoClip: Обрезанный видеофайл.
    """
    video = mp.VideoFileClip(file_path).subclip(0, duration)
    return video


def combine_videos(video1, video2):
    """
    Соединяет два видеофайла в один.

    Параметры:
        video1 (moviepy.editor.VideoClip): Первый видеофайл для объединения.
        video2 (moviepy.editor.VideoClip): Второй видеофайл для объединения.

    Возвращает:
        moviepy.editor.VideoClip: Объединенный видеофайл.
    """
    final_video = mp.concatenate_videoclips([video1, video2])
    return final_video


def add_music(video, music_file, duration):
    """
    Накладывает музыку на видеофайл.

    Параметры:
        video (moviepy.editor.VideoClip): Видеофайл, к которому нужно добавить музыку.
        music_file (str): Путь к аудиофайлу с музыкой.
        duration (float): Желаемая длительность музыки в секундах.

    Возвращает:
        moviepy.editor.VideoClip: Видеофайл с добавленной музыкой.
    """
    audio = mp.AudioFileClip(music_file).subclip(0, duration)
    video = video.set_audio(audio)
    return video


def save_result(video, output_file):
    """
    Сохраняет итоговый видеофайл.

    Параметры:
        video (moviepy.editor.VideoClip): Видеофайл, который нужно сохранить.
        output_file (str): Имя и путь для сохранения итогового видеофайла.
    """
    video.write_videofile(output_file)


def get_random_file_from_folder(folder, file_extension):
    """
    Выбирает случайный файл с указанным расширением из указанной папки.

    Параметры:
        folder (str): Путь к папке, из которой нужно выбрать файл.
        file_extension (str): Расширение файла, например, '.mp3'.

    Возвращает:
        str: Полный путь к случайно выбранному файлу.
    """
    files = [f for f in os.listdir(folder) if f.endswith(file_extension)]
    if not files:
        raise ValueError(f"No {file_extension} files found in folder: {folder}")
    return os.path.join(folder, random.choice(files))


# Остальные функции остаются без изменений

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Process video files and combine them.")
    parser.add_argument("-f1", "--folder1", type=str, required=True, help="Path to folder 1 with video files")
    parser.add_argument("-f2", "--folder2", type=str, required=True, help="Path to folder 2 with video files")
    parser.add_argument("-m", "--music_folder", type=str, required=True, help="Path to the folder with music files")
    args = parser.parse_args()

    # Step 1
    video1_file = get_random_file_from_folder(args.folder1, ".mp4")
    print(f"Selected random video file from folder 1: {video1_file}")

    # Step 2
    video2_file = get_random_file_from_folder(args.folder2, ".mp4")
    print(f"Selected random video file from folder 2: {video2_file}")

    # Step 3
    trimmed_video1 = trim_video(video1_file, duration=2)
    trimmed_video2 = trim_video(video2_file, duration=2)

    # Step 4
    music_file = get_random_file_from_folder(args.music_folder, ".mp3")
    print(f"Selected random music file: {music_file}")

    # Set music duration to 5 seconds
    music_duration = 5.0

    combined_video = combine_videos(trimmed_video1, trimmed_video2)
    video_with_music = add_music(combined_video, music_file, duration=music_duration)

    # Step 5
    output_file = "result.mp4"
    save_result(video_with_music, output_file)
    print(f"Result video saved to: {output_file}")
