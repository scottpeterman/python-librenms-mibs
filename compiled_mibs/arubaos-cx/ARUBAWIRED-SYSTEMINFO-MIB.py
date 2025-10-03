# SNMP MIB module (ARUBAWIRED-SYSTEMINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-SYSTEMINFO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:28 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

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

arubaWiredSystemInfoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22)
)
if mibBuilder.loadTexts:
    arubaWiredSystemInfoMIB.setRevisions(
        ("2021-11-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredSystemInfoNotifications_ObjectIdentity = ObjectIdentity
arubaWiredSystemInfoNotifications = _ArubaWiredSystemInfoNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 0)
)
_ArubaWiredSystemInfoObjects_ObjectIdentity = ObjectIdentity
arubaWiredSystemInfoObjects = _ArubaWiredSystemInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1)
)
_ArubaWiredSystemInfo_ObjectIdentity = ObjectIdentity
arubaWiredSystemInfo = _ArubaWiredSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0)
)
_ArubaWiredSystemInfoTable_Object = MibTable
arubaWiredSystemInfoTable = _ArubaWiredSystemInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1)
)
if mibBuilder.loadTexts:
    arubaWiredSystemInfoTable.setStatus("current")
_ArubaWiredSystemInfoEntry_Object = MibTableRow
arubaWiredSystemInfoEntry = _ArubaWiredSystemInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1)
)
arubaWiredSystemInfoEntry.setIndexNames(
    (0, "ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoModuleType"),
    (0, "ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoModuleName"),
)
if mibBuilder.loadTexts:
    arubaWiredSystemInfoEntry.setStatus("current")


class _ArubaWiredSystemInfoModuleType_Type(DisplayString):
    """Custom type arubaWiredSystemInfoModuleType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ArubaWiredSystemInfoModuleType_Type.__name__ = "DisplayString"
_ArubaWiredSystemInfoModuleType_Object = MibTableColumn
arubaWiredSystemInfoModuleType = _ArubaWiredSystemInfoModuleType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1, 1),
    _ArubaWiredSystemInfoModuleType_Type()
)
arubaWiredSystemInfoModuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredSystemInfoModuleType.setStatus("current")


class _ArubaWiredSystemInfoModuleName_Type(DisplayString):
    """Custom type arubaWiredSystemInfoModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ArubaWiredSystemInfoModuleName_Type.__name__ = "DisplayString"
_ArubaWiredSystemInfoModuleName_Object = MibTableColumn
arubaWiredSystemInfoModuleName = _ArubaWiredSystemInfoModuleName_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1, 2),
    _ArubaWiredSystemInfoModuleName_Type()
)
arubaWiredSystemInfoModuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredSystemInfoModuleName.setStatus("current")


class _ArubaWiredSystemInfoCpu_Type(Unsigned32):
    """Custom type arubaWiredSystemInfoCpu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArubaWiredSystemInfoCpu_Type.__name__ = "Unsigned32"
_ArubaWiredSystemInfoCpu_Object = MibTableColumn
arubaWiredSystemInfoCpu = _ArubaWiredSystemInfoCpu_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1, 3),
    _ArubaWiredSystemInfoCpu_Type()
)
arubaWiredSystemInfoCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSystemInfoCpu.setStatus("current")


class _ArubaWiredSystemInfoMemory_Type(Unsigned32):
    """Custom type arubaWiredSystemInfoMemory based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArubaWiredSystemInfoMemory_Type.__name__ = "Unsigned32"
_ArubaWiredSystemInfoMemory_Object = MibTableColumn
arubaWiredSystemInfoMemory = _ArubaWiredSystemInfoMemory_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1, 4),
    _ArubaWiredSystemInfoMemory_Type()
)
arubaWiredSystemInfoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSystemInfoMemory.setStatus("current")


