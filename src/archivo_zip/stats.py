
"""Compression statistics utilities."""

from dataclasses import dataclass


@dataclass
class CompressionStats:
    """Store statistics for a compression operation."""

    files_count: int
    original_size: int
    compressed_size: int
    elapsed_time: float

    @property
    def saved_bytes(self) -> int:
        """Return the number of bytes saved by compression."""
        return max(0, self.original_size - self.compressed_size)

    @property
    def compression_ratio(self) -> float:
        """Return the percentage of space saved."""
        if self.original_size == 0:
            return 0.0

        return (self.saved_bytes / self.original_size) * 100
