# Ordered Dict

This one was simple, the attention goes to the input, during the spliting. Some products
are composed by more than one word, so we have to take the price as the last element, then we need to
join the remaining array to create the product key for the dict. Then I do a simple check in the key, if
it is present I just sum with the existing value.