class _ArubaWiredSystemInfoStorageNos_Type(Unsigned32):
    """Custom type arubaWiredSystemInfoStorageNos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArubaWiredSystemInfoStorageNos_Type.__name__ = "Unsigned32"
_ArubaWiredSystemInfoStorageNos_Object = MibTableColumn
arubaWiredSystemInfoStorageNos = _ArubaWiredSystemInfoStorageNos_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1, 5),
    _ArubaWiredSystemInfoStorageNos_Type()
)
arubaWiredSystemInfoStorageNos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSystemInfoStorageNos.setStatus("current")


class _ArubaWiredSystemInfoStorageLog_Type(Unsigned32):
    """Custom type arubaWiredSystemInfoStorageLog based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArubaWiredSystemInfoStorageLog_Type.__name__ = "Unsigned32"
_ArubaWiredSystemInfoStorageLog_Object = MibTableColumn
arubaWiredSystemInfoStorageLog = _ArubaWiredSystemInfoStorageLog_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1, 6),
    _ArubaWiredSystemInfoStorageLog_Type()
)
arubaWiredSystemInfoStorageLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSystemInfoStorageLog.setStatus("current")


class _ArubaWiredSystemInfoStorageCoredump_Type(Unsigned32):
    """Custom type arubaWiredSystemInfoStorageCoredump based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArubaWiredSystemInfoStorageCoredump_Type.__name__ = "Unsigned32"
_ArubaWiredSystemInfoStorageCoredump_Object = MibTableColumn
arubaWiredSystemInfoStorageCoredump = _ArubaWiredSystemInfoStorageCoredump_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1, 7),
    _ArubaWiredSystemInfoStorageCoredump_Type()
)
arubaWiredSystemInfoStorageCoredump.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSystemInfoStorageCoredump.setStatus("current")


class _ArubaWiredSystemInfoStorageSecurity_Type(Unsigned32):
    """Custom type arubaWiredSystemInfoStorageSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArubaWiredSystemInfoStorageSecurity_Type.__name__ = "Unsigned32"
_ArubaWiredSystemInfoStorageSecurity_Object = MibTableColumn
arubaWiredSystemInfoStorageSecurity = _ArubaWiredSystemInfoStorageSecurity_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1, 8),
    _ArubaWiredSystemInfoStorageSecurity_Type()
)
arubaWiredSystemInfoStorageSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSystemInfoStorageSecurity.setStatus("current")


class _ArubaWiredSystemInfoStorageSelftest_Type(Unsigned32):
    """Custom type arubaWiredSystemInfoStorageSelftest based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArubaWiredSystemInfoStorageSelftest_Type.__name__ = "Unsigned32"
_ArubaWiredSystemInfoStorageSelftest_Object = MibTableColumn
arubaWiredSystemInfoStorageSelftest = _ArubaWiredSystemInfoStorageSelftest_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1, 9),
    _ArubaWiredSystemInfoStorageSelftest_Type()
)
arubaWiredSystemInfoStorageSelftest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSystemInfoStorageSelftest.setStatus("current")


class _ArubaWiredSystemInfoCpuAvgOneMin_Type(Unsigned32):
    """Custom type arubaWiredSystemInfoCpuAvgOneMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArubaWiredSystemInfoCpuAvgOneMin_Type.__name__ = "Unsigned32"
_ArubaWiredSystemInfoCpuAvgOneMin_Object = MibTableColumn
arubaWiredSystemInfoCpuAvgOneMin = _ArubaWiredSystemInfoCpuAvgOneMin_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1, 10),
    _ArubaWiredSystemInfoCpuAvgOneMin_Type()
)
arubaWiredSystemInfoCpuAvgOneMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSystemInfoCpuAvgOneMin.setStatus("current")


