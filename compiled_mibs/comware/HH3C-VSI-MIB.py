# SNMP MIB module (HH3C-VSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-VSI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:11 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cVsi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105)
)
if mibBuilder.loadTexts:
    hh3cVsi.setRevisions(
        ("2016-10-29 16:50",
         "2015-05-26 15:55",
         "2009-08-08 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVsiObjects_ObjectIdentity = ObjectIdentity
hh3cVsiObjects = _Hh3cVsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1)
)
_Hh3cVsiScalarGroup_ObjectIdentity = ObjectIdentity
hh3cVsiScalarGroup = _Hh3cVsiScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 1)
)
_Hh3cVsiNextAvailableVsiIndex_Type = Unsigned32
_Hh3cVsiNextAvailableVsiIndex_Object = MibScalar
hh3cVsiNextAvailableVsiIndex = _Hh3cVsiNextAvailableVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 1, 1),
    _Hh3cVsiNextAvailableVsiIndex_Type()
)
hh3cVsiNextAvailableVsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiNextAvailableVsiIndex.setStatus("current")
_Hh3cVsiL2vpnStatus_Type = TruthValue
_Hh3cVsiL2vpnStatus_Object = MibScalar
hh3cVsiL2vpnStatus = _Hh3cVsiL2vpnStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 1, 2),
    _Hh3cVsiL2vpnStatus_Type()
)
hh3cVsiL2vpnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsiL2vpnStatus.setStatus("current")
_Hh3cVsiTable_Object = MibTable
hh3cVsiTable = _Hh3cVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cVsiTable.setStatus("current")
_Hh3cVsiEntry_Object = MibTableRow
hh3cVsiEntry = _Hh3cVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1)
)
hh3cVsiEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsiEntry.setStatus("current")
_Hh3cVsiIndex_Type = Unsigned32
_Hh3cVsiIndex_Object = MibTableColumn
hh3cVsiIndex = _Hh3cVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 1),
    _Hh3cVsiIndex_Type()
)
hh3cVsiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsiIndex.setStatus("current")


class _Hh3cVsiName_Type(OctetString):
    """Custom type hh3cVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cVsiName_Type.__name__ = "OctetString"
_Hh3cVsiName_Object = MibTableColumn
hh3cVsiName = _Hh3cVsiName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 2),
    _Hh3cVsiName_Type()
)
hh3cVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiName.setStatus("current")


class _Hh3cVsiMode_Type(Integer32):
    """Custom type hh3cVsiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("martini", 1),
          ("minm", 2),
          ("martiniAndMinm", 3),
          ("kompella", 4),
          ("kompellaAndMinm", 5),
          ("minmpxp", 6),
          ("martiniAndMinmpxp", 7),
          ("kompellaAndMinmpxp", 8),
          ("vxlan", 9))
    )


_Hh3cVsiMode_Type.__name__ = "Integer32"
_Hh3cVsiMode_Object = MibTableColumn
hh3cVsiMode = _Hh3cVsiMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 3),
    _Hh3cVsiMode_Type()
)
hh3cVsiMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiMode.setStatus("current")
_Hh3cMinmIsid_Type = Integer32
_Hh3cMinmIsid_Object = MibTableColumn
hh3cMinmIsid = _Hh3cMinmIsid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 4),
    _Hh3cMinmIsid_Type()
)
hh3cMinmIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMinmIsid.setStatus("current")
_Hh3cVsiId_Type = Unsigned32
_Hh3cVsiId_Object = MibTableColumn
hh3cVsiId = _Hh3cVsiId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 5),
    _Hh3cVsiId_Type()
)
hh3cVsiId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiId.setStatus("current")


