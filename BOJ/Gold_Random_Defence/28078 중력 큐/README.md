<p>$\huge{\large{\color{#dfc901}Gold 5}}$</p>

<img width="506" height="308" alt="image" src="https://github.com/user-attachments/assets/f7837dba-f402-443e-890b-c44b96c0357a" />
<img width="470" height="300" alt="image" src="https://github.com/user-attachments/assets/5013a4ef-af45-4995-b7b9-1a34bdd18ff2" />


큐가 회전할 수 있고 큐 안에는 가림막과 공이 있다. 가림막은 중력의 영향을 안받고 공은 중력의 영향을 받는다 한다.

일단 문제에서 중요하게 봐야할 점은 큐의 앞과 뒤가 정해져있다는 것이다. 모든 push연산은 큐의 뒤에 삽입하고 모든 pop연산은 큐의 앞을 꺼낸다.

그 말인즉슨 큐가 뒤집혀도 push와 pop은 동일한 곳에 일관되게 해야한다.

큐의 형태가 뒤--앞, 앞--뒤 두가지 경우가 있다고 하자. 여기서 push를 하게 된다면 1번째 경우에는 left에 삽입하고 2번째 경우에는 right에 삽입하는 것이 아니다.

둘다 일관되게 left자리에 삽입해야 한다. 큐가 뒤집힌 것은 실제로 컴퓨터에서 반영하기 않기 때문이다. 큐를 직접 뒤집으면 시간복잡도가 O(N^2)으로 통과되지 못할 것이다.

따라서 큐를 직접 뒤집지 않고 뒤집혔다는 것을 알리는 수단이 필요하다.

큐의 형태는 총 4개가 될 수 있다. (0도 회전, 90도 회전, 180도 회전, 270도 회전)

0도 회전일때는 뒤--앞 형태의 큐 일것이다. 180도 회전일때는 앞--뒤 형태일 것이다. 그렇다면 0도, 180도 일때는 자료구조에서 left에 삽입하고 right를 pop하는 연산을 해주면 된다.

90도, 270도일때는 세로 형태이기 때문에 떨어지는 공이 존재할 수 있다. 뒤집었을 때 가림막보다 아래에 있는 공을 떨어뜨리는 연산을 해주면 된다.

90도 일때는 큐의 앞이 아래에 있을 것이다. 그러면 이 경우에는 가림막이 나올때까지 right를 pop해주면 될 것이다.

270도 일때는 큐의 뒤가 아래에 있을 것이다. 이 경우에는 가림막이 나올때까지 left를 pop해주면 될 것이다.

left, right 어디서나 pop해야하므로 덱 자료구조를 쓰면 된다.

구현을 하다가 주의해야할 점이 있다.

1. 큐가 세로이고 큐의 아래쪽이 앞이라면 큐가 존재한다 했을 때 큐의 맨 앞은 무조건 가림막일 것이고 그 가림막을 빼면 공이 떨어질 수 있다.

2. 큐가 세로이고 큐의 아래쪽이 뒤라면 공을 넣는 경우 공이 다시 떨어진다.

3. 큐가 세로인데 비어있을 시 공을 넣으면 공은 그대로 떨어진다.

이것들을 고려하고 그냥 구현만 하면 될 것이다.
