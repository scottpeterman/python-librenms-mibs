# SNMP MIB module (HH3C-SRV6POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-SRV6POLICY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:01 2025
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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cSrv6Policy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189)
)
if mibBuilder.loadTexts:
    hh3cSrv6Policy.setRevisions(
        ("2020-06-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSrv6PolicyNotifications_ObjectIdentity = ObjectIdentity
hh3cSrv6PolicyNotifications = _Hh3cSrv6PolicyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 0)
)
_Hh3cSrv6PolicyObjects_ObjectIdentity = ObjectIdentity
hh3cSrv6PolicyObjects = _Hh3cSrv6PolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1)
)
_Hh3cSrv6PolicyResourceTable_Object = MibTable
hh3cSrv6PolicyResourceTable = _Hh3cSrv6PolicyResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyResourceTable.setStatus("current")
_Hh3cSrv6PolicyResourceEntry_Object = MibTableRow
hh3cSrv6PolicyResourceEntry = _Hh3cSrv6PolicyResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 1, 1)
)
hh3cSrv6PolicyResourceEntry.setIndexNames(
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyResourceType"),
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyResourceEntry.setStatus("current")


class _Hh3cSrv6PolicyResourceType_Type(Integer32):
    """Custom type hh3cSrv6PolicyResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("srv6Policy", 2),
          ("srv6PolicySegmentList", 3),
          ("srv6PolicyGroup", 4),
          ("srv6PolicyFwdPath", 5))
    )


_Hh3cSrv6PolicyResourceType_Type.__name__ = "Integer32"
_Hh3cSrv6PolicyResourceType_Object = MibTableColumn
hh3cSrv6PolicyResourceType = _Hh3cSrv6PolicyResourceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 1, 1, 1),
    _Hh3cSrv6PolicyResourceType_Type()
)
hh3cSrv6PolicyResourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyResourceType.setStatus("current")
_Hh3cSrv6PolicyResCurrentCnt_Type = Unsigned32
_Hh3cSrv6PolicyResCurrentCnt_Object = MibTableColumn
hh3cSrv6PolicyResCurrentCnt = _Hh3cSrv6PolicyResCurrentCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 1, 1, 2),
    _Hh3cSrv6PolicyResCurrentCnt_Type()
)
hh3cSrv6PolicyResCurrentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyResCurrentCnt.setStatus("current")


class _Hh3cSrv6PolicyResUpperLimit_Type(Unsigned32):
    """Custom type hh3cSrv6PolicyResUpperLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cSrv6PolicyResUpperLimit_Type.__name__ = "Unsigned32"
_Hh3cSrv6PolicyResUpperLimit_Object = MibTableColumn
hh3cSrv6PolicyResUpperLimit = _Hh3cSrv6PolicyResUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 1, 1, 3),
    _Hh3cSrv6PolicyResUpperLimit_Type()
)
hh3cSrv6PolicyResUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyResUpperLimit.setStatus("current")


class _Hh3cSrv6PolicyResLowerLimit_Type(Unsigned32):
    """Custom type hh3cSrv6PolicyResLowerLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cSrv6PolicyResLowerLimit_Type.__name__ = "Unsigned32"
_Hh3cSrv6PolicyResLowerLimit_Object = MibTableColumn
hh3cSrv6PolicyResLowerLimit = _Hh3cSrv6PolicyResLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 1, 1, 4),
    _Hh3cSrv6PolicyResLowerLimit_Type()
)
hh3cSrv6PolicyResLowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyResLowerLimit.setStatus("current")
_Hh3cSrv6PolicyResourceTotalCnt_Type = Unsigned32
_Hh3cSrv6PolicyResourceTotalCnt_Object = MibTableColumn
hh3cSrv6PolicyResourceTotalCnt = _Hh3cSrv6PolicyResourceTotalCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 1, 1, 5),
    _Hh3cSrv6PolicyResourceTotalCnt_Type()
)
hh3cSrv6PolicyResourceTotalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyResourceTotalCnt.setStatus("current")
_Hh3cSrv6PolicyTable_Object = MibTable
hh3cSrv6PolicyTable = _Hh3cSrv6PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyTable.setStatus("current")
_Hh3cSrv6PolicyEntry_Object = MibTableRow
hh3cSrv6PolicyEntry = _Hh3cSrv6PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 2, 1)
)
hh3cSrv6PolicyEntry.setIndexNames(
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyColor"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyEndPoint"),
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyEntry.setStatus("current")


class _Hh3cSrv6PolicyColor_Type(Unsigned32):
    """Custom type hh3cSrv6PolicyColor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cSrv6PolicyColor_Type.__name__ = "Unsigned32"
