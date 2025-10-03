# SNMP MIB module (ZEBRA-QL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zebra\ZEBRA-QL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:35 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zebra_ObjectIdentity = ObjectIdentity
zebra = _Zebra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642)
)
_Zql_zebra_ql_ObjectIdentity = ObjectIdentity
zql_zebra_ql = _Zql_zebra_ql_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200)
)
_Zql_ql_bluetooth_ObjectIdentity = ObjectIdentity
zql_ql_bluetooth = _Zql_ql_bluetooth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1)
)
_Zql_bluetooth_discoverable_Type = OctetString
_Zql_bluetooth_discoverable_Object = MibScalar
zql_bluetooth_discoverable = _Zql_bluetooth_discoverable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 3),
    _Zql_bluetooth_discoverable_Type()
)
zql_bluetooth_discoverable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_bluetooth_discoverable.setStatus("current")
_Zql_bluetooth_friendly_name_Type = OctetString
_Zql_bluetooth_friendly_name_Object = MibScalar
zql_bluetooth_friendly_name = _Zql_bluetooth_friendly_name_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 5),
    _Zql_bluetooth_friendly_name_Type()
)
zql_bluetooth_friendly_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_bluetooth_friendly_name.setStatus("current")
_Zql_bluetooth_version_Type = OctetString
_Zql_bluetooth_version_Object = MibScalar
zql_bluetooth_version = _Zql_bluetooth_version_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 6),
    _Zql_bluetooth_version_Type()
)
zql_bluetooth_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_bluetooth_version.setStatus("current")
_Zql_bluetooth_date_Type = OctetString
_Zql_bluetooth_date_Object = MibScalar
zql_bluetooth_date = _Zql_bluetooth_date_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 7),
    _Zql_bluetooth_date_Type()
)
zql_bluetooth_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_bluetooth_date.setStatus("current")
_Zql_bluetooth_local_name_Type = OctetString
_Zql_bluetooth_local_name_Object = MibScalar
zql_bluetooth_local_name = _Zql_bluetooth_local_name_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 10),
    _Zql_bluetooth_local_name_Type()
)
zql_bluetooth_local_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_bluetooth_local_name.setStatus("current")
_Zql_bluetooth_address_Type = OctetString
_Zql_bluetooth_address_Object = MibScalar
zql_bluetooth_address = _Zql_bluetooth_address_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 11),
    _Zql_bluetooth_address_Type()
)
zql_bluetooth_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_bluetooth_address.setStatus("current")
_Zql_bluetooth_bluetooth_pin_Type = OctetString
_Zql_bluetooth_bluetooth_pin_Object = MibScalar
zql_bluetooth_bluetooth_pin = _Zql_bluetooth_bluetooth_pin_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 12),
    _Zql_bluetooth_bluetooth_pin_Type()
)
zql_bluetooth_bluetooth_pin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_bluetooth_bluetooth_pin.setStatus("current")
_Zql_bluetooth_short_address_Type = OctetString
_Zql_bluetooth_short_address_Object = MibScalar
zql_bluetooth_short_address = _Zql_bluetooth_short_address_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 13),
    _Zql_bluetooth_short_address_Type()
)
zql_bluetooth_short_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_bluetooth_short_address.setStatus("current")
_Zql_bluetooth_radio_version_Type = OctetString
_Zql_bluetooth_radio_version_Object = MibScalar
zql_bluetooth_radio_version = _Zql_bluetooth_radio_version_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 14),
    _Zql_bluetooth_radio_version_Type()
)
zql_bluetooth_radio_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_bluetooth_radio_version.setStatus("current")
_Zql_bluetooth_afh_mode_Type = OctetString
_Zql_bluetooth_afh_mode_Object = MibScalar
zql_bluetooth_afh_mode = _Zql_bluetooth_afh_mode_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 15),
    _Zql_bluetooth_afh_mode_Type()
)
zql_bluetooth_afh_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_bluetooth_afh_mode.setStatus("current")
_Zql_bluetooth_afh_map_Type = OctetString
_Zql_bluetooth_afh_map_Object = MibScalar
zql_bluetooth_afh_map = _Zql_bluetooth_afh_map_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 16),
    _Zql_bluetooth_afh_map_Type()
)
zql_bluetooth_afh_map.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_bluetooth_afh_map.setStatus("current")
_Zql_bluetooth_afh_map_curr_Type = OctetString
_Zql_bluetooth_afh_map_curr_Object = MibScalar
zql_bluetooth_afh_map_curr = _Zql_bluetooth_afh_map_curr_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 17),
    _Zql_bluetooth_afh_map_curr_Type()
)
zql_bluetooth_afh_map_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_bluetooth_afh_map_curr.setStatus("current")
_Zql_bluetooth_enable_Type = OctetString
_Zql_bluetooth_enable_Object = MibScalar
zql_bluetooth_enable = _Zql_bluetooth_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 19),
    _Zql_bluetooth_enable_Type()
)
zql_bluetooth_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_bluetooth_enable.setStatus("current")
_Zql_bluetooth_connected_Type = OctetString
_Zql_bluetooth_connected_Object = MibScalar
zql_bluetooth_connected = _Zql_bluetooth_connected_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 1, 21),
    _Zql_bluetooth_connected_Type()
)
zql_bluetooth_connected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_bluetooth_connected.setStatus("current")
_Zql_ql_card_ObjectIdentity = ObjectIdentity
zql_ql_card = _Zql_ql_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 2)
)
_Zql_card_inserted_Type = OctetString
_Zql_card_inserted_Object = MibScalar
zql_card_inserted = _Zql_card_inserted_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 2, 1),
    _Zql_card_inserted_Type()
)
zql_card_inserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_card_inserted.setStatus("current")
_Zql_card_idtext1_Type = OctetString
_Zql_card_idtext1_Object = MibScalar
zql_card_idtext1 = _Zql_card_idtext1_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 2, 6),
    _Zql_card_idtext1_Type()
)
zql_card_idtext1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_card_idtext1.setStatus("current")
_Zql_card_idtext2_Type = OctetString
_Zql_card_idtext2_Object = MibScalar
zql_card_idtext2 = _Zql_card_idtext2_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 2, 7),
    _Zql_card_idtext2_Type()
)
zql_card_idtext2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_card_idtext2.setStatus("current")
_Zql_card_idtext3_Type = OctetString
_Zql_card_idtext3_Object = MibScalar
zql_card_idtext3 = _Zql_card_idtext3_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 2, 8),
    _Zql_card_idtext3_Type()
)
zql_card_idtext3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_card_idtext3.setStatus("current")
_Zql_card_idtext4_Type = OctetString
_Zql_card_idtext4_Object = MibScalar
zql_card_idtext4 = _Zql_card_idtext4_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 2, 9),
    _Zql_card_idtext4_Type()
)
zql_card_idtext4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_card_idtext4.setStatus("current")
_Zql_card_mac_addr_Type = OctetString
_Zql_card_mac_addr_Object = MibScalar
zql_card_mac_addr = _Zql_card_mac_addr_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 2, 15),
    _Zql_card_mac_addr_Type()
)
zql_card_mac_addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_card_mac_addr.setStatus("current")
_Zql_card_mac_raw_Type = OctetString
_Zql_card_mac_raw_Object = MibScalar
zql_card_mac_raw = _Zql_card_mac_raw_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 2, 16),
    _Zql_card_mac_raw_Type()
)
zql_card_mac_raw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_card_mac_raw.setStatus("current")
_Zql_card_enable_Type = OctetString
_Zql_card_enable_Object = MibScalar
zql_card_enable = _Zql_card_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 2, 17),
    _Zql_card_enable_Type()
)
zql_card_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_card_enable.setStatus("current")
_Zql_ql_comm_ObjectIdentity = ObjectIdentity
zql_ql_comm = _Zql_ql_comm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 3)
)
_Zql_comm_baud_Type = OctetString
_Zql_comm_baud_Object = MibScalar
zql_comm_baud = _Zql_comm_baud_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 3, 1),
    _Zql_comm_baud_Type()
)
zql_comm_baud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_comm_baud.setStatus("current")
_Zql_comm_data_bits_Type = OctetString
_Zql_comm_data_bits_Object = MibScalar
zql_comm_data_bits = _Zql_comm_data_bits_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 3, 2),
    _Zql_comm_data_bits_Type()
)
zql_comm_data_bits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_comm_data_bits.setStatus("current")
_Zql_comm_parity_Type = OctetString
_Zql_comm_parity_Object = MibScalar
zql_comm_parity = _Zql_comm_parity_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 3, 3),
    _Zql_comm_parity_Type()
)
zql_comm_parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_comm_parity.setStatus("current")
_Zql_comm_stop_bits_Type = OctetString
_Zql_comm_stop_bits_Object = MibScalar
zql_comm_stop_bits = _Zql_comm_stop_bits_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 3, 4),
    _Zql_comm_stop_bits_Type()
)
zql_comm_stop_bits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_comm_stop_bits.setStatus("current")
_Zql_comm_dsr_Type = OctetString
_Zql_comm_dsr_Object = MibScalar
zql_comm_dsr = _Zql_comm_dsr_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 3, 5),
    _Zql_comm_dsr_Type()
)
zql_comm_dsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_comm_dsr.setStatus("current")
_Zql_ql_head_ObjectIdentity = ObjectIdentity
zql_ql_head = _Zql_ql_head_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 4)
)
_Zql_head_latch_Type = OctetString
_Zql_head_latch_Object = MibScalar
zql_head_latch = _Zql_head_latch_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 4, 1),
    _Zql_head_latch_Type()
)
zql_head_latch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_head_latch.setStatus("current")
_Zql_ql_ip_ObjectIdentity = ObjectIdentity
zql_ql_ip = _Zql_ql_ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5)
)
_Zql_ip_dhcp_ObjectIdentity = ObjectIdentity
zql_ip_dhcp = _Zql_ip_dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1)
)
_Zql_dhcp_enable_Type = OctetString
_Zql_dhcp_enable_Object = MibScalar
zql_dhcp_enable = _Zql_dhcp_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 1),
    _Zql_dhcp_enable_Type()
)
zql_dhcp_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_enable.setStatus("current")
_Zql_dhcp_cid_type_Type = OctetString
_Zql_dhcp_cid_type_Object = MibScalar
zql_dhcp_cid_type = _Zql_dhcp_cid_type_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 2),
    _Zql_dhcp_cid_type_Type()
)
zql_dhcp_cid_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_cid_type.setStatus("current")
_Zql_dhcp_cid_prefix_Type = OctetString
_Zql_dhcp_cid_prefix_Object = MibScalar
zql_dhcp_cid_prefix = _Zql_dhcp_cid_prefix_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 3),
    _Zql_dhcp_cid_prefix_Type()
)
zql_dhcp_cid_prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_cid_prefix.setStatus("current")
_Zql_dhcp_cid_value_Type = OctetString
_Zql_dhcp_cid_value_Object = MibScalar
zql_dhcp_cid_value = _Zql_dhcp_cid_value_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 4),
    _Zql_dhcp_cid_value_Type()
)
zql_dhcp_cid_value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_cid_value.setStatus("current")
_Zql_dhcp_requests_per_session_Type = OctetString
_Zql_dhcp_requests_per_session_Object = MibScalar
zql_dhcp_requests_per_session = _Zql_dhcp_requests_per_session_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 5),
    _Zql_dhcp_requests_per_session_Type()
)
zql_dhcp_requests_per_session.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_requests_per_session.setStatus("current")
_Zql_dhcp_request_timeout_Type = OctetString
_Zql_dhcp_request_timeout_Object = MibScalar
zql_dhcp_request_timeout = _Zql_dhcp_request_timeout_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 6),
    _Zql_dhcp_request_timeout_Type()
)
zql_dhcp_request_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_request_timeout.setStatus("current")
_Zql_dhcp_session_interval_Type = OctetString
_Zql_dhcp_session_interval_Object = MibScalar
zql_dhcp_session_interval = _Zql_dhcp_session_interval_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 7),
    _Zql_dhcp_session_interval_Type()
)
zql_dhcp_session_interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_session_interval.setStatus("current")
_Zql_dhcp_lease_ObjectIdentity = ObjectIdentity
zql_dhcp_lease = _Zql_dhcp_lease_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 8)
)
_Zql_lease_length_Type = OctetString
_Zql_lease_length_Object = MibScalar
zql_lease_length = _Zql_lease_length_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 8, 1),
    _Zql_lease_length_Type()
)
zql_lease_length.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_lease_length.setStatus("current")
_Zql_lease_time_left_Type = OctetString
_Zql_lease_time_left_Object = MibScalar
zql_lease_time_left = _Zql_lease_time_left_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 8, 2),
    _Zql_lease_time_left_Type()
)
zql_lease_time_left.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_lease_time_left.setStatus("current")
_Zql_lease_server_Type = OctetString
_Zql_lease_server_Object = MibScalar
zql_lease_server = _Zql_lease_server_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 8, 3),
    _Zql_lease_server_Type()
)
zql_lease_server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_lease_server.setStatus("current")
_Zql_lease_last_attempt_Type = OctetString
_Zql_lease_last_attempt_Object = MibScalar
zql_lease_last_attempt = _Zql_lease_last_attempt_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 8, 4),
    _Zql_lease_last_attempt_Type()
)
zql_lease_last_attempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_lease_last_attempt.setStatus("current")
_Zql_dhcp_cache_ip_Type = OctetString
_Zql_dhcp_cache_ip_Object = MibScalar
zql_dhcp_cache_ip = _Zql_dhcp_cache_ip_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 9),
    _Zql_dhcp_cache_ip_Type()
)
zql_dhcp_cache_ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_cache_ip.setStatus("current")
_Zql_dhcp_vendor_class_id_Type = OctetString
_Zql_dhcp_vendor_class_id_Object = MibScalar
zql_dhcp_vendor_class_id = _Zql_dhcp_vendor_class_id_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 10),
    _Zql_dhcp_vendor_class_id_Type()
)
zql_dhcp_vendor_class_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_vendor_class_id.setStatus("current")
_Zql_dhcp_user_class_id_Type = OctetString
_Zql_dhcp_user_class_id_Object = MibScalar
zql_dhcp_user_class_id = _Zql_dhcp_user_class_id_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 11),
    _Zql_dhcp_user_class_id_Type()
)
zql_dhcp_user_class_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_user_class_id.setStatus("current")
_Zql_dhcp_option12_Type = OctetString
_Zql_dhcp_option12_Object = MibScalar
zql_dhcp_option12 = _Zql_dhcp_option12_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 12),
    _Zql_dhcp_option12_Type()
)
zql_dhcp_option12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_option12.setStatus("current")
_Zql_dhcp_option12_format_Type = OctetString
_Zql_dhcp_option12_format_Object = MibScalar
zql_dhcp_option12_format = _Zql_dhcp_option12_format_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 13),
    _Zql_dhcp_option12_format_Type()
)
zql_dhcp_option12_format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_dhcp_option12_format.setStatus("current")
_Zql_dhcp_option12_value_Type = OctetString
_Zql_dhcp_option12_value_Object = MibScalar
zql_dhcp_option12_value = _Zql_dhcp_option12_value_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 1, 14),
    _Zql_dhcp_option12_value_Type()
)
zql_dhcp_option12_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_dhcp_option12_value.setStatus("current")
_Zql_ip_ftp_ObjectIdentity = ObjectIdentity
zql_ip_ftp = _Zql_ip_ftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 2)
)
_Zql_ftp_enable_Type = OctetString
_Zql_ftp_enable_Object = MibScalar
zql_ftp_enable = _Zql_ftp_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 2, 1),
    _Zql_ftp_enable_Type()
)
zql_ftp_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_ftp_enable.setStatus("current")
_Zql_ftp_execute_file_Type = OctetString
_Zql_ftp_execute_file_Object = MibScalar
zql_ftp_execute_file = _Zql_ftp_execute_file_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 2, 2),
    _Zql_ftp_execute_file_Type()
)
zql_ftp_execute_file.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_ftp_execute_file.setStatus("current")
_Zql_ip_lpd_ObjectIdentity = ObjectIdentity
zql_ip_lpd = _Zql_ip_lpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 3)
)
_Zql_lpd_enable_Type = OctetString
_Zql_lpd_enable_Object = MibScalar
zql_lpd_enable = _Zql_lpd_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 3, 1),
    _Zql_lpd_enable_Type()
)
zql_lpd_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_lpd_enable.setStatus("current")
_Zql_ip_tcp_ObjectIdentity = ObjectIdentity
zql_ip_tcp = _Zql_ip_tcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 4)
)
_Zql_tcp_enable_Type = OctetString
_Zql_tcp_enable_Object = MibScalar
zql_tcp_enable = _Zql_tcp_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 4, 1),
    _Zql_tcp_enable_Type()
)
zql_tcp_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_tcp_enable.setStatus("current")
_Zql_ip_udp_ObjectIdentity = ObjectIdentity
zql_ip_udp = _Zql_ip_udp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 5)
)
_Zql_udp_enable_Type = OctetString
_Zql_udp_enable_Object = MibScalar
zql_udp_enable = _Zql_udp_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 5, 1),
    _Zql_udp_enable_Type()
)
zql_udp_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_udp_enable.setStatus("current")
_Zql_ip_http_ObjectIdentity = ObjectIdentity
zql_ip_http = _Zql_ip_http_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 6)
)
_Zql_http_enable_Type = OctetString
_Zql_http_enable_Object = MibScalar
zql_http_enable = _Zql_http_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 6, 1),
    _Zql_http_enable_Type()
)
zql_http_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_http_enable.setStatus("current")
_Zql_ip_smtp_ObjectIdentity = ObjectIdentity
zql_ip_smtp = _Zql_ip_smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 7)
)
_Zql_smtp_enable_Type = OctetString
_Zql_smtp_enable_Object = MibScalar
zql_smtp_enable = _Zql_smtp_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 7, 1),
    _Zql_smtp_enable_Type()
)
zql_smtp_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_smtp_enable.setStatus("current")
_Zql_smtp_server_addr_Type = OctetString
_Zql_smtp_server_addr_Object = MibScalar
zql_smtp_server_addr = _Zql_smtp_server_addr_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 7, 2),
    _Zql_smtp_server_addr_Type()
)
zql_smtp_server_addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_smtp_server_addr.setStatus("current")
_Zql_ip_pop3_ObjectIdentity = ObjectIdentity
zql_ip_pop3 = _Zql_ip_pop3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 8)
)
_Zql_pop3_enable_Type = OctetString
_Zql_pop3_enable_Object = MibScalar
zql_pop3_enable = _Zql_pop3_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 8, 1),
    _Zql_pop3_enable_Type()
)
zql_pop3_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_pop3_enable.setStatus("current")
_Zql_pop3_print_headers_Type = OctetString
_Zql_pop3_print_headers_Object = MibScalar
zql_pop3_print_headers = _Zql_pop3_print_headers_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 8, 2),
    _Zql_pop3_print_headers_Type()
)
zql_pop3_print_headers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_pop3_print_headers.setStatus("current")
_Zql_pop3_verbose_headers_Type = OctetString
_Zql_pop3_verbose_headers_Object = MibScalar
zql_pop3_verbose_headers = _Zql_pop3_verbose_headers_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 8, 3),
    _Zql_pop3_verbose_headers_Type()
)
zql_pop3_verbose_headers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_pop3_verbose_headers.setStatus("current")
_Zql_pop3_print_body_Type = OctetString
_Zql_pop3_print_body_Object = MibScalar
zql_pop3_print_body = _Zql_pop3_print_body_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 8, 4),
    _Zql_pop3_print_body_Type()
)
zql_pop3_print_body.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_pop3_print_body.setStatus("current")
_Zql_pop3_save_attachments_Type = OctetString
_Zql_pop3_save_attachments_Object = MibScalar
zql_pop3_save_attachments = _Zql_pop3_save_attachments_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 8, 5),
    _Zql_pop3_save_attachments_Type()
)
zql_pop3_save_attachments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_pop3_save_attachments.setStatus("current")
_Zql_pop3_poll_Type = OctetString
_Zql_pop3_poll_Object = MibScalar
zql_pop3_poll = _Zql_pop3_poll_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 8, 6),
    _Zql_pop3_poll_Type()
)
zql_pop3_poll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_pop3_poll.setStatus("current")
_Zql_pop3_username_Type = OctetString
_Zql_pop3_username_Object = MibScalar
zql_pop3_username = _Zql_pop3_username_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 8, 7),
    _Zql_pop3_username_Type()
)
zql_pop3_username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_pop3_username.setStatus("current")
_Zql_pop3_password_Type = OctetString
_Zql_pop3_password_Object = MibScalar
zql_pop3_password = _Zql_pop3_password_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 8, 8),
    _Zql_pop3_password_Type()
)
zql_pop3_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_pop3_password.setStatus("current")
_Zql_pop3_server_addr_Type = OctetString
_Zql_pop3_server_addr_Object = MibScalar
zql_pop3_server_addr = _Zql_pop3_server_addr_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 8, 9),
    _Zql_pop3_server_addr_Type()
)
zql_pop3_server_addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_pop3_server_addr.setStatus("current")
_Zql_pop3_print_attachments_Type = OctetString
_Zql_pop3_print_attachments_Object = MibScalar
zql_pop3_print_attachments = _Zql_pop3_print_attachments_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 8, 10),
    _Zql_pop3_print_attachments_Type()
)
zql_pop3_print_attachments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_pop3_print_attachments.setStatus("current")
_Zql_ip_snmp_ObjectIdentity = ObjectIdentity
zql_ip_snmp = _Zql_ip_snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 9)
)
_Zql_snmp_enable_Type = OctetString
_Zql_snmp_enable_Object = MibScalar
zql_snmp_enable = _Zql_snmp_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 9, 1),
    _Zql_snmp_enable_Type()
)
zql_snmp_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_snmp_enable.setStatus("current")
_Zql_snmp_get_community_name_Type = OctetString
_Zql_snmp_get_community_name_Object = MibScalar
zql_snmp_get_community_name = _Zql_snmp_get_community_name_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 9, 2),
    _Zql_snmp_get_community_name_Type()
)
zql_snmp_get_community_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_snmp_get_community_name.setStatus("current")
_Zql_snmp_set_community_name_Type = OctetString
_Zql_snmp_set_community_name_Object = MibScalar
zql_snmp_set_community_name = _Zql_snmp_set_community_name_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 9, 3),
    _Zql_snmp_set_community_name_Type()
)
zql_snmp_set_community_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_snmp_set_community_name.setStatus("current")
_Zql_snmp_create_mib_Type = OctetString
_Zql_snmp_create_mib_Object = MibScalar
zql_snmp_create_mib = _Zql_snmp_create_mib_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 9, 4),
    _Zql_snmp_create_mib_Type()
)
zql_snmp_create_mib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_snmp_create_mib.setStatus("current")
_Zql_ip_telnet_ObjectIdentity = ObjectIdentity
zql_ip_telnet = _Zql_ip_telnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 10)
)
_Zql_telnet_enable_Type = OctetString
_Zql_telnet_enable_Object = MibScalar
zql_telnet_enable = _Zql_telnet_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 10, 1),
    _Zql_telnet_enable_Type()
)
zql_telnet_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_telnet_enable.setStatus("current")
_Zql_telnet_disconnect_Type = OctetString
_Zql_telnet_disconnect_Object = MibScalar
zql_telnet_disconnect = _Zql_telnet_disconnect_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 10, 2),
    _Zql_telnet_disconnect_Type()
)
zql_telnet_disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_telnet_disconnect.setStatus("current")
_Zql_ip_addr_Type = OctetString
_Zql_ip_addr_Object = MibScalar
zql_ip_addr = _Zql_ip_addr_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 11),
    _Zql_ip_addr_Type()
)
zql_ip_addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_ip_addr.setStatus("current")
_Zql_ip_netmask_Type = OctetString
_Zql_ip_netmask_Object = MibScalar
zql_ip_netmask = _Zql_ip_netmask_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 12),
    _Zql_ip_netmask_Type()
)
zql_ip_netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_ip_netmask.setStatus("current")
_Zql_ip_gateway_Type = OctetString
_Zql_ip_gateway_Object = MibScalar
zql_ip_gateway = _Zql_ip_gateway_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 13),
    _Zql_ip_gateway_Type()
)
zql_ip_gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_ip_gateway.setStatus("current")
_Zql_ip_port_Type = OctetString
_Zql_ip_port_Object = MibScalar
zql_ip_port = _Zql_ip_port_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 14),
    _Zql_ip_port_Type()
)
zql_ip_port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_ip_port.setStatus("current")
_Zql_ip_remote_Type = OctetString
_Zql_ip_remote_Object = MibScalar
zql_ip_remote = _Zql_ip_remote_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 15),
    _Zql_ip_remote_Type()
)
zql_ip_remote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_ip_remote.setStatus("current")
_Zql_ip_ping_remote_Type = OctetString
_Zql_ip_ping_remote_Object = MibScalar
zql_ip_ping_remote = _Zql_ip_ping_remote_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 16),
    _Zql_ip_ping_remote_Type()
)
zql_ip_ping_remote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_ip_ping_remote.setStatus("current")
_Zql_ip_netstat_Type = OctetString
_Zql_ip_netstat_Object = MibScalar
zql_ip_netstat = _Zql_ip_netstat_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 17),
    _Zql_ip_netstat_Type()
)
zql_ip_netstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_ip_netstat.setStatus("current")
_Zql_ip_remote_port_Type = OctetString
_Zql_ip_remote_port_Object = MibScalar
zql_ip_remote_port = _Zql_ip_remote_port_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 18),
    _Zql_ip_remote_port_Type()
)
zql_ip_remote_port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_ip_remote_port.setStatus("current")
_Zql_ip_bootp_ObjectIdentity = ObjectIdentity
zql_ip_bootp = _Zql_ip_bootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 20)
)
_Zql_bootp_enable_Type = OctetString
_Zql_bootp_enable_Object = MibScalar
zql_bootp_enable = _Zql_bootp_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 20, 1),
    _Zql_bootp_enable_Type()
)
zql_bootp_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_bootp_enable.setStatus("current")
_Zql_ip_mirror_ObjectIdentity = ObjectIdentity
zql_ip_mirror = _Zql_ip_mirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21)
)
_Zql_mirror_auto_Type = OctetString
_Zql_mirror_auto_Object = MibScalar
zql_mirror_auto = _Zql_mirror_auto_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 1),
    _Zql_mirror_auto_Type()
)
zql_mirror_auto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_mirror_auto.setStatus("current")
_Zql_mirror_username_Type = OctetString
_Zql_mirror_username_Object = MibScalar
zql_mirror_username = _Zql_mirror_username_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 2),
    _Zql_mirror_username_Type()
)
zql_mirror_username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_mirror_username.setStatus("current")
_Zql_mirror_password_Type = OctetString
_Zql_mirror_password_Object = MibScalar
zql_mirror_password = _Zql_mirror_password_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 3),
    _Zql_mirror_password_Type()
)
zql_mirror_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_mirror_password.setStatus("current")
_Zql_mirror_server_Type = OctetString
_Zql_mirror_server_Object = MibScalar
zql_mirror_server = _Zql_mirror_server_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 4),
    _Zql_mirror_server_Type()
)
zql_mirror_server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_mirror_server.setStatus("current")
_Zql_mirror_path_Type = OctetString
_Zql_mirror_path_Object = MibScalar
zql_mirror_path = _Zql_mirror_path_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 5),
    _Zql_mirror_path_Type()
)
zql_mirror_path.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_mirror_path.setStatus("current")
_Zql_mirror_freq_Type = OctetString
_Zql_mirror_freq_Object = MibScalar
zql_mirror_freq = _Zql_mirror_freq_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 6),
    _Zql_mirror_freq_Type()
)
zql_mirror_freq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_mirror_freq.setStatus("current")
_Zql_mirror_fetch_Type = OctetString
_Zql_mirror_fetch_Object = MibScalar
zql_mirror_fetch = _Zql_mirror_fetch_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 7),
    _Zql_mirror_fetch_Type()
)
zql_mirror_fetch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_mirror_fetch.setStatus("current")
_Zql_mirror_version_Type = OctetString
_Zql_mirror_version_Object = MibScalar
zql_mirror_version = _Zql_mirror_version_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 8),
    _Zql_mirror_version_Type()
)
zql_mirror_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_mirror_version.setStatus("current")
_Zql_mirror_freq_hours_Type = OctetString
_Zql_mirror_freq_hours_Object = MibScalar
zql_mirror_freq_hours = _Zql_mirror_freq_hours_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 9),
    _Zql_mirror_freq_hours_Type()
)
zql_mirror_freq_hours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_mirror_freq_hours.setStatus("current")
_Zql_mirror_error_retry_Type = OctetString
_Zql_mirror_error_retry_Object = MibScalar
zql_mirror_error_retry = _Zql_mirror_error_retry_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 10),
    _Zql_mirror_error_retry_Type()
)
zql_mirror_error_retry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_mirror_error_retry.setStatus("current")
_Zql_mirror_feedback_ObjectIdentity = ObjectIdentity
zql_mirror_feedback = _Zql_mirror_feedback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 11)
)
_Zql_feedback_auto_Type = OctetString
_Zql_feedback_auto_Object = MibScalar
zql_feedback_auto = _Zql_feedback_auto_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 11, 1),
    _Zql_feedback_auto_Type()
)
zql_feedback_auto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_feedback_auto.setStatus("current")
_Zql_feedback_path_Type = OctetString
_Zql_feedback_path_Object = MibScalar
zql_feedback_path = _Zql_feedback_path_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 11, 2),
    _Zql_feedback_path_Type()
)
zql_feedback_path.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_feedback_path.setStatus("current")
_Zql_feedback_freq_Type = OctetString
_Zql_feedback_freq_Object = MibScalar
zql_feedback_freq = _Zql_feedback_freq_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 11, 3),
    _Zql_feedback_freq_Type()
)
zql_feedback_freq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_feedback_freq.setStatus("current")
_Zql_mirror_success_Type = OctetString
_Zql_mirror_success_Object = MibScalar
zql_mirror_success = _Zql_mirror_success_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 12),
    _Zql_mirror_success_Type()
)
zql_mirror_success.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_mirror_success.setStatus("current")
_Zql_mirror_success_time_Type = OctetString
_Zql_mirror_success_time_Object = MibScalar
zql_mirror_success_time = _Zql_mirror_success_time_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 13),
    _Zql_mirror_success_time_Type()
)
zql_mirror_success_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_mirror_success_time.setStatus("current")
_Zql_mirror_last_time_Type = OctetString
_Zql_mirror_last_time_Object = MibScalar
zql_mirror_last_time = _Zql_mirror_last_time_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 14),
    _Zql_mirror_last_time_Type()
)
zql_mirror_last_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_mirror_last_time.setStatus("current")
_Zql_mirror_last_error_Type = OctetString
_Zql_mirror_last_error_Object = MibScalar
zql_mirror_last_error = _Zql_mirror_last_error_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 15),
    _Zql_mirror_last_error_Type()
)
zql_mirror_last_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_mirror_last_error.setStatus("current")
_Zql_mirror_mode_Type = OctetString
_Zql_mirror_mode_Object = MibScalar
zql_mirror_mode = _Zql_mirror_mode_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 21, 17),
    _Zql_mirror_mode_Type()
)
zql_mirror_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_mirror_mode.setStatus("current")
_Zql_ip_ping_len_Type = OctetString
_Zql_ip_ping_len_Object = MibScalar
zql_ip_ping_len = _Zql_ip_ping_len_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 24),
    _Zql_ip_ping_len_Type()
)
zql_ip_ping_len.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_ip_ping_len.setStatus("current")
_Zql_ip_dns_ObjectIdentity = ObjectIdentity
zql_ip_dns = _Zql_ip_dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 25)
)
_Zql_dns_domain_Type = OctetString
_Zql_dns_domain_Object = MibScalar
zql_dns_domain = _Zql_dns_domain_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 25, 1),
    _Zql_dns_domain_Type()
)
zql_dns_domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_dns_domain.setStatus("current")
_Zql_dns_servers_Type = OctetString
_Zql_dns_servers_Object = MibScalar
zql_dns_servers = _Zql_dns_servers_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 25, 2),
    _Zql_dns_servers_Type()
)
zql_dns_servers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_dns_servers.setStatus("current")
_Zql_ip_discovery_ObjectIdentity = ObjectIdentity
zql_ip_discovery = _Zql_ip_discovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 26)
)
_Zql_discovery_enable_Type = OctetString
_Zql_discovery_enable_Object = MibScalar
zql_discovery_enable = _Zql_discovery_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 26, 1),
    _Zql_discovery_enable_Type()
)
zql_discovery_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_discovery_enable.setStatus("current")
_Zql_discovery_port_Type = OctetString
_Zql_discovery_port_Object = MibScalar
zql_discovery_port = _Zql_discovery_port_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 26, 2),
    _Zql_discovery_port_Type()
)
zql_discovery_port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_discovery_port.setStatus("current")
_Zql_ip_roam_packet_Type = OctetString
_Zql_ip_roam_packet_Object = MibScalar
zql_ip_roam_packet = _Zql_ip_roam_packet_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 5, 27),
    _Zql_ip_roam_packet_Type()
)
zql_ip_roam_packet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_ip_roam_packet.setStatus("current")
_Zql_ql_label_ObjectIdentity = ObjectIdentity
zql_ql_label = _Zql_ql_label_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 6)
)
_Zql_label_x_move_Type = OctetString
_Zql_label_x_move_Object = MibScalar
zql_label_x_move = _Zql_label_x_move_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 6, 1),
    _Zql_label_x_move_Type()
)
zql_label_x_move.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_label_x_move.setStatus("current")
_Zql_label_y_move_Type = OctetString
_Zql_label_y_move_Object = MibScalar
zql_label_y_move = _Zql_label_y_move_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 6, 2),
    _Zql_label_y_move_Type()
)
zql_label_y_move.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_label_y_move.setStatus("current")
_Zql_ql_motor_ObjectIdentity = ObjectIdentity
zql_ql_motor = _Zql_ql_motor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 7)
)
_Zql_ql_media_ObjectIdentity = ObjectIdentity
zql_ql_media = _Zql_ql_media_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8)
)
_Zql_media_status_Type = OctetString
_Zql_media_status_Object = MibScalar
zql_media_status = _Zql_media_status_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 1),
    _Zql_media_status_Type()
)
zql_media_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_media_status.setStatus("current")
_Zql_media_sense_mode_Type = OctetString
_Zql_media_sense_mode_Object = MibScalar
zql_media_sense_mode = _Zql_media_sense_mode_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 2),
    _Zql_media_sense_mode_Type()
)
zql_media_sense_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_media_sense_mode.setStatus("current")
_Zql_media_tof_Type = OctetString
_Zql_media_tof_Object = MibScalar
zql_media_tof = _Zql_media_tof_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 3),
    _Zql_media_tof_Type()
)
zql_media_tof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_media_tof.setStatus("current")
_Zql_media_type_Type = OctetString
_Zql_media_type_Object = MibScalar
zql_media_type = _Zql_media_type_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 4),
    _Zql_media_type_Type()
)
zql_media_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_media_type.setStatus("current")
_Zql_media_width_sense_ObjectIdentity = ObjectIdentity
zql_media_width_sense = _Zql_media_width_sense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 5)
)
_Zql_width_sense_enable_Type = OctetString
_Zql_width_sense_enable_Object = MibScalar
zql_width_sense_enable = _Zql_width_sense_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 5, 1),
    _Zql_width_sense_enable_Type()
)
zql_width_sense_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_width_sense_enable.setStatus("current")
_Zql_width_sense_in_mm_Type = OctetString
_Zql_width_sense_in_mm_Object = MibScalar
zql_width_sense_in_mm = _Zql_width_sense_in_mm_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 5, 2),
    _Zql_width_sense_in_mm_Type()
)
zql_width_sense_in_mm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_width_sense_in_mm.setStatus("current")
_Zql_width_sense_in_cm_Type = OctetString
_Zql_width_sense_in_cm_Object = MibScalar
zql_width_sense_in_cm = _Zql_width_sense_in_cm_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 5, 3),
    _Zql_width_sense_in_cm_Type()
)
zql_width_sense_in_cm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_width_sense_in_cm.setStatus("current")
_Zql_width_sense_in_dots_Type = OctetString
_Zql_width_sense_in_dots_Object = MibScalar
zql_width_sense_in_dots = _Zql_width_sense_in_dots_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 5, 4),
    _Zql_width_sense_in_dots_Type()
)
zql_width_sense_in_dots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_width_sense_in_dots.setStatus("current")
_Zql_width_sense_in_inches_Type = OctetString
_Zql_width_sense_in_inches_Object = MibScalar
zql_width_sense_in_inches = _Zql_width_sense_in_inches_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 5, 5),
    _Zql_width_sense_in_inches_Type()
)
zql_width_sense_in_inches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_width_sense_in_inches.setStatus("current")
_Zql_media_measure_label_Type = OctetString
_Zql_media_measure_label_Object = MibScalar
zql_media_measure_label = _Zql_media_measure_label_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 11),
    _Zql_media_measure_label_Type()
)
zql_media_measure_label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_media_measure_label.setStatus("current")
_Zql_media_measured_lbl_height_ObjectIdentity = ObjectIdentity
zql_media_measured_lbl_height = _Zql_media_measured_lbl_height_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 12)
)
_Zql_measured_lbl_height_min_Type = OctetString
_Zql_measured_lbl_height_min_Object = MibScalar
zql_measured_lbl_height_min = _Zql_measured_lbl_height_min_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 12, 1),
    _Zql_measured_lbl_height_min_Type()
)
zql_measured_lbl_height_min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_measured_lbl_height_min.setStatus("current")
_Zql_measured_lbl_height_max_Type = OctetString
_Zql_measured_lbl_height_max_Object = MibScalar
zql_measured_lbl_height_max = _Zql_measured_lbl_height_max_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 12, 2),
    _Zql_measured_lbl_height_max_Type()
)
zql_measured_lbl_height_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_measured_lbl_height_max.setStatus("current")
_Zql_measured_lbl_height_avg_Type = OctetString
_Zql_measured_lbl_height_avg_Object = MibScalar
zql_measured_lbl_height_avg = _Zql_measured_lbl_height_avg_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 12, 3),
    _Zql_measured_lbl_height_avg_Type()
)
zql_measured_lbl_height_avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_measured_lbl_height_avg.setStatus("current")
_Zql_measured_lbl_height_std_dev_Type = OctetString
_Zql_measured_lbl_height_std_dev_Object = MibScalar
zql_measured_lbl_height_std_dev = _Zql_measured_lbl_height_std_dev_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 8, 12, 4),
    _Zql_measured_lbl_height_std_dev_Type()
)
zql_measured_lbl_height_std_dev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_measured_lbl_height_std_dev.setStatus("current")
_Zql_ql_sensor_ObjectIdentity = ObjectIdentity
zql_ql_sensor = _Zql_ql_sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 9)
)
_Zql_sensor_paper_supply_Type = OctetString
_Zql_sensor_paper_supply_Object = MibScalar
zql_sensor_paper_supply = _Zql_sensor_paper_supply_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 9, 2),
    _Zql_sensor_paper_supply_Type()
)
zql_sensor_paper_supply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_sensor_paper_supply.setStatus("current")
_Zql_sensor_peeler_Type = OctetString
_Zql_sensor_peeler_Object = MibScalar
zql_sensor_peeler = _Zql_sensor_peeler_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 9, 3),
    _Zql_sensor_peeler_Type()
)
zql_sensor_peeler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_sensor_peeler.setStatus("current")
_Zql_ql_srf_ObjectIdentity = ObjectIdentity
zql_ql_srf = _Zql_ql_srf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 10)
)
_Zql_ql_wlan_ObjectIdentity = ObjectIdentity
zql_ql_wlan = _Zql_ql_wlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11)
)
_Zql_wlan_operating_mode_Type = OctetString
_Zql_wlan_operating_mode_Object = MibScalar
zql_wlan_operating_mode = _Zql_wlan_operating_mode_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 1),
    _Zql_wlan_operating_mode_Type()
)
zql_wlan_operating_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_operating_mode.setStatus("current")
_Zql_wlan_essid_Type = OctetString
_Zql_wlan_essid_Object = MibScalar
zql_wlan_essid = _Zql_wlan_essid_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 2),
    _Zql_wlan_essid_Type()
)
zql_wlan_essid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_essid.setStatus("current")
_Zql_wlan_current_essid_Type = OctetString
_Zql_wlan_current_essid_Object = MibScalar
zql_wlan_current_essid = _Zql_wlan_current_essid_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 3),
    _Zql_wlan_current_essid_Type()
)
zql_wlan_current_essid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wlan_current_essid.setStatus("current")
_Zql_wlan_station_name_Type = OctetString
_Zql_wlan_station_name_Object = MibScalar
zql_wlan_station_name = _Zql_wlan_station_name_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 4),
    _Zql_wlan_station_name_Type()
)
zql_wlan_station_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_station_name.setStatus("current")
_Zql_wlan_current_tx_rate_Type = OctetString
_Zql_wlan_current_tx_rate_Object = MibScalar
zql_wlan_current_tx_rate = _Zql_wlan_current_tx_rate_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 6),
    _Zql_wlan_current_tx_rate_Type()
)
zql_wlan_current_tx_rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wlan_current_tx_rate.setStatus("current")
_Zql_wlan_encryption_mode_Type = OctetString
_Zql_wlan_encryption_mode_Object = MibScalar
zql_wlan_encryption_mode = _Zql_wlan_encryption_mode_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 7),
    _Zql_wlan_encryption_mode_Type()
)
zql_wlan_encryption_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_encryption_mode.setStatus("current")
_Zql_wlan_associated_Type = OctetString
_Zql_wlan_associated_Object = MibScalar
zql_wlan_associated = _Zql_wlan_associated_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 8),
    _Zql_wlan_associated_Type()
)
zql_wlan_associated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wlan_associated.setStatus("current")
_Zql_wlan_encryption_index_Type = OctetString
_Zql_wlan_encryption_index_Object = MibScalar
zql_wlan_encryption_index = _Zql_wlan_encryption_index_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 9),
    _Zql_wlan_encryption_index_Type()
)
zql_wlan_encryption_index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_encryption_index.setStatus("current")
_Zql_wlan_encryption_key1_Type = OctetString
_Zql_wlan_encryption_key1_Object = MibScalar
zql_wlan_encryption_key1 = _Zql_wlan_encryption_key1_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 10),
    _Zql_wlan_encryption_key1_Type()
)
zql_wlan_encryption_key1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_encryption_key1.setStatus("current")
_Zql_wlan_encryption_key2_Type = OctetString
_Zql_wlan_encryption_key2_Object = MibScalar
zql_wlan_encryption_key2 = _Zql_wlan_encryption_key2_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 11),
    _Zql_wlan_encryption_key2_Type()
)
zql_wlan_encryption_key2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_encryption_key2.setStatus("current")
_Zql_wlan_encryption_key3_Type = OctetString
_Zql_wlan_encryption_key3_Object = MibScalar
zql_wlan_encryption_key3 = _Zql_wlan_encryption_key3_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 12),
    _Zql_wlan_encryption_key3_Type()
)
zql_wlan_encryption_key3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_encryption_key3.setStatus("current")
_Zql_wlan_encryption_key4_Type = OctetString
_Zql_wlan_encryption_key4_Object = MibScalar
zql_wlan_encryption_key4 = _Zql_wlan_encryption_key4_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 13),
    _Zql_wlan_encryption_key4_Type()
)
zql_wlan_encryption_key4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_encryption_key4.setStatus("current")
_Zql_wlan_leap_mode_Type = OctetString
_Zql_wlan_leap_mode_Object = MibScalar
zql_wlan_leap_mode = _Zql_wlan_leap_mode_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 14),
    _Zql_wlan_leap_mode_Type()
)
zql_wlan_leap_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_leap_mode.setStatus("current")
_Zql_wlan_leap_username_Type = OctetString
_Zql_wlan_leap_username_Object = MibScalar
zql_wlan_leap_username = _Zql_wlan_leap_username_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 15),
    _Zql_wlan_leap_username_Type()
)
zql_wlan_leap_username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_leap_username.setStatus("current")
_Zql_wlan_leap_password_Type = OctetString
_Zql_wlan_leap_password_Object = MibScalar
zql_wlan_leap_password = _Zql_wlan_leap_password_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 16),
    _Zql_wlan_leap_password_Type()
)
zql_wlan_leap_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_leap_password.setStatus("current")
_Zql_wlan_power_save_Type = OctetString
_Zql_wlan_power_save_Object = MibScalar
zql_wlan_power_save = _Zql_wlan_power_save_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 17),
    _Zql_wlan_power_save_Type()
)
zql_wlan_power_save.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_power_save.setStatus("current")
_Zql_wlan_test_ObjectIdentity = ObjectIdentity
zql_wlan_test = _Zql_wlan_test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 18)
)
_Zql_wlan_auth_type_Type = OctetString
_Zql_wlan_auth_type_Object = MibScalar
zql_wlan_auth_type = _Zql_wlan_auth_type_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 20),
    _Zql_wlan_auth_type_Type()
)
zql_wlan_auth_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_auth_type.setStatus("current")
_Zql_wlan_preamble_Type = OctetString
_Zql_wlan_preamble_Object = MibScalar
zql_wlan_preamble = _Zql_wlan_preamble_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 21),
    _Zql_wlan_preamble_Type()
)
zql_wlan_preamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_preamble.setStatus("current")
_Zql_wlan_bssid_Type = OctetString
_Zql_wlan_bssid_Object = MibScalar
zql_wlan_bssid = _Zql_wlan_bssid_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 22),
    _Zql_wlan_bssid_Type()
)
zql_wlan_bssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wlan_bssid.setStatus("current")
_Zql_wlan_firmware_version_Type = OctetString
_Zql_wlan_firmware_version_Object = MibScalar
zql_wlan_firmware_version = _Zql_wlan_firmware_version_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 24),
    _Zql_wlan_firmware_version_Type()
)
zql_wlan_firmware_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wlan_firmware_version.setStatus("current")
_Zql_wlan_signal_strength_Type = OctetString
_Zql_wlan_signal_strength_Object = MibScalar
zql_wlan_signal_strength = _Zql_wlan_signal_strength_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 25),
    _Zql_wlan_signal_strength_Type()
)
zql_wlan_signal_strength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wlan_signal_strength.setStatus("current")
_Zql_wlan_current_freq_Type = OctetString
_Zql_wlan_current_freq_Object = MibScalar
zql_wlan_current_freq = _Zql_wlan_current_freq_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 28),
    _Zql_wlan_current_freq_Type()
)
zql_wlan_current_freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wlan_current_freq.setStatus("current")
_Zql_wlan_roam_ObjectIdentity = ObjectIdentity
zql_wlan_roam = _Zql_wlan_roam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 31)
)
_Zql_roam_signal_Type = OctetString
_Zql_roam_signal_Object = MibScalar
zql_roam_signal = _Zql_roam_signal_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 31, 1),
    _Zql_roam_signal_Type()
)
zql_roam_signal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_roam_signal.setStatus("current")
_Zql_roam_interval_Type = OctetString
_Zql_roam_interval_Object = MibScalar
zql_roam_interval = _Zql_roam_interval_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 31, 2),
    _Zql_roam_interval_Type()
)
zql_roam_interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_roam_interval.setStatus("current")
_Zql_roam_interchannel_delay_Type = OctetString
_Zql_roam_interchannel_delay_Object = MibScalar
zql_roam_interchannel_delay = _Zql_roam_interchannel_delay_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 31, 4),
    _Zql_roam_interchannel_delay_Type()
)
zql_roam_interchannel_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_roam_interchannel_delay.setStatus("current")
_Zql_roam_max_chan_scan_time_Type = OctetString
_Zql_roam_max_chan_scan_time_Object = MibScalar
zql_roam_max_chan_scan_time = _Zql_roam_max_chan_scan_time_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 31, 5),
    _Zql_roam_max_chan_scan_time_Type()
)
zql_roam_max_chan_scan_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_roam_max_chan_scan_time.setStatus("current")
_Zql_roam_rssi_Type = OctetString
_Zql_roam_rssi_Object = MibScalar
zql_roam_rssi = _Zql_roam_rssi_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 31, 6),
    _Zql_roam_rssi_Type()
)
zql_roam_rssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_roam_rssi.setStatus("current")
_Zql_roam_max_fail_Type = OctetString
_Zql_roam_max_fail_Object = MibScalar
zql_roam_max_fail = _Zql_roam_max_fail_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 31, 7),
    _Zql_roam_max_fail_Type()
)
zql_roam_max_fail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_roam_max_fail.setStatus("current")
_Zql_wlan_channel_Type = OctetString
_Zql_wlan_channel_Object = MibScalar
zql_wlan_channel = _Zql_wlan_channel_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 35),
    _Zql_wlan_channel_Type()
)
zql_wlan_channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wlan_channel.setStatus("current")
_Zql_wlan_wpa_ObjectIdentity = ObjectIdentity
zql_wlan_wpa = _Zql_wlan_wpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 36)
)
_Zql_wpa_enable_Type = OctetString
_Zql_wpa_enable_Object = MibScalar
zql_wpa_enable = _Zql_wpa_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 36, 1),
    _Zql_wpa_enable_Type()
)
zql_wpa_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wpa_enable.setStatus("current")
_Zql_wpa_authentication_Type = OctetString
_Zql_wpa_authentication_Object = MibScalar
zql_wpa_authentication = _Zql_wpa_authentication_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 36, 2),
    _Zql_wpa_authentication_Type()
)
zql_wpa_authentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wpa_authentication.setStatus("current")
_Zql_wpa_psk_Type = OctetString
_Zql_wpa_psk_Object = MibScalar
zql_wpa_psk = _Zql_wpa_psk_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 36, 3),
    _Zql_wpa_psk_Type()
)
zql_wpa_psk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wpa_psk.setStatus("current")
_Zql_wpa_wpa_version_Type = OctetString
_Zql_wpa_wpa_version_Object = MibScalar
zql_wpa_wpa_version = _Zql_wpa_wpa_version_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 36, 5),
    _Zql_wpa_wpa_version_Type()
)
zql_wpa_wpa_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wpa_wpa_version.setStatus("current")
_Zql_wpa_groupkey_ciphersuite_Type = OctetString
_Zql_wpa_groupkey_ciphersuite_Object = MibScalar
zql_wpa_groupkey_ciphersuite = _Zql_wpa_groupkey_ciphersuite_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 36, 6),
    _Zql_wpa_groupkey_ciphersuite_Type()
)
zql_wpa_groupkey_ciphersuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wpa_groupkey_ciphersuite.setStatus("current")
_Zql_wpa_pairwise_ciphersuite_Type = OctetString
_Zql_wpa_pairwise_ciphersuite_Object = MibScalar
zql_wpa_pairwise_ciphersuite = _Zql_wpa_pairwise_ciphersuite_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 36, 7),
    _Zql_wpa_pairwise_ciphersuite_Type()
)
zql_wpa_pairwise_ciphersuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wpa_pairwise_ciphersuite.setStatus("current")
_Zql_wlan_8021x_ObjectIdentity = ObjectIdentity
zql_wlan_8021x = _Zql_wlan_8021x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 37)
)
_Zql_8021x_enable_Type = OctetString
_Zql_8021x_enable_Object = MibScalar
zql_8021x_enable = _Zql_8021x_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 37, 1),
    _Zql_8021x_enable_Type()
)
zql_8021x_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_8021x_enable.setStatus("current")
_Zql_8021x_authentication_Type = OctetString
_Zql_8021x_authentication_Object = MibScalar
zql_8021x_authentication = _Zql_8021x_authentication_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 37, 2),
    _Zql_8021x_authentication_Type()
)
zql_8021x_authentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_8021x_authentication.setStatus("current")
_Zql_8021x_peap_ObjectIdentity = ObjectIdentity
zql_8021x_peap = _Zql_8021x_peap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 37, 3)
)
_Zql_peap_peap_username_Type = OctetString
_Zql_peap_peap_username_Object = MibScalar
zql_peap_peap_username = _Zql_peap_peap_username_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 37, 3, 1),
    _Zql_peap_peap_username_Type()
)
zql_peap_peap_username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_peap_peap_username.setStatus("current")
_Zql_peap_peap_password_Type = OctetString
_Zql_peap_peap_password_Object = MibScalar
zql_peap_peap_password = _Zql_peap_peap_password_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 37, 3, 2),
    _Zql_peap_peap_password_Type()
)
zql_peap_peap_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_peap_peap_password.setStatus("current")
_Zql_peap_privkey_password_Type = OctetString
_Zql_peap_privkey_password_Object = MibScalar
zql_peap_privkey_password = _Zql_peap_privkey_password_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 37, 3, 3),
    _Zql_peap_privkey_password_Type()
)
zql_peap_privkey_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_peap_privkey_password.setStatus("current")
_Zql_8021x_eap_ObjectIdentity = ObjectIdentity
zql_8021x_eap = _Zql_8021x_eap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 37, 4)
)
_Zql_eap_username_Type = OctetString
_Zql_eap_username_Object = MibScalar
zql_eap_username = _Zql_eap_username_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 37, 4, 1),
    _Zql_eap_username_Type()
)
zql_eap_username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_eap_username.setStatus("current")
_Zql_eap_password_Type = OctetString
_Zql_eap_password_Object = MibScalar
zql_eap_password = _Zql_eap_password_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 37, 4, 2),
    _Zql_eap_password_Type()
)
zql_eap_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_eap_password.setStatus("current")
_Zql_eap_privkey_password_Type = OctetString
_Zql_eap_privkey_password_Object = MibScalar
zql_eap_privkey_password = _Zql_eap_privkey_password_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 37, 4, 3),
    _Zql_eap_privkey_password_Type()
)
zql_eap_privkey_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_eap_privkey_password.setStatus("current")
_Zql_wlan_adhocchannel_Type = OctetString
_Zql_wlan_adhocchannel_Object = MibScalar
zql_wlan_adhocchannel = _Zql_wlan_adhocchannel_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 38),
    _Zql_wlan_adhocchannel_Type()
)
zql_wlan_adhocchannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_adhocchannel.setStatus("current")
_Zql_wlan_adhocautomode_Type = OctetString
_Zql_wlan_adhocautomode_Object = MibScalar
zql_wlan_adhocautomode = _Zql_wlan_adhocautomode_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 39),
    _Zql_wlan_adhocautomode_Type()
)
zql_wlan_adhocautomode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_adhocautomode.setStatus("current")
_Zql_wlan_enable_Type = OctetString
_Zql_wlan_enable_Object = MibScalar
zql_wlan_enable = _Zql_wlan_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 40),
    _Zql_wlan_enable_Type()
)
zql_wlan_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_enable.setStatus("current")
_Zql_wlan_encryption_optional_Type = OctetString
_Zql_wlan_encryption_optional_Object = MibScalar
zql_wlan_encryption_optional = _Zql_wlan_encryption_optional_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 41),
    _Zql_wlan_encryption_optional_Type()
)
zql_wlan_encryption_optional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_encryption_optional.setStatus("current")
_Zql_wlan_adhoc_last_channel_Type = OctetString
_Zql_wlan_adhoc_last_channel_Object = MibScalar
zql_wlan_adhoc_last_channel = _Zql_wlan_adhoc_last_channel_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 42),
    _Zql_wlan_adhoc_last_channel_Type()
)
zql_wlan_adhoc_last_channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_wlan_adhoc_last_channel.setStatus("current")
_Zql_wlan_secure_ssid_Type = OctetString
_Zql_wlan_secure_ssid_Object = MibScalar
zql_wlan_secure_ssid = _Zql_wlan_secure_ssid_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 43),
    _Zql_wlan_secure_ssid_Type()
)
zql_wlan_secure_ssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_secure_ssid.setStatus("current")
_Zql_wlan_ip_ObjectIdentity = ObjectIdentity
zql_wlan_ip = _Zql_wlan_ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 44)
)
_Zql_wlan_ip_addr_Type = OctetString
_Zql_wlan_ip_addr_Object = MibScalar
zql_wlan_ip_addr = _Zql_wlan_ip_addr_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 44, 1),
    _Zql_wlan_ip_addr_Type()
)
zql_wlan_ip_addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_ip_addr.setStatus("current")
_Zql_wlan_ip_netmask_Type = OctetString
_Zql_wlan_ip_netmask_Object = MibScalar
zql_wlan_ip_netmask = _Zql_wlan_ip_netmask_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 44, 2),
    _Zql_wlan_ip_netmask_Type()
)
zql_wlan_ip_netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_wlan_ip_netmask.setStatus("current")
_Zql_wlan_keep_alive_ObjectIdentity = ObjectIdentity
zql_wlan_keep_alive = _Zql_wlan_keep_alive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 45)
)
_Zql_keep_alive_enable_Type = OctetString
_Zql_keep_alive_enable_Object = MibScalar
zql_keep_alive_enable = _Zql_keep_alive_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 45, 1),
    _Zql_keep_alive_enable_Type()
)
zql_keep_alive_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_keep_alive_enable.setStatus("current")
_Zql_keep_alive_timeout_Type = OctetString
_Zql_keep_alive_timeout_Object = MibScalar
zql_keep_alive_timeout = _Zql_keep_alive_timeout_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 11, 45, 2),
    _Zql_keep_alive_timeout_Type()
)
zql_keep_alive_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_keep_alive_timeout.setStatus("current")
_Zql_ql_display_ObjectIdentity = ObjectIdentity
zql_ql_display = _Zql_ql_display_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 12)
)
_Zql_display_contrast_Type = OctetString
_Zql_display_contrast_Object = MibScalar
zql_display_contrast = _Zql_display_contrast_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 12, 1),
    _Zql_display_contrast_Type()
)
zql_display_contrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_display_contrast.setStatus("current")
_Zql_display_text_Type = OctetString
_Zql_display_text_Object = MibScalar
zql_display_text = _Zql_display_text_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 12, 2),
    _Zql_display_text_Type()
)
zql_display_text.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_display_text.setStatus("current")
_Zql_display_backlight_Type = OctetString
_Zql_display_backlight_Object = MibScalar
zql_display_backlight = _Zql_display_backlight_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 12, 3),
    _Zql_display_backlight_Type()
)
zql_display_backlight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_display_backlight.setStatus("current")
_Zql_display_backlight_on_time_Type = OctetString
_Zql_display_backlight_on_time_Object = MibScalar
zql_display_backlight_on_time = _Zql_display_backlight_on_time_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 12, 8),
    _Zql_display_backlight_on_time_Type()
)
zql_display_backlight_on_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_display_backlight_on_time.setStatus("current")
_Zql_ql_memory_ObjectIdentity = ObjectIdentity
zql_ql_memory = _Zql_ql_memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 13)
)
_Zql_memory_flash_size_Type = OctetString
_Zql_memory_flash_size_Object = MibScalar
zql_memory_flash_size = _Zql_memory_flash_size_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 13, 1),
    _Zql_memory_flash_size_Type()
)
zql_memory_flash_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_memory_flash_size.setStatus("current")
_Zql_memory_ram_size_Type = OctetString
_Zql_memory_ram_size_Object = MibScalar
zql_memory_ram_size = _Zql_memory_ram_size_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 13, 2),
    _Zql_memory_ram_size_Type()
)
zql_memory_ram_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_memory_ram_size.setStatus("current")
_Zql_memory_flash_free_Type = OctetString
_Zql_memory_flash_free_Object = MibScalar
zql_memory_flash_free = _Zql_memory_flash_free_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 13, 3),
    _Zql_memory_flash_free_Type()
)
zql_memory_flash_free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_memory_flash_free.setStatus("current")
_Zql_memory_ram_free_Type = OctetString
_Zql_memory_ram_free_Object = MibScalar
zql_memory_ram_free = _Zql_memory_ram_free_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 13, 4),
    _Zql_memory_ram_free_Type()
)
zql_memory_ram_free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_memory_ram_free.setStatus("current")
_Zql_ql_power_ObjectIdentity = ObjectIdentity
zql_ql_power = _Zql_ql_power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14)
)
_Zql_power_voltage_Type = OctetString
_Zql_power_voltage_Object = MibScalar
zql_power_voltage = _Zql_power_voltage_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 1),
    _Zql_power_voltage_Type()
)
zql_power_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_voltage.setStatus("current")
_Zql_power_percent_full_Type = OctetString
_Zql_power_percent_full_Object = MibScalar
zql_power_percent_full = _Zql_power_percent_full_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 2),
    _Zql_power_percent_full_Type()
)
zql_power_percent_full.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_percent_full.setStatus("current")
_Zql_power_status_Type = OctetString
_Zql_power_status_Object = MibScalar
zql_power_status = _Zql_power_status_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 3),
    _Zql_power_status_Type()
)
zql_power_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_status.setStatus("current")
_Zql_power_low_battery_warning_Type = OctetString
_Zql_power_low_battery_warning_Object = MibScalar
zql_power_low_battery_warning = _Zql_power_low_battery_warning_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 4),
    _Zql_power_low_battery_warning_Type()
)
zql_power_low_battery_warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_low_battery_warning.setStatus("current")
_Zql_power_low_battery_shutdown_Type = OctetString
_Zql_power_low_battery_shutdown_Object = MibScalar
zql_power_low_battery_shutdown = _Zql_power_low_battery_shutdown_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 5),
    _Zql_power_low_battery_shutdown_Type()
)
zql_power_low_battery_shutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_low_battery_shutdown.setStatus("current")
_Zql_power_low_battery_timeout_Type = OctetString
_Zql_power_low_battery_timeout_Object = MibScalar
zql_power_low_battery_timeout = _Zql_power_low_battery_timeout_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 6),
    _Zql_power_low_battery_timeout_Type()
)
zql_power_low_battery_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_power_low_battery_timeout.setStatus("current")
_Zql_power_inactivity_timeout_Type = OctetString
_Zql_power_inactivity_timeout_Object = MibScalar
zql_power_inactivity_timeout = _Zql_power_inactivity_timeout_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 7),
    _Zql_power_inactivity_timeout_Type()
)
zql_power_inactivity_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_power_inactivity_timeout.setStatus("current")
_Zql_power_dtr_power_off_Type = OctetString
_Zql_power_dtr_power_off_Object = MibScalar
zql_power_dtr_power_off = _Zql_power_dtr_power_off_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 8),
    _Zql_power_dtr_power_off_Type()
)
zql_power_dtr_power_off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_power_dtr_power_off.setStatus("current")
_Zql_power_shutdown_Type = OctetString
_Zql_power_shutdown_Object = MibScalar
zql_power_shutdown = _Zql_power_shutdown_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 9),
    _Zql_power_shutdown_Type()
)
zql_power_shutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_power_shutdown.setStatus("current")
_Zql_power_ascii_graph_Type = OctetString
_Zql_power_ascii_graph_Object = MibScalar
zql_power_ascii_graph = _Zql_power_ascii_graph_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 10),
    _Zql_power_ascii_graph_Type()
)
zql_power_ascii_graph.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_ascii_graph.setStatus("current")
_Zql_power_low_battery_warning_raw_Type = OctetString
_Zql_power_low_battery_warning_raw_Object = MibScalar
zql_power_low_battery_warning_raw = _Zql_power_low_battery_warning_raw_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 11),
    _Zql_power_low_battery_warning_raw_Type()
)
zql_power_low_battery_warning_raw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_low_battery_warning_raw.setStatus("current")
_Zql_power_power_on_cycles_Type = OctetString
_Zql_power_power_on_cycles_Object = MibScalar
zql_power_power_on_cycles = _Zql_power_power_on_cycles_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 12),
    _Zql_power_power_on_cycles_Type()
)
zql_power_power_on_cycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_power_on_cycles.setStatus("current")
_Zql_power_design_voltage_Type = OctetString
_Zql_power_design_voltage_Object = MibScalar
zql_power_design_voltage = _Zql_power_design_voltage_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 16),
    _Zql_power_design_voltage_Type()
)
zql_power_design_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_design_voltage.setStatus("current")
_Zql_power_design_capacity_Type = OctetString
_Zql_power_design_capacity_Object = MibScalar
zql_power_design_capacity = _Zql_power_design_capacity_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 17),
    _Zql_power_design_capacity_Type()
)
zql_power_design_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_design_capacity.setStatus("current")
_Zql_power_manufacture_date_Type = OctetString
_Zql_power_manufacture_date_Object = MibScalar
zql_power_manufacture_date = _Zql_power_manufacture_date_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 19),
    _Zql_power_manufacture_date_Type()
)
zql_power_manufacture_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_manufacture_date.setStatus("current")
_Zql_power_relative_state_of_charge_Type = OctetString
_Zql_power_relative_state_of_charge_Object = MibScalar
zql_power_relative_state_of_charge = _Zql_power_relative_state_of_charge_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 20),
    _Zql_power_relative_state_of_charge_Type()
)
zql_power_relative_state_of_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_relative_state_of_charge.setStatus("current")
_Zql_power_serial_number_Type = OctetString
_Zql_power_serial_number_Object = MibScalar
zql_power_serial_number = _Zql_power_serial_number_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 21),
    _Zql_power_serial_number_Type()
)
zql_power_serial_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_serial_number.setStatus("current")
_Zql_power_cycle_count_Type = OctetString
_Zql_power_cycle_count_Object = MibScalar
zql_power_cycle_count = _Zql_power_cycle_count_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 23),
    _Zql_power_cycle_count_Type()
)
zql_power_cycle_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_cycle_count.setStatus("current")
_Zql_power_full_charge_capacity_Type = OctetString
_Zql_power_full_charge_capacity_Object = MibScalar
zql_power_full_charge_capacity = _Zql_power_full_charge_capacity_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 30),
    _Zql_power_full_charge_capacity_Type()
)
zql_power_full_charge_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_full_charge_capacity.setStatus("current")
_Zql_power_health_Type = OctetString
_Zql_power_health_Object = MibScalar
zql_power_health = _Zql_power_health_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 45),
    _Zql_power_health_Type()
)
zql_power_health.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_health.setStatus("current")
_Zql_power_date_first_used_Type = OctetString
_Zql_power_date_first_used_Object = MibScalar
zql_power_date_first_used = _Zql_power_date_first_used_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 14, 47),
    _Zql_power_date_first_used_Type()
)
zql_power_date_first_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_power_date_first_used.setStatus("current")
_Zql_ql_file_ObjectIdentity = ObjectIdentity
zql_ql_file = _Zql_ql_file_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 15)
)
_Zql_file_dir_Type = OctetString
_Zql_file_dir_Object = MibScalar
zql_file_dir = _Zql_file_dir_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 15, 1),
    _Zql_file_dir_Type()
)
zql_file_dir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_file_dir.setStatus("current")
_Zql_file_type_Type = OctetString
_Zql_file_type_Object = MibScalar
zql_file_type = _Zql_file_type_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 15, 2),
    _Zql_file_type_Type()
)
zql_file_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_file_type.setStatus("current")
_Zql_file_delete_Type = OctetString
_Zql_file_delete_Object = MibScalar
zql_file_delete = _Zql_file_delete_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 15, 3),
    _Zql_file_delete_Type()
)
zql_file_delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_file_delete.setStatus("current")
_Zql_file_print_Type = OctetString
_Zql_file_print_Object = MibScalar
zql_file_print = _Zql_file_print_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 15, 4),
    _Zql_file_print_Type()
)
zql_file_print.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_file_print.setStatus("current")
_Zql_file_run_Type = OctetString
_Zql_file_run_Object = MibScalar
zql_file_run = _Zql_file_run_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 15, 5),
    _Zql_file_run_Type()
)
zql_file_run.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_file_run.setStatus("current")
_Zql_file_rename_Type = OctetString
_Zql_file_rename_Object = MibScalar
zql_file_rename = _Zql_file_rename_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 15, 6),
    _Zql_file_rename_Type()
)
zql_file_rename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_file_rename.setStatus("current")
_Zql_file_append_Type = OctetString
_Zql_file_append_Object = MibScalar
zql_file_append = _Zql_file_append_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 15, 7),
    _Zql_file_append_Type()
)
zql_file_append.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_file_append.setStatus("current")
_Zql_ql_odometer_ObjectIdentity = ObjectIdentity
zql_ql_odometer = _Zql_ql_odometer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 17)
)
_Zql_odometer_user_label_count_Type = OctetString
_Zql_odometer_user_label_count_Object = MibScalar
zql_odometer_user_label_count = _Zql_odometer_user_label_count_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 17, 1),
    _Zql_odometer_user_label_count_Type()
)
zql_odometer_user_label_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_odometer_user_label_count.setStatus("current")
_Zql_odometer_total_label_count_Type = OctetString
_Zql_odometer_total_label_count_Object = MibScalar
zql_odometer_total_label_count = _Zql_odometer_total_label_count_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 17, 2),
    _Zql_odometer_total_label_count_Type()
)
zql_odometer_total_label_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_odometer_total_label_count.setStatus("current")
_Zql_odometer_total_print_length_Type = OctetString
_Zql_odometer_total_print_length_Object = MibScalar
zql_odometer_total_print_length = _Zql_odometer_total_print_length_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 17, 3),
    _Zql_odometer_total_print_length_Type()
)
zql_odometer_total_print_length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_odometer_total_print_length.setStatus("current")
_Zql_odometer_latch_open_count_Type = OctetString
_Zql_odometer_latch_open_count_Object = MibScalar
zql_odometer_latch_open_count = _Zql_odometer_latch_open_count_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 17, 5),
    _Zql_odometer_latch_open_count_Type()
)
zql_odometer_latch_open_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_odometer_latch_open_count.setStatus("current")
_Zql_odometer_label_dot_length_Type = OctetString
_Zql_odometer_label_dot_length_Object = MibScalar
zql_odometer_label_dot_length = _Zql_odometer_label_dot_length_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 17, 6),
    _Zql_odometer_label_dot_length_Type()
)
zql_odometer_label_dot_length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_odometer_label_dot_length.setStatus("current")
_Zql_odometer_rfid_ObjectIdentity = ObjectIdentity
zql_odometer_rfid = _Zql_odometer_rfid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 17, 11)
)
_Zql_ql_appl_ObjectIdentity = ObjectIdentity
zql_ql_appl = _Zql_ql_appl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 18)
)
_Zql_appl_date_Type = OctetString
_Zql_appl_date_Object = MibScalar
zql_appl_date = _Zql_appl_date_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 18, 1),
    _Zql_appl_date_Type()
)
zql_appl_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_appl_date.setStatus("current")
_Zql_appl_name_Type = OctetString
_Zql_appl_name_Object = MibScalar
zql_appl_name = _Zql_appl_name_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 18, 2),
    _Zql_appl_name_Type()
)
zql_appl_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_appl_name.setStatus("current")
_Zql_appl_version_Type = OctetString
_Zql_appl_version_Object = MibScalar
zql_appl_version = _Zql_appl_version_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 18, 3),
    _Zql_appl_version_Type()
)
zql_appl_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_appl_version.setStatus("current")
_Zql_appl_ps_ObjectIdentity = ObjectIdentity
zql_appl_ps = _Zql_appl_ps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 18, 4)
)
_Zql_ql_device_ObjectIdentity = ObjectIdentity
zql_ql_device = _Zql_ql_device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19)
)
_Zql_device_reset_Type = OctetString
_Zql_device_reset_Object = MibScalar
zql_device_reset = _Zql_device_reset_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 1),
    _Zql_device_reset_Type()
)
zql_device_reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_reset.setStatus("current")
_Zql_device_restore_defaults_Type = OctetString
_Zql_device_restore_defaults_Object = MibScalar
zql_device_restore_defaults = _Zql_device_restore_defaults_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 2),
    _Zql_device_restore_defaults_Type()
)
zql_device_restore_defaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_restore_defaults.setStatus("current")
_Zql_device_card_ObjectIdentity = ObjectIdentity
zql_device_card = _Zql_device_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 3)
)
_Zql_device_friendly_name_Type = OctetString
_Zql_device_friendly_name_Object = MibScalar
zql_device_friendly_name = _Zql_device_friendly_name_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 5),
    _Zql_device_friendly_name_Type()
)
zql_device_friendly_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_friendly_name.setStatus("current")
_Zql_device_company_name_Type = OctetString
_Zql_device_company_name_Object = MibScalar
zql_device_company_name = _Zql_device_company_name_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 6),
    _Zql_device_company_name_Type()
)
zql_device_company_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_company_name.setStatus("current")
_Zql_device_product_name_Type = OctetString
_Zql_device_product_name_Object = MibScalar
zql_device_product_name = _Zql_device_product_name_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 7),
    _Zql_device_product_name_Type()
)
zql_device_product_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_product_name.setStatus("current")
_Zql_device_status_Type = OctetString
_Zql_device_status_Object = MibScalar
zql_device_status = _Zql_device_status_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 8),
    _Zql_device_status_Type()
)
zql_device_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_status.setStatus("current")
_Zql_device_pld_ObjectIdentity = ObjectIdentity
zql_device_pld = _Zql_device_pld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 9)
)
_Zql_device_languages_Type = OctetString
_Zql_device_languages_Object = MibScalar
zql_device_languages = _Zql_device_languages_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 13),
    _Zql_device_languages_Type()
)
zql_device_languages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_languages.setStatus("current")
_Zql_device_cph_enable_Type = OctetString
_Zql_device_cph_enable_Object = MibScalar
zql_device_cph_enable = _Zql_device_cph_enable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 14),
    _Zql_device_cph_enable_Type()
)
zql_device_cph_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_cph_enable.setStatus("current")
_Zql_device_cph_interval_Type = OctetString
_Zql_device_cph_interval_Object = MibScalar
zql_device_cph_interval = _Zql_device_cph_interval_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 15),
    _Zql_device_cph_interval_Type()
)
zql_device_cph_interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_cph_interval.setStatus("current")
_Zql_device_macro_get_Type = OctetString
_Zql_device_macro_get_Object = MibScalar
zql_device_macro_get = _Zql_device_macro_get_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 16),
    _Zql_device_macro_get_Type()
)
zql_device_macro_get.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_macro_get.setStatus("current")
_Zql_device_user_p1_Type = OctetString
_Zql_device_user_p1_Object = MibScalar
zql_device_user_p1 = _Zql_device_user_p1_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 17),
    _Zql_device_user_p1_Type()
)
zql_device_user_p1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_user_p1.setStatus("current")
_Zql_device_user_p2_Type = OctetString
_Zql_device_user_p2_Object = MibScalar
zql_device_user_p2 = _Zql_device_user_p2_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 18),
    _Zql_device_user_p2_Type()
)
zql_device_user_p2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_user_p2.setStatus("current")
_Zql_device_uptime_Type = OctetString
_Zql_device_uptime_Object = MibScalar
zql_device_uptime = _Zql_device_uptime_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 20),
    _Zql_device_uptime_Type()
)
zql_device_uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_uptime.setStatus("current")
_Zql_device_volume_Type = OctetString
_Zql_device_volume_Object = MibScalar
zql_device_volume = _Zql_device_volume_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 21),
    _Zql_device_volume_Type()
)
zql_device_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_volume.setStatus("current")
_Zql_device_local_menu_mode_Type = OctetString
_Zql_device_local_menu_mode_Object = MibScalar
zql_device_local_menu_mode = _Zql_device_local_menu_mode_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 22),
    _Zql_device_local_menu_mode_Type()
)
zql_device_local_menu_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_local_menu_mode.setStatus("current")
_Zql_device_ff_disable_Type = OctetString
_Zql_device_ff_disable_Object = MibScalar
zql_device_ff_disable = _Zql_device_ff_disable_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 19, 35),
    _Zql_device_ff_disable_Type()
)
zql_device_ff_disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_ff_disable.setStatus("current")
_Zql_ql_input_ObjectIdentity = ObjectIdentity
zql_ql_input = _Zql_ql_input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 20)
)
_Zql_input_capture_Type = OctetString
_Zql_input_capture_Object = MibScalar
zql_input_capture = _Zql_input_capture_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 20, 1),
    _Zql_input_capture_Type()
)
zql_input_capture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_input_capture.setStatus("current")
_Zql_ql_print_ObjectIdentity = ObjectIdentity
zql_ql_print = _Zql_ql_print_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 21)
)
_Zql_print_contrast_Type = OctetString
_Zql_print_contrast_Object = MibScalar
zql_print_contrast = _Zql_print_contrast_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 21, 1),
    _Zql_print_contrast_Type()
)
zql_print_contrast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_print_contrast.setStatus("current")
_Zql_print_tone_Type = OctetString
_Zql_print_tone_Object = MibScalar
zql_print_tone = _Zql_print_tone_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 21, 2),
    _Zql_print_tone_Type()
)
zql_print_tone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_print_tone.setStatus("current")
_Zql_print_print_adj_Type = OctetString
_Zql_print_print_adj_Object = MibScalar
zql_print_print_adj = _Zql_print_print_adj_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 21, 4),
    _Zql_print_print_adj_Type()
)
zql_print_print_adj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_print_print_adj.setStatus("current")
_Zql_ql_rtc_ObjectIdentity = ObjectIdentity
zql_ql_rtc = _Zql_ql_rtc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 23)
)
_Zql_rtc_time_Type = OctetString
_Zql_rtc_time_Object = MibScalar
zql_rtc_time = _Zql_rtc_time_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 23, 1),
    _Zql_rtc_time_Type()
)
zql_rtc_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_rtc_time.setStatus("current")
_Zql_rtc_date_Type = OctetString
_Zql_rtc_date_Object = MibScalar
zql_rtc_date = _Zql_rtc_date_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 23, 2),
    _Zql_rtc_date_Type()
)
zql_rtc_date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_rtc_date.setStatus("current")
_Zql_rtc_set_counter_Type = OctetString
_Zql_rtc_set_counter_Object = MibScalar
zql_rtc_set_counter = _Zql_rtc_set_counter_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 23, 5),
    _Zql_rtc_set_counter_Type()
)
zql_rtc_set_counter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_rtc_set_counter.setStatus("current")
_Zql_rtc_enable_counter_Type = OctetString
_Zql_rtc_enable_counter_Object = MibScalar
zql_rtc_enable_counter = _Zql_rtc_enable_counter_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 23, 6),
    _Zql_rtc_enable_counter_Type()
)
zql_rtc_enable_counter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_rtc_enable_counter.setStatus("current")
_Zql_ql_usb_ObjectIdentity = ObjectIdentity
zql_ql_usb = _Zql_ql_usb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25)
)
_Zql_usb_device_ObjectIdentity = ObjectIdentity
zql_usb_device = _Zql_usb_device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25, 1)
)
_Zql_device_vendor_id_Type = OctetString
_Zql_device_vendor_id_Object = MibScalar
zql_device_vendor_id = _Zql_device_vendor_id_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25, 1, 1),
    _Zql_device_vendor_id_Type()
)
zql_device_vendor_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_vendor_id.setStatus("current")
_Zql_device_product_id_Type = OctetString
_Zql_device_product_id_Object = MibScalar
zql_device_product_id = _Zql_device_product_id_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25, 1, 2),
    _Zql_device_product_id_Type()
)
zql_device_product_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_product_id.setStatus("current")
_Zql_device_device_version_Type = OctetString
_Zql_device_device_version_Object = MibScalar
zql_device_device_version = _Zql_device_device_version_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25, 1, 3),
    _Zql_device_device_version_Type()
)
zql_device_device_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_device_version.setStatus("current")
_Zql_device_product_string_Type = OctetString
_Zql_device_product_string_Object = MibScalar
zql_device_product_string = _Zql_device_product_string_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25, 1, 4),
    _Zql_device_product_string_Type()
)
zql_device_product_string.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_product_string.setStatus("current")
_Zql_device_manufacturer_string_Type = OctetString
_Zql_device_manufacturer_string_Object = MibScalar
zql_device_manufacturer_string = _Zql_device_manufacturer_string_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25, 1, 5),
    _Zql_device_manufacturer_string_Type()
)
zql_device_manufacturer_string.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_manufacturer_string.setStatus("current")
_Zql_device_serial_string_Type = OctetString
_Zql_device_serial_string_Object = MibScalar
zql_device_serial_string = _Zql_device_serial_string_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25, 1, 6),
    _Zql_device_serial_string_Type()
)
zql_device_serial_string.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_serial_string.setStatus("current")
_Zql_device_device_id_string_Type = OctetString
_Zql_device_device_id_string_Object = MibScalar
zql_device_device_id_string = _Zql_device_device_id_string_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25, 1, 7),
    _Zql_device_device_id_string_Type()
)
zql_device_device_id_string.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_device_device_id_string.setStatus("current")
_Zql_device_device_unique_id_Type = OctetString
_Zql_device_device_unique_id_Object = MibScalar
zql_device_device_unique_id = _Zql_device_device_unique_id_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25, 1, 8),
    _Zql_device_device_unique_id_Type()
)
zql_device_device_unique_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_device_device_unique_id.setStatus("current")
_Zql_usb_connected_Type = OctetString
_Zql_usb_connected_Object = MibScalar
zql_usb_connected = _Zql_usb_connected_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25, 2),
    _Zql_usb_connected_Type()
)
zql_usb_connected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_usb_connected.setStatus("current")
_Zql_usb_halt_Type = OctetString
_Zql_usb_halt_Object = MibScalar
zql_usb_halt = _Zql_usb_halt_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 25, 3),
    _Zql_usb_halt_Type()
)
zql_usb_halt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_usb_halt.setStatus("current")
_Zql_ql_log_ObjectIdentity = ObjectIdentity
zql_ql_log = _Zql_ql_log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 27)
)
_Zql_log_reboot_ObjectIdentity = ObjectIdentity
zql_log_reboot = _Zql_log_reboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 27, 1)
)
_Zql_reboot_code_Type = OctetString
_Zql_reboot_code_Object = MibScalar
zql_reboot_code = _Zql_reboot_code_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 27, 1, 1),
    _Zql_reboot_code_Type()
)
zql_reboot_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_reboot_code.setStatus("current")
_Zql_reboot_reason_Type = OctetString
_Zql_reboot_reason_Object = MibScalar
zql_reboot_reason = _Zql_reboot_reason_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 27, 1, 2),
    _Zql_reboot_reason_Type()
)
zql_reboot_reason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_reboot_reason.setStatus("current")
_Zql_reboot_codes_Type = OctetString
_Zql_reboot_codes_Object = MibScalar
zql_reboot_codes = _Zql_reboot_codes_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 27, 1, 3),
    _Zql_reboot_codes_Type()
)
zql_reboot_codes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_reboot_codes.setStatus("current")
_Zql_reboot_report_Type = OctetString
_Zql_reboot_report_Object = MibScalar
zql_reboot_report = _Zql_reboot_report_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 27, 1, 4),
    _Zql_reboot_report_Type()
)
zql_reboot_report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_reboot_report.setStatus("current")
_Zql_ql_netmanage_ObjectIdentity = ObjectIdentity
zql_ql_netmanage = _Zql_ql_netmanage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28)
)
_Zql_netmanage_type_Type = OctetString
_Zql_netmanage_type_Object = MibScalar
zql_netmanage_type = _Zql_netmanage_type_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 1),
    _Zql_netmanage_type_Type()
)
zql_netmanage_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_netmanage_type.setStatus("current")
_Zql_netmanage_status_code_Type = OctetString
_Zql_netmanage_status_code_Object = MibScalar
zql_netmanage_status_code = _Zql_netmanage_status_code_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 2),
    _Zql_netmanage_status_code_Type()
)
zql_netmanage_status_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_netmanage_status_code.setStatus("current")
_Zql_netmanage_state_code_Type = OctetString
_Zql_netmanage_state_code_Object = MibScalar
zql_netmanage_state_code = _Zql_netmanage_state_code_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 3),
    _Zql_netmanage_state_code_Type()
)
zql_netmanage_state_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_netmanage_state_code.setStatus("current")
_Zql_netmanage_error_code_Type = OctetString
_Zql_netmanage_error_code_Object = MibScalar
zql_netmanage_error_code = _Zql_netmanage_error_code_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 4),
    _Zql_netmanage_error_code_Type()
)
zql_netmanage_error_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_netmanage_error_code.setStatus("current")
_Zql_netmanage_avalanche_ObjectIdentity = ObjectIdentity
zql_netmanage_avalanche = _Zql_netmanage_avalanche_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5)
)
_Zql_avalanche_model_name_Type = OctetString
_Zql_avalanche_model_name_Object = MibScalar
zql_avalanche_model_name = _Zql_avalanche_model_name_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 1),
    _Zql_avalanche_model_name_Type()
)
zql_avalanche_model_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_avalanche_model_name.setStatus("current")
_Zql_avalanche_interval_Type = OctetString
_Zql_avalanche_interval_Object = MibScalar
zql_avalanche_interval = _Zql_avalanche_interval_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 2),
    _Zql_avalanche_interval_Type()
)
zql_avalanche_interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_avalanche_interval.setStatus("current")
_Zql_avalanche_startup_update_Type = OctetString
_Zql_avalanche_startup_update_Object = MibScalar
zql_avalanche_startup_update = _Zql_avalanche_startup_update_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 3),
    _Zql_avalanche_startup_update_Type()
)
zql_avalanche_startup_update.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_avalanche_startup_update.setStatus("current")
_Zql_avalanche_interval_update_Type = OctetString
_Zql_avalanche_interval_update_Object = MibScalar
zql_avalanche_interval_update = _Zql_avalanche_interval_update_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 4),
    _Zql_avalanche_interval_update_Type()
)
zql_avalanche_interval_update.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_avalanche_interval_update.setStatus("current")
_Zql_avalanche_agent_addr_Type = OctetString
_Zql_avalanche_agent_addr_Object = MibScalar
zql_avalanche_agent_addr = _Zql_avalanche_agent_addr_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 5),
    _Zql_avalanche_agent_addr_Type()
)
zql_avalanche_agent_addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_avalanche_agent_addr.setStatus("current")
_Zql_avalanche_available_agent_Type = OctetString
_Zql_avalanche_available_agent_Object = MibScalar
zql_avalanche_available_agent = _Zql_avalanche_available_agent_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 6),
    _Zql_avalanche_available_agent_Type()
)
zql_avalanche_available_agent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_avalanche_available_agent.setStatus("current")
_Zql_avalanche_available_port_Type = OctetString
_Zql_avalanche_available_port_Object = MibScalar
zql_avalanche_available_port = _Zql_avalanche_available_port_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 7),
    _Zql_avalanche_available_port_Type()
)
zql_avalanche_available_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zql_avalanche_available_port.setStatus("current")
_Zql_avalanche_encryption_type_Type = OctetString
_Zql_avalanche_encryption_type_Object = MibScalar
zql_avalanche_encryption_type = _Zql_avalanche_encryption_type_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 9),
    _Zql_avalanche_encryption_type_Type()
)
zql_avalanche_encryption_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_avalanche_encryption_type.setStatus("current")
_Zql_avalanche_udp_timeout_Type = OctetString
_Zql_avalanche_udp_timeout_Object = MibScalar
zql_avalanche_udp_timeout = _Zql_avalanche_udp_timeout_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 10),
    _Zql_avalanche_udp_timeout_Type()
)
zql_avalanche_udp_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_avalanche_udp_timeout.setStatus("current")
_Zql_avalanche_tcp_connection_timeout_Type = OctetString
_Zql_avalanche_tcp_connection_timeout_Object = MibScalar
zql_avalanche_tcp_connection_timeout = _Zql_avalanche_tcp_connection_timeout_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 11),
    _Zql_avalanche_tcp_connection_timeout_Type()
)
zql_avalanche_tcp_connection_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_avalanche_tcp_connection_timeout.setStatus("current")
_Zql_avalanche_terminal_id_Type = OctetString
_Zql_avalanche_terminal_id_Object = MibScalar
zql_avalanche_terminal_id = _Zql_avalanche_terminal_id_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 18),
    _Zql_avalanche_terminal_id_Type()
)
zql_avalanche_terminal_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_avalanche_terminal_id.setStatus("current")
_Zql_avalanche_text_msg_ObjectIdentity = ObjectIdentity
zql_avalanche_text_msg = _Zql_avalanche_text_msg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 19)
)
_Zql_text_msg_print_Type = OctetString
_Zql_text_msg_print_Object = MibScalar
zql_text_msg_print = _Zql_text_msg_print_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 19, 1),
    _Zql_text_msg_print_Type()
)
zql_text_msg_print.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_text_msg_print.setStatus("current")
_Zql_text_msg_display_Type = OctetString
_Zql_text_msg_display_Object = MibScalar
zql_text_msg_display = _Zql_text_msg_display_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 19, 2),
    _Zql_text_msg_display_Type()
)
zql_text_msg_display.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_text_msg_display.setStatus("current")
_Zql_text_msg_beep_Type = OctetString
_Zql_text_msg_beep_Object = MibScalar
zql_text_msg_beep = _Zql_text_msg_beep_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 19, 3),
    _Zql_text_msg_beep_Type()
)
zql_text_msg_beep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_text_msg_beep.setStatus("current")
_Zql_avalanche_app_ObjectIdentity = ObjectIdentity
zql_avalanche_app = _Zql_avalanche_app_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 20)
)
_Zql_avalanche_set_property_Type = OctetString
_Zql_avalanche_set_property_Object = MibScalar
zql_avalanche_set_property = _Zql_avalanche_set_property_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 28, 5, 21),
    _Zql_avalanche_set_property_Type()
)
zql_avalanche_set_property.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_avalanche_set_property.setStatus("current")
_Zql_ql_zpl_ObjectIdentity = ObjectIdentity
zql_ql_zpl = _Zql_ql_zpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 41)
)
_Zql_zpl_save_Type = OctetString
_Zql_zpl_save_Object = MibScalar
zql_zpl_save = _Zql_zpl_save_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 41, 2),
    _Zql_zpl_save_Type()
)
zql_zpl_save.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_zpl_save.setStatus("current")
_Zql_zpl_label_length_Type = OctetString
_Zql_zpl_label_length_Object = MibScalar
zql_zpl_label_length = _Zql_zpl_label_length_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 41, 8),
    _Zql_zpl_label_length_Type()
)
zql_zpl_label_length.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_zpl_label_length.setStatus("current")
_Zql_ql_rfid_ObjectIdentity = ObjectIdentity
zql_ql_rfid = _Zql_ql_rfid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 46)
)
_Zql_ql_event_log_ObjectIdentity = ObjectIdentity
zql_ql_event_log = _Zql_ql_event_log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 49)
)
_Zql_ql_line_print_ObjectIdentity = ObjectIdentity
zql_ql_line_print = _Zql_ql_line_print_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 52)
)
_Zql_line_print_buffer_height_Type = OctetString
_Zql_line_print_buffer_height_Object = MibScalar
zql_line_print_buffer_height = _Zql_line_print_buffer_height_Object(
    (1, 3, 6, 1, 4, 1, 10642, 200, 52, 1),
    _Zql_line_print_buffer_height_Type()
)
zql_line_print_buffer_height.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zql_line_print_buffer_height.setStatus("current")
_Zql_ql_apl_ObjectIdentity = ObjectIdentity
zql_ql_apl = _Zql_ql_apl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10642, 200, 53)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZEBRA-QL-MIB",
    **{"zebra": zebra,
       "zql-zebra-ql": zql_zebra_ql,
       "zql-ql-bluetooth": zql_ql_bluetooth,
       "zql-bluetooth-discoverable": zql_bluetooth_discoverable,
       "zql-bluetooth-friendly-name": zql_bluetooth_friendly_name,
       "zql-bluetooth-version": zql_bluetooth_version,
       "zql-bluetooth-date": zql_bluetooth_date,
       "zql-bluetooth-local-name": zql_bluetooth_local_name,
       "zql-bluetooth-address": zql_bluetooth_address,
       "zql-bluetooth-bluetooth-pin": zql_bluetooth_bluetooth_pin,
       "zql-bluetooth-short-address": zql_bluetooth_short_address,
       "zql-bluetooth-radio-version": zql_bluetooth_radio_version,
       "zql-bluetooth-afh-mode": zql_bluetooth_afh_mode,
       "zql-bluetooth-afh-map": zql_bluetooth_afh_map,
       "zql-bluetooth-afh-map-curr": zql_bluetooth_afh_map_curr,
       "zql-bluetooth-enable": zql_bluetooth_enable,
       "zql-bluetooth-connected": zql_bluetooth_connected,
       "zql-ql-card": zql_ql_card,
       "zql-card-inserted": zql_card_inserted,
       "zql-card-idtext1": zql_card_idtext1,
       "zql-card-idtext2": zql_card_idtext2,
       "zql-card-idtext3": zql_card_idtext3,
       "zql-card-idtext4": zql_card_idtext4,
       "zql-card-mac-addr": zql_card_mac_addr,
       "zql-card-mac-raw": zql_card_mac_raw,
       "zql-card-enable": zql_card_enable,
       "zql-ql-comm": zql_ql_comm,
       "zql-comm-baud": zql_comm_baud,
       "zql-comm-data-bits": zql_comm_data_bits,
       "zql-comm-parity": zql_comm_parity,
       "zql-comm-stop-bits": zql_comm_stop_bits,
       "zql-comm-dsr": zql_comm_dsr,
       "zql-ql-head": zql_ql_head,
       "zql-head-latch": zql_head_latch,
       "zql-ql-ip": zql_ql_ip,
       "zql-ip-dhcp": zql_ip_dhcp,
       "zql-dhcp-enable": zql_dhcp_enable,
       "zql-dhcp-cid-type": zql_dhcp_cid_type,
       "zql-dhcp-cid-prefix": zql_dhcp_cid_prefix,
       "zql-dhcp-cid-value": zql_dhcp_cid_value,
       "zql-dhcp-requests-per-session": zql_dhcp_requests_per_session,
       "zql-dhcp-request-timeout": zql_dhcp_request_timeout,
       "zql-dhcp-session-interval": zql_dhcp_session_interval,
       "zql-dhcp-lease": zql_dhcp_lease,
       "zql-lease-length": zql_lease_length,
       "zql-lease-time-left": zql_lease_time_left,
       "zql-lease-server": zql_lease_server,
       "zql-lease-last-attempt": zql_lease_last_attempt,
       "zql-dhcp-cache-ip": zql_dhcp_cache_ip,
       "zql-dhcp-vendor-class-id": zql_dhcp_vendor_class_id,
       "zql-dhcp-user-class-id": zql_dhcp_user_class_id,
       "zql-dhcp-option12": zql_dhcp_option12,
       "zql-dhcp-option12-format": zql_dhcp_option12_format,
       "zql-dhcp-option12-value": zql_dhcp_option12_value,
       "zql-ip-ftp": zql_ip_ftp,
       "zql-ftp-enable": zql_ftp_enable,
       "zql-ftp-execute-file": zql_ftp_execute_file,
       "zql-ip-lpd": zql_ip_lpd,
       "zql-lpd-enable": zql_lpd_enable,
       "zql-ip-tcp": zql_ip_tcp,
       "zql-tcp-enable": zql_tcp_enable,
       "zql-ip-udp": zql_ip_udp,
       "zql-udp-enable": zql_udp_enable,
       "zql-ip-http": zql_ip_http,
       "zql-http-enable": zql_http_enable,
       "zql-ip-smtp": zql_ip_smtp,
       "zql-smtp-enable": zql_smtp_enable,
       "zql-smtp-server-addr": zql_smtp_server_addr,
       "zql-ip-pop3": zql_ip_pop3,
       "zql-pop3-enable": zql_pop3_enable,
       "zql-pop3-print-headers": zql_pop3_print_headers,
       "zql-pop3-verbose-headers": zql_pop3_verbose_headers,
       "zql-pop3-print-body": zql_pop3_print_body,
       "zql-pop3-save-attachments": zql_pop3_save_attachments,
       "zql-pop3-poll": zql_pop3_poll,
       "zql-pop3-username": zql_pop3_username,
       "zql-pop3-password": zql_pop3_password,
       "zql-pop3-server-addr": zql_pop3_server_addr,
       "zql-pop3-print-attachments": zql_pop3_print_attachments,
       "zql-ip-snmp": zql_ip_snmp,
       "zql-snmp-enable": zql_snmp_enable,
       "zql-snmp-get-community-name": zql_snmp_get_community_name,
       "zql-snmp-set-community-name": zql_snmp_set_community_name,
       "zql-snmp-create-mib": zql_snmp_create_mib,
       "zql-ip-telnet": zql_ip_telnet,
       "zql-telnet-enable": zql_telnet_enable,
       "zql-telnet-disconnect": zql_telnet_disconnect,
       "zql-ip-addr": zql_ip_addr,
       "zql-ip-netmask": zql_ip_netmask,
       "zql-ip-gateway": zql_ip_gateway,
       "zql-ip-port": zql_ip_port,
       "zql-ip-remote": zql_ip_remote,
       "zql-ip-ping-remote": zql_ip_ping_remote,
       "zql-ip-netstat": zql_ip_netstat,
       "zql-ip-remote-port": zql_ip_remote_port,
       "zql-ip-bootp": zql_ip_bootp,
       "zql-bootp-enable": zql_bootp_enable,
       "zql-ip-mirror": zql_ip_mirror,
       "zql-mirror-auto": zql_mirror_auto,
       "zql-mirror-username": zql_mirror_username,
       "zql-mirror-password": zql_mirror_password,
       "zql-mirror-server": zql_mirror_server,
       "zql-mirror-path": zql_mirror_path,
       "zql-mirror-freq": zql_mirror_freq,
       "zql-mirror-fetch": zql_mirror_fetch,
       "zql-mirror-version": zql_mirror_version,
       "zql-mirror-freq-hours": zql_mirror_freq_hours,
       "zql-mirror-error-retry": zql_mirror_error_retry,
       "zql-mirror-feedback": zql_mirror_feedback,
       "zql-feedback-auto": zql_feedback_auto,
       "zql-feedback-path": zql_feedback_path,
       "zql-feedback-freq": zql_feedback_freq,
       "zql-mirror-success": zql_mirror_success,
       "zql-mirror-success-time": zql_mirror_success_time,
       "zql-mirror-last-time": zql_mirror_last_time,
       "zql-mirror-last-error": zql_mirror_last_error,
       "zql-mirror-mode": zql_mirror_mode,
       "zql-ip-ping-len": zql_ip_ping_len,
       "zql-ip-dns": zql_ip_dns,
       "zql-dns-domain": zql_dns_domain,
       "zql-dns-servers": zql_dns_servers,
       "zql-ip-discovery": zql_ip_discovery,
       "zql-discovery-enable": zql_discovery_enable,
       "zql-discovery-port": zql_discovery_port,
       "zql-ip-roam-packet": zql_ip_roam_packet,
       "zql-ql-label": zql_ql_label,
       "zql-label-x-move": zql_label_x_move,
       "zql-label-y-move": zql_label_y_move,
       "zql-ql-motor": zql_ql_motor,
       "zql-ql-media": zql_ql_media,
       "zql-media-status": zql_media_status,
       "zql-media-sense-mode": zql_media_sense_mode,
       "zql-media-tof": zql_media_tof,
       "zql-media-type": zql_media_type,
       "zql-media-width-sense": zql_media_width_sense,
       "zql-width-sense-enable": zql_width_sense_enable,
       "zql-width-sense-in-mm": zql_width_sense_in_mm,
       "zql-width-sense-in-cm": zql_width_sense_in_cm,
       "zql-width-sense-in-dots": zql_width_sense_in_dots,
       "zql-width-sense-in-inches": zql_width_sense_in_inches,
       "zql-media-measure-label": zql_media_measure_label,
       "zql-media-measured-lbl-height": zql_media_measured_lbl_height,
       "zql-measured-lbl-height-min": zql_measured_lbl_height_min,
       "zql-measured-lbl-height-max": zql_measured_lbl_height_max,
       "zql-measured-lbl-height-avg": zql_measured_lbl_height_avg,
       "zql-measured-lbl-height-std-dev": zql_measured_lbl_height_std_dev,
       "zql-ql-sensor": zql_ql_sensor,
       "zql-sensor-paper-supply": zql_sensor_paper_supply,
       "zql-sensor-peeler": zql_sensor_peeler,
       "zql-ql-srf": zql_ql_srf,
       "zql-ql-wlan": zql_ql_wlan,
       "zql-wlan-operating-mode": zql_wlan_operating_mode,
       "zql-wlan-essid": zql_wlan_essid,
       "zql-wlan-current-essid": zql_wlan_current_essid,
       "zql-wlan-station-name": zql_wlan_station_name,
       "zql-wlan-current-tx-rate": zql_wlan_current_tx_rate,
       "zql-wlan-encryption-mode": zql_wlan_encryption_mode,
       "zql-wlan-associated": zql_wlan_associated,
       "zql-wlan-encryption-index": zql_wlan_encryption_index,
       "zql-wlan-encryption-key1": zql_wlan_encryption_key1,
       "zql-wlan-encryption-key2": zql_wlan_encryption_key2,
       "zql-wlan-encryption-key3": zql_wlan_encryption_key3,
       "zql-wlan-encryption-key4": zql_wlan_encryption_key4,
       "zql-wlan-leap-mode": zql_wlan_leap_mode,
       "zql-wlan-leap-username": zql_wlan_leap_username,
       "zql-wlan-leap-password": zql_wlan_leap_password,
       "zql-wlan-power-save": zql_wlan_power_save,
       "zql-wlan-test": zql_wlan_test,
       "zql-wlan-auth-type": zql_wlan_auth_type,
       "zql-wlan-preamble": zql_wlan_preamble,
       "zql-wlan-bssid": zql_wlan_bssid,
       "zql-wlan-firmware-version": zql_wlan_firmware_version,
       "zql-wlan-signal-strength": zql_wlan_signal_strength,
       "zql-wlan-current-freq": zql_wlan_current_freq,
       "zql-wlan-roam": zql_wlan_roam,
       "zql-roam-signal": zql_roam_signal,
       "zql-roam-interval": zql_roam_interval,
       "zql-roam-interchannel-delay": zql_roam_interchannel_delay,
       "zql-roam-max-chan-scan-time": zql_roam_max_chan_scan_time,
       "zql-roam-rssi": zql_roam_rssi,
       "zql-roam-max-fail": zql_roam_max_fail,
       "zql-wlan-channel": zql_wlan_channel,
       "zql-wlan-wpa": zql_wlan_wpa,
       "zql-wpa-enable": zql_wpa_enable,
       "zql-wpa-authentication": zql_wpa_authentication,
       "zql-wpa-psk": zql_wpa_psk,
       "zql-wpa-wpa-version": zql_wpa_wpa_version,
       "zql-wpa-groupkey-ciphersuite": zql_wpa_groupkey_ciphersuite,
       "zql-wpa-pairwise-ciphersuite": zql_wpa_pairwise_ciphersuite,
       "zql-wlan-8021x": zql_wlan_8021x,
       "zql-8021x-enable": zql_8021x_enable,
       "zql-8021x-authentication": zql_8021x_authentication,
       "zql-8021x-peap": zql_8021x_peap,
       "zql-peap-peap-username": zql_peap_peap_username,
       "zql-peap-peap-password": zql_peap_peap_password,
       "zql-peap-privkey-password": zql_peap_privkey_password,
       "zql-8021x-eap": zql_8021x_eap,
       "zql-eap-username": zql_eap_username,
       "zql-eap-password": zql_eap_password,
       "zql-eap-privkey-password": zql_eap_privkey_password,
       "zql-wlan-adhocchannel": zql_wlan_adhocchannel,
       "zql-wlan-adhocautomode": zql_wlan_adhocautomode,
       "zql-wlan-enable": zql_wlan_enable,
       "zql-wlan-encryption-optional": zql_wlan_encryption_optional,
       "zql-wlan-adhoc-last-channel": zql_wlan_adhoc_last_channel,
       "zql-wlan-secure-ssid": zql_wlan_secure_ssid,
       "zql-wlan-ip": zql_wlan_ip,
       "zql-wlan-ip-addr": zql_wlan_ip_addr,
       "zql-wlan-ip-netmask": zql_wlan_ip_netmask,
       "zql-wlan-keep-alive": zql_wlan_keep_alive,
       "zql-keep-alive-enable": zql_keep_alive_enable,
       "zql-keep-alive-timeout": zql_keep_alive_timeout,
       "zql-ql-display": zql_ql_display,
       "zql-display-contrast": zql_display_contrast,
       "zql-display-text": zql_display_text,
       "zql-display-backlight": zql_display_backlight,
       "zql-display-backlight-on-time": zql_display_backlight_on_time,
       "zql-ql-memory": zql_ql_memory,
       "zql-memory-flash-size": zql_memory_flash_size,
       "zql-memory-ram-size": zql_memory_ram_size,
       "zql-memory-flash-free": zql_memory_flash_free,
       "zql-memory-ram-free": zql_memory_ram_free,
       "zql-ql-power": zql_ql_power,
       "zql-power-voltage": zql_power_voltage,
       "zql-power-percent-full": zql_power_percent_full,
       "zql-power-status": zql_power_status,
       "zql-power-low-battery-warning": zql_power_low_battery_warning,
       "zql-power-low-battery-shutdown": zql_power_low_battery_shutdown,
       "zql-power-low-battery-timeout": zql_power_low_battery_timeout,
       "zql-power-inactivity-timeout": zql_power_inactivity_timeout,
       "zql-power-dtr-power-off": zql_power_dtr_power_off,
       "zql-power-shutdown": zql_power_shutdown,
       "zql-power-ascii-graph": zql_power_ascii_graph,
       "zql-power-low-battery-warning-raw": zql_power_low_battery_warning_raw,
       "zql-power-power-on-cycles": zql_power_power_on_cycles,
       "zql-power-design-voltage": zql_power_design_voltage,
       "zql-power-design-capacity": zql_power_design_capacity,
       "zql-power-manufacture-date": zql_power_manufacture_date,
       "zql-power-relative-state-of-charge": zql_power_relative_state_of_charge,
       "zql-power-serial-number": zql_power_serial_number,
       "zql-power-cycle-count": zql_power_cycle_count,
       "zql-power-full-charge-capacity": zql_power_full_charge_capacity,
       "zql-power-health": zql_power_health,
       "zql-power-date-first-used": zql_power_date_first_used,
       "zql-ql-file": zql_ql_file,
       "zql-file-dir": zql_file_dir,
       "zql-file-type": zql_file_type,
       "zql-file-delete": zql_file_delete,
       "zql-file-print": zql_file_print,
       "zql-file-run": zql_file_run,
       "zql-file-rename": zql_file_rename,
       "zql-file-append": zql_file_append,
       "zql-ql-odometer": zql_ql_odometer,
       "zql-odometer-user-label-count": zql_odometer_user_label_count,
       "zql-odometer-total-label-count": zql_odometer_total_label_count,
       "zql-odometer-total-print-length": zql_odometer_total_print_length,
       "zql-odometer-latch-open-count": zql_odometer_latch_open_count,
       "zql-odometer-label-dot-length": zql_odometer_label_dot_length,
       "zql-odometer-rfid": zql_odometer_rfid,
       "zql-ql-appl": zql_ql_appl,
       "zql-appl-date": zql_appl_date,
       "zql-appl-name": zql_appl_name,
       "zql-appl-version": zql_appl_version,
       "zql-appl-ps": zql_appl_ps,
       "zql-ql-device": zql_ql_device,
       "zql-device-reset": zql_device_reset,
       "zql-device-restore-defaults": zql_device_restore_defaults,
       "zql-device-card": zql_device_card,
       "zql-device-friendly-name": zql_device_friendly_name,
       "zql-device-company-name": zql_device_company_name,
       "zql-device-product-name": zql_device_product_name,
       "zql-device-status": zql_device_status,
       "zql-device-pld": zql_device_pld,
       "zql-device-languages": zql_device_languages,
       "zql-device-cph-enable": zql_device_cph_enable,
       "zql-device-cph-interval": zql_device_cph_interval,
       "zql-device-macro-get": zql_device_macro_get,
       "zql-device-user-p1": zql_device_user_p1,
       "zql-device-user-p2": zql_device_user_p2,
       "zql-device-uptime": zql_device_uptime,
       "zql-device-volume": zql_device_volume,
       "zql-device-local-menu-mode": zql_device_local_menu_mode,
       "zql-device-ff-disable": zql_device_ff_disable,
       "zql-ql-input": zql_ql_input,
       "zql-input-capture": zql_input_capture,
       "zql-ql-print": zql_ql_print,
       "zql-print-contrast": zql_print_contrast,
       "zql-print-tone": zql_print_tone,
       "zql-print-print-adj": zql_print_print_adj,
       "zql-ql-rtc": zql_ql_rtc,
       "zql-rtc-time": zql_rtc_time,
       "zql-rtc-date": zql_rtc_date,
       "zql-rtc-set-counter": zql_rtc_set_counter,
       "zql-rtc-enable-counter": zql_rtc_enable_counter,
       "zql-ql-usb": zql_ql_usb,
       "zql-usb-device": zql_usb_device,
       "zql-device-vendor-id": zql_device_vendor_id,
       "zql-device-product-id": zql_device_product_id,
       "zql-device-device-version": zql_device_device_version,
       "zql-device-product-string": zql_device_product_string,
       "zql-device-manufacturer-string": zql_device_manufacturer_string,
       "zql-device-serial-string": zql_device_serial_string,
       "zql-device-device-id-string": zql_device_device_id_string,
       "zql-device-device-unique-id": zql_device_device_unique_id,
       "zql-usb-connected": zql_usb_connected,
       "zql-usb-halt": zql_usb_halt,
       "zql-ql-log": zql_ql_log,
       "zql-log-reboot": zql_log_reboot,
       "zql-reboot-code": zql_reboot_code,
       "zql-reboot-reason": zql_reboot_reason,
       "zql-reboot-codes": zql_reboot_codes,
       "zql-reboot-report": zql_reboot_report,
       "zql-ql-netmanage": zql_ql_netmanage,
       "zql-netmanage-type": zql_netmanage_type,
       "zql-netmanage-status-code": zql_netmanage_status_code,
       "zql-netmanage-state-code": zql_netmanage_state_code,
       "zql-netmanage-error-code": zql_netmanage_error_code,
       "zql-netmanage-avalanche": zql_netmanage_avalanche,
       "zql-avalanche-model-name": zql_avalanche_model_name,
       "zql-avalanche-interval": zql_avalanche_interval,
       "zql-avalanche-startup-update": zql_avalanche_startup_update,
       "zql-avalanche-interval-update": zql_avalanche_interval_update,
       "zql-avalanche-agent-addr": zql_avalanche_agent_addr,
       "zql-avalanche-available-agent": zql_avalanche_available_agent,
       "zql-avalanche-available-port": zql_avalanche_available_port,
       "zql-avalanche-encryption-type": zql_avalanche_encryption_type,
       "zql-avalanche-udp-timeout": zql_avalanche_udp_timeout,
       "zql-avalanche-tcp-connection-timeout": zql_avalanche_tcp_connection_timeout,
       "zql-avalanche-terminal-id": zql_avalanche_terminal_id,
       "zql-avalanche-text-msg": zql_avalanche_text_msg,
       "zql-text-msg-print": zql_text_msg_print,
       "zql-text-msg-display": zql_text_msg_display,
       "zql-text-msg-beep": zql_text_msg_beep,
       "zql-avalanche-app": zql_avalanche_app,
       "zql-avalanche-set-property": zql_avalanche_set_property,
       "zql-ql-zpl": zql_ql_zpl,
       "zql-zpl-save": zql_zpl_save,
       "zql-zpl-label-length": zql_zpl_label_length,
       "zql-ql-rfid": zql_ql_rfid,
       "zql-ql-event-log": zql_ql_event_log,
       "zql-ql-line-print": zql_ql_line_print,
       "zql-line-print-buffer-height": zql_line_print_buffer_height,
       "zql-ql-apl": zql_ql_apl}
)
