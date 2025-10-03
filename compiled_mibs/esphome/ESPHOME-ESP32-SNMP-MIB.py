# SNMP MIB module (ESPHOME-ESP32-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\esphome\ESPHOME-ESP32-SNMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:53 2025
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

(hrMemorySize,
 hrStorageAllocationUnits,
 hrStorageDescr,
 hrStorageGroup,
 hrStorageIndex,
 hrStorageSize,
 hrStorageUsed,
 hrSystemUptime) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrMemorySize",
    "hrStorageAllocationUnits",
    "hrStorageDescr",
    "hrStorageGroup",
    "hrStorageIndex",
    "hrStorageSize",
    "hrStorageUsed",
    "hrSystemUptime")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmp,
 sysDescr) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp",
    "sysDescr")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

esphome = ModuleIdentity(
    (1, 3, 9999)
)
if mibBuilder.loadTexts:
    esphome.setRevisions(
        ("2017-04-20 00:00",)
    )


# Types definitions



class KBytes(Integer32):
    """Custom type KBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Chip_ObjectIdentity = ObjectIdentity
chip = _Chip_ObjectIdentity(
    (1, 3, 9999, 2)
)


class _ChipType_Type(DisplayString):
    """Custom type chipType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChipType_Type.__name__ = "DisplayString"
_ChipType_Object = MibScalar
chipType = _ChipType_Object(
    (1, 3, 9999, 2, 1),
    _ChipType_Type()
)
chipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipType.setStatus("current")


class _CpuClock_Type(DisplayString):
    """Custom type cpuClock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpuClock_Type.__name__ = "DisplayString"
_CpuClock_Object = MibScalar
cpuClock = _CpuClock_Object(
    (1, 3, 9999, 2, 2),
    _CpuClock_Type()
)
cpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuClock.setStatus("current")


class _ChipModel_Type(DisplayString):
    """Custom type chipModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChipModel_Type.__name__ = "DisplayString"
_ChipModel_Object = MibScalar
chipModel = _ChipModel_Object(
    (1, 3, 9999, 2, 3),
    _ChipModel_Type()
)
chipModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipModel.setStatus("current")


class _NumCores_Type(DisplayString):
    """Custom type numCores based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NumCores_Type.__name__ = "DisplayString"
_NumCores_Object = MibScalar
numCores = _NumCores_Object(
    (1, 3, 9999, 2, 4),
    _NumCores_Type()
)
numCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numCores.setStatus("current")


class _ChipRevision_Type(DisplayString):
    """Custom type chipRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChipRevision_Type.__name__ = "DisplayString"
_ChipRevision_Object = MibScalar
chipRevision = _ChipRevision_Object(
    (1, 3, 9999, 2, 5),
    _ChipRevision_Type()
)
chipRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipRevision.setStatus("current")
_Wifi_ObjectIdentity = ObjectIdentity
wifi = _Wifi_ObjectIdentity(
    (1, 3, 9999, 4)
)


class _Rssi_Type(DisplayString):
    """Custom type rssi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rssi_Type.__name__ = "DisplayString"
_Rssi_Object = MibScalar
rssi = _Rssi_Object(
    (1, 3, 9999, 4, 1),
    _Rssi_Type()
)
rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssi.setStatus("current")


class _Bssi_Type(DisplayString):
    """Custom type bssi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Bssi_Type.__name__ = "DisplayString"
_Bssi_Object = MibScalar
bssi = _Bssi_Object(
    (1, 3, 9999, 4, 2),
    _Bssi_Type()
)
bssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bssi.setStatus("current")


class _Ssid_Type(DisplayString):
    """Custom type ssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ssid_Type.__name__ = "DisplayString"
_Ssid_Object = MibScalar
ssid = _Ssid_Object(
    (1, 3, 9999, 4, 3),
    _Ssid_Type()
)
ssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssid.setStatus("current")


class _Ipaddress_Type(DisplayString):
    """Custom type ipaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ipaddress_Type.__name__ = "DisplayString"
