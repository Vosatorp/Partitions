import typing as tp
import json

def check(Title: str,
          Points: tp.Dict[str, tp.Tuple[float, float]],
          Omega: tp.Tuple[str],
          Partition: tp.List[tp.Tuple[str]]) -> None:
    """
    The function takes the name of the partition(Title),
    a list of used points(Points), a tire(Omega),
    and array(Partition) containing the polygons of the partition.

    It is assumed, that the points of Omega and Parts of Partition
    are given in the counterclockwise order.
    """

    dist = lambda A, B: abs(complex(*Points[A]) - complex(*Points[B]))
    cross_product = lambda A, B: A[0] * B[1] - A[1] * B[0]

    def get_diameter(Part: tp.Tuple[str]) -> float:
        """
        Returns the diameter of the polygon that the given part is
        """
        res = 0
        for A in Part:
            for B in Part:
                res = max(res, dist(A, B))
        return res

    def check_diameters():
        """
        Outputs the diameters of all parts, counts
        and returns the maximum diameter among all parts.
        """
        max_diam = 0
        for Part in Partition:
            cur_diam = get_diameter(Part)
            max_diam = max(max_diam, cur_diam)
            # print('diameter:', cur_diam)
            # uncomment the line if you want to see the diameter of each part
        print('maximum of diameters:', max_diam)
        return max_diam

    def get_area(Part: tp.Tuple[str]) -> float:
        res = 0
        for i in range(len(Part)):
            res += cross_product(Points[Part[i]], Points[Part[i - 1]])
        return abs(res) / 2

    def check_sum_area() -> bool:
        """
        Calculates the area of all the parts
        and checks that their sum is equal to the area of Omega.
        """
        eps = 1e-9
        total_area = sum(get_area(Part) for Part in Partition)
        omega_area = get_area(Omega)
        print('total area:', total_area)
        print('area of Omega:', omega_area)
        return abs(total_area - omega_area) < eps

    def check_any_edge_in_two() -> bool:
        """
        Checks that each edge of the partition is in exactly
        two parts if it is not on the boundary of Omega,
        and checks that it is in exactly one part
        if the edge is on the boundary.
        """
        flag = True
        for A in Points:
            for B in Points:
                if A == B:
                    continue
                cnt_AB = 0
                cnt_BA = 0
                for Part in Partition:
                    for i in range(len(Part)):
                        if (Part[i - 1], Part[i]) == (A, B):
                            cnt_AB += 1
                        elif (Part[i - 1], Part[i]) == (B, A):
                            cnt_BA += 1
                for i in range(len(Omega)):
                    if (Omega[i], Omega[i - 1]) == (A, B):
                        cnt_AB += 1
                    elif (Omega[i], Omega[i - 1]) == (B, A):
                        cnt_BA += 1
                if cnt_BA + cnt_AB > 0:
                    if not (cnt_AB == cnt_BA == 1):
                        print(cnt_AB, cnt_BA)
                        print(f'Partition failed for segment ({A}, {B})')
                        return False
        print('All edges are in exactly two parts')
        return True
    
    print('\n' + Title)
    mxdiam = check_diameters()
    flag1 = check_sum_area()
    flag2 = check_any_edge_in_two()
    if flag1 and flag2:
        print('Partition of Omega is correct')
    else:
        print('Partition is incorrect')

    return None

def read_json(file):
    """
    Reads the json file containing
    the fields Title, Points Omega and Partition.
    """
    with open(file) as json_file:
        data = json.load(json_file)
        Title = data['Title']
        raw_points = data['Points']
        Points = {key: eval(val) for key, val in raw_points.items()}
        Omega = eval(data['Omega'])
        raw_partition = data['Partition']
        Partition = [eval(polygon) for polygon in raw_partition]
    return Title, Points, Omega, Partition

check(*read_json('d5_omega2.json'))
check(*read_json('d5_omega11.json'))
check(*read_json('d5_omega121.json'))
check(*read_json('d5_omega123.json'))
check(*read_json('d11_omega2.json'))
check(*read_json('d13_omega2.json'))
check(*read_json('d15_omega2.json'))
check(*read_json('d16_omega6.json'))
check(*read_json('d17_omega2.json'))
check(*read_json('d18_omega6.json'))
check(*read_json('d21_omega2.json'))
check(*read_json('d22_omega2.json'))
check(*read_json('d24_omega61.json'))
check(*read_json('d24_omega62.json'))