class _Hh3cVsiTransMode_Type(Integer32):
    """Custom type hh3cVsiTransMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("ethernet", 2))
    )


_Hh3cVsiTransMode_Type.__name__ = "Integer32"
_Hh3cVsiTransMode_Object = MibTableColumn
hh3cVsiTransMode = _Hh3cVsiTransMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 6),
    _Hh3cVsiTransMode_Type()
)
hh3cVsiTransMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiTransMode.setStatus("current")


class _Hh3cVsiEnableHubSpoke_Type(Integer32):
    """Custom type hh3cVsiEnableHubSpoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Hh3cVsiEnableHubSpoke_Type.__name__ = "Integer32"
_Hh3cVsiEnableHubSpoke_Object = MibTableColumn
hh3cVsiEnableHubSpoke = _Hh3cVsiEnableHubSpoke_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 7),
    _Hh3cVsiEnableHubSpoke_Type()
)
hh3cVsiEnableHubSpoke.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiEnableHubSpoke.setStatus("current")


class _Hh3cVsiAdminState_Type(Integer32):
    """Custom type hh3cVsiAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminUp", 1),
          ("adminDown", 2))
    )


_Hh3cVsiAdminState_Type.__name__ = "Integer32"
_Hh3cVsiAdminState_Object = MibTableColumn
hh3cVsiAdminState = _Hh3cVsiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 8),
    _Hh3cVsiAdminState_Type()
)
hh3cVsiAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiAdminState.setStatus("current")
_Hh3cVsiRowStatus_Type = RowStatus
_Hh3cVsiRowStatus_Object = MibTableColumn
hh3cVsiRowStatus = _Hh3cVsiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 9),
    _Hh3cVsiRowStatus_Type()
)
hh3cVsiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiRowStatus.setStatus("current")
_Hh3cVsiSpbIsid_Type = Integer32
_Hh3cVsiSpbIsid_Object = MibTableColumn
hh3cVsiSpbIsid = _Hh3cVsiSpbIsid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 10),
    _Hh3cVsiSpbIsid_Type()
)
hh3cVsiSpbIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiSpbIsid.setStatus("current")
_Hh3cVsiVxlanID_Type = Unsigned32
_Hh3cVsiVxlanID_Object = MibTableColumn
hh3cVsiVxlanID = _Hh3cVsiVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 11),
    _Hh3cVsiVxlanID_Type()
)
hh3cVsiVxlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiVxlanID.setStatus("current")


class _Hh3cVsiArpSuppression_Type(TruthValue):
    """Custom type hh3cVsiArpSuppression based on TruthValue"""
    defaultValue = 2


_Hh3cVsiArpSuppression_Type.__name__ = "TruthValue"
_Hh3cVsiArpSuppression_Object = MibTableColumn
hh3cVsiArpSuppression = _Hh3cVsiArpSuppression_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 12),
    _Hh3cVsiArpSuppression_Type()
)
hh3cVsiArpSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiArpSuppression.setStatus("current")


class _Hh3cVsiFlooding_Type(TruthValue):
    """Custom type hh3cVsiFlooding based on TruthValue"""
    defaultValue = 1


_Hh3cVsiFlooding_Type.__name__ = "TruthValue"
_Hh3cVsiFlooding_Object = MibTableColumn
hh3cVsiFlooding = _Hh3cVsiFlooding_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 13),
    _Hh3cVsiFlooding_Type()
)
hh3cVsiFlooding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiFlooding.setStatus("current")
_Hh3cVsiLocalMacCount_Type = Unsigned32
_Hh3cVsiLocalMacCount_Object = MibTableColumn
hh3cVsiLocalMacCount = _Hh3cVsiLocalMacCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 14),
    _Hh3cVsiLocalMacCount_Type()
)
hh3cVsiLocalMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiLocalMacCount.setStatus("current")
_Hh3cVsiInterfaceID_Type = Unsigned32
_Hh3cVsiInterfaceID_Object = MibTableColumn
hh3cVsiInterfaceID = _Hh3cVsiInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 15),
    _Hh3cVsiInterfaceID_Type()
)
hh3cVsiInterfaceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiInterfaceID.setStatus("current")


class _Hh3cVsiStatistics_Type(TruthValue):
    """Custom type hh3cVsiStatistics based on TruthValue"""
    defaultValue = 2


_Hh3cVsiStatistics_Type.__name__ = "TruthValue"
_Hh3cVsiStatistics_Object = MibTableColumn
hh3cVsiStatistics = _Hh3cVsiStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 16),
    _Hh3cVsiStatistics_Type()
)
hh3cVsiStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiStatistics.setStatus("current")
_Hh3cVsiNvgreID_Type = Unsigned32
_Hh3cVsiNvgreID_Object = MibTableColumn
hh3cVsiNvgreID = _Hh3cVsiNvgreID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 17),
    _Hh3cVsiNvgreID_Type()
)
hh3cVsiNvgreID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiNvgreID.setStatus("current")
_Hh3cVsiXconnectTable_Object = MibTable
hh3cVsiXconnectTable = _Hh3cVsiXconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cVsiXconnectTable.setStatus("current")
_Hh3cVsiXconnectEntry_Object = MibTableRow
hh3cVsiXconnectEntry = _Hh3cVsiXconnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1)
)
hh3cVsiXconnectEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiXconnectIfIndex"),
    (0, "HH3C-VSI-MIB", "hh3cVsiXconnectEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hh3cVsiXconnectEntry.setStatus("current")
_Hh3cVsiXconnectIfIndex_Type = Unsigned32
_Hh3cVsiXconnectIfIndex_Object = MibTableColumn
hh3cVsiXconnectIfIndex = _Hh3cVsiXconnectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 1),
    _Hh3cVsiXconnectIfIndex_Type()
)
hh3cVsiXconnectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsiXconnectIfIndex.setStatus("current")
_Hh3cVsiXconnectEvcSrvInstId_Type = Unsigned32
_Hh3cVsiXconnectEvcSrvInstId_Object = MibTableColumn
hh3cVsiXconnectEvcSrvInstId = _Hh3cVsiXconnectEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 2),
    _Hh3cVsiXconnectEvcSrvInstId_Type()
)
hh3cVsiXconnectEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsiXconnectEvcSrvInstId.setStatus("current")


class _Hh3cVsiXconnectVsiName_Type(OctetString):
    """Custom type hh3cVsiXconnectVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cVsiXconnectVsiName_Type.__name__ = "OctetString"
