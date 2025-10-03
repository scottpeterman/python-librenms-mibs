# SNMP MIB module (HH3C-DOT11-WM2U-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DOT11-WM2U-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:09 2025
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

(hh3cDot11,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cDot11")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cDot11WM2U = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16)
)
if mibBuilder.loadTexts:
    hh3cDot11WM2U.setRevisions(
        ("2016-01-25 10:20",
         "2015-03-31 15:51")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cDot11WM2UEnableStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



class Hh3cDot11WM2UAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("unicast", 2),
          ("multicast", 3))
    )



class Hh3cDot11WM2UGroupVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("igmpv1orv2", 1),
          ("igmpv3", 2),
          ("mldv1", 3),
          ("mldv2", 4))
    )



class Hh3cDot11WM2UGroupMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11WM2UConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11WM2UConfigGroup = _Hh3cDot11WM2UConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1)
)
_Hh3cDot11WM2USrvTempStatesTable_Object = MibTable
hh3cDot11WM2USrvTempStatesTable = _Hh3cDot11WM2USrvTempStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11WM2USrvTempStatesTable.setStatus("current")
_Hh3cDot11WM2USrvTempStatesEntry_Object = MibTableRow
hh3cDot11WM2USrvTempStatesEntry = _Hh3cDot11WM2USrvTempStatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 1, 1)
)
hh3cDot11WM2USrvTempStatesEntry.setIndexNames(
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2USrvTempName"),
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2USrvTempAddressType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WM2USrvTempStatesEntry.setStatus("current")


class _Hh3cDot11WM2USrvTempName_Type(OctetString):
    """Custom type hh3cDot11WM2USrvTempName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WM2USrvTempName_Type.__name__ = "OctetString"
_Hh3cDot11WM2USrvTempName_Object = MibTableColumn
hh3cDot11WM2USrvTempName = _Hh3cDot11WM2USrvTempName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 1, 1, 1),
    _Hh3cDot11WM2USrvTempName_Type()
)
hh3cDot11WM2USrvTempName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2USrvTempName.setStatus("current")
_Hh3cDot11WM2USrvTempAddressType_Type = InetAddressType
_Hh3cDot11WM2USrvTempAddressType_Object = MibTableColumn
hh3cDot11WM2USrvTempAddressType = _Hh3cDot11WM2USrvTempAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 1, 1, 2),
    _Hh3cDot11WM2USrvTempAddressType_Type()
)
hh3cDot11WM2USrvTempAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2USrvTempAddressType.setStatus("current")
_Hh3cDot11WM2USrvTempState_Type = Hh3cDot11WM2UEnableStatus
_Hh3cDot11WM2USrvTempState_Object = MibTableColumn
hh3cDot11WM2USrvTempState = _Hh3cDot11WM2USrvTempState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 1, 1, 3),
    _Hh3cDot11WM2USrvTempState_Type()
)
hh3cDot11WM2USrvTempState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2USrvTempState.setStatus("current")
_Hh3cDot11WM2UAgingTimeTable_Object = MibTable
hh3cDot11WM2UAgingTimeTable = _Hh3cDot11WM2UAgingTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UAgingTimeTable.setStatus("current")
_Hh3cDot11WM2UAgingTimeEntry_Object = MibTableRow
hh3cDot11WM2UAgingTimeEntry = _Hh3cDot11WM2UAgingTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 2, 1)
)
hh3cDot11WM2UAgingTimeEntry.setIndexNames(
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2UAgingAddressType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UAgingTimeEntry.setStatus("current")
_Hh3cDot11WM2UAgingAddressType_Type = InetAddressType
_Hh3cDot11WM2UAgingAddressType_Object = MibTableColumn
hh3cDot11WM2UAgingAddressType = _Hh3cDot11WM2UAgingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 2, 1, 1),
    _Hh3cDot11WM2UAgingAddressType_Type()
)
hh3cDot11WM2UAgingAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2UAgingAddressType.setStatus("current")


class _Hh3cDot11WM2UAgingTime_Type(Unsigned32):
    """Custom type hh3cDot11WM2UAgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_Hh3cDot11WM2UAgingTime_Type.__name__ = "Unsigned32"
_Hh3cDot11WM2UAgingTime_Object = MibTableColumn
hh3cDot11WM2UAgingTime = _Hh3cDot11WM2UAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 2, 1, 2),
    _Hh3cDot11WM2UAgingTime_Type()
)
hh3cDot11WM2UAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2UAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11WM2UAgingTime.setUnits("seconds")
_Hh3cDot11WM2UAgingTimeState_Type = Hh3cDot11WM2UEnableStatus
_Hh3cDot11WM2UAgingTimeState_Object = MibTableColumn
hh3cDot11WM2UAgingTimeState = _Hh3cDot11WM2UAgingTimeState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 2, 1, 3),
    _Hh3cDot11WM2UAgingTimeState_Type()
)
hh3cDot11WM2UAgingTimeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2UAgingTimeState.setStatus("current")
_Hh3cDot11WM2UClientEtyLmtTable_Object = MibTable
hh3cDot11WM2UClientEtyLmtTable = _Hh3cDot11WM2UClientEtyLmtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UClientEtyLmtTable.setStatus("current")
_Hh3cDot11WM2UClientEtyLmtEntry_Object = MibTableRow
hh3cDot11WM2UClientEtyLmtEntry = _Hh3cDot11WM2UClientEtyLmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 3, 1)
)
hh3cDot11WM2UClientEtyLmtEntry.setIndexNames(
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2UClientEtyAddrType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UClientEtyLmtEntry.setStatus("current")
_Hh3cDot11WM2UClientEtyAddrType_Type = InetAddressType
_Hh3cDot11WM2UClientEtyAddrType_Object = MibTableColumn
hh3cDot11WM2UClientEtyAddrType = _Hh3cDot11WM2UClientEtyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 3, 1, 1),
    _Hh3cDot11WM2UClientEtyAddrType_Type()
)
hh3cDot11WM2UClientEtyAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2UClientEtyAddrType.setStatus("current")