_Ipaddress_Object = MibScalar
ipaddress = _Ipaddress_Object(
    (1, 3, 9999, 4, 4),
    _Ipaddress_Type()
)
ipaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddress.setStatus("current")
_Heap_ObjectIdentity = ObjectIdentity
heap = _Heap_ObjectIdentity(
    (1, 3, 9999, 32)
)
_HeapSize_Type = Integer32
_HeapSize_Object = MibScalar
heapSize = _HeapSize_Object(
    (1, 3, 9999, 32, 1),
    _HeapSize_Type()
)
heapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heapSize.setStatus("current")
_FreeHeap_Type = Integer32
_FreeHeap_Object = MibScalar
freeHeap = _FreeHeap_Object(
    (1, 3, 9999, 32, 2),
    _FreeHeap_Type()
)
freeHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeHeap.setStatus("current")
_MaxFreeHeapBlock_Type = Integer32
_MaxFreeHeapBlock_Object = MibScalar
maxFreeHeapBlock = _MaxFreeHeapBlock_Object(
    (1, 3, 9999, 32, 3),
    _MaxFreeHeapBlock_Type()
)
maxFreeHeapBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxFreeHeapBlock.setStatus("current")
_MinimumFreeHeap_Type = Integer32
_MinimumFreeHeap_Object = MibScalar
minimumFreeHeap = _MinimumFreeHeap_Object(
    (1, 3, 9999, 32, 3),
    _MinimumFreeHeap_Type()
)
minimumFreeHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minimumFreeHeap.setStatus("current")
_MaximumAllocatedHeap_Type = Integer32
_MaximumAllocatedHeap_Object = MibScalar
maximumAllocatedHeap = _MaximumAllocatedHeap_Object(
    (1, 3, 9999, 32, 4),
    _MaximumAllocatedHeap_Type()
)
maximumAllocatedHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumAllocatedHeap.setStatus("current")
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 9999, 9999)
)

# Managed Objects groups

chipGroup = ObjectGroup(
    (1, 3, 9999, 9999, 2)
)
chipGroup.setObjects(
      *(("ESPHOME-ESP32-SNMP-MIB", "chipType"),
        ("ESPHOME-ESP32-SNMP-MIB", "cpuClock"),
        ("ESPHOME-ESP32-SNMP-MIB", "chipModel"),
        ("ESPHOME-ESP32-SNMP-MIB", "numCores"),
        ("ESPHOME-ESP32-SNMP-MIB", "chipRevision"))
)
if mibBuilder.loadTexts:
    chipGroup.setStatus("current")

wifiGroup = ObjectGroup(
    (1, 3, 9999, 9999, 4)
)
wifiGroup.setObjects(
      *(("ESPHOME-ESP32-SNMP-MIB", "rssi"),
        ("ESPHOME-ESP32-SNMP-MIB", "bssi"),
        ("ESPHOME-ESP32-SNMP-MIB", "ssid"),
        ("ESPHOME-ESP32-SNMP-MIB", "ipaddress"))
)
if mibBuilder.loadTexts:
    wifiGroup.setStatus("current")

espHeapGroup = ObjectGroup(
    (1, 3, 9999, 9999, 32)
)
espHeapGroup.setObjects(
      *(("ESPHOME-ESP32-SNMP-MIB", "heapSize"),
        ("ESPHOME-ESP32-SNMP-MIB", "freeHeap"),
        ("ESPHOME-ESP32-SNMP-MIB", "minimumFreeHeap"),
        ("ESPHOME-ESP32-SNMP-MIB", "maximumAllocatedHeap"))
)
if mibBuilder.loadTexts:
    espHeapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ESPHOME-ESP32-SNMP-MIB",
    **{"KBytes": KBytes,
       "esphome": esphome,
       "chip": chip,
       "chipType": chipType,
       "cpuClock": cpuClock,
       "chipModel": chipModel,
       "numCores": numCores,
       "chipRevision": chipRevision,
       "wifi": wifi,
       "rssi": rssi,
       "bssi": bssi,
       "ssid": ssid,
       "ipaddress": ipaddress,
       "heap": heap,
       "heapSize": heapSize,
       "freeHeap": freeHeap,
       "maxFreeHeapBlock": maxFreeHeapBlock,
       "minimumFreeHeap": minimumFreeHeap,
       "maximumAllocatedHeap": maximumAllocatedHeap,
       "groups": groups,
       "chipGroup": chipGroup,
       "wifiGroup": wifiGroup,
       "espHeapGroup": espHeapGroup}
)
