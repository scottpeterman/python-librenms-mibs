# SNMP MIB module (HH3C-NPV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-NPV-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:24 2025
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

(Hh3cFcVsanIndex,) = mibBuilder.importSymbols(
    "HH3C-FC-TC-MIB",
    "Hh3cFcVsanIndex")

(hh3cSan,
 hh3cVsanIndex) = mibBuilder.importSymbols(
    "HH3C-VSAN-MIB",
    "hh3cSan",
    "hh3cVsanIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hh3cNpv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6)
)
if mibBuilder.loadTexts:
    hh3cNpv.setRevisions(
        ("2014-07-21 00:00",
         "2013-04-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cNpvIfIndexList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cNpvMibObjects_ObjectIdentity = ObjectIdentity
hh3cNpvMibObjects = _Hh3cNpvMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1)
)
_Hh3cNpvConfiguration_ObjectIdentity = ObjectIdentity
hh3cNpvConfiguration = _Hh3cNpvConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1)
)
_Hh3cNpvGlobalObjects_ObjectIdentity = ObjectIdentity
hh3cNpvGlobalObjects = _Hh3cNpvGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 1)
)
_Hh3cNpvLoadbalanceVsan_Type = Hh3cFcVsanIndex
_Hh3cNpvLoadbalanceVsan_Object = MibScalar
hh3cNpvLoadbalanceVsan = _Hh3cNpvLoadbalanceVsan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 1, 1),
    _Hh3cNpvLoadbalanceVsan_Type()
)
hh3cNpvLoadbalanceVsan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNpvLoadbalanceVsan.setStatus("current")
_Hh3cNpvTrafficMapConfigTable_Object = MibTable
hh3cNpvTrafficMapConfigTable = _Hh3cNpvTrafficMapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cNpvTrafficMapConfigTable.setStatus("current")
_Hh3cNpvTrafficMapConfigEntry_Object = MibTableRow
hh3cNpvTrafficMapConfigEntry = _Hh3cNpvTrafficMapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 2, 1)
)
hh3cNpvTrafficMapConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cNpvTrafficMapConfigEntry.setStatus("current")
_Hh3cNpvTrafficMapExternalIfIndexList_Type = Hh3cNpvIfIndexList
_Hh3cNpvTrafficMapExternalIfIndexList_Object = MibTableColumn
hh3cNpvTrafficMapExternalIfIndexList = _Hh3cNpvTrafficMapExternalIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 2, 1, 1),
    _Hh3cNpvTrafficMapExternalIfIndexList_Type()
)
hh3cNpvTrafficMapExternalIfIndexList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNpvTrafficMapExternalIfIndexList.setStatus("current")
_Hh3cNpvTrafficMapLastChange_Type = TimeStamp
_Hh3cNpvTrafficMapLastChange_Object = MibTableColumn
hh3cNpvTrafficMapLastChange = _Hh3cNpvTrafficMapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 2, 1, 2),
    _Hh3cNpvTrafficMapLastChange_Type()
)
hh3cNpvTrafficMapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNpvTrafficMapLastChange.setStatus("current")
_Hh3cNpvTrafficMapRowStatus_Type = RowStatus
_Hh3cNpvTrafficMapRowStatus_Object = MibTableColumn
hh3cNpvTrafficMapRowStatus = _Hh3cNpvTrafficMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 2, 1, 3),
    _Hh3cNpvTrafficMapRowStatus_Type()
)
hh3cNpvTrafficMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNpvTrafficMapRowStatus.setStatus("current")
_Hh3cNpvServerIfTable_Object = MibTable
hh3cNpvServerIfTable = _Hh3cNpvServerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cNpvServerIfTable.setStatus("current")
_Hh3cNpvServerIfEntry_Object = MibTableRow
hh3cNpvServerIfEntry = _Hh3cNpvServerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 3, 1)
)
hh3cNpvServerIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cNpvServerIfEntry.setStatus("current")
_Hh3cNpvExternalIfIndex_Type = InterfaceIndex
_Hh3cNpvExternalIfIndex_Object = MibTableColumn
hh3cNpvExternalIfIndex = _Hh3cNpvExternalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 3, 1, 1),
    _Hh3cNpvExternalIfIndex_Type()
)
hh3cNpvExternalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNpvExternalIfIndex.setStatus("current")
_Hh3cNpvLoadBalanceTable_Object = MibTable
hh3cNpvLoadBalanceTable = _Hh3cNpvLoadBalanceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cNpvLoadBalanceTable.setStatus("current")
_Hh3cNpvLoadBalanceEntry_Object = MibTableRow
hh3cNpvLoadBalanceEntry = _Hh3cNpvLoadBalanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 4, 1)
)
hh3cNpvLoadBalanceEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cNpvLoadBalanceEntry.setStatus("current")


