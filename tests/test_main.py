"""
Tests for Voynich Manuscript Decoder
"""

import pytest
from voynich_manuscript_decoder import VoynichManuscriptDecoder


@pytest.fixture
def system():
    """Create system instance for tests"""
    return VoynichManuscriptDecoder()


def test_initialization(system):
    """Test system initialization"""
    assert system.version == "3.0.0"
    assert system.status == "Academic Publication"


def test_process(system):
    """Test process function"""
    result = system.process({"test": "input"})
    
    assert result["status"] == "success"
    assert result["project"] == "Voynich Manuscript Decoder"
    assert result["version"] == "3.0.0"


def test_info(system):
    """Test get_info function"""
    info = system.get_info()
    
    assert info["name"] == "Voynich Manuscript Decoder"
    assert info["version"] == "3.0.0"
    assert info["type"] == "nlp"


@pytest.mark.asyncio
async def test_async_process(system):
    """Test async process"""
    result = await system.process_async({"test": "async"})
    assert result["status"] == "success"