class _Hh3cDot11WM2UClientValue_Type(Unsigned32):
    """Custom type hh3cDot11WM2UClientValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1024),
    )


_Hh3cDot11WM2UClientValue_Type.__name__ = "Unsigned32"
_Hh3cDot11WM2UClientValue_Object = MibTableColumn
hh3cDot11WM2UClientValue = _Hh3cDot11WM2UClientValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 3, 1, 2),
    _Hh3cDot11WM2UClientValue_Type()
)
hh3cDot11WM2UClientValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2UClientValue.setStatus("current")
_Hh3cDot11WM2UClientState_Type = Hh3cDot11WM2UEnableStatus
_Hh3cDot11WM2UClientState_Object = MibTableColumn
hh3cDot11WM2UClientState = _Hh3cDot11WM2UClientState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 3, 1, 3),
    _Hh3cDot11WM2UClientState_Type()
)
hh3cDot11WM2UClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2UClientState.setStatus("current")
_Hh3cDot11WM2UGlobalEtyLmtTable_Object = MibTable
hh3cDot11WM2UGlobalEtyLmtTable = _Hh3cDot11WM2UGlobalEtyLmtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UGlobalEtyLmtTable.setStatus("current")
_Hh3cDot11WM2UGlobalEtyLmtEntry_Object = MibTableRow
hh3cDot11WM2UGlobalEtyLmtEntry = _Hh3cDot11WM2UGlobalEtyLmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 4, 1)
)
hh3cDot11WM2UGlobalEtyLmtEntry.setIndexNames(
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2UGlobalEtyAddrType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UGlobalEtyLmtEntry.setStatus("current")
_Hh3cDot11WM2UGlobalEtyAddrType_Type = InetAddressType
_Hh3cDot11WM2UGlobalEtyAddrType_Object = MibTableColumn
hh3cDot11WM2UGlobalEtyAddrType = _Hh3cDot11WM2UGlobalEtyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 4, 1, 1),
    _Hh3cDot11WM2UGlobalEtyAddrType_Type()
)
hh3cDot11WM2UGlobalEtyAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2UGlobalEtyAddrType.setStatus("current")


class _Hh3cDot11WM2UGlobalValue_Type(Unsigned32):
    """Custom type hh3cDot11WM2UGlobalValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8192),
    )


