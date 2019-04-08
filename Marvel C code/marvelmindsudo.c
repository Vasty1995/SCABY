void printStationaryBeaconsPositionsFromMarvelmindHedge (struct MarvelmindHedge * hedge,
                                                         bool onlyNew)
{struct StationaryBeaconsPositions positions;
  double xm,ym,zm;

    getStationaryBeaconsPositionsFromMarvelmindHedge(hedge, &positions);

    if (positions.updated || (!onlyNew))
    {uint8_t i;
     uint8_t n= hedge->positionsBeacons.numBeacons;
     struct StationaryBeaconPosition *b;

        for(i=0;i<n;i++)
        {
            b= &positions.beacons[i];
            xm= ((double) b->x)/1000.0;
            ym= ((double) b->y)/1000.0;
            zm= ((double) b->z)/1000.0;
            if (positions.beacons[i].highResolution)
            {
                printf ("Stationary beacon: address: %d, X: %.3f, Y: %.3f, Z: %.3f \n",
                            b->address,xm, ym, zm);
            } else
            {
                printf ("Stationary beacon: address: %d, X: %.2f, Y: %.2f, Z: %.2f \n",
                            b->address,xm, ym, zm);
            }
        }

        hedge->positionsBeacons.updated= false;
    }
}
