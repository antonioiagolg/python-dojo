# Time delta

This is a interesting challenge. the first thing I had to tackle was to find the proper timezone object, based on the last part of the datetime
string. To find the timezone, we need a time delta. The last part of the string has the pattern `-0400` or `+0940` where the first digit half
correspond to the hours and the second half corresponds to the minutes. Breaking down this info we can have the timedelta.

With the timedelta, we can create a timezone object, and with the timezone we can create the datetime objects to perform the substract calculation.

The subtract will generate a timedelta, and we can fetch the seconds from it.
