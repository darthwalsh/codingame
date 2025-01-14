import os
import pytest

from codingame.client.async_ import AsyncClient
from codingame.codingamer import CodinGamer
from codingame.exceptions import LoginRequired


@pytest.fixture(name="codingamer")
async def get_codingamer(auth_client) -> CodinGamer:
    return await auth_client.get_codingamer(
        os.environ.get("TEST_CODINGAMER_PUBLIC_HANDLE")
    )


@pytest.mark.asyncio
async def test_codingamer_avatar_and_cover_urls(client: AsyncClient):
    codingamer = await client.get_codingamer("Takos")
    assert isinstance(codingamer.avatar_url, str)
    assert isinstance(codingamer.cover_url, str)
    assert isinstance(codingamer.profile_url, str)


@pytest.mark.asyncio
async def test_codingamer_eq(client: AsyncClient, codingamer: CodinGamer):
    other_codingamer = await client.get_codingamer(
        os.environ.get("TEST_CODINGAMER_PUBLIC_HANDLE")
    )
    assert codingamer == other_codingamer


@pytest.mark.asyncio
async def test_codingamer_get_followers(codingamer: CodinGamer):
    async for follower in codingamer.get_followers():
        assert isinstance(follower, CodinGamer)


@pytest.mark.asyncio
async def test_codingamer_get_followers_error(client: AsyncClient):
    codingamer = await client.get_codingamer(
        os.environ.get("TEST_CODINGAMER_PUBLIC_HANDLE")
    )
    with pytest.raises(LoginRequired):
        next(await codingamer.get_followers())


@pytest.mark.asyncio
async def test_codingamer_get_followers_ids(codingamer: CodinGamer):
    followers_ids = await codingamer.get_followers_ids()
    assert isinstance(followers_ids, list)
    assert all(isinstance(follower_id, int) for follower_id in followers_ids)


@pytest.mark.asyncio
async def test_codingamer_get_followed(codingamer: CodinGamer):
    async for followed in codingamer.get_followed():
        assert isinstance(followed, CodinGamer)


@pytest.mark.asyncio
async def test_codingamer_get_followed_error(client: AsyncClient):
    codingamer = await client.get_codingamer(
        os.environ.get("TEST_CODINGAMER_PUBLIC_HANDLE")
    )
    with pytest.raises(LoginRequired):
        next(await codingamer.get_followed())


@pytest.mark.asyncio
async def test_codingamer_get_followed_ids(codingamer: CodinGamer):
    followed_ids = await codingamer.get_followed_ids()
    assert isinstance(followed_ids, list)
    assert all(isinstance(followed_id, int) for followed_id in followed_ids)


@pytest.mark.asyncio
async def test_codingamer_get_clash_of_code_rank(codingamer: CodinGamer):
    rank = await codingamer.get_clash_of_code_rank()
    assert isinstance(rank, int)