_Hh3cDot11WM2UGlobalValue_Type.__name__ = "Unsigned32"
_Hh3cDot11WM2UGlobalValue_Object = MibTableColumn
hh3cDot11WM2UGlobalValue = _Hh3cDot11WM2UGlobalValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 4, 1, 2),
    _Hh3cDot11WM2UGlobalValue_Type()
)
hh3cDot11WM2UGlobalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2UGlobalValue.setStatus("current")
_Hh3cDot11WM2UGlobalState_Type = Hh3cDot11WM2UEnableStatus
_Hh3cDot11WM2UGlobalState_Object = MibTableColumn
hh3cDot11WM2UGlobalState = _Hh3cDot11WM2UGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 4, 1, 3),
    _Hh3cDot11WM2UGlobalState_Type()
)
hh3cDot11WM2UGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2UGlobalState.setStatus("current")
_Hh3cDot11WM2UFwdClientLmtsTable_Object = MibTable
hh3cDot11WM2UFwdClientLmtsTable = _Hh3cDot11WM2UFwdClientLmtsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UFwdClientLmtsTable.setStatus("current")
_Hh3cDot11WM2UFwdClientLmtsEntry_Object = MibTableRow
hh3cDot11WM2UFwdClientLmtsEntry = _Hh3cDot11WM2UFwdClientLmtsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 5, 1)
)
hh3cDot11WM2UFwdClientLmtsEntry.setIndexNames(
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2UFwdClientAddrType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UFwdClientLmtsEntry.setStatus("current")
_Hh3cDot11WM2UFwdClientAddrType_Type = InetAddressType
_Hh3cDot11WM2UFwdClientAddrType_Object = MibTableColumn
hh3cDot11WM2UFwdClientAddrType = _Hh3cDot11WM2UFwdClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 5, 1, 1),
    _Hh3cDot11WM2UFwdClientAddrType_Type()
)
hh3cDot11WM2UFwdClientAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2UFwdClientAddrType.setStatus("current")


class _Hh3cDot11WM2UFwdClientValue_Type(Unsigned32):
    """Custom type hh3cDot11WM2UFwdClientValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Hh3cDot11WM2UFwdClientValue_Type.__name__ = "Unsigned32"
_Hh3cDot11WM2UFwdClientValue_Object = MibTableColumn
hh3cDot11WM2UFwdClientValue = _Hh3cDot11WM2UFwdClientValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 5, 1, 2),
    _Hh3cDot11WM2UFwdClientValue_Type()
)
hh3cDot11WM2UFwdClientValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2UFwdClientValue.setStatus("current")
_Hh3cDot11WM2UFwdClientAction_Type = Hh3cDot11WM2UAction
_Hh3cDot11WM2UFwdClientAction_Object = MibTableColumn
hh3cDot11WM2UFwdClientAction = _Hh3cDot11WM2UFwdClientAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 5, 1, 3),
    _Hh3cDot11WM2UFwdClientAction_Type()
)
hh3cDot11WM2UFwdClientAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2UFwdClientAction.setStatus("current")
_Hh3cDot11WM2UFwdClientState_Type = Hh3cDot11WM2UEnableStatus
_Hh3cDot11WM2UFwdClientState_Object = MibTableColumn
hh3cDot11WM2UFwdClientState = _Hh3cDot11WM2UFwdClientState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 5, 1, 4),
    _Hh3cDot11WM2UFwdClientState_Type()
)
hh3cDot11WM2UFwdClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2UFwdClientState.setStatus("current")
_Hh3cDot11WM2URateLimitsTable_Object = MibTable
hh3cDot11WM2URateLimitsTable = _Hh3cDot11WM2URateLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11WM2URateLimitsTable.setStatus("current")
_Hh3cDot11WM2URateLimitsEntry_Object = MibTableRow
hh3cDot11WM2URateLimitsEntry = _Hh3cDot11WM2URateLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 6, 1)
)
hh3cDot11WM2URateLimitsEntry.setIndexNames(
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2URateLmtsAddrType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WM2URateLimitsEntry.setStatus("current")
_Hh3cDot11WM2URateLmtsAddrType_Type = InetAddressType
_Hh3cDot11WM2URateLmtsAddrType_Object = MibTableColumn
hh3cDot11WM2URateLmtsAddrType = _Hh3cDot11WM2URateLmtsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 6, 1, 1),
    _Hh3cDot11WM2URateLmtsAddrType_Type()
)
hh3cDot11WM2URateLmtsAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2URateLmtsAddrType.setStatus("current")


class _Hh3cDot11WM2UInterval_Type(Unsigned32):
    """Custom type hh3cDot11WM2UInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_Hh3cDot11WM2UInterval_Type.__name__ = "Unsigned32"