_Hh3cVsiXconnectVsiName_Object = MibTableColumn
hh3cVsiXconnectVsiName = _Hh3cVsiXconnectVsiName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 3),
    _Hh3cVsiXconnectVsiName_Type()
)
hh3cVsiXconnectVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiXconnectVsiName.setStatus("current")


class _Hh3cVsiXconnectAccessMode_Type(Integer32):
    """Custom type hh3cVsiXconnectAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("ethernet", 2))
    )


_Hh3cVsiXconnectAccessMode_Type.__name__ = "Integer32"
_Hh3cVsiXconnectAccessMode_Object = MibTableColumn
hh3cVsiXconnectAccessMode = _Hh3cVsiXconnectAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 4),
    _Hh3cVsiXconnectAccessMode_Type()
)
hh3cVsiXconnectAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiXconnectAccessMode.setStatus("current")


class _Hh3cVsiXconnectHubSpoke_Type(Integer32):
    """Custom type hh3cVsiXconnectHubSpoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("hub", 2),
          ("spoke", 3))
    )


_Hh3cVsiXconnectHubSpoke_Type.__name__ = "Integer32"
_Hh3cVsiXconnectHubSpoke_Object = MibTableColumn
hh3cVsiXconnectHubSpoke = _Hh3cVsiXconnectHubSpoke_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 5),
    _Hh3cVsiXconnectHubSpoke_Type()
)
hh3cVsiXconnectHubSpoke.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiXconnectHubSpoke.setStatus("current")
_Hh3cVsiXconnectRowStatus_Type = RowStatus
_Hh3cVsiXconnectRowStatus_Object = MibTableColumn
hh3cVsiXconnectRowStatus = _Hh3cVsiXconnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 6),
    _Hh3cVsiXconnectRowStatus_Type()
)
hh3cVsiXconnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiXconnectRowStatus.setStatus("current")
_Hh3cVsiPwBindTable_Object = MibTable
hh3cVsiPwBindTable = _Hh3cVsiPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cVsiPwBindTable.setStatus("current")
_Hh3cVsiPwBindEntry_Object = MibTableRow
hh3cVsiPwBindEntry = _Hh3cVsiPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 4, 1)
)
hh3cVsiPwBindEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiIndex"),
    (0, "HH3C-VSI-MIB", "hh3cVsiPwIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsiPwBindEntry.setStatus("current")
_Hh3cVsiPwIndex_Type = Unsigned32
_Hh3cVsiPwIndex_Object = MibTableColumn
hh3cVsiPwIndex = _Hh3cVsiPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 4, 1, 1),
    _Hh3cVsiPwIndex_Type()
)
hh3cVsiPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsiPwIndex.setStatus("current")


