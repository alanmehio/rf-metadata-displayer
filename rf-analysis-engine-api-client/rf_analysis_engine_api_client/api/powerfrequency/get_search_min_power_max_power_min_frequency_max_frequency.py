from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data import Data
from ...types import Response


def _get_kwargs(
    min_power: float,
    max_power: float,
    min_frequency: float,
    max_frequency: float,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/search/{min_power}/{max_power}/{min_frequency}/{max_frequency}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Data]]:
    if response.status_code == 200:
        response_200 = Data.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Data]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    min_power: float,
    max_power: float,
    min_frequency: float,
    max_frequency: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Data]]:
    """Get list of powers and frequencies with their timestamps

    Args:
        min_power (float):
        max_power (float):
        min_frequency (float):
        max_frequency (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Data]]
    """

    kwargs = _get_kwargs(
        min_power=min_power,
        max_power=max_power,
        min_frequency=min_frequency,
        max_frequency=max_frequency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    min_power: float,
    max_power: float,
    min_frequency: float,
    max_frequency: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Data]]:
    """Get list of powers and frequencies with their timestamps

    Args:
        min_power (float):
        max_power (float):
        min_frequency (float):
        max_frequency (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Data]
    """

    return sync_detailed(
        min_power=min_power,
        max_power=max_power,
        min_frequency=min_frequency,
        max_frequency=max_frequency,
        client=client,
    ).parsed


async def asyncio_detailed(
    min_power: float,
    max_power: float,
    min_frequency: float,
    max_frequency: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Data]]:
    """Get list of powers and frequencies with their timestamps

    Args:
        min_power (float):
        max_power (float):
        min_frequency (float):
        max_frequency (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Data]]
    """

    kwargs = _get_kwargs(
        min_power=min_power,
        max_power=max_power,
        min_frequency=min_frequency,
        max_frequency=max_frequency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    min_power: float,
    max_power: float,
    min_frequency: float,
    max_frequency: float,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Data]]:
    """Get list of powers and frequencies with their timestamps

    Args:
        min_power (float):
        max_power (float):
        min_frequency (float):
        max_frequency (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Data]
    """

    return (
        await asyncio_detailed(
            min_power=min_power,
            max_power=max_power,
            min_frequency=min_frequency,
            max_frequency=max_frequency,
            client=client,
        )
    ).parsed
