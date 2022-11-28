# использвал прокси-класс с мьютексом для обеспечения выполнения лишь один раз

from threading import Thread, Lock
from time import sleep


class YoutubeDownloader:
    def download_video(self, url: str) -> Thread:
        process = Thread(target=self._download, args=(5,), name=url)
        process.start()
        return process

    @staticmethod
    def _download(secs: float) -> None:
        sleep(secs)


def client_code(downloader: YoutubeDownloader, url: str) -> None:
    process = downloader.download_video(url)
    process.join()
    print(f"Video was successfully downloaded: {url}")

class SingleDownloader(YoutubeDownloader):
    def __init__(self):
        self._url_to_result = {}
        self._lock = Lock()

    def download_video(self, url: str) -> Thread:
        self._lock.acquire()
        if url not in self._url_to_result:
            result = super().download_video(url)
            self._url_to_result[url] = result
        self._lock.release()
        return self._url_to_result[url]


if __name__ == "__main__":
    downloader = SingleDownloader()

    def download_video(url: str) -> None:
        client_code(downloader, url)

    print("Start downloading video_1 (I)")
    process_1 = Thread(target=download_video, args=("video_1",))
    process_1.start()

    sleep(3)

    print("Start downloading video_1 (II)")
    process_2 = Thread(target=download_video, args=("video_1",))
    process_2.start()

    print("If you see next two lines not simultaneously - something wrong")