```
import React from 'react';
import { useLocation, useHistory } from "react-router-dom";
import { response } from '../response';

const index = 0;

function LeaderBoard({ boardList }) {
  const history = useHistory();
  const location = useLocation();
  const { rank, name, points, age } = response.list[index];
  console.log(location)

  const handleRouteRank = () => {
    history.push("/rank")
  }
  const handleRouteName = () => {
    history.push("/name")
  }
  const handleRoutePoints = () => {
    history.push("/points")
  }
  const handleRouteAge = () => {
    history.push("/age")
  }

  const filterdBoardList = React.useMemo(() => {
    if (location.pathname === "/rank") {
      boardList.sort((a, b) => {
        return  Number(a.rank) - Number(b.rank) ;
      })
      return boardList
    }
    else if (location.pathname === "/points") {
      boardList.sort((a, b) => {
        return Number(a.points) - Number(b.points);
      })
      return boardList
    }
    else if (location.pathname === "/name") {
      boardList.sort((a,b)=>a.name.localeCompare(b.name))
      console.log("boardList sorted by name ",boardList);
      
      return boardList
    }
    else if (location.pathname === "/age") {
      boardList.sort((a, b) => {
        return  Number(a.age) - Number(b.age);
      })
      return boardList
    }
    else {
      return boardList
    }

  }, [boardList,location])
  console.log("filterdBoardList",filterdBoardList);
  

  return (
    <div className="text-center mt-50">

      <div>
        <div>
          <button onClick={handleRouteRank} data-testid="route-rank" className={`${location.pathname === "/rank" ? "" : "outlined"}`} type="button">Rank</button>
          <button onClick={handleRouteName} data-testid="route-name" className={`${location.pathname === "/name" ? "" : "outlined"}`} type="button">Name</button>
          <button onClick={handleRoutePoints} data-testid="route-points" className={`${location.pathname === "/points" ? "" : "outlined"}`} type="button">Points</button>
          <button onClick={handleRouteAge} data-testid="route-age" className={`${location.pathname === "/age" ? "" : "outlined"}`} type="button">Age</button>
        </div>
      </div>

      <div className="card mx-auto pb-20 mb-30" style={{ width: '50%' }}>
        <table className="mt-50" data-testid="app-table">
          <thead>
            <tr>
              <th>Rank</th>
              <th>Name</th>
              <th className="numeric">Points</th>
              <th className="numeric">Age</th>
            </tr>
          </thead>
          <tbody data-testid="app-tbody">
            {/* <tr key={rank}>
							<td data-testid={`rank-${index}`}>{rank}</td>
							<td data-testid={`name-${index}`}>{name}</td>
							<td data-testid={`points-${index}`} className="numeric">{points}</td>
							<td data-testid={`age-${index}`} className="numeric">{age}</td>
						</tr> */}
            {
              filterdBoardList &&
              filterdBoardList.map((board, index) => {
                return (
                  <tr key={index}>
                    <td data-testid={`rank-${index}`}>{board.rank}</td>
                    <td data-testid={`name-${index}`}>{board.name}</td>
                    <td data-testid={`points-${index}`} className="numeric">{board.points}</td>
                    <td data-testid={`age-${index}`} className="numeric">{board.age}</td>
                  </tr>
                )
              })
            }
          </tbody>
        </table>
      </div>

    </div>
  );
}

export default LeaderBoard;

```