_Hh3cSrv6PolicyColor_Object = MibTableColumn
hh3cSrv6PolicyColor = _Hh3cSrv6PolicyColor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 2, 1, 1),
    _Hh3cSrv6PolicyColor_Type()
)
hh3cSrv6PolicyColor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyColor.setStatus("current")
_Hh3cSrv6PolicyEndPoint_Type = InetAddressIPv6
_Hh3cSrv6PolicyEndPoint_Object = MibTableColumn
hh3cSrv6PolicyEndPoint = _Hh3cSrv6PolicyEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 2, 1, 2),
    _Hh3cSrv6PolicyEndPoint_Type()
)
hh3cSrv6PolicyEndPoint.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyEndPoint.setStatus("current")


class _Hh3cSrv6PolicyName_Type(OctetString):
    """Custom type hh3cSrv6PolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hh3cSrv6PolicyName_Type.__name__ = "OctetString"
_Hh3cSrv6PolicyName_Object = MibTableColumn
hh3cSrv6PolicyName = _Hh3cSrv6PolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 2, 1, 3),
    _Hh3cSrv6PolicyName_Type()
)
hh3cSrv6PolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyName.setStatus("current")
_Hh3cSrv6PolicyBsid_Type = InetAddressIPv6
_Hh3cSrv6PolicyBsid_Object = MibTableColumn
hh3cSrv6PolicyBsid = _Hh3cSrv6PolicyBsid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 2, 1, 4),
    _Hh3cSrv6PolicyBsid_Type()
)
hh3cSrv6PolicyBsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyBsid.setStatus("current")


class _Hh3cSrv6PolicyStatus_Type(OctetString):
    """Custom type hh3cSrv6PolicyStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cSrv6PolicyStatus_Type.__name__ = "OctetString"
_Hh3cSrv6PolicyStatus_Object = MibTableColumn
hh3cSrv6PolicyStatus = _Hh3cSrv6PolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 2, 1, 5),
    _Hh3cSrv6PolicyStatus_Type()
)
hh3cSrv6PolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyStatus.setStatus("current")


class _Hh3cSrv6PolicyDownReason_Type(OctetString):
    """Custom type hh3cSrv6PolicyDownReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_Hh3cSrv6PolicyDownReason_Type.__name__ = "OctetString"
_Hh3cSrv6PolicyDownReason_Object = MibTableColumn
hh3cSrv6PolicyDownReason = _Hh3cSrv6PolicyDownReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 2, 1, 6),
    _Hh3cSrv6PolicyDownReason_Type()
)
hh3cSrv6PolicyDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyDownReason.setStatus("current")


class _Hh3cSrv6PolicyBsidFailReason_Type(OctetString):
    """Custom type hh3cSrv6PolicyBsidFailReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSrv6PolicyBsidFailReason_Type.__name__ = "OctetString"
_Hh3cSrv6PolicyBsidFailReason_Object = MibTableColumn
hh3cSrv6PolicyBsidFailReason = _Hh3cSrv6PolicyBsidFailReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 2, 1, 7),
    _Hh3cSrv6PolicyBsidFailReason_Type()
)
hh3cSrv6PolicyBsidFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyBsidFailReason.setStatus("current")


