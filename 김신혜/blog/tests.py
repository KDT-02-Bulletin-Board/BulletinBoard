from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.
# 하나의 TestCase에서 기본설정은 setUp에서 정의
class TextView(TestCase):
    def setUp(self):
        self.client = Client() # Client함수를 사용하겠다는 내용
        
    def test_post_list(self):
        # 포스트 목록 페이지 가져옴
        response = self.client.get('/blog/')
        # 페이지가 정상적으로 로드됨
        self.assertEqual(response.status_code, 200)
        # 페이지 타이틀 Blog
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, ' Blog')
        # 내비바 있음
        navbar = soup.nav
        # Blog, about_me가 내비바에 있음
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)
        
        # 게시물(post)이 하나도 없다면
        self.assertEqual(Post.objects.count(),0)
        # main area에 '아직 게시물이 없습니다'라는 문구가 나타남
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다', main_area.text)
        
        # 포스트가 2개라면
        post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World. we are the world.',
        )
        post_002 = Post.objects.create(
            title='두 번째 포스트입니다.',
            content='1등이 전부는 아니잖아요?',
        )
        self.assertEqual(Post.objects.count(), 2)
        
        # 포스트 목록 페이지를 새로고침했을 때
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)
        # main area에 포스트 2개의 제목이 존재한다.
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        # '아직 게시물이 없습니다.'라는 문구는 더 이상 나타나지 않는다.
        self.assertNotIn('아직 게시물이 없습니다', main_area.text)
        
    def test_post_detail(self):
        # Post가 하나 있다.
        post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World. We are the world.',
        )
        # 그 포스트의 url은 'blog/1/'이다.
        self.assertEqual(post_001.get_absolute_url(), '/blog/1/')
        
        # 첫 번째 포스트의 상세 페이지 테스트
        # 첫 번째 post url로 접근하면 정상적으로 작동한다(status code:200)
        response = self.client.get(post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 포스트 목록 페이지와 똑같은 내비게이션 바가 있다.
        navbar = soup.nav
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)
        
        # 첫 번째 포스트의 제목(title)이 웹 브라우저 탭 타이틀에 들어 있음
        self.assertIn(post_001.title, soup.title.text)
        
        # 첫 번째 포스트의 제목(title)이 포스트 영역(post_area)에 있음
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area')
        self.assertIn(post_001.title, post_area.text)
        
        # 첫 번째 포스트의 작성자(author)이 포스트 영역(post_area)에 있음
        # 첫 번째 포스트의 내용(content)이 포스트 영역(post_area)에 있음
        self.assertIn(post_001.content, post_area.text)
        
        