from src.wikipedia_api import client

from validators import url


JSON = client.get_random_summary_page_as_json()


class TestThumbnail:
    def test_thumbnail_source(self):
        assert url(JSON["thumbnail"]["source"])


class TestOriginalimage:
    def test_originalimage_source(self):
        assert url(JSON["originalimage"]["source"])


class TestContentUrls:
    def test_desktop_page(self):
        assert url(JSON["content_urls"]["desktop"]["page"])

    def test_desktop_revisions(self):
        assert url(JSON["content_urls"]["desktop"]["revisions"])

    def test_desktop_edit(self):
        assert url(JSON["content_urls"]["desktop"]["edit"])

    def test_desktop_talk(self):
        assert url(JSON["content_urls"]["desktop"]["talk"])

    def test_mobile_page(self):
        assert url(JSON["content_urls"]["mobile"]["page"])

    def test_mobile_revisions(self):
        assert url(JSON["content_urls"]["mobile"]["revisions"])

    def test_mobile_edit(self):
        assert url(JSON["content_urls"]["mobile"]["edit"])

    def test_mobile_talk(self):
        assert url(JSON["content_urls"]["mobile"]["talk"])