class _ArubaWiredSystemInfoCpuAvgFiveMin_Type(Unsigned32):
    """Custom type arubaWiredSystemInfoCpuAvgFiveMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArubaWiredSystemInfoCpuAvgFiveMin_Type.__name__ = "Unsigned32"
_ArubaWiredSystemInfoCpuAvgFiveMin_Object = MibTableColumn
arubaWiredSystemInfoCpuAvgFiveMin = _ArubaWiredSystemInfoCpuAvgFiveMin_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 1, 0, 1, 1, 11),
    _ArubaWiredSystemInfoCpuAvgFiveMin_Type()
)
arubaWiredSystemInfoCpuAvgFiveMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredSystemInfoCpuAvgFiveMin.setStatus("current")
_ArubaWiredSystemInfoConformance_ObjectIdentity = ObjectIdentity
arubaWiredSystemInfoConformance = _ArubaWiredSystemInfoConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 2)
)
_ArubaWiredSystemInfoCompliances_ObjectIdentity = ObjectIdentity
arubaWiredSystemInfoCompliances = _ArubaWiredSystemInfoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 2, 1)
)
_ArubaWiredSystemInfoGroups_ObjectIdentity = ObjectIdentity
arubaWiredSystemInfoGroups = _ArubaWiredSystemInfoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 2, 2)
)

# Managed Objects groups

arubaWiredSystemInfoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 2, 2, 1)
)
arubaWiredSystemInfoTableGroup.setObjects(
      *(("ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoCpu"),
        ("ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoMemory"),
        ("ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoStorageNos"),
        ("ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoStorageLog"),
        ("ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoStorageCoredump"),
        ("ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoStorageSecurity"),
        ("ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoStorageSelftest"),
        ("ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoCpuAvgOneMin"),
        ("ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoCpuAvgFiveMin"))
)
if mibBuilder.loadTexts:
    arubaWiredSystemInfoTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredSystemInfoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22, 2, 1, 1)
)
arubaWiredSystemInfoCompliance.setObjects(
    ("ARUBAWIRED-SYSTEMINFO-MIB", "arubaWiredSystemInfoTableGroup")
)
if mibBuilder.loadTexts:
    arubaWiredSystemInfoCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-SYSTEMINFO-MIB",
    **{"arubaWiredSystemInfoMIB": arubaWiredSystemInfoMIB,
       "arubaWiredSystemInfoNotifications": arubaWiredSystemInfoNotifications,
       "arubaWiredSystemInfoObjects": arubaWiredSystemInfoObjects,
       "arubaWiredSystemInfo": arubaWiredSystemInfo,
       "arubaWiredSystemInfoTable": arubaWiredSystemInfoTable,
       "arubaWiredSystemInfoEntry": arubaWiredSystemInfoEntry,
       "arubaWiredSystemInfoModuleType": arubaWiredSystemInfoModuleType,
       "arubaWiredSystemInfoModuleName": arubaWiredSystemInfoModuleName,
       "arubaWiredSystemInfoCpu": arubaWiredSystemInfoCpu,
       "arubaWiredSystemInfoMemory": arubaWiredSystemInfoMemory,
       "arubaWiredSystemInfoStorageNos": arubaWiredSystemInfoStorageNos,
       "arubaWiredSystemInfoStorageLog": arubaWiredSystemInfoStorageLog,
       "arubaWiredSystemInfoStorageCoredump": arubaWiredSystemInfoStorageCoredump,
       "arubaWiredSystemInfoStorageSecurity": arubaWiredSystemInfoStorageSecurity,
       "arubaWiredSystemInfoStorageSelftest": arubaWiredSystemInfoStorageSelftest,
       "arubaWiredSystemInfoCpuAvgOneMin": arubaWiredSystemInfoCpuAvgOneMin,
       "arubaWiredSystemInfoCpuAvgFiveMin": arubaWiredSystemInfoCpuAvgFiveMin,
       "arubaWiredSystemInfoConformance": arubaWiredSystemInfoConformance,
       "arubaWiredSystemInfoCompliances": arubaWiredSystemInfoCompliances,
       "arubaWiredSystemInfoCompliance": arubaWiredSystemInfoCompliance,
       "arubaWiredSystemInfoGroups": arubaWiredSystemInfoGroups,
       "arubaWiredSystemInfoTableGroup": arubaWiredSystemInfoTableGroup}
)