class _Hh3cSrv6PolicyBsidConflictState_Type(Integer32):
    """Custom type hh3cSrv6PolicyBsidConflictState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inConflict", 1),
          ("conflictResolved", 2))
    )


_Hh3cSrv6PolicyBsidConflictState_Type.__name__ = "Integer32"
_Hh3cSrv6PolicyBsidConflictState_Object = MibTableColumn
hh3cSrv6PolicyBsidConflictState = _Hh3cSrv6PolicyBsidConflictState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 2, 1, 8),
    _Hh3cSrv6PolicyBsidConflictState_Type()
)
hh3cSrv6PolicyBsidConflictState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyBsidConflictState.setStatus("current")
_Hh3cSrv6PolicyPathTable_Object = MibTable
hh3cSrv6PolicyPathTable = _Hh3cSrv6PolicyPathTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyPathTable.setStatus("current")
_Hh3cSrv6PolicyPathEntry_Object = MibTableRow
hh3cSrv6PolicyPathEntry = _Hh3cSrv6PolicyPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 3, 1)
)
hh3cSrv6PolicyPathEntry.setIndexNames(
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathColor"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathEndPoint"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathProto"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathInst"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathOri"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathDis"),
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyPathEntry.setStatus("current")


class _Hh3cSrv6PolicyPathColor_Type(Unsigned32):
    """Custom type hh3cSrv6PolicyPathColor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cSrv6PolicyPathColor_Type.__name__ = "Unsigned32"
_Hh3cSrv6PolicyPathColor_Object = MibTableColumn
hh3cSrv6PolicyPathColor = _Hh3cSrv6PolicyPathColor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 3, 1, 1),
    _Hh3cSrv6PolicyPathColor_Type()
)
hh3cSrv6PolicyPathColor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyPathColor.setStatus("current")
_Hh3cSrv6PolicyPathEndPoint_Type = InetAddressIPv6
_Hh3cSrv6PolicyPathEndPoint_Object = MibTableColumn
hh3cSrv6PolicyPathEndPoint = _Hh3cSrv6PolicyPathEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 3, 1, 2),
    _Hh3cSrv6PolicyPathEndPoint_Type()
)
hh3cSrv6PolicyPathEndPoint.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyPathEndPoint.setStatus("current")


class _Hh3cSrv6PolicyPathProto_Type(Integer32):
    """Custom type hh3cSrv6PolicyPathProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("pcep", 10),
          ("bgp", 20),
          ("cli", 30))
    )


_Hh3cSrv6PolicyPathProto_Type.__name__ = "Integer32"
_Hh3cSrv6PolicyPathProto_Object = MibTableColumn
hh3cSrv6PolicyPathProto = _Hh3cSrv6PolicyPathProto_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 3, 1, 3),
    _Hh3cSrv6PolicyPathProto_Type()
)
hh3cSrv6PolicyPathProto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyPathProto.setStatus("current")


class _Hh3cSrv6PolicyPathInst_Type(Integer32):
    """Custom type hh3cSrv6PolicyPathInst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cSrv6PolicyPathInst_Type.__name__ = "Integer32"
_Hh3cSrv6PolicyPathInst_Object = MibTableColumn
hh3cSrv6PolicyPathInst = _Hh3cSrv6PolicyPathInst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 3, 1, 4),
    _Hh3cSrv6PolicyPathInst_Type()
)
hh3cSrv6PolicyPathInst.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyPathInst.setStatus("current")


class _Hh3cSrv6PolicyPathOri_Type(OctetString):
    """Custom type hh3cSrv6PolicyPathOri based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cSrv6PolicyPathOri_Type.__name__ = "OctetString"
_Hh3cSrv6PolicyPathOri_Object = MibTableColumn
hh3cSrv6PolicyPathOri = _Hh3cSrv6PolicyPathOri_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 3, 1, 5),
    _Hh3cSrv6PolicyPathOri_Type()
)
hh3cSrv6PolicyPathOri.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyPathOri.setStatus("current")
_Hh3cSrv6PolicyPathDis_Type = Unsigned32
_Hh3cSrv6PolicyPathDis_Object = MibTableColumn
hh3cSrv6PolicyPathDis = _Hh3cSrv6PolicyPathDis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 3, 1, 6),
    _Hh3cSrv6PolicyPathDis_Type()
)
hh3cSrv6PolicyPathDis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyPathDis.setStatus("current")
_Hh3cSrv6PolicyPathPref_Type = Unsigned32
_Hh3cSrv6PolicyPathPref_Object = MibTableColumn
hh3cSrv6PolicyPathPref = _Hh3cSrv6PolicyPathPref_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 3, 1, 7),
    _Hh3cSrv6PolicyPathPref_Type()
)
hh3cSrv6PolicyPathPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyPathPref.setStatus("current")


class _Hh3cSrv6PolicyPathPreviousRole_Type(OctetString):
    """Custom type hh3cSrv6PolicyPathPreviousRole based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cSrv6PolicyPathPreviousRole_Type.__name__ = "OctetString"
