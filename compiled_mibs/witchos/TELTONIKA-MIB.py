# SNMP MIB module (TELTONIKA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\witchos\TELTONIKA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:22 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

teltonika = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48690)
)
if mibBuilder.loadTexts:
    teltonika.setRevisions(
        ("2022-06-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TeltonikaSnmpGroups_ObjectIdentity = ObjectIdentity
teltonikaSnmpGroups = _TeltonikaSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 0)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 1)
)


class _Serial_Type(DisplayString):
    """Custom type serial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Serial_Type.__name__ = "DisplayString"
_Serial_Object = MibScalar
serial = _Serial_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 1),
    _Serial_Type()
)
serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serial.setStatus("current")


class _DeviceName_Type(DisplayString):
    """Custom type deviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceName_Type.__name__ = "DisplayString"
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")


class _ProductCode_Type(DisplayString):
    """Custom type productCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProductCode_Type.__name__ = "DisplayString"
_ProductCode_Object = MibScalar
productCode = _ProductCode_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 3),
    _ProductCode_Type()
)
productCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productCode.setStatus("current")


class _BatchNumber_Type(DisplayString):
    """Custom type batchNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BatchNumber_Type.__name__ = "DisplayString"
_BatchNumber_Object = MibScalar
batchNumber = _BatchNumber_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 4),
    _BatchNumber_Type()
)
batchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batchNumber.setStatus("current")


class _HardwareRevision_Type(DisplayString):
    """Custom type hardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HardwareRevision_Type.__name__ = "DisplayString"
_HardwareRevision_Object = MibScalar
hardwareRevision = _HardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 5),
    _HardwareRevision_Type()
)
hardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareRevision.setStatus("current")


class _FwVersion_Type(DisplayString):
    """Custom type fwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwVersion_Type.__name__ = "DisplayString"
_FwVersion_Object = MibScalar
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 6),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("current")


class _DeviceUptime_Type(DisplayString):
    """Custom type deviceUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeviceUptime_Type.__name__ = "DisplayString"
_DeviceUptime_Object = MibScalar
deviceUptime = _DeviceUptime_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 7),
    _DeviceUptime_Type()
)
deviceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUptime.setStatus("current")


class _CpuUsage_Type(DisplayString):
    """Custom type cpuUsage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpuUsage_Type.__name__ = "DisplayString"
_CpuUsage_Object = MibScalar
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 48690, 1, 8),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 8)
)
_PVlanCount_Type = Integer32
_PVlanCount_Object = MibScalar
pVlanCount = _PVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 48690, 8, 1),
    _PVlanCount_Type()
)
pVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pVlanCount.setStatus("current")
_Iface_ObjectIdentity = ObjectIdentity
iface = _Iface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48690, 11)
)
_IfaceCount_Type = Integer32
_IfaceCount_Object = MibScalar
ifaceCount = _IfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 1),
    _IfaceCount_Type()
)
ifaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceCount.setStatus("current")
_IfaceTable_Object = MibTable
ifaceTable = _IfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2)
)
if mibBuilder.loadTexts:
    ifaceTable.setStatus("current")
_IfaceEntry_Object = MibTableRow
ifaceEntry = _IfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1)
)
ifaceEntry.setIndexNames(
    (0, "TELTONIKA-MIB", "ifaceIndex"),
)
if mibBuilder.loadTexts:
    ifaceEntry.setStatus("current")


class _IfaceIndex_Type(Integer32):
    """Custom type ifaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IfaceIndex_Type.__name__ = "Integer32"
_IfaceIndex_Object = MibTableColumn
ifaceIndex = _IfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1, 1),
    _IfaceIndex_Type()
)
ifaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceIndex.setStatus("current")


class _IfaceName_Type(DisplayString):
    """Custom type ifaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfaceName_Type.__name__ = "DisplayString"
_IfaceName_Object = MibTableColumn
ifaceName = _IfaceName_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1, 2),
    _IfaceName_Type()
)
ifaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceName.setStatus("current")


