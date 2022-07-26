# CONDITIONAL DEBUGGING (with reference to IntelliJ ide)

# above is a debugging feature where conditions can be attached to the created breakpoints
# the feature is available in most IDEs in some forms though missing in IDLE
# Steps:
# click on the code line counting pane to create a break point
# right-click the break point to add a condition

# continuing with the hi-lo game example:

low = 1
high = 1000
print("please think of a no. between {} and {}"
      .format(high, low))
input("please hit enter")
guesses = 1
while low != high:  # 1) created a break point with condition: low == high
    # the debugger will stop at the breakpoint as soon as the condition is met,
    # loop-else block executed
    guess = low + (high-low)//2
    hi_lo = input("my guess is {} should i guess high or low"
                  "enter either h, l or c respectively"
                  .format(guess)).casefold()
    if hi_lo == "h":
        low = guess + 1
    elif hi_lo == "l":
        high = guess - 1
    elif hi_lo == "c":
        print("thank you, it took us {} attempts to figure out"
              .format(guesses))
        break  # 2) after testing and removing 1 create a normal break point here without condition
        # this time loop-else block will not be executed
    else:
        print("please enter h, l or c")
    guesses += 1
else:
    print("we've guessed it, the no. is {}"
          .format(low))
    print("thank you, it took us {} attempts to figure out"
          .format(guesses))
