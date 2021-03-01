ds_bath = plotADCP(ds,
                 inc=2,
                 dlat=1,dlon=2,
                 bins=v,binb=v+dz,
                 t1=pd.to_datetime(df_log.first().iloc[j,0]  + ' ' + df_log.first().iloc[j,1]),
                 t2=pd.to_datetime(df_log.last().iloc[ j,3]  + ' ' + df_log.last().iloc[ j,4]),
                 resample='30min',
                 res='h',
                 scale=3,
                 vmin=0.,
                 vmax=.6,
                 name=n,
                 ax=ax)

        fig.savefig("%s_%s_ADCP_%s_%s_bins_%s_to_%s.png" %(thisStation,n,ds.sonar,ds.time[0].dt.strftime("%d%b%Y%H%M%S").values.tolist(),v,v+dz),bbox_inches='tight')