class _Hh3cVsiPwBindAttributes_Type(Bits):
    """Custom type hh3cVsiPwBindAttributes based on Bits"""
    namedValues = NamedValues(
        *(("noSplitHorizon", 0),
          ("hub", 1))
    )

_Hh3cVsiPwBindAttributes_Type.__name__ = "Bits"
_Hh3cVsiPwBindAttributes_Object = MibTableColumn
hh3cVsiPwBindAttributes = _Hh3cVsiPwBindAttributes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 4, 1, 2),
    _Hh3cVsiPwBindAttributes_Type()
)
hh3cVsiPwBindAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiPwBindAttributes.setStatus("current")
_Hh3cVsiPwBindRowStatus_Type = RowStatus
_Hh3cVsiPwBindRowStatus_Object = MibTableColumn
hh3cVsiPwBindRowStatus = _Hh3cVsiPwBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 4, 1, 3),
    _Hh3cVsiPwBindRowStatus_Type()
)
hh3cVsiPwBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiPwBindRowStatus.setStatus("current")
_Hh3cVsiFloodMacTable_Object = MibTable
hh3cVsiFloodMacTable = _Hh3cVsiFloodMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cVsiFloodMacTable.setStatus("current")
_Hh3cVsiFloodMacEntry_Object = MibTableRow
hh3cVsiFloodMacEntry = _Hh3cVsiFloodMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 5, 1)
)
hh3cVsiFloodMacEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiIndex"),
    (0, "HH3C-VSI-MIB", "hh3cVsiFloodMac"),
)
if mibBuilder.loadTexts:
    hh3cVsiFloodMacEntry.setStatus("current")
