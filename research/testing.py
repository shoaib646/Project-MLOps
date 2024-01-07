def rotate_array(nums, k):
    print(nums)
    k = k % len(nums)
    print(k)

    # Rotate the array using slicing
    rotated_array = nums[-k:] + nums[:-k]

    return rotated_array

# Example usage:
original_array = [1, 2, 3, 4, 5]
k_steps = 4
result = rotate_array(original_array, k_steps)

print("Original Array:", original_array)
print(f"Rotated to the right by {k_steps} steps:", result)
