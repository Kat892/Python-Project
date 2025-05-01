List=[1,2,3,4,5,6,7,8,9,10]
print("Original list: ",List)
start=int(input())
end=int(input())
Extracted_elements=List[start:end]
print("Extracted five elements: ",Extracted_elements)
Reversed=list(reversed(Extracted_elements))
print("Reversed extracted elements: ",Reversed)