class _Hh3cNpvAutoLoadBalanceEnable_Type(TruthValue):
    """Custom type hh3cNpvAutoLoadBalanceEnable based on TruthValue"""
    defaultValue = 2


_Hh3cNpvAutoLoadBalanceEnable_Type.__name__ = "TruthValue"
_Hh3cNpvAutoLoadBalanceEnable_Object = MibTableColumn
hh3cNpvAutoLoadBalanceEnable = _Hh3cNpvAutoLoadBalanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 4, 1, 1),
    _Hh3cNpvAutoLoadBalanceEnable_Type()
)
hh3cNpvAutoLoadBalanceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNpvAutoLoadBalanceEnable.setStatus("current")


class _Hh3cNpvAutoLoadBalanceInterval_Type(Unsigned32):
    """Custom type hh3cNpvAutoLoadBalanceInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_Hh3cNpvAutoLoadBalanceInterval_Type.__name__ = "Unsigned32"
_Hh3cNpvAutoLoadBalanceInterval_Object = MibTableColumn
hh3cNpvAutoLoadBalanceInterval = _Hh3cNpvAutoLoadBalanceInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 6, 1, 1, 4, 1, 2),
    _Hh3cNpvAutoLoadBalanceInterval_Type()
)
hh3cNpvAutoLoadBalanceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNpvAutoLoadBalanceInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNpvAutoLoadBalanceInterval.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NPV-MIB",
    **{"Hh3cNpvIfIndexList": Hh3cNpvIfIndexList,
       "hh3cNpv": hh3cNpv,
       "hh3cNpvMibObjects": hh3cNpvMibObjects,
       "hh3cNpvConfiguration": hh3cNpvConfiguration,
       "hh3cNpvGlobalObjects": hh3cNpvGlobalObjects,
       "hh3cNpvLoadbalanceVsan": hh3cNpvLoadbalanceVsan,
       "hh3cNpvTrafficMapConfigTable": hh3cNpvTrafficMapConfigTable,
       "hh3cNpvTrafficMapConfigEntry": hh3cNpvTrafficMapConfigEntry,
       "hh3cNpvTrafficMapExternalIfIndexList": hh3cNpvTrafficMapExternalIfIndexList,
       "hh3cNpvTrafficMapLastChange": hh3cNpvTrafficMapLastChange,
       "hh3cNpvTrafficMapRowStatus": hh3cNpvTrafficMapRowStatus,
       "hh3cNpvServerIfTable": hh3cNpvServerIfTable,
       "hh3cNpvServerIfEntry": hh3cNpvServerIfEntry,
       "hh3cNpvExternalIfIndex": hh3cNpvExternalIfIndex,
       "hh3cNpvLoadBalanceTable": hh3cNpvLoadBalanceTable,
       "hh3cNpvLoadBalanceEntry": hh3cNpvLoadBalanceEntry,
       "hh3cNpvAutoLoadBalanceEnable": hh3cNpvAutoLoadBalanceEnable,
       "hh3cNpvAutoLoadBalanceInterval": hh3cNpvAutoLoadBalanceInterval}
)
