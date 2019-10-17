

def subdomain(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

def read_domain(lst_a, list_b):
    #read_domain(d_names, p_zones)

    #return [i for i, x in enumerate(lst) if x == item]
    map_domain = {}
    print (lst_a)
    print (list_b)
    list_total = []
    #-----------------
    for x in range(len(lst_a)):

        list_domain = []
        list_domain.append(lst_a[x])

        if lst_a[x] not in list_total:

            list_total.append(lst_a[x])

            for i in subdomain(list_b, lst_a[x]):
                list_domain.append(lst_a[i])
                list_total.append(lst_a[i])

            map_domain.update({lst_a[x]: list_domain})

    print (map_domain)

    return map_domain