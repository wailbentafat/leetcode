package main
import (
	"fmt"
	"sort"
)
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    var nums []int
    nums=append(nums1,nums2...)
	
	sort.Ints(nums)

	if len(nums)%2==0{
		return float64(nums[len(nums)/2-1]+nums[len(nums)/2])/2
	}else{
		return float64(nums[len(nums)/2])
	}

}
func main(){
	fmt.Println(findMedianSortedArrays([]int{1,2},[]int{3,4}))
}