_Hh3cVsiFloodMac_Type = MacAddress
_Hh3cVsiFloodMac_Object = MibTableColumn
hh3cVsiFloodMac = _Hh3cVsiFloodMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 5, 1, 1),
    _Hh3cVsiFloodMac_Type()
)
hh3cVsiFloodMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsiFloodMac.setStatus("current")
_Hh3cVsiFloodMacRowStatus_Type = RowStatus
_Hh3cVsiFloodMacRowStatus_Object = MibTableColumn
hh3cVsiFloodMacRowStatus = _Hh3cVsiFloodMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 5, 1, 2),
    _Hh3cVsiFloodMacRowStatus_Type()
)
hh3cVsiFloodMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiFloodMacRowStatus.setStatus("current")
_Hh3cVsiLocalMacTable_Object = MibTable
hh3cVsiLocalMacTable = _Hh3cVsiLocalMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cVsiLocalMacTable.setStatus("current")
_Hh3cVsiLocalMacEntry_Object = MibTableRow
hh3cVsiLocalMacEntry = _Hh3cVsiLocalMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 6, 1)
)
hh3cVsiLocalMacEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiIndex"),
    (0, "HH3C-VSI-MIB", "hh3cVsiLocalMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cVsiLocalMacEntry.setStatus("current")
_Hh3cVsiLocalMacAddr_Type = MacAddress
_Hh3cVsiLocalMacAddr_Object = MibTableColumn
hh3cVsiLocalMacAddr = _Hh3cVsiLocalMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 6, 1, 1),
    _Hh3cVsiLocalMacAddr_Type()
)
hh3cVsiLocalMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsiLocalMacAddr.setStatus("current")
_Hh3cVsiLocalMacIfIndex_Type = InterfaceIndex
_Hh3cVsiLocalMacIfIndex_Object = MibTableColumn
hh3cVsiLocalMacIfIndex = _Hh3cVsiLocalMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 6, 1, 2),
    _Hh3cVsiLocalMacIfIndex_Type()
)
hh3cVsiLocalMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiLocalMacIfIndex.setStatus("current")
_Hh3cVsiLocalMacSrvID_Type = Unsigned32
_Hh3cVsiLocalMacSrvID_Object = MibTableColumn
hh3cVsiLocalMacSrvID = _Hh3cVsiLocalMacSrvID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 6, 1, 3),
    _Hh3cVsiLocalMacSrvID_Type()
)
hh3cVsiLocalMacSrvID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiLocalMacSrvID.setStatus("current")
_Hh3cVsiPerfTable_Object = MibTable
hh3cVsiPerfTable = _Hh3cVsiPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cVsiPerfTable.setStatus("current")
_Hh3cVsiPerfEntry_Object = MibTableRow
hh3cVsiPerfEntry = _Hh3cVsiPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 7, 1)
)
hh3cVsiPerfEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsiPerfEntry.setStatus("current")
_Hh3cVsiPerfInOctets_Type = Counter64
_Hh3cVsiPerfInOctets_Object = MibTableColumn
hh3cVsiPerfInOctets = _Hh3cVsiPerfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 7, 1, 1),
    _Hh3cVsiPerfInOctets_Type()
)
hh3cVsiPerfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiPerfInOctets.setStatus("current")
_Hh3cVsiPerfInPackets_Type = Counter64
_Hh3cVsiPerfInPackets_Object = MibTableColumn
hh3cVsiPerfInPackets = _Hh3cVsiPerfInPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 7, 1, 2),
    _Hh3cVsiPerfInPackets_Type()
)
hh3cVsiPerfInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiPerfInPackets.setStatus("current")
_Hh3cVsiPerfInErrors_Type = Counter64
_Hh3cVsiPerfInErrors_Object = MibTableColumn
hh3cVsiPerfInErrors = _Hh3cVsiPerfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 7, 1, 3),
    _Hh3cVsiPerfInErrors_Type()
)
hh3cVsiPerfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiPerfInErrors.setStatus("current")
_Hh3cVsiPerfInDiscards_Type = Counter64
_Hh3cVsiPerfInDiscards_Object = MibTableColumn
hh3cVsiPerfInDiscards = _Hh3cVsiPerfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 7, 1, 4),
    _Hh3cVsiPerfInDiscards_Type()
)
hh3cVsiPerfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiPerfInDiscards.setStatus("current")
_Hh3cVsiPerfOutOctets_Type = Counter64
_Hh3cVsiPerfOutOctets_Object = MibTableColumn
hh3cVsiPerfOutOctets = _Hh3cVsiPerfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 7, 1, 5),
    _Hh3cVsiPerfOutOctets_Type()
)
hh3cVsiPerfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiPerfOutOctets.setStatus("current")
_Hh3cVsiPerfOutPackets_Type = Counter64
_Hh3cVsiPerfOutPackets_Object = MibTableColumn
hh3cVsiPerfOutPackets = _Hh3cVsiPerfOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 7, 1, 6),
    _Hh3cVsiPerfOutPackets_Type()
)
hh3cVsiPerfOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiPerfOutPackets.setStatus("current")
_Hh3cVsiPerfOutErrors_Type = Counter64
_Hh3cVsiPerfOutErrors_Object = MibTableColumn
hh3cVsiPerfOutErrors = _Hh3cVsiPerfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 7, 1, 7),
    _Hh3cVsiPerfOutErrors_Type()
)
hh3cVsiPerfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiPerfOutErrors.setStatus("current")
_Hh3cVsiPerfOutDiscards_Type = Counter64
_Hh3cVsiPerfOutDiscards_Object = MibTableColumn
hh3cVsiPerfOutDiscards = _Hh3cVsiPerfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 7, 1, 8),
    _Hh3cVsiPerfOutDiscards_Type()
)
hh3cVsiPerfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiPerfOutDiscards.setStatus("current")
_Hh3cVsiNextAvailableVsiIfID_Type = Unsigned32
_Hh3cVsiNextAvailableVsiIfID_Object = MibScalar
hh3cVsiNextAvailableVsiIfID = _Hh3cVsiNextAvailableVsiIfID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 8),
    _Hh3cVsiNextAvailableVsiIfID_Type()
)
hh3cVsiNextAvailableVsiIfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiNextAvailableVsiIfID.setStatus("current")
_Hh3cVsiIfTable_Object = MibTable
hh3cVsiIfTable = _Hh3cVsiIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cVsiIfTable.setStatus("current")
_Hh3cVsiIfEntry_Object = MibTableRow
hh3cVsiIfEntry = _Hh3cVsiIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 9, 1)
)
hh3cVsiIfEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiIfID"),
)
if mibBuilder.loadTexts:
    hh3cVsiIfEntry.setStatus("current")
