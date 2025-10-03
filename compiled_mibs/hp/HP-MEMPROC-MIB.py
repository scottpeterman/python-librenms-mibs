# SNMP MIB module (HP-MEMPROC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hp\HP-MEMPROC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:50:40 2025
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

(hpProcurveCommon,) = mibBuilder.importSymbols(
    "HP-BASE-MIB",
    "hpProcurveCommon")

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
 Opaque,
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
    "Opaque",
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

hpMemprocMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5)
)
if mibBuilder.loadTexts:
    hpMemprocMIB.setRevisions(
        ("2005-02-01 14:55",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Float(TextualConvention, Opaque):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7



# MIB Managed Objects in the order of their OIDs

_HpMemprocMIBObjects_ObjectIdentity = ObjectIdentity
hpMemprocMIBObjects = _HpMemprocMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1)
)
_HpmpCPU_ObjectIdentity = ObjectIdentity
hpmpCPU = _HpmpCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1)
)
_HpmpCPUTable_Object = MibTable
hpmpCPUTable = _HpmpCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpmpCPUTable.setStatus("current")
_HpmpCPUEntry_Object = MibTableRow
hpmpCPUEntry = _HpmpCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1)
)
hpmpCPUEntry.setIndexNames(
    (0, "HP-MEMPROC-MIB", "hpmpCPUIndex"),
)
if mibBuilder.loadTexts:
    hpmpCPUEntry.setStatus("current")


class _HpmpCPUIndex_Type(Unsigned32):
    """Custom type hpmpCPUIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpmpCPUIndex_Type.__name__ = "Unsigned32"
_HpmpCPUIndex_Object = MibTableColumn
hpmpCPUIndex = _HpmpCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1, 1),
    _HpmpCPUIndex_Type()
)
hpmpCPUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpmpCPUIndex.setStatus("current")
_HpmpCPULoad1min_Type = Integer32
_HpmpCPULoad1min_Object = MibTableColumn
hpmpCPULoad1min = _HpmpCPULoad1min_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1, 2),
    _HpmpCPULoad1min_Type()
)
hpmpCPULoad1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpmpCPULoad1min.setStatus("current")
_HpmpCPULoad5min_Type = Integer32
_HpmpCPULoad5min_Object = MibTableColumn
hpmpCPULoad5min = _HpmpCPULoad5min_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1, 3),
    _HpmpCPULoad5min_Type()
)
hpmpCPULoad5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpmpCPULoad5min.setStatus("current")
_HpmpCPULoad15min_Type = Integer32
_HpmpCPULoad15min_Object = MibTableColumn
hpmpCPULoad15min = _HpmpCPULoad15min_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1, 4),
    _HpmpCPULoad15min_Type()
)
hpmpCPULoad15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpmpCPULoad15min.setStatus("current")
_HpmpCPUPctBusy_Type = Gauge32
_HpmpCPUPctBusy_Object = MibTableColumn
hpmpCPUPctBusy = _HpmpCPUPctBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1, 5),
    _HpmpCPUPctBusy_Type()
)
hpmpCPUPctBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpmpCPUPctBusy.setStatus("current")
if mibBuilder.loadTexts:
    hpmpCPUPctBusy.setUnits("percent")
_HpmpMemory_ObjectIdentity = ObjectIdentity
hpmpMemory = _HpmpMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2)
)
_HpmpMemTable_Object = MibTable
hpmpMemTable = _HpmpMemTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpmpMemTable.setStatus("current")
_HpmpMemEntry_Object = MibTableRow
hpmpMemEntry = _HpmpMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1)
)
hpmpMemEntry.setIndexNames(
    (0, "HP-MEMPROC-MIB", "hpmpMemIndex"),
)
if mibBuilder.loadTexts:
    hpmpMemEntry.setStatus("current")


class _HpmpMemIndex_Type(Unsigned32):
    """Custom type hpmpMemIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpmpMemIndex_Type.__name__ = "Unsigned32"
_HpmpMemIndex_Object = MibTableColumn
hpmpMemIndex = _HpmpMemIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1, 1),
    _HpmpMemIndex_Type()
)
hpmpMemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpmpMemIndex.setStatus("current")
_HpmpMemDescr_Type = DisplayString
_HpmpMemDescr_Object = MibTableColumn
hpmpMemDescr = _HpmpMemDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1, 2),
    _HpmpMemDescr_Type()
)
hpmpMemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpmpMemDescr.setStatus("current")
_HpmpMemInUse_Type = Unsigned32
_HpmpMemInUse_Object = MibTableColumn
hpmpMemInUse = _HpmpMemInUse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1, 3),
    _HpmpMemInUse_Type()
)
hpmpMemInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpmpMemInUse.setStatus("current")
if mibBuilder.loadTexts:
    hpmpMemInUse.setUnits("Kbytes")