class _IfaceState_Type(DisplayString):
    """Custom type ifaceState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfaceState_Type.__name__ = "DisplayString"
_IfaceState_Object = MibTableColumn
ifaceState = _IfaceState_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1, 3),
    _IfaceState_Type()
)
ifaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceState.setStatus("current")
_IfaceSpeed_Type = Integer32
_IfaceSpeed_Object = MibTableColumn
ifaceSpeed = _IfaceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1, 4),
    _IfaceSpeed_Type()
)
ifaceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceSpeed.setStatus("current")
_IfaceMulticast_Type = Integer32
_IfaceMulticast_Object = MibTableColumn
ifaceMulticast = _IfaceMulticast_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1, 5),
    _IfaceMulticast_Type()
)
ifaceMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceMulticast.setStatus("current")
_IfaceRDiscards_Type = Integer32
_IfaceRDiscards_Object = MibTableColumn
ifaceRDiscards = _IfaceRDiscards_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1, 6),
    _IfaceRDiscards_Type()
)
ifaceRDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceRDiscards.setStatus("current")
_IfaceRErrors_Type = Integer32
_IfaceRErrors_Object = MibTableColumn
ifaceRErrors = _IfaceRErrors_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1, 7),
    _IfaceRErrors_Type()
)
ifaceRErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceRErrors.setStatus("current")
_IfaceRTraffic_Type = Integer32
_IfaceRTraffic_Object = MibTableColumn
ifaceRTraffic = _IfaceRTraffic_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1, 8),
    _IfaceRTraffic_Type()
)
ifaceRTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceRTraffic.setStatus("current")
_IfaceTDiscards_Type = Integer32
_IfaceTDiscards_Object = MibTableColumn
ifaceTDiscards = _IfaceTDiscards_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1, 9),
    _IfaceTDiscards_Type()
)
ifaceTDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceTDiscards.setStatus("current")
_IfaceTErrors_Type = Integer32
_IfaceTErrors_Object = MibTableColumn
ifaceTErrors = _IfaceTErrors_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1, 10),
    _IfaceTErrors_Type()
)
ifaceTErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceTErrors.setStatus("current")
_IfaceTTraffic_Type = Integer32
_IfaceTTraffic_Object = MibTableColumn
ifaceTTraffic = _IfaceTTraffic_Object(
    (1, 3, 6, 1, 4, 1, 48690, 11, 2, 1, 11),
    _IfaceTTraffic_Type()
)
ifaceTTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaceTTraffic.setStatus("current")

# Managed Objects groups

deviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 1)
)
deviceGroup.setObjects(
      *(("TELTONIKA-MIB", "serial"),
        ("TELTONIKA-MIB", "deviceName"),
        ("TELTONIKA-MIB", "productCode"),
        ("TELTONIKA-MIB", "batchNumber"),
        ("TELTONIKA-MIB", "hardwareRevision"),
        ("TELTONIKA-MIB", "fwVersion"),
        ("TELTONIKA-MIB", "deviceUptime"),
        ("TELTONIKA-MIB", "cpuUsage"))
)
if mibBuilder.loadTexts:
    deviceGroup.setStatus("current")

ifaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48690, 0, 13)
)
ifaceGroup.setObjects(
      *(("TELTONIKA-MIB", "ifaceCount"),
        ("TELTONIKA-MIB", "ifaceIndex"),
        ("TELTONIKA-MIB", "ifaceName"),
        ("TELTONIKA-MIB", "ifaceState"),
        ("TELTONIKA-MIB", "ifaceSpeed"),
        ("TELTONIKA-MIB", "ifaceMulticast"),
        ("TELTONIKA-MIB", "ifaceRDiscards"),
        ("TELTONIKA-MIB", "ifaceRErrors"),
        ("TELTONIKA-MIB", "ifaceRTraffic"),
        ("TELTONIKA-MIB", "ifaceTDiscards"),
        ("TELTONIKA-MIB", "ifaceTErrors"),
        ("TELTONIKA-MIB", "ifaceTTraffic"))
)
if mibBuilder.loadTexts:
    ifaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELTONIKA-MIB",
    **{"teltonika": teltonika,
       "teltonikaSnmpGroups": teltonikaSnmpGroups,
       "deviceGroup": deviceGroup,
       "ifaceGroup": ifaceGroup,
       "device": device,
       "serial": serial,
       "deviceName": deviceName,
       "productCode": productCode,
       "batchNumber": batchNumber,
       "hardwareRevision": hardwareRevision,
       "fwVersion": fwVersion,
       "deviceUptime": deviceUptime,
       "cpuUsage": cpuUsage,
       "vlan": vlan,
       "pVlanCount": pVlanCount,
       "iface": iface,
       "ifaceCount": ifaceCount,
       "ifaceTable": ifaceTable,
       "ifaceEntry": ifaceEntry,
       "ifaceIndex": ifaceIndex,
       "ifaceName": ifaceName,
       "ifaceState": ifaceState,
       "ifaceSpeed": ifaceSpeed,
       "ifaceMulticast": ifaceMulticast,
       "ifaceRDiscards": ifaceRDiscards,
       "ifaceRErrors": ifaceRErrors,
       "ifaceRTraffic": ifaceRTraffic,
       "ifaceTDiscards": ifaceTDiscards,
       "ifaceTErrors": ifaceTErrors,
       "ifaceTTraffic": ifaceTTraffic}
)
