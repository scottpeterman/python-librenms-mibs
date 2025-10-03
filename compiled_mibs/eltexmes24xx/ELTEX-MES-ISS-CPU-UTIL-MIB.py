# SNMP MIB module (ELTEX-MES-ISS-CPU-UTIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eltexmes24xx\ELTEX-MES-ISS-CPU-UTIL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:47 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssCpuUtilMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6)
)
if mibBuilder.loadTexts:
    eltMesIssCpuUtilMIB.setRevisions(
        ("2018-12-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssCpuUtilObjects_ObjectIdentity = ObjectIdentity
eltMesIssCpuUtilObjects = _EltMesIssCpuUtilObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1)
)
_EltMesIssCpuUtilGlobal_ObjectIdentity = ObjectIdentity
eltMesIssCpuUtilGlobal = _EltMesIssCpuUtilGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 1)
)
_EltMesIssCpuUtilGlobalConfig_ObjectIdentity = ObjectIdentity
eltMesIssCpuUtilGlobalConfig = _EltMesIssCpuUtilGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 1, 1)
)


class _EltMesIssCpuUtilEnable_Type(TruthValue):
    """Custom type eltMesIssCpuUtilEnable based on TruthValue"""
    defaultValue = 1


_EltMesIssCpuUtilEnable_Type.__name__ = "TruthValue"
_EltMesIssCpuUtilEnable_Object = MibScalar
eltMesIssCpuUtilEnable = _EltMesIssCpuUtilEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 1, 1, 1),
    _EltMesIssCpuUtilEnable_Type()
)
eltMesIssCpuUtilEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssCpuUtilEnable.setStatus("current")
_EltMesIssCpuUtilGlobalStat_ObjectIdentity = ObjectIdentity
eltMesIssCpuUtilGlobalStat = _EltMesIssCpuUtilGlobalStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 1, 2)
)


class _EltMesIssCpuUtilLast5Seconds_Type(Integer32):
    """Custom type eltMesIssCpuUtilLast5Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EltMesIssCpuUtilLast5Seconds_Type.__name__ = "Integer32"
_EltMesIssCpuUtilLast5Seconds_Object = MibScalar
eltMesIssCpuUtilLast5Seconds = _EltMesIssCpuUtilLast5Seconds_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 1, 2, 1),
    _EltMesIssCpuUtilLast5Seconds_Type()
)
eltMesIssCpuUtilLast5Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssCpuUtilLast5Seconds.setStatus("current")


class _EltMesIssCpuUtilLastMinute_Type(Integer32):
    """Custom type eltMesIssCpuUtilLastMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EltMesIssCpuUtilLastMinute_Type.__name__ = "Integer32"
_EltMesIssCpuUtilLastMinute_Object = MibScalar
eltMesIssCpuUtilLastMinute = _EltMesIssCpuUtilLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 1, 2, 2),
    _EltMesIssCpuUtilLastMinute_Type()
)
eltMesIssCpuUtilLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssCpuUtilLastMinute.setStatus("current")


class _EltMesIssCpuUtilLast5Minutes_Type(Integer32):
    """Custom type eltMesIssCpuUtilLast5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EltMesIssCpuUtilLast5Minutes_Type.__name__ = "Integer32"
_EltMesIssCpuUtilLast5Minutes_Object = MibScalar
eltMesIssCpuUtilLast5Minutes = _EltMesIssCpuUtilLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 1, 2, 3),
    _EltMesIssCpuUtilLast5Minutes_Type()
)
eltMesIssCpuUtilLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssCpuUtilLast5Minutes.setStatus("current")
_EltMesIssCpuUtilTask_ObjectIdentity = ObjectIdentity
eltMesIssCpuUtilTask = _EltMesIssCpuUtilTask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 2)
)
_EltMesIssCpuUtilTaskConfig_ObjectIdentity = ObjectIdentity
eltMesIssCpuUtilTaskConfig = _EltMesIssCpuUtilTaskConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 2, 1)
)


class _EltMesIssCpuUtilTaskEnable_Type(TruthValue):
    """Custom type eltMesIssCpuUtilTaskEnable based on TruthValue"""
    defaultValue = 1


_EltMesIssCpuUtilTaskEnable_Type.__name__ = "TruthValue"
_EltMesIssCpuUtilTaskEnable_Object = MibScalar
eltMesIssCpuUtilTaskEnable = _EltMesIssCpuUtilTaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 2, 1, 1),
    _EltMesIssCpuUtilTaskEnable_Type()
)
eltMesIssCpuUtilTaskEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssCpuUtilTaskEnable.setStatus("current")
_EltMesIssCpuUtilTaskStat_ObjectIdentity = ObjectIdentity
eltMesIssCpuUtilTaskStat = _EltMesIssCpuUtilTaskStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 2, 2)
)
_EltMesIssCpuUtilTaskStatTable_Object = MibTable
eltMesIssCpuUtilTaskStatTable = _EltMesIssCpuUtilTaskStatTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssCpuUtilTaskStatTable.setStatus("current")
_EltMesIssCpuUtilTaskStatEntry_Object = MibTableRow
eltMesIssCpuUtilTaskStatEntry = _EltMesIssCpuUtilTaskStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 2, 2, 1, 1)
)
eltMesIssCpuUtilTaskStatEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-CPU-UTIL-MIB", "eltMesIssCpuUtilTaskStatIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssCpuUtilTaskStatEntry.setStatus("current")
_EltMesIssCpuUtilTaskStatIndex_Type = Integer32
_EltMesIssCpuUtilTaskStatIndex_Object = MibTableColumn
eltMesIssCpuUtilTaskStatIndex = _EltMesIssCpuUtilTaskStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 2, 2, 1, 1, 1),
    _EltMesIssCpuUtilTaskStatIndex_Type()
)
eltMesIssCpuUtilTaskStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssCpuUtilTaskStatIndex.setStatus("current")
_EltMesIssCpuUtilTaskStatName_Type = DisplayString
_EltMesIssCpuUtilTaskStatName_Object = MibTableColumn
eltMesIssCpuUtilTaskStatName = _EltMesIssCpuUtilTaskStatName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 2, 2, 1, 1, 2),
    _EltMesIssCpuUtilTaskStatName_Type()
)
eltMesIssCpuUtilTaskStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssCpuUtilTaskStatName.setStatus("current")


class _EltMesIssCpuUtilTaskStatLast5Seconds_Type(Integer32):
    """Custom type eltMesIssCpuUtilTaskStatLast5Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EltMesIssCpuUtilTaskStatLast5Seconds_Type.__name__ = "Integer32"