_HpmpMemTotal_Type = Unsigned32
_HpmpMemTotal_Object = MibTableColumn
hpmpMemTotal = _HpmpMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1, 4),
    _HpmpMemTotal_Type()
)
hpmpMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpmpMemTotal.setStatus("current")
if mibBuilder.loadTexts:
    hpmpMemTotal.setUnits("Kbytes")
_HpmpMemPctInUse_Type = Gauge32
_HpmpMemPctInUse_Object = MibTableColumn
hpmpMemPctInUse = _HpmpMemPctInUse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1, 5),
    _HpmpMemPctInUse_Type()
)
hpmpMemPctInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpmpMemPctInUse.setStatus("current")
if mibBuilder.loadTexts:
    hpmpMemPctInUse.setUnits("percent")
_HpMemprocNotificationsPrefix_ObjectIdentity = ObjectIdentity
hpMemprocNotificationsPrefix = _HpMemprocNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 2)
)
_HpMemprocNotifications_ObjectIdentity = ObjectIdentity
hpMemprocNotifications = _HpMemprocNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 2, 0)
)
_HpMemprocMIBConformance_ObjectIdentity = ObjectIdentity
hpMemprocMIBConformance = _HpMemprocMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3)
)
_HpmpCompliances_ObjectIdentity = ObjectIdentity
hpmpCompliances = _HpmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3, 1)
)
_HpmpGroups_ObjectIdentity = ObjectIdentity
hpmpGroups = _HpmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3, 2)
)

# Managed Objects groups

hpmpCPUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3, 2, 1)
)
hpmpCPUGroup.setObjects(
      *(("HP-MEMPROC-MIB", "hpmpCPULoad1min"),
        ("HP-MEMPROC-MIB", "hpmpCPULoad5min"),
        ("HP-MEMPROC-MIB", "hpmpCPULoad15min"),
        ("HP-MEMPROC-MIB", "hpmpCPUPctBusy"))
)
if mibBuilder.loadTexts:
    hpmpCPUGroup.setStatus("current")

hpmpMemoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3, 2, 2)
)
hpmpMemoryGroup.setObjects(
      *(("HP-MEMPROC-MIB", "hpmpMemDescr"),
        ("HP-MEMPROC-MIB", "hpmpMemInUse"),
        ("HP-MEMPROC-MIB", "hpmpMemTotal"),
        ("HP-MEMPROC-MIB", "hpmpMemPctInUse"))
)
if mibBuilder.loadTexts:
    hpmpMemoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpMemprocMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3, 1, 1)
)
hpMemprocMIBCompliance1.setObjects(
      *(("HP-MEMPROC-MIB", "hpmpCPUGroup"),
        ("HP-MEMPROC-MIB", "hpmpMemoryGroup"))
)
if mibBuilder.loadTexts:
    hpMemprocMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-MEMPROC-MIB",
    **{"Float": Float,
       "hpMemprocMIB": hpMemprocMIB,
       "hpMemprocMIBObjects": hpMemprocMIBObjects,
       "hpmpCPU": hpmpCPU,
       "hpmpCPUTable": hpmpCPUTable,
       "hpmpCPUEntry": hpmpCPUEntry,
       "hpmpCPUIndex": hpmpCPUIndex,
       "hpmpCPULoad1min": hpmpCPULoad1min,
       "hpmpCPULoad5min": hpmpCPULoad5min,
       "hpmpCPULoad15min": hpmpCPULoad15min,
       "hpmpCPUPctBusy": hpmpCPUPctBusy,
       "hpmpMemory": hpmpMemory,
       "hpmpMemTable": hpmpMemTable,
       "hpmpMemEntry": hpmpMemEntry,
       "hpmpMemIndex": hpmpMemIndex,
       "hpmpMemDescr": hpmpMemDescr,
       "hpmpMemInUse": hpmpMemInUse,
       "hpmpMemTotal": hpmpMemTotal,
       "hpmpMemPctInUse": hpmpMemPctInUse,
       "hpMemprocNotificationsPrefix": hpMemprocNotificationsPrefix,
       "hpMemprocNotifications": hpMemprocNotifications,
       "hpMemprocMIBConformance": hpMemprocMIBConformance,
       "hpmpCompliances": hpmpCompliances,
       "hpMemprocMIBCompliance1": hpMemprocMIBCompliance1,
       "hpmpGroups": hpmpGroups,
       "hpmpCPUGroup": hpmpCPUGroup,
       "hpmpMemoryGroup": hpmpMemoryGroup}
)