_Hh3cVsiIfID_Type = Unsigned32
_Hh3cVsiIfID_Object = MibTableColumn
hh3cVsiIfID = _Hh3cVsiIfID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 9, 1, 1),
    _Hh3cVsiIfID_Type()
)
hh3cVsiIfID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsiIfID.setStatus("current")
_Hh3cVsiIfIndex_Type = InterfaceIndex
_Hh3cVsiIfIndex_Object = MibTableColumn
hh3cVsiIfIndex = _Hh3cVsiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 9, 1, 2),
    _Hh3cVsiIfIndex_Type()
)
hh3cVsiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsiIfIndex.setStatus("current")
_Hh3cVsiIfRowStatus_Type = RowStatus
_Hh3cVsiIfRowStatus_Object = MibTableColumn
hh3cVsiIfRowStatus = _Hh3cVsiIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 9, 1, 3),
    _Hh3cVsiIfRowStatus_Type()
)
hh3cVsiIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsiIfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VSI-MIB",
    **{"hh3cVsi": hh3cVsi,
       "hh3cVsiObjects": hh3cVsiObjects,
       "hh3cVsiScalarGroup": hh3cVsiScalarGroup,
       "hh3cVsiNextAvailableVsiIndex": hh3cVsiNextAvailableVsiIndex,
       "hh3cVsiL2vpnStatus": hh3cVsiL2vpnStatus,
       "hh3cVsiTable": hh3cVsiTable,
       "hh3cVsiEntry": hh3cVsiEntry,
       "hh3cVsiIndex": hh3cVsiIndex,
       "hh3cVsiName": hh3cVsiName,
       "hh3cVsiMode": hh3cVsiMode,
       "hh3cMinmIsid": hh3cMinmIsid,
       "hh3cVsiId": hh3cVsiId,
       "hh3cVsiTransMode": hh3cVsiTransMode,
       "hh3cVsiEnableHubSpoke": hh3cVsiEnableHubSpoke,
       "hh3cVsiAdminState": hh3cVsiAdminState,
       "hh3cVsiRowStatus": hh3cVsiRowStatus,
       "hh3cVsiSpbIsid": hh3cVsiSpbIsid,
       "hh3cVsiVxlanID": hh3cVsiVxlanID,
       "hh3cVsiArpSuppression": hh3cVsiArpSuppression,
       "hh3cVsiFlooding": hh3cVsiFlooding,
       "hh3cVsiLocalMacCount": hh3cVsiLocalMacCount,
       "hh3cVsiInterfaceID": hh3cVsiInterfaceID,
       "hh3cVsiStatistics": hh3cVsiStatistics,
       "hh3cVsiNvgreID": hh3cVsiNvgreID,
       "hh3cVsiXconnectTable": hh3cVsiXconnectTable,
       "hh3cVsiXconnectEntry": hh3cVsiXconnectEntry,
       "hh3cVsiXconnectIfIndex": hh3cVsiXconnectIfIndex,
       "hh3cVsiXconnectEvcSrvInstId": hh3cVsiXconnectEvcSrvInstId,
       "hh3cVsiXconnectVsiName": hh3cVsiXconnectVsiName,
       "hh3cVsiXconnectAccessMode": hh3cVsiXconnectAccessMode,
       "hh3cVsiXconnectHubSpoke": hh3cVsiXconnectHubSpoke,
       "hh3cVsiXconnectRowStatus": hh3cVsiXconnectRowStatus,
       "hh3cVsiPwBindTable": hh3cVsiPwBindTable,
       "hh3cVsiPwBindEntry": hh3cVsiPwBindEntry,
       "hh3cVsiPwIndex": hh3cVsiPwIndex,
       "hh3cVsiPwBindAttributes": hh3cVsiPwBindAttributes,
       "hh3cVsiPwBindRowStatus": hh3cVsiPwBindRowStatus,
       "hh3cVsiFloodMacTable": hh3cVsiFloodMacTable,
       "hh3cVsiFloodMacEntry": hh3cVsiFloodMacEntry,
       "hh3cVsiFloodMac": hh3cVsiFloodMac,
       "hh3cVsiFloodMacRowStatus": hh3cVsiFloodMacRowStatus,
       "hh3cVsiLocalMacTable": hh3cVsiLocalMacTable,
       "hh3cVsiLocalMacEntry": hh3cVsiLocalMacEntry,
       "hh3cVsiLocalMacAddr": hh3cVsiLocalMacAddr,
       "hh3cVsiLocalMacIfIndex": hh3cVsiLocalMacIfIndex,
       "hh3cVsiLocalMacSrvID": hh3cVsiLocalMacSrvID,
       "hh3cVsiPerfTable": hh3cVsiPerfTable,
       "hh3cVsiPerfEntry": hh3cVsiPerfEntry,
       "hh3cVsiPerfInOctets": hh3cVsiPerfInOctets,
       "hh3cVsiPerfInPackets": hh3cVsiPerfInPackets,
       "hh3cVsiPerfInErrors": hh3cVsiPerfInErrors,
       "hh3cVsiPerfInDiscards": hh3cVsiPerfInDiscards,
       "hh3cVsiPerfOutOctets": hh3cVsiPerfOutOctets,
       "hh3cVsiPerfOutPackets": hh3cVsiPerfOutPackets,
       "hh3cVsiPerfOutErrors": hh3cVsiPerfOutErrors,
       "hh3cVsiPerfOutDiscards": hh3cVsiPerfOutDiscards,
       "hh3cVsiNextAvailableVsiIfID": hh3cVsiNextAvailableVsiIfID,
       "hh3cVsiIfTable": hh3cVsiIfTable,
       "hh3cVsiIfEntry": hh3cVsiIfEntry,
       "hh3cVsiIfID": hh3cVsiIfID,
       "hh3cVsiIfIndex": hh3cVsiIfIndex,
       "hh3cVsiIfRowStatus": hh3cVsiIfRowStatus}
)
