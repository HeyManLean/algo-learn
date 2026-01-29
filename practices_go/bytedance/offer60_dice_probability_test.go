package bytedance

import (
	"math"
	"testing"
)

func TestDicesProbability(t *testing.T) {
	tests := []struct {
		name string
		n    int
		want []float64
	}{
		{
			name: "1个骰子",
			n:    1,
			want: []float64{0.16667, 0.16667, 0.16667, 0.16667, 0.16667, 0.16667},
		},
		{
			name: "2个骰子",
			n:    2,
			want: []float64{0.02778, 0.05556, 0.08333, 0.11111, 0.13889, 0.16667, 0.13889, 0.11111, 0.08333, 0.05556, 0.02778},
		},
		{
			name: "3个骰子",
			n:    3,
			want: []float64{0.00463, 0.01389, 0.02778, 0.04630, 0.06944, 0.09722, 0.11574, 0.12500, 0.12500, 0.11574, 0.09722, 0.06944, 0.04630, 0.02778, 0.01389, 0.00463},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := statisticsProbability(tt.n)
			if len(got) != len(tt.want) {
				t.Errorf("dicesProbability() 返回长度 = %v, 期望长度 %v", len(got), len(tt.want))
				return
			}
			for i := range got {
				if math.Abs(got[i]-tt.want[i]) > 0.00001 {
					t.Errorf("dicesProbability()[%d] = %v, 期望 %v", i, got[i], tt.want[i])
				}
			}
		})
	}
}
