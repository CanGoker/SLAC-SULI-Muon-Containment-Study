def plot_segments(input_file, numID,  output_file):
        """
        produce a single 3D plot of the segments
        in the input TG4Event
        """
        segments = input_file['segments']
        event_segments = segments[segments['eventID'] == numID]
        import matplotlib.pyplot as plt

        def color_by_PID(pid):
            known_pids = {11: 'blue',
                          -11: 'green',
                          13: 'orange',
                          22: 'yellow',
                          2112: 'cyan',
                          }
            if pid in known_pids.keys():
                return known_pids[pid]
            else:
                return 'gray'

        seen_pids = []
        fig = plt.figure()
        ax = fig.add_subplot(111, projection = '3d')

        for segment in event_segments:
            segment_pid = segment['pdgId']
            if segment_pid not in seen_pids:
                seen_pids.append(segment_pid)
            ax.plot((segment['x_start'],
                     segment['x_end']),
                    (segment['y_start'],
                     segment['y_end']),
                    (segment['z_start'],
                     segment['z_end']),
                    color = color_by_PID(segment_pid)
                    )
        plt.savefig(output_file)


def plot_segmentx(input_file, numID,  output_file):
        """
        produce a single 3D plot of the segments
        in the input TG4Event
        """
        segments = input_file['segments']
        event_segments = segments[segments['eventID'] == numID]
        import matplotlib.pyplot as plt

        def color_by_PID(pid):
            known_pids = {11: 'blue',
                          -11: 'blue',
                          211: 'green',
                          -211: 'green',
                          13: 'orange',
                          -13: 'orange',
                          22: 'yellow',
                          2112: 'cyan',
                          2212: 'black',
                          }
            if pid in known_pids.keys():
                return known_pids[pid]
            else:
                return 'gray'

        seen_pids = []
        fig = plt.figure()
        ax = fig.add_subplot(111)

        for segment in event_segments:
            segment_pid = segment['pdgId']
            if segment_pid not in seen_pids:
                seen_pids.append(segment_pid)
            ax.plot(
                    (segment['y_start'],
                     segment['y_end']),
                    (segment['z_start'],
                     segment['z_end']),
                    color = color_by_PID(segment_pid)
                    )
        ax.vlines(
            x=min(event_segments['y_start']),
            ymin=min(event_segments['z_start']),
            ymax=min(event_segments['z_start']) + 3000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
        ax.vlines(
            x=min(event_segments['y_start']) + 7000,
            ymin=min(event_segments['z_start']),
            ymax=min(event_segments['z_start']) + 3000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
        ax.hlines(
            y=min(event_segments['z_start']),
            xmin=min(event_segments['y_start']),
            xmax=min(event_segments['y_start']) + 7000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
        ax.hlines(
            y=min(event_segments['z_start']) + 3000,
            xmin=min(event_segments['y_start']),
            xmax=min(event_segments['y_start']) + 7000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
        ax.set_title('ND X Projection, Event'+str(numID))
        ax.set_xlabel('Y')
        ax.set_ylabel('Z')
        plt.savefig(output_file)


def plot_segmenty(input_file, numID,  output_file):
        """
        produce a single 3D plot of the segments
        in the input TG4Event
        """
        segments = input_file['segments']
        event_segments = segments[segments['eventID'] == numID]
        import matplotlib.pyplot as plt

        def color_by_PID(pid):
            known_pids = {11: 'blue',
                          -11: 'blue',
                          211: 'green',
                          -211: 'green',
                          13: 'orange',
                          -13: 'orange',
                          22: 'yellow',
                          2112: 'cyan',
                          2212: 'black',
                          }

            if pid in known_pids.keys():
                return known_pids[pid]
            else:
                return 'gray'

        seen_pids = []
        fig = plt.figure()
        ax = fig.add_subplot(111)

        for segment in event_segments:
            segment_pid = segment['pdgId']
            if segment_pid not in seen_pids:
                seen_pids.append(segment_pid)
            ax.plot(
                    (segment['x_start'],
                     segment['x_end']),
                    (segment['z_start'],
                     segment['z_end']),
                    color = color_by_PID(segment_pid)
                    )
        ax.vlines(
            x=min(event_segments['x_start']),
            ymin=min(event_segments['z_start']),
            ymax=min(event_segments['z_start']) + 3000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
        ax.vlines(
            x=min(event_segments['x_start']) + 5000,
            ymin=min(event_segments['z_start']),
            ymax=min(event_segments['z_start']) + 3000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
        ax.hlines(
            y=min(event_segments['z_start']),
            xmin=min(event_segments['x_start']),
            xmax=min(event_segments['x_start']) + 5000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
        ax.hlines(
            y=min(event_segments['z_start']) + 3000,
            xmin=min(event_segments['x_start']),
            xmax=min(event_segments['x_start']) + 5000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
        ax.set_title('ND Y Projection, Event'+str(numID))
        ax.set_xlabel('X (beam direction)')
        ax.set_ylabel('Z')
        plt.savefig(output_file)

def plot_segmentz(input_file, numID,  output_file):
        """
        produce a single 3D plot of the segments
        in the input TG4Event
        """
        segments = input_file['segments']
        event_segments = segments[segments['eventID'] == numID]
        import matplotlib.pyplot as plt

        def color_by_PID(pid):
            known_pids = {11: 'blue',
                          -11: 'blue',
                          211: 'green',
                          -211: 'green',
                          13: 'orange',
                          -13: 'orange',
                          22: 'yellow',
                          2112: 'cyan',
                          2212: 'black',
                          }

            if pid in known_pids.keys():
                return known_pids[pid]
            else:
                return 'gray'

        seen_pids = []
        fig = plt.figure()
        ax = fig.add_subplot(111)

        for segment in event_segments:
            segment_pid = segment['pdgId']
            if segment_pid not in seen_pids:
                seen_pids.append(segment_pid)
            ax.plot(
                    (segment['x_start'],
                     segment['x_end']),
                    (segment['y_start'],
                     segment['y_end']),
                    color = color_by_PID(segment_pid)
                    )
        ax.vlines(
            x=min(event_segments['x_start']),
            ymin=min(event_segments['y_start']),
            ymax=min(event_segments['y_start']) + 7000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
        ax.vlines(
            x=min(event_segments['x_start']) + 5000,
            ymin=min(event_segments['y_start']),
            ymax=min(event_segments['y_start']) + 7000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
       ax.hlines(
            y=min(event_segments['y_start']),
            xmin=min(event_segments['x_start']),
            xmax=min(event_segments['x_start']) + 5000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
        ax.hlines(
            y=min(event_segments['y_start']) + 7000,
            xmin=min(event_segments['x_start']),
            xmax=min(event_segments['x_start']) + 5000,
            colors='red',                # color of the vertical line
            linestyles='solid',           # style of the vertical line (optional)
            linewidth=1                    # width of the vertical line (optional)
                )
        ax.set_title('ND Z Projection, Event'+str(numID))
        ax.set_xlabel('X (beam direction)')         
        ax.set_ylabel('Y')
        plt.savefig(output_file)