_Hh3cDot11WM2UInterval_Object = MibTableColumn
hh3cDot11WM2UInterval = _Hh3cDot11WM2UInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 6, 1, 2),
    _Hh3cDot11WM2UInterval_Type()
)
hh3cDot11WM2UInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2UInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11WM2UInterval.setUnits("seconds")


class _Hh3cDot11WM2UThreshold_Type(Unsigned32):
    """Custom type hh3cDot11WM2UThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_Hh3cDot11WM2UThreshold_Type.__name__ = "Unsigned32"
_Hh3cDot11WM2UThreshold_Object = MibTableColumn
hh3cDot11WM2UThreshold = _Hh3cDot11WM2UThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 6, 1, 3),
    _Hh3cDot11WM2UThreshold_Type()
)
hh3cDot11WM2UThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2UThreshold.setStatus("current")
_Hh3cDot11WM2URateLmtsState_Type = Hh3cDot11WM2UEnableStatus
_Hh3cDot11WM2URateLmtsState_Object = MibTableColumn
hh3cDot11WM2URateLmtsState = _Hh3cDot11WM2URateLmtsState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 1, 6, 1, 4),
    _Hh3cDot11WM2URateLmtsState_Type()
)
hh3cDot11WM2URateLmtsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WM2URateLmtsState.setStatus("current")
_Hh3cDot11WM2UDataGroup_ObjectIdentity = ObjectIdentity
hh3cDot11WM2UDataGroup = _Hh3cDot11WM2UDataGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2)
)
_Hh3cDot11WM2UClientsTable_Object = MibTable
hh3cDot11WM2UClientsTable = _Hh3cDot11WM2UClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UClientsTable.setStatus("current")
_Hh3cDot11WM2UClientsEntry_Object = MibTableRow
hh3cDot11WM2UClientsEntry = _Hh3cDot11WM2UClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 1, 1)
)
hh3cDot11WM2UClientsEntry.setIndexNames(
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2UClientMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UClientsEntry.setStatus("current")
_Hh3cDot11WM2UClientMacAddress_Type = MacAddress
_Hh3cDot11WM2UClientMacAddress_Object = MibTableColumn
hh3cDot11WM2UClientMacAddress = _Hh3cDot11WM2UClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 1, 1, 1),
    _Hh3cDot11WM2UClientMacAddress_Type()
)
hh3cDot11WM2UClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2UClientMacAddress.setStatus("current")
_Hh3cDot11WM2UDuration_Type = TimeTicks
_Hh3cDot11WM2UDuration_Object = MibTableColumn
hh3cDot11WM2UDuration = _Hh3cDot11WM2UDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 1, 1, 2),
    _Hh3cDot11WM2UDuration_Type()
)
hh3cDot11WM2UDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WM2UDuration.setStatus("current")
_Hh3cDot11WM2UGroupNum4_Type = Unsigned32
_Hh3cDot11WM2UGroupNum4_Object = MibTableColumn
hh3cDot11WM2UGroupNum4 = _Hh3cDot11WM2UGroupNum4_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 1, 1, 3),
    _Hh3cDot11WM2UGroupNum4_Type()
)
hh3cDot11WM2UGroupNum4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WM2UGroupNum4.setStatus("current")
_Hh3cDot11WM2UGroupNum6_Type = Unsigned32
_Hh3cDot11WM2UGroupNum6_Object = MibTableColumn
hh3cDot11WM2UGroupNum6 = _Hh3cDot11WM2UGroupNum6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 1, 1, 4),
    _Hh3cDot11WM2UGroupNum6_Type()
)
hh3cDot11WM2UGroupNum6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WM2UGroupNum6.setStatus("current")
_Hh3cDot11WM2UGroupsTable_Object = MibTable
hh3cDot11WM2UGroupsTable = _Hh3cDot11WM2UGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UGroupsTable.setStatus("current")
_Hh3cDot11WM2UGroupsEntry_Object = MibTableRow
hh3cDot11WM2UGroupsEntry = _Hh3cDot11WM2UGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 2, 1)
)
hh3cDot11WM2UGroupsEntry.setIndexNames(
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2UGrpMacAddress"),
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2UGrpAddressType"),
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2UAddress"),
)
if mibBuilder.loadTexts:
    hh3cDot11WM2UGroupsEntry.setStatus("current")
_Hh3cDot11WM2UGrpMacAddress_Type = MacAddress
_Hh3cDot11WM2UGrpMacAddress_Object = MibTableColumn
hh3cDot11WM2UGrpMacAddress = _Hh3cDot11WM2UGrpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 2, 1, 1),
    _Hh3cDot11WM2UGrpMacAddress_Type()
)
hh3cDot11WM2UGrpMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2UGrpMacAddress.setStatus("current")
_Hh3cDot11WM2UGrpAddressType_Type = InetAddressType
_Hh3cDot11WM2UGrpAddressType_Object = MibTableColumn
hh3cDot11WM2UGrpAddressType = _Hh3cDot11WM2UGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 2, 1, 2),
    _Hh3cDot11WM2UGrpAddressType_Type()
)
hh3cDot11WM2UGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2UGrpAddressType.setStatus("current")
_Hh3cDot11WM2UAddress_Type = InetAddress
_Hh3cDot11WM2UAddress_Object = MibTableColumn
hh3cDot11WM2UAddress = _Hh3cDot11WM2UAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 2, 1, 3),
    _Hh3cDot11WM2UAddress_Type()
)
hh3cDot11WM2UAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2UAddress.setStatus("current")
_Hh3cDot11WM2UVersion_Type = Hh3cDot11WM2UGroupVersion
_Hh3cDot11WM2UVersion_Object = MibTableColumn
hh3cDot11WM2UVersion = _Hh3cDot11WM2UVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 2, 1, 4),
    _Hh3cDot11WM2UVersion_Type()
)
hh3cDot11WM2UVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WM2UVersion.setStatus("current")
_Hh3cDot11WM2UMode_Type = Hh3cDot11WM2UGroupMode
_Hh3cDot11WM2UMode_Object = MibTableColumn
hh3cDot11WM2UMode = _Hh3cDot11WM2UMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 2, 1, 5),
    _Hh3cDot11WM2UMode_Type()
)
hh3cDot11WM2UMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WM2UMode.setStatus("current")
_Hh3cDot11WM2USourceNum_Type = Unsigned32
_Hh3cDot11WM2USourceNum_Object = MibTableColumn
hh3cDot11WM2USourceNum = _Hh3cDot11WM2USourceNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 2, 1, 6),
    _Hh3cDot11WM2USourceNum_Type()
)
hh3cDot11WM2USourceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WM2USourceNum.setStatus("current")
_Hh3cDot11WM2UGrpDurLastRefTime_Type = TimeTicks
_Hh3cDot11WM2UGrpDurLastRefTime_Object = MibTableColumn
hh3cDot11WM2UGrpDurLastRefTime = _Hh3cDot11WM2UGrpDurLastRefTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 2, 1, 7),
    _Hh3cDot11WM2UGrpDurLastRefTime_Type()
)
hh3cDot11WM2UGrpDurLastRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WM2UGrpDurLastRefTime.setStatus("current")
_Hh3cDot11WM2USourcesTable_Object = MibTable
hh3cDot11WM2USourcesTable = _Hh3cDot11WM2USourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11WM2USourcesTable.setStatus("current")
_Hh3cDot11WM2USourcesEntry_Object = MibTableRow
hh3cDot11WM2USourcesEntry = _Hh3cDot11WM2USourcesEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 3, 1)
)
hh3cDot11WM2USourcesEntry.setIndexNames(
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2USrcMacAddress"),
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2USrcAddressType"),
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2UGroupAddress"),
    (0, "HH3C-DOT11-WM2U-MIB", "hh3cDot11WM2USourceAddress"),
)
if mibBuilder.loadTexts:
    hh3cDot11WM2USourcesEntry.setStatus("current")
_Hh3cDot11WM2USrcMacAddress_Type = MacAddress
_Hh3cDot11WM2USrcMacAddress_Object = MibTableColumn
hh3cDot11WM2USrcMacAddress = _Hh3cDot11WM2USrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 3, 1, 1),
    _Hh3cDot11WM2USrcMacAddress_Type()
)
hh3cDot11WM2USrcMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2USrcMacAddress.setStatus("current")
_Hh3cDot11WM2USrcAddressType_Type = InetAddressType
_Hh3cDot11WM2USrcAddressType_Object = MibTableColumn
hh3cDot11WM2USrcAddressType = _Hh3cDot11WM2USrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 3, 1, 2),
    _Hh3cDot11WM2USrcAddressType_Type()
)
hh3cDot11WM2USrcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2USrcAddressType.setStatus("current")
_Hh3cDot11WM2UGroupAddress_Type = InetAddress
_Hh3cDot11WM2UGroupAddress_Object = MibTableColumn
hh3cDot11WM2UGroupAddress = _Hh3cDot11WM2UGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 3, 1, 3),
    _Hh3cDot11WM2UGroupAddress_Type()
)
hh3cDot11WM2UGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2UGroupAddress.setStatus("current")
_Hh3cDot11WM2USourceAddress_Type = InetAddress
_Hh3cDot11WM2USourceAddress_Object = MibTableColumn
hh3cDot11WM2USourceAddress = _Hh3cDot11WM2USourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 3, 1, 4),
    _Hh3cDot11WM2USourceAddress_Type()
)
hh3cDot11WM2USourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WM2USourceAddress.setStatus("current")
_Hh3cDot11WM2USrcDurLastRefTime_Type = TimeTicks
_Hh3cDot11WM2USrcDurLastRefTime_Object = MibTableColumn
hh3cDot11WM2USrcDurLastRefTime = _Hh3cDot11WM2USrcDurLastRefTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 16, 2, 3, 1, 5),
    _Hh3cDot11WM2USrcDurLastRefTime_Type()
)
hh3cDot11WM2USrcDurLastRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WM2USrcDurLastRefTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-WM2U-MIB",
    **{"Hh3cDot11WM2UEnableStatus": Hh3cDot11WM2UEnableStatus,
       "Hh3cDot11WM2UAction": Hh3cDot11WM2UAction,
       "Hh3cDot11WM2UGroupVersion": Hh3cDot11WM2UGroupVersion,
       "Hh3cDot11WM2UGroupMode": Hh3cDot11WM2UGroupMode,
       "hh3cDot11WM2U": hh3cDot11WM2U,
       "hh3cDot11WM2UConfigGroup": hh3cDot11WM2UConfigGroup,
       "hh3cDot11WM2USrvTempStatesTable": hh3cDot11WM2USrvTempStatesTable,
       "hh3cDot11WM2USrvTempStatesEntry": hh3cDot11WM2USrvTempStatesEntry,
       "hh3cDot11WM2USrvTempName": hh3cDot11WM2USrvTempName,
       "hh3cDot11WM2USrvTempAddressType": hh3cDot11WM2USrvTempAddressType,
       "hh3cDot11WM2USrvTempState": hh3cDot11WM2USrvTempState,
       "hh3cDot11WM2UAgingTimeTable": hh3cDot11WM2UAgingTimeTable,
       "hh3cDot11WM2UAgingTimeEntry": hh3cDot11WM2UAgingTimeEntry,
       "hh3cDot11WM2UAgingAddressType": hh3cDot11WM2UAgingAddressType,
       "hh3cDot11WM2UAgingTime": hh3cDot11WM2UAgingTime,
       "hh3cDot11WM2UAgingTimeState": hh3cDot11WM2UAgingTimeState,
       "hh3cDot11WM2UClientEtyLmtTable": hh3cDot11WM2UClientEtyLmtTable,
       "hh3cDot11WM2UClientEtyLmtEntry": hh3cDot11WM2UClientEtyLmtEntry,
       "hh3cDot11WM2UClientEtyAddrType": hh3cDot11WM2UClientEtyAddrType,
       "hh3cDot11WM2UClientValue": hh3cDot11WM2UClientValue,
       "hh3cDot11WM2UClientState": hh3cDot11WM2UClientState,
       "hh3cDot11WM2UGlobalEtyLmtTable": hh3cDot11WM2UGlobalEtyLmtTable,
       "hh3cDot11WM2UGlobalEtyLmtEntry": hh3cDot11WM2UGlobalEtyLmtEntry,
       "hh3cDot11WM2UGlobalEtyAddrType": hh3cDot11WM2UGlobalEtyAddrType,
       "hh3cDot11WM2UGlobalValue": hh3cDot11WM2UGlobalValue,
       "hh3cDot11WM2UGlobalState": hh3cDot11WM2UGlobalState,
       "hh3cDot11WM2UFwdClientLmtsTable": hh3cDot11WM2UFwdClientLmtsTable,
       "hh3cDot11WM2UFwdClientLmtsEntry": hh3cDot11WM2UFwdClientLmtsEntry,
       "hh3cDot11WM2UFwdClientAddrType": hh3cDot11WM2UFwdClientAddrType,
       "hh3cDot11WM2UFwdClientValue": hh3cDot11WM2UFwdClientValue,
       "hh3cDot11WM2UFwdClientAction": hh3cDot11WM2UFwdClientAction,
       "hh3cDot11WM2UFwdClientState": hh3cDot11WM2UFwdClientState,
       "hh3cDot11WM2URateLimitsTable": hh3cDot11WM2URateLimitsTable,
       "hh3cDot11WM2URateLimitsEntry": hh3cDot11WM2URateLimitsEntry,
       "hh3cDot11WM2URateLmtsAddrType": hh3cDot11WM2URateLmtsAddrType,
       "hh3cDot11WM2UInterval": hh3cDot11WM2UInterval,
       "hh3cDot11WM2UThreshold": hh3cDot11WM2UThreshold,
       "hh3cDot11WM2URateLmtsState": hh3cDot11WM2URateLmtsState,
       "hh3cDot11WM2UDataGroup": hh3cDot11WM2UDataGroup,
       "hh3cDot11WM2UClientsTable": hh3cDot11WM2UClientsTable,
       "hh3cDot11WM2UClientsEntry": hh3cDot11WM2UClientsEntry,
       "hh3cDot11WM2UClientMacAddress": hh3cDot11WM2UClientMacAddress,
       "hh3cDot11WM2UDuration": hh3cDot11WM2UDuration,
       "hh3cDot11WM2UGroupNum4": hh3cDot11WM2UGroupNum4,
       "hh3cDot11WM2UGroupNum6": hh3cDot11WM2UGroupNum6,
       "hh3cDot11WM2UGroupsTable": hh3cDot11WM2UGroupsTable,
       "hh3cDot11WM2UGroupsEntry": hh3cDot11WM2UGroupsEntry,
       "hh3cDot11WM2UGrpMacAddress": hh3cDot11WM2UGrpMacAddress,
       "hh3cDot11WM2UGrpAddressType": hh3cDot11WM2UGrpAddressType,
       "hh3cDot11WM2UAddress": hh3cDot11WM2UAddress,
       "hh3cDot11WM2UVersion": hh3cDot11WM2UVersion,
       "hh3cDot11WM2UMode": hh3cDot11WM2UMode,
       "hh3cDot11WM2USourceNum": hh3cDot11WM2USourceNum,
       "hh3cDot11WM2UGrpDurLastRefTime": hh3cDot11WM2UGrpDurLastRefTime,
       "hh3cDot11WM2USourcesTable": hh3cDot11WM2USourcesTable,
       "hh3cDot11WM2USourcesEntry": hh3cDot11WM2USourcesEntry,
       "hh3cDot11WM2USrcMacAddress": hh3cDot11WM2USrcMacAddress,
       "hh3cDot11WM2USrcAddressType": hh3cDot11WM2USrcAddressType,
       "hh3cDot11WM2UGroupAddress": hh3cDot11WM2UGroupAddress,
       "hh3cDot11WM2USourceAddress": hh3cDot11WM2USourceAddress,
       "hh3cDot11WM2USrcDurLastRefTime": hh3cDot11WM2USrcDurLastRefTime}
)