_Hh3cSrv6PolicyPathPreviousRole_Object = MibTableColumn
hh3cSrv6PolicyPathPreviousRole = _Hh3cSrv6PolicyPathPreviousRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 3, 1, 8),
    _Hh3cSrv6PolicyPathPreviousRole_Type()
)
hh3cSrv6PolicyPathPreviousRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyPathPreviousRole.setStatus("current")


class _Hh3cSrv6PolicyPathDownReason_Type(OctetString):
    """Custom type hh3cSrv6PolicyPathDownReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_Hh3cSrv6PolicyPathDownReason_Type.__name__ = "OctetString"
_Hh3cSrv6PolicyPathDownReason_Object = MibTableColumn
hh3cSrv6PolicyPathDownReason = _Hh3cSrv6PolicyPathDownReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 3, 1, 9),
    _Hh3cSrv6PolicyPathDownReason_Type()
)
hh3cSrv6PolicyPathDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicyPathDownReason.setStatus("current")
_Hh3cSrv6PolicySeglistTable_Object = MibTable
hh3cSrv6PolicySeglistTable = _Hh3cSrv6PolicySeglistTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistTable.setStatus("current")
_Hh3cSrv6PolicySeglistEntry_Object = MibTableRow
hh3cSrv6PolicySeglistEntry = _Hh3cSrv6PolicySeglistEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4, 1)
)
hh3cSrv6PolicySeglistEntry.setIndexNames(
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistColor"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistEndPoint"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathProto"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathInst"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathOri"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathDis"),
    (0, "HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistId"),
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistEntry.setStatus("current")


class _Hh3cSrv6PolicySeglistColor_Type(Unsigned32):
    """Custom type hh3cSrv6PolicySeglistColor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cSrv6PolicySeglistColor_Type.__name__ = "Unsigned32"
_Hh3cSrv6PolicySeglistColor_Object = MibTableColumn
hh3cSrv6PolicySeglistColor = _Hh3cSrv6PolicySeglistColor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4, 1, 1),
    _Hh3cSrv6PolicySeglistColor_Type()
)
hh3cSrv6PolicySeglistColor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistColor.setStatus("current")
_Hh3cSrv6PolicySeglistEndPoint_Type = InetAddressIPv6
_Hh3cSrv6PolicySeglistEndPoint_Object = MibTableColumn
hh3cSrv6PolicySeglistEndPoint = _Hh3cSrv6PolicySeglistEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4, 1, 2),
    _Hh3cSrv6PolicySeglistEndPoint_Type()
)
hh3cSrv6PolicySeglistEndPoint.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistEndPoint.setStatus("current")


class _Hh3cSrv6PolicySeglistPathProto_Type(Integer32):
    """Custom type hh3cSrv6PolicySeglistPathProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("pcep", 10),
          ("bgp", 20),
          ("cli", 30))
    )


_Hh3cSrv6PolicySeglistPathProto_Type.__name__ = "Integer32"
_Hh3cSrv6PolicySeglistPathProto_Object = MibTableColumn
hh3cSrv6PolicySeglistPathProto = _Hh3cSrv6PolicySeglistPathProto_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4, 1, 3),
    _Hh3cSrv6PolicySeglistPathProto_Type()
)
hh3cSrv6PolicySeglistPathProto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistPathProto.setStatus("current")


class _Hh3cSrv6PolicySeglistPathInst_Type(Integer32):
    """Custom type hh3cSrv6PolicySeglistPathInst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cSrv6PolicySeglistPathInst_Type.__name__ = "Integer32"