_EltMesIssCpuUtilTaskStatLast5Seconds_Object = MibTableColumn
eltMesIssCpuUtilTaskStatLast5Seconds = _EltMesIssCpuUtilTaskStatLast5Seconds_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 2, 2, 1, 1, 3),
    _EltMesIssCpuUtilTaskStatLast5Seconds_Type()
)
eltMesIssCpuUtilTaskStatLast5Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssCpuUtilTaskStatLast5Seconds.setStatus("current")


class _EltMesIssCpuUtilTaskStatLastMinute_Type(Integer32):
    """Custom type eltMesIssCpuUtilTaskStatLastMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EltMesIssCpuUtilTaskStatLastMinute_Type.__name__ = "Integer32"
_EltMesIssCpuUtilTaskStatLastMinute_Object = MibTableColumn
eltMesIssCpuUtilTaskStatLastMinute = _EltMesIssCpuUtilTaskStatLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 2, 2, 1, 1, 4),
    _EltMesIssCpuUtilTaskStatLastMinute_Type()
)
eltMesIssCpuUtilTaskStatLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssCpuUtilTaskStatLastMinute.setStatus("current")


class _EltMesIssCpuUtilTaskStatLast5Minutes_Type(Integer32):
    """Custom type eltMesIssCpuUtilTaskStatLast5Minutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EltMesIssCpuUtilTaskStatLast5Minutes_Type.__name__ = "Integer32"
_EltMesIssCpuUtilTaskStatLast5Minutes_Object = MibTableColumn
eltMesIssCpuUtilTaskStatLast5Minutes = _EltMesIssCpuUtilTaskStatLast5Minutes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6, 1, 2, 2, 1, 1, 5),
    _EltMesIssCpuUtilTaskStatLast5Minutes_Type()
)
eltMesIssCpuUtilTaskStatLast5Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssCpuUtilTaskStatLast5Minutes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-CPU-UTIL-MIB",
    **{"eltMesIssCpuUtilMIB": eltMesIssCpuUtilMIB,
       "eltMesIssCpuUtilObjects": eltMesIssCpuUtilObjects,
       "eltMesIssCpuUtilGlobal": eltMesIssCpuUtilGlobal,
       "eltMesIssCpuUtilGlobalConfig": eltMesIssCpuUtilGlobalConfig,
       "eltMesIssCpuUtilEnable": eltMesIssCpuUtilEnable,
       "eltMesIssCpuUtilGlobalStat": eltMesIssCpuUtilGlobalStat,
       "eltMesIssCpuUtilLast5Seconds": eltMesIssCpuUtilLast5Seconds,
       "eltMesIssCpuUtilLastMinute": eltMesIssCpuUtilLastMinute,
       "eltMesIssCpuUtilLast5Minutes": eltMesIssCpuUtilLast5Minutes,
       "eltMesIssCpuUtilTask": eltMesIssCpuUtilTask,
       "eltMesIssCpuUtilTaskConfig": eltMesIssCpuUtilTaskConfig,
       "eltMesIssCpuUtilTaskEnable": eltMesIssCpuUtilTaskEnable,
       "eltMesIssCpuUtilTaskStat": eltMesIssCpuUtilTaskStat,
       "eltMesIssCpuUtilTaskStatTable": eltMesIssCpuUtilTaskStatTable,
       "eltMesIssCpuUtilTaskStatEntry": eltMesIssCpuUtilTaskStatEntry,
       "eltMesIssCpuUtilTaskStatIndex": eltMesIssCpuUtilTaskStatIndex,
       "eltMesIssCpuUtilTaskStatName": eltMesIssCpuUtilTaskStatName,
       "eltMesIssCpuUtilTaskStatLast5Seconds": eltMesIssCpuUtilTaskStatLast5Seconds,
       "eltMesIssCpuUtilTaskStatLastMinute": eltMesIssCpuUtilTaskStatLastMinute,
       "eltMesIssCpuUtilTaskStatLast5Minutes": eltMesIssCpuUtilTaskStatLast5Minutes}
)
