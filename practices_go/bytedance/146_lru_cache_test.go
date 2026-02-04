package bytedance

import (
	"testing"
)

func TestLRUCache(t *testing.T) {
	t.Run("示例", func(t *testing.T) {
		cache := Constructor(2)

		cache.Put(1, 1) // 缓存 {1=1}
		cache.Put(2, 2) // 缓存 {1=1, 2=2}

		if got := cache.Get(1); got != 1 {
			t.Errorf("Get(1) = %d, want 1", got)
		}

		cache.Put(3, 3) // 驱逐 2，缓存 {1=1, 3=3}

		if got := cache.Get(2); got != -1 {
			t.Errorf("Get(2) = %d, want -1 (未找到)", got)
		}

		cache.Put(4, 4) // 驱逐 1，缓存 {3=3, 4=4}

		if got := cache.Get(1); got != -1 {
			t.Errorf("Get(1) = %d, want -1 (未找到)", got)
		}
		if got := cache.Get(3); got != 3 {
			t.Errorf("Get(3) = %d, want 3", got)
		}
		if got := cache.Get(4); got != 4 {
			t.Errorf("Get(4) = %d, want 4", got)
		}
	})
}

func TestLRUCache_CapacityOne(t *testing.T) {
	cache := Constructor(1)
	cache.Put(1, 1)
	if got := cache.Get(1); got != 1 {
		t.Errorf("Get(1) = %d, want 1", got)
	}
	cache.Put(2, 2) // 驱逐 1
	if got := cache.Get(1); got != -1 {
		t.Errorf("Get(1) = %d, want -1", got)
	}
	if got := cache.Get(2); got != 2 {
		t.Errorf("Get(2) = %d, want 2", got)
	}
}

func TestLRUCache_UpdateExisting(t *testing.T) {
	cache := Constructor(2)
	cache.Put(1, 1)
	cache.Put(1, 10) // 更新已存在的 key
	if got := cache.Get(1); got != 10 {
		t.Errorf("Get(1) = %d, want 10", got)
	}
}

func TestLRUCache_GetMovesToRecent(t *testing.T) {
	cache := Constructor(2)
	cache.Put(1, 1)
	cache.Put(2, 2)
	_ = cache.Get(1)   // 1 变为最近使用
	cache.Put(3, 3)    // 应驱逐 2
	if got := cache.Get(2); got != -1 {
		t.Errorf("Get(2) = %d, want -1 (2 应被驱逐)", got)
	}
	if got := cache.Get(1); got != 1 {
		t.Errorf("Get(1) = %d, want 1", got)
	}
	if got := cache.Get(3); got != 3 {
		t.Errorf("Get(3) = %d, want 3", got)
	}
}
