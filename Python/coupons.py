coupons = {
    flashsale20: 0.2
    newcomer10: 0.1,
}

coupon = input('Enter your coupon code: ').lower()
total = 100

if coupon in coupons:
    discount = coupon[coupons]
    total -= total * discount
    print(f'Your total cost is total')
else:
    print(f'Your total cost is {total})