_Hh3cSrv6PolicySeglistPathInst_Object = MibTableColumn
hh3cSrv6PolicySeglistPathInst = _Hh3cSrv6PolicySeglistPathInst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4, 1, 4),
    _Hh3cSrv6PolicySeglistPathInst_Type()
)
hh3cSrv6PolicySeglistPathInst.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistPathInst.setStatus("current")


class _Hh3cSrv6PolicySeglistPathOri_Type(OctetString):
    """Custom type hh3cSrv6PolicySeglistPathOri based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cSrv6PolicySeglistPathOri_Type.__name__ = "OctetString"
_Hh3cSrv6PolicySeglistPathOri_Object = MibTableColumn
hh3cSrv6PolicySeglistPathOri = _Hh3cSrv6PolicySeglistPathOri_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4, 1, 5),
    _Hh3cSrv6PolicySeglistPathOri_Type()
)
hh3cSrv6PolicySeglistPathOri.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistPathOri.setStatus("current")
_Hh3cSrv6PolicySeglistPathDis_Type = Unsigned32
_Hh3cSrv6PolicySeglistPathDis_Object = MibTableColumn
hh3cSrv6PolicySeglistPathDis = _Hh3cSrv6PolicySeglistPathDis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4, 1, 6),
    _Hh3cSrv6PolicySeglistPathDis_Type()
)
hh3cSrv6PolicySeglistPathDis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistPathDis.setStatus("current")


class _Hh3cSrv6PolicySeglistId_Type(Unsigned32):
    """Custom type hh3cSrv6PolicySeglistId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cSrv6PolicySeglistId_Type.__name__ = "Unsigned32"
_Hh3cSrv6PolicySeglistId_Object = MibTableColumn
hh3cSrv6PolicySeglistId = _Hh3cSrv6PolicySeglistId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4, 1, 7),
    _Hh3cSrv6PolicySeglistId_Type()
)
hh3cSrv6PolicySeglistId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistId.setStatus("current")


class _Hh3cSrv6PolicySeglistName_Type(OctetString):
    """Custom type hh3cSrv6PolicySeglistName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hh3cSrv6PolicySeglistName_Type.__name__ = "OctetString"
_Hh3cSrv6PolicySeglistName_Object = MibTableColumn
hh3cSrv6PolicySeglistName = _Hh3cSrv6PolicySeglistName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4, 1, 8),
    _Hh3cSrv6PolicySeglistName_Type()
)
hh3cSrv6PolicySeglistName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistName.setStatus("current")


class _Hh3cSrv6PolicySeglistStatus_Type(OctetString):
    """Custom type hh3cSrv6PolicySeglistStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cSrv6PolicySeglistStatus_Type.__name__ = "OctetString"
_Hh3cSrv6PolicySeglistStatus_Object = MibTableColumn
hh3cSrv6PolicySeglistStatus = _Hh3cSrv6PolicySeglistStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4, 1, 9),
    _Hh3cSrv6PolicySeglistStatus_Type()
)
hh3cSrv6PolicySeglistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistStatus.setStatus("current")


