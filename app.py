import customtkinter as ctk
import oracledb as cx_Oracle 
import tkinter as tk
from tkinter import ttk  # Importamos ttk para usar Treeview
import tkinter.messagebox as messagebox
from datetime import datetime

# Configuración de la conexión a la base de datos Oracle
def get_connection():
    try:
        dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='XEPDB1')  # Ajusta según tu configuración
        connection = cx_Oracle.connect(user='gr3', password='gr3', dsn=dsn_tns)
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

# Clases Modelo

class Cliente:
    def __init__(self, cliente_id=None, nombre='', apellido='', email='', telefono=''):
        self.cliente_id = cliente_id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            if self.cliente_id is None:
                cursor.execute("""
                    INSERT INTO Clientes (nombre, apellido, email, telefono)
                    VALUES (:1, :2, :3, :4)
                """, (self.nombre, self.apellido, self.email, self.telefono))
            else:
                cursor.execute("""
                    UPDATE Clientes SET nombre=:1, apellido=:2, email=:3, telefono=:4
                    WHERE cliente_id=:5
                """, (self.nombre, self.apellido, self.email, self.telefono, self.cliente_id))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al guardar el cliente: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    def delete(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Clientes WHERE cliente_id=:1", (self.cliente_id,))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al eliminar el cliente: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_all():
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Clientes ORDER BY cliente_id")
            rows = cursor.fetchall()
            clientes = [Cliente(*row) for row in rows]
            return clientes
        except Exception as e:
            print(f"Error al obtener los clientes: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

class Mesa:
    def __init__(self, mesa_id=None, numero_mesa=0, capacidad=0, ubicacion=''):
        self.mesa_id = mesa_id
        self.numero_mesa = numero_mesa
        self.capacidad = capacidad
        self.ubicacion = ubicacion

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            if self.mesa_id is None:
                cursor.execute("""
                    INSERT INTO Mesas (numero_mesa, capacidad, ubicacion)
                    VALUES (:1, :2, :3)
                """, (self.numero_mesa, self.capacidad, self.ubicacion))
            else:
                cursor.execute("""
                    UPDATE Mesas SET numero_mesa=:1, capacidad=:2, ubicacion=:3
                    WHERE mesa_id=:4
                """, (self.numero_mesa, self.capacidad, self.ubicacion, self.mesa_id))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al guardar la mesa: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    def delete(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Mesas WHERE mesa_id=:1", (self.mesa_id,))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al eliminar la mesa: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_all():
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Mesas ORDER BY mesa_id")
            rows = cursor.fetchall()
            mesas = [Mesa(*row) for row in rows]
            return mesas
        except Exception as e:
            print(f"Error al obtener las mesas: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

class Empleado:
    def __init__(self, empleado_id=None, nombre='', apellido='', cargo=''):
        self.empleado_id = empleado_id
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            if self.empleado_id is None:
                cursor.execute("""
                    INSERT INTO Empleados (nombre, apellido, cargo)
                    VALUES (:1, :2, :3)
                """, (self.nombre, self.apellido, self.cargo))
            else:
                cursor.execute("""
                    UPDATE Empleados SET nombre=:1, apellido=:2, cargo=:3
                    WHERE empleado_id=:4
                """, (self.nombre, self.apellido, self.cargo, self.empleado_id))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al guardar el empleado: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    def delete(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Empleados WHERE empleado_id=:1", (self.empleado_id,))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al eliminar el empleado: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_all():
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Empleados ORDER BY empleado_id")
            rows = cursor.fetchall()
            empleados = [Empleado(*row) for row in rows]
            return empleados
        except Exception as e:
            print(f"Error al obtener los empleados: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

class Menu:
    def __init__(self, menu_id=None, nombre_plato='', descripcion='', precio=0.0):
        self.menu_id = menu_id
        self.nombre_plato = nombre_plato
        self.descripcion = descripcion
        self.precio = precio

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            if self.menu_id is None:
                cursor.execute("""
                    INSERT INTO Menus (nombre_plato, descripcion, precio)
                    VALUES (:1, :2, :3)
                """, (self.nombre_plato, self.descripcion, self.precio))
            else:
                cursor.execute("""
                    UPDATE Menus SET nombre_plato=:1, descripcion=:2, precio=:3
                    WHERE menu_id=:4
                """, (self.nombre_plato, self.descripcion, self.precio, self.menu_id))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al guardar el menú: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    def delete(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Menus WHERE menu_id=:1", (self.menu_id,))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al eliminar el menú: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_all():
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Menus ORDER BY menu_id")
            rows = cursor.fetchall()
            menus = [Menu(*row) for row in rows]
            return menus
        except Exception as e:
            print(f"Error al obtener los menús: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

class Reserva:
    def __init__(self, reserva_id=None, cliente_id=None, mesa_id=None, empleado_id=None, fecha_reserva=None, hora_reserva='', numero_personas=0):
        self.reserva_id = reserva_id
        self.cliente_id = cliente_id
        self.mesa_id = mesa_id
        self.empleado_id = empleado_id  # Nuevo campo
        self.fecha_reserva = fecha_reserva
        self.hora_reserva = hora_reserva
        self.numero_personas = numero_personas

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            # Verificar disponibilidad de la mesa
            cursor.execute("""
                SELECT COUNT(*) FROM Reservas
                WHERE mesa_id=:1 AND fecha_reserva=:2 AND hora_reserva=:3 AND reserva_id != :4
            """, (self.mesa_id, self.fecha_reserva, self.hora_reserva, self.reserva_id if self.reserva_id else -1))
            count = cursor.fetchone()[0]
            if count > 0:
                messagebox.showwarning("Advertencia", "La mesa no está disponible en esa fecha y hora.")
                return
            if self.reserva_id is None:
                cursor.execute("""
                    INSERT INTO Reservas (cliente_id, mesa_id, empleado_id, fecha_reserva, hora_reserva, numero_personas)
                    VALUES (:1, :2, :3, :4, :5, :6)
                """, (self.cliente_id, self.mesa_id, self.empleado_id, self.fecha_reserva, self.hora_reserva, self.numero_personas))
            else:
                cursor.execute("""
                    UPDATE Reservas SET cliente_id=:1, mesa_id=:2, empleado_id=:3, fecha_reserva=:4, hora_reserva=:5, numero_personas=:6
                    WHERE reserva_id=:7
                """, (self.cliente_id, self.mesa_id, self.empleado_id, self.fecha_reserva, self.hora_reserva, self.numero_personas, self.reserva_id))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al guardar la reserva: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    def delete(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Reservas WHERE reserva_id=:1", (self.reserva_id,))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al eliminar la reserva: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_all():
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT r.reserva_id,
                       c.cliente_id || ' - ' || c.nombre || ' ' || c.apellido,
                       m.mesa_id || ' - Mesa ' || m.numero_mesa,
                       e.empleado_id || ' - ' || e.nombre || ' ' || e.apellido,
                       r.fecha_reserva,
                       r.hora_reserva,
                       r.numero_personas
                FROM Reservas r
                JOIN Clientes c ON r.cliente_id = c.cliente_id
                JOIN Mesas m ON r.mesa_id = m.mesa_id
                JOIN Empleados e ON r.empleado_id = e.empleado_id
                ORDER BY r.reserva_id
            """)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(f"Error al obtener las reservas: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

class Pedido:
    def __init__(self, pedido_id=None, reserva_id=None, menu_id=None, cantidad=0):
        self.pedido_id = pedido_id
        self.reserva_id = reserva_id
        self.menu_id = menu_id
        self.cantidad = cantidad

    def save(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            if self.pedido_id is None:
                cursor.execute("""
                    INSERT INTO Pedidos (reserva_id, menu_id, cantidad)
                    VALUES (:1, :2, :3)
                """, (self.reserva_id, self.menu_id, self.cantidad))
            else:
                cursor.execute("""
                    UPDATE Pedidos SET reserva_id=:1, menu_id=:2, cantidad=:3
                    WHERE pedido_id=:4
                """, (self.reserva_id, self.menu_id, self.cantidad, self.pedido_id))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al guardar el pedido: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    def delete(self):
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Pedidos WHERE pedido_id=:1", (self.pedido_id,))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error al eliminar el pedido: {e}")
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_all():
        connection = get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT p.pedido_id, r.reserva_id || ' - ' || c.nombre || ' ' || c.apellido, m.menu_id || ' - ' || m.nombre_plato, p.cantidad
                FROM Pedidos p
                JOIN Reservas r ON p.reserva_id = r.reserva_id
                JOIN Clientes c ON r.cliente_id = c.cliente_id
                JOIN Menus m ON p.menu_id = m.menu_id
                ORDER BY p.pedido_id
            """)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(f"Error al obtener los pedidos: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

# Interfaz Gráfica con customtkinter

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Reservas de Restaurante")
        self.geometry("1000x700")
        self.create_widgets()
        self.set_theme_switcher()

    def create_widgets(self):
        self.tabview = ctk.CTkTabview(master=self)
        self.tabview.pack(fill="both", expand=True)

        # Pestaña de Clientes
        self.tabview.add("Clientes")
        self.clientes_tab = self.tabview.tab("Clientes")
        self.setup_clientes_tab()

        # Pestaña de Mesas
        self.tabview.add("Mesas")
        self.mesas_tab = self.tabview.tab("Mesas")
        self.setup_mesas_tab()

        # Pestaña de Reservas
        self.tabview.add("Reservas")
        self.reservas_tab = self.tabview.tab("Reservas")
        self.setup_reservas_tab()

        # Pestaña de Empleados
        self.tabview.add("Empleados")
        self.empleados_tab = self.tabview.tab("Empleados")
        self.setup_empleados_tab()

        # Pestaña de Menús
        self.tabview.add("Menús")
        self.menus_tab = self.tabview.tab("Menús")
        self.setup_menus_tab()

        # Pestaña de Pedidos
        self.tabview.add("Pedidos")
        self.pedidos_tab = self.tabview.tab("Pedidos")
        self.setup_pedidos_tab()

    def set_theme_switcher(self):
        switch_var = ctk.StringVar(value="Light")
        theme_switch = ctk.CTkSwitch(master=self, text="Modo Oscuro", command=self.switch_theme,
                                     variable=switch_var, onvalue="Dark", offvalue="Light")
        theme_switch.pack(pady=10)

    def switch_theme(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")

    # Métodos para Clientes
    def setup_clientes_tab(self):
        frame = ctk.CTkFrame(master=self.clientes_tab)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Campos de entrada
        form_frame = ctk.CTkFrame(master=frame)
        form_frame.pack(side="left", fill="y", padx=20)

        ctk.CTkLabel(master=form_frame, text="Nombre:").pack(pady=5)
        self.nombre_entry = ctk.CTkEntry(master=form_frame)
        self.nombre_entry.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Apellido:").pack(pady=5)
        self.apellido_entry = ctk.CTkEntry(master=form_frame)
        self.apellido_entry.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Email:").pack(pady=5)
        self.email_entry = ctk.CTkEntry(master=form_frame)
        self.email_entry.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Teléfono:").pack(pady=5)
        self.telefono_entry = ctk.CTkEntry(master=form_frame)
        self.telefono_entry.pack(pady=5)

        self.add_button = ctk.CTkButton(master=form_frame, text="Agregar Cliente", command=self.add_cliente)
        self.add_button.pack(pady=20)

        # Lista de clientes
        list_frame = ctk.CTkFrame(master=frame)
        list_frame.pack(side="right", fill="both", expand=True, padx=20)

        # Usamos ttk.Treeview en lugar de CTkTreeview
        self.clientes_tree = ttk.Treeview(master=list_frame, columns=("ID", "Nombre", "Apellido", "Email", "Teléfono"), show="headings")
        self.clientes_tree.heading("ID", text="ID")
        self.clientes_tree.heading("Nombre", text="Nombre")
        self.clientes_tree.heading("Apellido", text="Apellido")
        self.clientes_tree.heading("Email", text="Email")
        self.clientes_tree.heading("Teléfono", text="Teléfono")
        self.clientes_tree.pack(fill="both", expand=True)

        # Estilo para el Treeview (opcional)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
        style.map('Treeview', background=[('selected', '#347083')])

        # Botones de edición y eliminación
        btn_frame = ctk.CTkFrame(master=form_frame)
        btn_frame.pack(pady=10)

        self.update_button = ctk.CTkButton(master=btn_frame, text="Actualizar", command=self.update_cliente)
        self.update_button.pack(side="left", padx=5)

        self.delete_button = ctk.CTkButton(master=btn_frame, text="Eliminar", command=self.delete_cliente)
        self.delete_button.pack(side="right", padx=5)

        self.load_clientes()
        self.clientes_tree.bind("<<TreeviewSelect>>", self.on_cliente_select)

    def add_cliente(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()

        if not nombre or not apellido:
            messagebox.showwarning("Advertencia", "El nombre y apellido son obligatorios.")
            return

        cliente = Cliente(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
        try:
            cliente.save()
            messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
            self.clear_cliente_entries()
            self.load_clientes()
            self.update_reserva_comboboxes()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar el cliente:\n{e}")

    def update_cliente(self):
        selected_item = self.clientes_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un cliente para actualizar.")
            return

        cliente_id = self.clientes_tree.item(selected_item)['values'][0]
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()

        if not nombre or not apellido:
            messagebox.showwarning("Advertencia", "El nombre y apellido son obligatorios.")
            return

        cliente = Cliente(cliente_id=cliente_id, nombre=nombre, apellido=apellido, email=email, telefono=telefono)
        try:
            cliente.save()
            messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
            self.clear_cliente_entries()
            self.load_clientes()
            self.update_reserva_comboboxes()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar el cliente:\n{e}")

    def delete_cliente(self):
        selected_item = self.clientes_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un cliente para eliminar.")
            return

        cliente_id = self.clientes_tree.item(selected_item)['values'][0]
        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este cliente?")
        if confirm:
            cliente = Cliente(cliente_id=cliente_id)
            try:
                cliente.delete()
                messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
                self.clear_cliente_entries()
                self.load_clientes()
                self.update_reserva_comboboxes()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al eliminar el cliente:\n{e}")

    def on_cliente_select(self, event):
        selected_item = self.clientes_tree.focus()
        if selected_item:
            cliente_data = self.clientes_tree.item(selected_item)['values']
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, cliente_data[1])
            self.apellido_entry.delete(0, tk.END)
            self.apellido_entry.insert(0, cliente_data[2])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, cliente_data[3])
            self.telefono_entry.delete(0, tk.END)
            self.telefono_entry.insert(0, cliente_data[4])

    def clear_cliente_entries(self):
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.clientes_tree.selection_remove(self.clientes_tree.selection())

    def load_clientes(self):
        for item in self.clientes_tree.get_children():
            self.clientes_tree.delete(item)
        clientes = Cliente.get_all()
        for cliente in clientes:
            self.clientes_tree.insert('', tk.END, values=(cliente.cliente_id, cliente.nombre, cliente.apellido, cliente.email, cliente.telefono))

    # Métodos para Mesas
    def setup_mesas_tab(self):
        frame = ctk.CTkFrame(master=self.mesas_tab)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Campos de entrada
        form_frame = ctk.CTkFrame(master=frame)
        form_frame.pack(side="left", fill="y", padx=20)

        ctk.CTkLabel(master=form_frame, text="Número de Mesa:").pack(pady=5)
        self.numero_mesa_entry = ctk.CTkEntry(master=form_frame)
        self.numero_mesa_entry.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Capacidad:").pack(pady=5)
        self.capacidad_entry = ctk.CTkEntry(master=form_frame)
        self.capacidad_entry.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Ubicación:").pack(pady=5)
        self.ubicacion_entry = ctk.CTkEntry(master=form_frame)
        self.ubicacion_entry.pack(pady=5)

        self.add_mesa_button = ctk.CTkButton(master=form_frame, text="Agregar Mesa", command=self.add_mesa)
        self.add_mesa_button.pack(pady=20)

        # Lista de mesas
        list_frame = ctk.CTkFrame(master=frame)
        list_frame.pack(side="right", fill="both", expand=True, padx=20)

        self.mesas_tree = ttk.Treeview(master=list_frame, columns=("ID", "Número", "Capacidad", "Ubicación"), show="headings")
        self.mesas_tree.heading("ID", text="ID")
        self.mesas_tree.heading("Número", text="Número de Mesa")
        self.mesas_tree.heading("Capacidad", text="Capacidad")
        self.mesas_tree.heading("Ubicación", text="Ubicación")
        self.mesas_tree.pack(fill="both", expand=True)

        # Botones de edición y eliminación
        btn_frame = ctk.CTkFrame(master=form_frame)
        btn_frame.pack(pady=10)

        self.update_mesa_button = ctk.CTkButton(master=btn_frame, text="Actualizar", command=self.update_mesa)
        self.update_mesa_button.pack(side="left", padx=5)

        self.delete_mesa_button = ctk.CTkButton(master=btn_frame, text="Eliminar", command=self.delete_mesa)
        self.delete_mesa_button.pack(side="right", padx=5)

        self.load_mesas()
        self.mesas_tree.bind("<<TreeviewSelect>>", self.on_mesa_select)

    def add_mesa(self):
        numero_mesa = self.numero_mesa_entry.get()
        capacidad = self.capacidad_entry.get()
        ubicacion = self.ubicacion_entry.get()

        if not numero_mesa or not capacidad:
            messagebox.showwarning("Advertencia", "El número de mesa y capacidad son obligatorios.")
            return

        try:
            numero_mesa_int = int(numero_mesa)
            capacidad_int = int(capacidad)
        except ValueError:
            messagebox.showwarning("Advertencia", "El número de mesa y capacidad deben ser números enteros.")
            return

        mesa = Mesa(numero_mesa=numero_mesa_int, capacidad=capacidad_int, ubicacion=ubicacion)
        try:
            mesa.save()
            messagebox.showinfo("Éxito", "Mesa agregada correctamente.")
            self.clear_mesa_entries()
            self.load_mesas()
            self.update_reserva_comboboxes()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar la mesa:\n{e}")

    def update_mesa(self):
        selected_item = self.mesas_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione una mesa para actualizar.")
            return

        mesa_id = self.mesas_tree.item(selected_item)['values'][0]
        numero_mesa = self.numero_mesa_entry.get()
        capacidad = self.capacidad_entry.get()
        ubicacion = self.ubicacion_entry.get()

        if not numero_mesa or not capacidad:
            messagebox.showwarning("Advertencia", "El número de mesa y capacidad son obligatorios.")
            return

        try:
            numero_mesa_int = int(numero_mesa)
            capacidad_int = int(capacidad)
        except ValueError:
            messagebox.showwarning("Advertencia", "El número de mesa y capacidad deben ser números enteros.")
            return

        mesa = Mesa(mesa_id=mesa_id, numero_mesa=numero_mesa_int, capacidad=capacidad_int, ubicacion=ubicacion)
        try:
            mesa.save()
            messagebox.showinfo("Éxito", "Mesa actualizada correctamente.")
            self.clear_mesa_entries()
            self.load_mesas()
            self.update_reserva_comboboxes()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar la mesa:\n{e}")

    def delete_mesa(self):
        selected_item = self.mesas_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione una mesa para eliminar.")
            return

        mesa_id = self.mesas_tree.item(selected_item)['values'][0]
        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta mesa?")
        if confirm:
            mesa = Mesa(mesa_id=mesa_id)
            try:
                mesa.delete()
                messagebox.showinfo("Éxito", "Mesa eliminada correctamente.")
                self.clear_mesa_entries()
                self.load_mesas()
                self.update_reserva_comboboxes()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al eliminar la mesa:\n{e}")

    def on_mesa_select(self, event):
        selected_item = self.mesas_tree.focus()
        if selected_item:
            mesa_data = self.mesas_tree.item(selected_item)['values']
            self.numero_mesa_entry.delete(0, tk.END)
            self.numero_mesa_entry.insert(0, mesa_data[1])
            self.capacidad_entry.delete(0, tk.END)
            self.capacidad_entry.insert(0, mesa_data[2])
            self.ubicacion_entry.delete(0, tk.END)
            self.ubicacion_entry.insert(0, mesa_data[3])

    def clear_mesa_entries(self):
        self.numero_mesa_entry.delete(0, tk.END)
        self.capacidad_entry.delete(0, tk.END)
        self.ubicacion_entry.delete(0, tk.END)
        self.mesas_tree.selection_remove(self.mesas_tree.selection())

    def load_mesas(self):
        for item in self.mesas_tree.get_children():
            self.mesas_tree.delete(item)
        mesas = Mesa.get_all()
        for mesa in mesas:
            self.mesas_tree.insert('', tk.END, values=(mesa.mesa_id, mesa.numero_mesa, mesa.capacidad, mesa.ubicacion))

    # Métodos para Empleados
    def setup_empleados_tab(self):
        frame = ctk.CTkFrame(master=self.empleados_tab)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Campos de entrada
        form_frame = ctk.CTkFrame(master=frame)
        form_frame.pack(side="left", fill="y", padx=20)

        ctk.CTkLabel(master=form_frame, text="Nombre:").pack(pady=5)
        self.nombre_empleado_entry = ctk.CTkEntry(master=form_frame)
        self.nombre_empleado_entry.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Apellido:").pack(pady=5)
        self.apellido_empleado_entry = ctk.CTkEntry(master=form_frame)
        self.apellido_empleado_entry.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Cargo:").pack(pady=5)
        self.cargo_entry = ctk.CTkEntry(master=form_frame)
        self.cargo_entry.pack(pady=5)

        self.add_empleado_button = ctk.CTkButton(master=form_frame, text="Agregar Empleado", command=self.add_empleado)
        self.add_empleado_button.pack(pady=20)

        # Lista de empleados
        list_frame = ctk.CTkFrame(master=frame)
        list_frame.pack(side="right", fill="both", expand=True, padx=20)

        self.empleados_tree = ttk.Treeview(master=list_frame, columns=("ID", "Nombre", "Apellido", "Cargo"), show="headings")
        self.empleados_tree.heading("ID", text="ID")
        self.empleados_tree.heading("Nombre", text="Nombre")
        self.empleados_tree.heading("Apellido", text="Apellido")
        self.empleados_tree.heading("Cargo", text="Cargo")
        self.empleados_tree.pack(fill="both", expand=True)

        # Botones de edición y eliminación
        btn_frame = ctk.CTkFrame(master=form_frame)
        btn_frame.pack(pady=10)

        self.update_empleado_button = ctk.CTkButton(master=btn_frame, text="Actualizar", command=self.update_empleado)
        self.update_empleado_button.pack(side="left", padx=5)

        self.delete_empleado_button = ctk.CTkButton(master=btn_frame, text="Eliminar", command=self.delete_empleado)
        self.delete_empleado_button.pack(side="right", padx=5)

        self.load_empleados()
        self.empleados_tree.bind("<<TreeviewSelect>>", self.on_empleado_select)

    def add_empleado(self):
        nombre = self.nombre_empleado_entry.get()
        apellido = self.apellido_empleado_entry.get()
        cargo = self.cargo_entry.get()

        if not nombre or not apellido or not cargo:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        empleado = Empleado(nombre=nombre, apellido=apellido, cargo=cargo)
        try:
            empleado.save()
            messagebox.showinfo("Éxito", "Empleado agregado correctamente.")
            self.clear_empleado_entries()
            self.load_empleados()
            self.update_reserva_comboboxes()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar el empleado:\n{e}")

    def update_empleado(self):
        selected_item = self.empleados_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para actualizar.")
            return

        empleado_id = self.empleados_tree.item(selected_item)['values'][0]
        nombre = self.nombre_empleado_entry.get()
        apellido = self.apellido_empleado_entry.get()
        cargo = self.cargo_entry.get()

        if not nombre or not apellido or not cargo:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        empleado = Empleado(empleado_id=empleado_id, nombre=nombre, apellido=apellido, cargo=cargo)
        try:
            empleado.save()
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente.")
            self.clear_empleado_entries()
            self.load_empleados()
            self.update_reserva_comboboxes()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar el empleado:\n{e}")

    def delete_empleado(self):
        selected_item = self.empleados_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para eliminar.")
            return

        empleado_id = self.empleados_tree.item(selected_item)['values'][0]
        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este empleado?")
        if confirm:
            empleado = Empleado(empleado_id=empleado_id)
            try:
                empleado.delete()
                messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
                self.clear_empleado_entries()
                self.load_empleados()
                self.update_reserva_comboboxes()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al eliminar el empleado:\n{e}")

    def on_empleado_select(self, event):
        selected_item = self.empleados_tree.focus()
        if selected_item:
            empleado_data = self.empleados_tree.item(selected_item)['values']
            self.nombre_empleado_entry.delete(0, tk.END)
            self.nombre_empleado_entry.insert(0, empleado_data[1])
            self.apellido_empleado_entry.delete(0, tk.END)
            self.apellido_empleado_entry.insert(0, empleado_data[2])
            self.cargo_entry.delete(0, tk.END)
            self.cargo_entry.insert(0, empleado_data[3])

    def clear_empleado_entries(self):
        self.nombre_empleado_entry.delete(0, tk.END)
        self.apellido_empleado_entry.delete(0, tk.END)
        self.cargo_entry.delete(0, tk.END)
        self.empleados_tree.selection_remove(self.empleados_tree.selection())

    def load_empleados(self):
        for item in self.empleados_tree.get_children():
            self.empleados_tree.delete(item)
        empleados = Empleado.get_all()
        for empleado in empleados:
            self.empleados_tree.insert('', tk.END, values=(empleado.empleado_id, empleado.nombre, empleado.apellido, empleado.cargo))

    # Métodos para Reservas
    def setup_reservas_tab(self):
        frame = ctk.CTkFrame(master=self.reservas_tab)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Campos de entrada
        form_frame = ctk.CTkFrame(master=frame)
        form_frame.pack(side="left", fill="y", padx=20)

        ctk.CTkLabel(master=form_frame, text="Cliente:").pack(pady=5)
        self.selected_cliente = ctk.StringVar()
        self.cliente_combobox = ctk.CTkComboBox(master=form_frame, variable=self.selected_cliente)
        self.cliente_combobox.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Mesa:").pack(pady=5)
        self.selected_mesa = ctk.StringVar()
        self.mesa_combobox = ctk.CTkComboBox(master=form_frame, variable=self.selected_mesa)
        self.mesa_combobox.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Empleado:").pack(pady=5)
        self.selected_empleado = ctk.StringVar()
        self.empleado_combobox = ctk.CTkComboBox(master=form_frame, variable=self.selected_empleado)
        self.empleado_combobox.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Fecha Reserva (YYYY-MM-DD):").pack(pady=5)
        self.fecha_reserva_entry = ctk.CTkEntry(master=form_frame)
        self.fecha_reserva_entry.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Hora Reserva (HH:MM):").pack(pady=5)
        self.hora_reserva_entry = ctk.CTkEntry(master=form_frame)
        self.hora_reserva_entry.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Número de Personas:").pack(pady=5)
        self.numero_personas_entry = ctk.CTkEntry(master=form_frame)
        self.numero_personas_entry.pack(pady=5)

        self.add_reserva_button = ctk.CTkButton(master=form_frame, text="Agregar Reserva", command=self.add_reserva)
        self.add_reserva_button.pack(pady=20)

        # Lista de reservas
        list_frame = ctk.CTkFrame(master=frame)
        list_frame.pack(side="right", fill="both", expand=True, padx=20)

        self.reservas_tree = ttk.Treeview(master=list_frame, columns=("ID", "Cliente", "Mesa", "Empleado", "Fecha", "Hora", "Personas"), show="headings")
        self.reservas_tree.heading("ID", text="ID")
        self.reservas_tree.heading("Cliente", text="Cliente")
        self.reservas_tree.heading("Mesa", text="Mesa")
        self.reservas_tree.heading("Empleado", text="Empleado")
        self.reservas_tree.heading("Fecha", text="Fecha")
        self.reservas_tree.heading("Hora", text="Hora")
        self.reservas_tree.heading("Personas", text="Personas")
        self.reservas_tree.pack(fill="both", expand=True)

        # Botones de edición y eliminación
        btn_frame = ctk.CTkFrame(master=form_frame)
        btn_frame.pack(pady=10)

        self.update_reserva_button = ctk.CTkButton(master=btn_frame, text="Actualizar", command=self.update_reserva)
        self.update_reserva_button.pack(side="left", padx=5)

        self.delete_reserva_button = ctk.CTkButton(master=btn_frame, text="Eliminar", command=self.delete_reserva)
        self.delete_reserva_button.pack(side="right", padx=5)

        self.load_reservas()
        self.update_reserva_comboboxes()
        self.reservas_tree.bind("<<TreeviewSelect>>", self.on_reserva_select)

    def update_reserva_comboboxes(self):
        clientes = Cliente.get_all()
        mesas = Mesa.get_all()
        empleados = Empleado.get_all()

        self.cliente_combobox.configure(values=[f"{c.cliente_id} - {c.nombre} {c.apellido}" for c in clientes])
        self.cliente_combobox.set("Seleccione un Cliente")

        self.mesa_combobox.configure(values=[f"{m.mesa_id} - Mesa {m.numero_mesa}" for m in mesas])
        self.mesa_combobox.set("Seleccione una Mesa")

        self.empleado_combobox.configure(values=[f"{e.empleado_id} - {e.nombre} {e.apellido}" for e in empleados])
        self.empleado_combobox.set("Seleccione un Empleado")

    def add_reserva(self):
        cliente_str = self.selected_cliente.get()
        mesa_str = self.selected_mesa.get()
        empleado_str = self.selected_empleado.get()
        fecha_reserva = self.fecha_reserva_entry.get()
        hora_reserva = self.hora_reserva_entry.get()
        numero_personas = self.numero_personas_entry.get()

        if " - " in cliente_str:
            cliente_id = int(cliente_str.split(" - ")[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione un cliente válido.")
            return

        if " - " in mesa_str:
            mesa_id = int(mesa_str.split(" - ")[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione una mesa válida.")
            return

        if " - " in empleado_str:
            empleado_id = int(empleado_str.split(" - ")[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione un empleado válido.")
            return

        if not fecha_reserva or not hora_reserva or not numero_personas:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        try:
            fecha_reserva_dt = datetime.strptime(fecha_reserva, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showwarning("Advertencia", "Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            return

        reserva = Reserva(cliente_id=cliente_id, mesa_id=mesa_id, empleado_id=empleado_id, fecha_reserva=fecha_reserva_dt,
                          hora_reserva=hora_reserva, numero_personas=int(numero_personas))
        try:
            reserva.save()
            messagebox.showinfo("Éxito", "Reserva agregada correctamente.")
            self.clear_reserva_entries()
            self.load_reservas()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar la reserva:\n{e}")

    def update_reserva(self):
        selected_item = self.reservas_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione una reserva para actualizar.")
            return

        reserva_id = self.reservas_tree.item(selected_item)['values'][0]

        cliente_str = self.selected_cliente.get()
        mesa_str = self.selected_mesa.get()
        empleado_str = self.selected_empleado.get()
        fecha_reserva = self.fecha_reserva_entry.get()
        hora_reserva = self.hora_reserva_entry.get()
        numero_personas = self.numero_personas_entry.get()

        if " - " in cliente_str:
            cliente_id = int(cliente_str.split(" - ")[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione un cliente válido.")
            return

        if " - " in mesa_str:
            mesa_id = int(mesa_str.split(" - ")[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione una mesa válida.")
            return

        if " - " in empleado_str:
            empleado_id = int(empleado_str.split(" - ")[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione un empleado válido.")
            return

        if not fecha_reserva or not hora_reserva or not numero_personas:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        try:
            fecha_reserva_dt = datetime.strptime(fecha_reserva, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showwarning("Advertencia", "Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            return

        reserva = Reserva(reserva_id=reserva_id, cliente_id=cliente_id, mesa_id=mesa_id, empleado_id=empleado_id, fecha_reserva=fecha_reserva_dt,
                          hora_reserva=hora_reserva, numero_personas=int(numero_personas))
        try:
            reserva.save()
            messagebox.showinfo("Éxito", "Reserva actualizada correctamente.")
            self.clear_reserva_entries()
            self.load_reservas()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar la reserva:\n{e}")

    def delete_reserva(self):
        selected_item = self.reservas_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione una reserva para eliminar.")
            return

        reserva_id = self.reservas_tree.item(selected_item)['values'][0]
        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta reserva?")
        if confirm:
            reserva = Reserva(reserva_id=reserva_id)
            try:
                reserva.delete()
                messagebox.showinfo("Éxito", "Reserva eliminada correctamente.")
                self.clear_reserva_entries()
                self.load_reservas()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al eliminar la reserva:\n{e}")

    def on_reserva_select(self, event):
        selected_item = self.reservas_tree.focus()
        if selected_item:
            reserva_data = self.reservas_tree.item(selected_item)['values']

            self.selected_cliente.set(reserva_data[1])
            self.selected_mesa.set(reserva_data[2])
            self.selected_empleado.set(reserva_data[3])

            self.fecha_reserva_entry.delete(0, tk.END)
            self.fecha_reserva_entry.insert(0, reserva_data[4])
            self.hora_reserva_entry.delete(0, tk.END)
            self.hora_reserva_entry.insert(0, reserva_data[5])
            self.numero_personas_entry.delete(0, tk.END)
            self.numero_personas_entry.insert(0, reserva_data[6])

    def clear_reserva_entries(self):
        self.fecha_reserva_entry.delete(0, tk.END)
        self.hora_reserva_entry.delete(0, tk.END)
        self.numero_personas_entry.delete(0, tk.END)
        self.cliente_combobox.set("Seleccione un Cliente")
        self.mesa_combobox.set("Seleccione una Mesa")
        self.empleado_combobox.set("Seleccione un Empleado")
        self.reservas_tree.selection_remove(self.reservas_tree.selection())

    def load_reservas(self):
        for item in self.reservas_tree.get_children():
            self.reservas_tree.delete(item)
        reservas = Reserva.get_all()
        for reserva in reservas:
            self.reservas_tree.insert('', tk.END, values=(reserva[0], reserva[1], reserva[2], reserva[3], reserva[4], reserva[5], reserva[6]))

    # Métodos para Menús
    def setup_menus_tab(self):
        frame = ctk.CTkFrame(master=self.menus_tab)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Campos de entrada
        form_frame = ctk.CTkFrame(master=frame)
        form_frame.pack(side="left", fill="y", padx=20)

        ctk.CTkLabel(master=form_frame, text="Nombre del Plato:").pack(pady=5)
        self.nombre_plato_entry = ctk.CTkEntry(master=form_frame)
        self.nombre_plato_entry.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Descripción:").pack(pady=5)
        self.descripcion_entry = ctk.CTkEntry(master=form_frame)
        self.descripcion_entry.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Precio:").pack(pady=5)
        self.precio_entry = ctk.CTkEntry(master=form_frame)
        self.precio_entry.pack(pady=5)

        self.add_menu_button = ctk.CTkButton(master=form_frame, text="Agregar Menú", command=self.add_menu)
        self.add_menu_button.pack(pady=20)

        # Lista de menús
        list_frame = ctk.CTkFrame(master=frame)
        list_frame.pack(side="right", fill="both", expand=True, padx=20)

        self.menus_tree = ttk.Treeview(master=list_frame, columns=("ID", "Nombre", "Descripción", "Precio"), show="headings")
        self.menus_tree.heading("ID", text="ID")
        self.menus_tree.heading("Nombre", text="Nombre del Plato")
        self.menus_tree.heading("Descripción", text="Descripción")
        self.menus_tree.heading("Precio", text="Precio")
        self.menus_tree.pack(fill="both", expand=True)

        # Botones de edición y eliminación
        btn_frame = ctk.CTkFrame(master=form_frame)
        btn_frame.pack(pady=10)

        self.update_menu_button = ctk.CTkButton(master=btn_frame, text="Actualizar", command=self.update_menu)
        self.update_menu_button.pack(side="left", padx=5)

        self.delete_menu_button = ctk.CTkButton(master=btn_frame, text="Eliminar", command=self.delete_menu)
        self.delete_menu_button.pack(side="right", padx=5)

        self.load_menus()
        self.menus_tree.bind("<<TreeviewSelect>>", self.on_menu_select)

    def add_menu(self):
        nombre_plato = self.nombre_plato_entry.get()
        descripcion = self.descripcion_entry.get()
        precio = self.precio_entry.get()

        if not nombre_plato or not precio:
            messagebox.showwarning("Advertencia", "El nombre del plato y el precio son obligatorios.")
            return

        try:
            precio_float = float(precio)
        except ValueError:
            messagebox.showwarning("Advertencia", "El precio debe ser un número válido.")
            return

        menu = Menu(nombre_plato=nombre_plato, descripcion=descripcion, precio=precio_float)
        try:
            menu.save()
            messagebox.showinfo("Éxito", "Menú agregado correctamente.")
            self.clear_menu_entries()
            self.load_menus()
            self.update_pedido_comboboxes()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar el menú:\n{e}")

    def update_menu(self):
        selected_item = self.menus_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un menú para actualizar.")
            return

        menu_id = self.menus_tree.item(selected_item)['values'][0]
        nombre_plato = self.nombre_plato_entry.get()
        descripcion = self.descripcion_entry.get()
        precio = self.precio_entry.get()

        if not nombre_plato or not precio:
            messagebox.showwarning("Advertencia", "El nombre del plato y el precio son obligatorios.")
            return

        try:
            precio_float = float(precio)
        except ValueError:
            messagebox.showwarning("Advertencia", "El precio debe ser un número válido.")
            return

        menu = Menu(menu_id=menu_id, nombre_plato=nombre_plato, descripcion=descripcion, precio=precio_float)
        try:
            menu.save()
            messagebox.showinfo("Éxito", "Menú actualizado correctamente.")
            self.clear_menu_entries()
            self.load_menus()
            self.update_pedido_comboboxes()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar el menú:\n{e}")

    def delete_menu(self):
        selected_item = self.menus_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un menú para eliminar.")
            return

        menu_id = self.menus_tree.item(selected_item)['values'][0]
        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este menú?")
        if confirm:
            menu = Menu(menu_id=menu_id)
            try:
                menu.delete()
                messagebox.showinfo("Éxito", "Menú eliminado correctamente.")
                self.clear_menu_entries()
                self.load_menus()
                self.update_pedido_comboboxes()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al eliminar el menú:\n{e}")

    def on_menu_select(self, event):
        selected_item = self.menus_tree.focus()
        if selected_item:
            menu_data = self.menus_tree.item(selected_item)['values']
            self.nombre_plato_entry.delete(0, tk.END)
            self.nombre_plato_entry.insert(0, menu_data[1])
            self.descripcion_entry.delete(0, tk.END)
            self.descripcion_entry.insert(0, menu_data[2])
            self.precio_entry.delete(0, tk.END)
            self.precio_entry.insert(0, menu_data[3])

    def clear_menu_entries(self):
        self.nombre_plato_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.menus_tree.selection_remove(self.menus_tree.selection())

    def load_menus(self):
        for item in self.menus_tree.get_children():
            self.menus_tree.delete(item)
        menus = Menu.get_all()
        for menu in menus:
            self.menus_tree.insert('', tk.END, values=(menu.menu_id, menu.nombre_plato, menu.descripcion, menu.precio))

    # Métodos para Pedidos
    def setup_pedidos_tab(self):
        frame = ctk.CTkFrame(master=self.pedidos_tab)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Campos de entrada
        form_frame = ctk.CTkFrame(master=frame)
        form_frame.pack(side="left", fill="y", padx=20)

        ctk.CTkLabel(master=form_frame, text="Reserva:").pack(pady=5)
        self.selected_reserva = ctk.StringVar()
        self.reserva_combobox = ctk.CTkComboBox(master=form_frame, variable=self.selected_reserva)
        self.reserva_combobox.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Menú:").pack(pady=5)
        self.selected_menu = ctk.StringVar()
        self.menu_combobox = ctk.CTkComboBox(master=form_frame, variable=self.selected_menu)
        self.menu_combobox.pack(pady=5)

        ctk.CTkLabel(master=form_frame, text="Cantidad:").pack(pady=5)
        self.cantidad_entry = ctk.CTkEntry(master=form_frame)
        self.cantidad_entry.pack(pady=5)

        self.add_pedido_button = ctk.CTkButton(master=form_frame, text="Agregar Pedido", command=self.add_pedido)
        self.add_pedido_button.pack(pady=20)

        # Lista de pedidos
        list_frame = ctk.CTkFrame(master=frame)
        list_frame.pack(side="right", fill="both", expand=True, padx=20)

        self.pedidos_tree = ttk.Treeview(master=list_frame, columns=("ID", "Reserva", "Menú", "Cantidad"), show="headings")
        self.pedidos_tree.heading("ID", text="ID")
        self.pedidos_tree.heading("Reserva", text="Reserva")
        self.pedidos_tree.heading("Menú", text="Menú")
        self.pedidos_tree.heading("Cantidad", text="Cantidad")
        self.pedidos_tree.pack(fill="both", expand=True)

        # Botones de edición y eliminación
        btn_frame = ctk.CTkFrame(master=form_frame)
        btn_frame.pack(pady=10)

        self.update_pedido_button = ctk.CTkButton(master=btn_frame, text="Actualizar", command=self.update_pedido)
        self.update_pedido_button.pack(side="left", padx=5)

        self.delete_pedido_button = ctk.CTkButton(master=btn_frame, text="Eliminar", command=self.delete_pedido)
        self.delete_pedido_button.pack(side="right", padx=5)

        self.load_pedidos()
        self.update_pedido_comboboxes()
        self.pedidos_tree.bind("<<TreeviewSelect>>", self.on_pedido_select)

    def update_pedido_comboboxes(self):
        reservas = Reserva.get_all()
        menus = Menu.get_all()

        self.reserva_combobox.configure(values=[f"{r[0]} - {r[1]}" for r in reservas])
        self.reserva_combobox.set("Seleccione una Reserva")

        self.menu_combobox.configure(values=[f"{m.menu_id} - {m.nombre_plato}" for m in menus])
        self.menu_combobox.set("Seleccione un Menú")

    def add_pedido(self):
        reserva_str = self.selected_reserva.get()
        menu_str = self.selected_menu.get()
        cantidad = self.cantidad_entry.get()

        if " - " in reserva_str:
            reserva_id = int(reserva_str.split(" - ")[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione una reserva válida.")
            return

        if " - " in menu_str:
            menu_id = int(menu_str.split(" - ")[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione un menú válido.")
            return

        if not cantidad:
            messagebox.showwarning("Advertencia", "La cantidad es obligatoria.")
            return

        try:
            cantidad_int = int(cantidad)
        except ValueError:
            messagebox.showwarning("Advertencia", "La cantidad debe ser un número entero.")
            return

        pedido = Pedido(reserva_id=reserva_id, menu_id=menu_id, cantidad=cantidad_int)
        try:
            pedido.save()
            messagebox.showinfo("Éxito", "Pedido agregado correctamente.")
            self.clear_pedido_entries()
            self.load_pedidos()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar el pedido:\n{e}")

    def update_pedido(self):
        selected_item = self.pedidos_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un pedido para actualizar.")
            return

        pedido_id = self.pedidos_tree.item(selected_item)['values'][0]

        reserva_str = self.selected_reserva.get()
        menu_str = self.selected_menu.get()
        cantidad = self.cantidad_entry.get()

        if " - " in reserva_str:
            reserva_id = int(reserva_str.split(" - ")[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione una reserva válida.")
            return

        if " - " in menu_str:
            menu_id = int(menu_str.split(" - ")[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione un menú válido.")
            return

        if not cantidad:
            messagebox.showwarning("Advertencia", "La cantidad es obligatoria.")
            return

        try:
            cantidad_int = int(cantidad)
        except ValueError:
            messagebox.showwarning("Advertencia", "La cantidad debe ser un número entero.")
            return

        pedido = Pedido(pedido_id=pedido_id, reserva_id=reserva_id, menu_id=menu_id, cantidad=cantidad_int)
        try:
            pedido.save()
            messagebox.showinfo("Éxito", "Pedido actualizado correctamente.")
            self.clear_pedido_entries()
            self.load_pedidos()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar el pedido:\n{e}")

    def delete_pedido(self):
        selected_item = self.pedidos_tree.focus()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un pedido para eliminar.")
            return

        pedido_id = self.pedidos_tree.item(selected_item)['values'][0]
        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este pedido?")
        if confirm:
            pedido = Pedido(pedido_id=pedido_id)
            try:
                pedido.delete()
                messagebox.showinfo("Éxito", "Pedido eliminado correctamente.")
                self.clear_pedido_entries()
                self.load_pedidos()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al eliminar el pedido:\n{e}")

    def on_pedido_select(self, event):
        selected_item = self.pedidos_tree.focus()
        if selected_item:
            pedido_data = self.pedidos_tree.item(selected_item)['values']
            self.selected_reserva.set(pedido_data[1])
            self.selected_menu.set(pedido_data[2])
            self.cantidad_entry.delete(0, tk.END)
            self.cantidad_entry.insert(0, pedido_data[3])

    def clear_pedido_entries(self):
        self.cantidad_entry.delete(0, tk.END)
        self.reserva_combobox.set("Seleccione una Reserva")
        self.menu_combobox.set("Seleccione un Menú")
        self.pedidos_tree.selection_remove(self.pedidos_tree.selection())

    def load_pedidos(self):
        for item in self.pedidos_tree.get_children():
            self.pedidos_tree.delete(item)
        pedidos = Pedido.get_all()
        for pedido in pedidos:
            self.pedidos_tree.insert('', tk.END, values=(pedido[0], pedido[1], pedido[2], pedido[3]))

if __name__ == "__main__":
    app = App()
    app.mainloop()