class _Hh3cSrv6PolicySeglistDownReason_Type(OctetString):
    """Custom type hh3cSrv6PolicySeglistDownReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_Hh3cSrv6PolicySeglistDownReason_Type.__name__ = "OctetString"
_Hh3cSrv6PolicySeglistDownReason_Object = MibTableColumn
hh3cSrv6PolicySeglistDownReason = _Hh3cSrv6PolicySeglistDownReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 1, 4, 1, 10),
    _Hh3cSrv6PolicySeglistDownReason_Type()
)
hh3cSrv6PolicySeglistDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistDownReason.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cSrv6PolicyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 0, 1)
)
hh3cSrv6PolicyStatusChange.setObjects(
      *(("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyColor"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyEndPoint"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyStatus"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyDownReason"))
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyStatusChange.setStatus(
        "current"
    )

hh3cSrv6PolicyBsidConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 0, 2)
)
hh3cSrv6PolicyBsidConflict.setObjects(
      *(("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyColor"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyEndPoint"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyBsid"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyBsidFailReason"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyBsidConflictState"))
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyBsidConflict.setStatus(
        "current"
    )

hh3cSrv6PolicyBsidConflictClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 0, 3)
)
hh3cSrv6PolicyBsidConflictClear.setObjects(
      *(("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyColor"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyEndPoint"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyBsid"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyBsidFailReason"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyBsidConflictState"))
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyBsidConflictClear.setStatus(
        "current"
    )

hh3cSrv6PolicyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 0, 4)
)
hh3cSrv6PolicyDown.setObjects(
      *(("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyColor"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyEndPoint"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyDownReason"))
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyDown.setStatus(
        "current"
    )

hh3cSrv6PolicyDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 0, 5)
)
hh3cSrv6PolicyDownClear.setObjects(
      *(("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyColor"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyEndPoint"))
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyDownClear.setStatus(
        "current"
    )

hh3cSrv6PolicyResExdUppLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 0, 6)
)
hh3cSrv6PolicyResExdUppLimit.setObjects(
      *(("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyResourceType"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyResCurrentCnt"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyResUpperLimit"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyResLowerLimit"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyResourceTotalCnt"))
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyResExdUppLimit.setStatus(
        "current"
    )

hh3cSrv6PolicyResExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 0, 7)
)
hh3cSrv6PolicyResExceedClear.setObjects(
      *(("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyResourceType"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyResCurrentCnt"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyResUpperLimit"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyResLowerLimit"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyResourceTotalCnt"))
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicyResExceedClear.setStatus(
        "current"
    )

hh3cSrv6PathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 0, 8)
)
hh3cSrv6PathDown.setObjects(
      *(("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathColor"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathEndPoint"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathProto"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathInst"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathOri"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathDis"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathPref"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathPreviousRole"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicyPathDownReason"))
)
if mibBuilder.loadTexts:
    hh3cSrv6PathDown.setStatus(
        "current"
    )

hh3cSrv6PolicySeglistDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 0, 9)
)
hh3cSrv6PolicySeglistDown.setObjects(
      *(("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistColor"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistEndPoint"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathProto"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathInst"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathOri"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathDis"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistId"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistStatus"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistDownReason"))
)
if mibBuilder.loadTexts:
    hh3cSrv6PolicySeglistDown.setStatus(
        "current"
    )

hh3cSrv6SeglistDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 189, 0, 10)
)
hh3cSrv6SeglistDownClear.setObjects(
      *(("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistColor"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistEndPoint"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathProto"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathInst"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathOri"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistPathDis"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistId"),
        ("HH3C-SRV6POLICY-MIB", "hh3cSrv6PolicySeglistStatus"))
)
if mibBuilder.loadTexts:
    hh3cSrv6SeglistDownClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SRV6POLICY-MIB",
    **{"hh3cSrv6Policy": hh3cSrv6Policy,
       "hh3cSrv6PolicyNotifications": hh3cSrv6PolicyNotifications,
       "hh3cSrv6PolicyStatusChange": hh3cSrv6PolicyStatusChange,
       "hh3cSrv6PolicyBsidConflict": hh3cSrv6PolicyBsidConflict,
       "hh3cSrv6PolicyBsidConflictClear": hh3cSrv6PolicyBsidConflictClear,
       "hh3cSrv6PolicyDown": hh3cSrv6PolicyDown,
       "hh3cSrv6PolicyDownClear": hh3cSrv6PolicyDownClear,
       "hh3cSrv6PolicyResExdUppLimit": hh3cSrv6PolicyResExdUppLimit,
       "hh3cSrv6PolicyResExceedClear": hh3cSrv6PolicyResExceedClear,
       "hh3cSrv6PathDown": hh3cSrv6PathDown,
       "hh3cSrv6PolicySeglistDown": hh3cSrv6PolicySeglistDown,
       "hh3cSrv6SeglistDownClear": hh3cSrv6SeglistDownClear,
       "hh3cSrv6PolicyObjects": hh3cSrv6PolicyObjects,
       "hh3cSrv6PolicyResourceTable": hh3cSrv6PolicyResourceTable,
       "hh3cSrv6PolicyResourceEntry": hh3cSrv6PolicyResourceEntry,
       "hh3cSrv6PolicyResourceType": hh3cSrv6PolicyResourceType,
       "hh3cSrv6PolicyResCurrentCnt": hh3cSrv6PolicyResCurrentCnt,
       "hh3cSrv6PolicyResUpperLimit": hh3cSrv6PolicyResUpperLimit,
       "hh3cSrv6PolicyResLowerLimit": hh3cSrv6PolicyResLowerLimit,
       "hh3cSrv6PolicyResourceTotalCnt": hh3cSrv6PolicyResourceTotalCnt,
       "hh3cSrv6PolicyTable": hh3cSrv6PolicyTable,
       "hh3cSrv6PolicyEntry": hh3cSrv6PolicyEntry,
       "hh3cSrv6PolicyColor": hh3cSrv6PolicyColor,
       "hh3cSrv6PolicyEndPoint": hh3cSrv6PolicyEndPoint,
       "hh3cSrv6PolicyName": hh3cSrv6PolicyName,
       "hh3cSrv6PolicyBsid": hh3cSrv6PolicyBsid,
       "hh3cSrv6PolicyStatus": hh3cSrv6PolicyStatus,
       "hh3cSrv6PolicyDownReason": hh3cSrv6PolicyDownReason,
       "hh3cSrv6PolicyBsidFailReason": hh3cSrv6PolicyBsidFailReason,
       "hh3cSrv6PolicyBsidConflictState": hh3cSrv6PolicyBsidConflictState,
       "hh3cSrv6PolicyPathTable": hh3cSrv6PolicyPathTable,
       "hh3cSrv6PolicyPathEntry": hh3cSrv6PolicyPathEntry,
       "hh3cSrv6PolicyPathColor": hh3cSrv6PolicyPathColor,
       "hh3cSrv6PolicyPathEndPoint": hh3cSrv6PolicyPathEndPoint,
       "hh3cSrv6PolicyPathProto": hh3cSrv6PolicyPathProto,
       "hh3cSrv6PolicyPathInst": hh3cSrv6PolicyPathInst,
       "hh3cSrv6PolicyPathOri": hh3cSrv6PolicyPathOri,
       "hh3cSrv6PolicyPathDis": hh3cSrv6PolicyPathDis,
       "hh3cSrv6PolicyPathPref": hh3cSrv6PolicyPathPref,
       "hh3cSrv6PolicyPathPreviousRole": hh3cSrv6PolicyPathPreviousRole,
       "hh3cSrv6PolicyPathDownReason": hh3cSrv6PolicyPathDownReason,
       "hh3cSrv6PolicySeglistTable": hh3cSrv6PolicySeglistTable,
       "hh3cSrv6PolicySeglistEntry": hh3cSrv6PolicySeglistEntry,
       "hh3cSrv6PolicySeglistColor": hh3cSrv6PolicySeglistColor,
       "hh3cSrv6PolicySeglistEndPoint": hh3cSrv6PolicySeglistEndPoint,
       "hh3cSrv6PolicySeglistPathProto": hh3cSrv6PolicySeglistPathProto,
       "hh3cSrv6PolicySeglistPathInst": hh3cSrv6PolicySeglistPathInst,
       "hh3cSrv6PolicySeglistPathOri": hh3cSrv6PolicySeglistPathOri,
       "hh3cSrv6PolicySeglistPathDis": hh3cSrv6PolicySeglistPathDis,
       "hh3cSrv6PolicySeglistId": hh3cSrv6PolicySeglistId,
       "hh3cSrv6PolicySeglistName": hh3cSrv6PolicySeglistName,
       "hh3cSrv6PolicySeglistStatus": hh3cSrv6PolicySeglistStatus,
       "hh3cSrv6PolicySeglistDownReason": hh3cSrv6PolicySeglistDownReason}
)
