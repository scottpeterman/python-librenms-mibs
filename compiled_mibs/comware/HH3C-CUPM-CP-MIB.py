# SNMP MIB module (HH3C-CUPM-CP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-CUPM-CP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:53 2025
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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cCupmCp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194)
)
if mibBuilder.loadTexts:
    hh3cCupmCp.setRevisions(
        ("2020-09-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cCupmCpNotifications_ObjectIdentity = ObjectIdentity
hh3cCupmCpNotifications = _Hh3cCupmCpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 0)
)
_Hh3cCupmCpNotifyVarObjects_ObjectIdentity = ObjectIdentity
hh3cCupmCpNotifyVarObjects = _Hh3cCupmCpNotifyVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 1)
)


class _Hh3cCupmCpVbUpID_Type(Integer32):
    """Custom type hh3cCupmCpVbUpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cCupmCpVbUpID_Type.__name__ = "Integer32"
_Hh3cCupmCpVbUpID_Object = MibScalar
hh3cCupmCpVbUpID = _Hh3cCupmCpVbUpID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 1, 1),
    _Hh3cCupmCpVbUpID_Type()
)
hh3cCupmCpVbUpID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmCpVbUpID.setStatus("current")


class _Hh3cCupmCpVbVxlanID_Type(Integer32):
    """Custom type hh3cCupmCpVbVxlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_Hh3cCupmCpVbVxlanID_Type.__name__ = "Integer32"
_Hh3cCupmCpVbVxlanID_Object = MibScalar
hh3cCupmCpVbVxlanID = _Hh3cCupmCpVbVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 1, 2),
    _Hh3cCupmCpVbVxlanID_Type()
)
hh3cCupmCpVbVxlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmCpVbVxlanID.setStatus("current")
_Hh3cCupmCpVbSrcAddrType_Type = InetAddressType
_Hh3cCupmCpVbSrcAddrType_Object = MibScalar
hh3cCupmCpVbSrcAddrType = _Hh3cCupmCpVbSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 1, 3),
    _Hh3cCupmCpVbSrcAddrType_Type()
)
hh3cCupmCpVbSrcAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmCpVbSrcAddrType.setStatus("current")
_Hh3cCupmCpVbSrcAddr_Type = InetAddress
_Hh3cCupmCpVbSrcAddr_Object = MibScalar
hh3cCupmCpVbSrcAddr = _Hh3cCupmCpVbSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 1, 4),
    _Hh3cCupmCpVbSrcAddr_Type()
)
hh3cCupmCpVbSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmCpVbSrcAddr.setStatus("current")
_Hh3cCupmCpVbDestAddrType_Type = InetAddressType
_Hh3cCupmCpVbDestAddrType_Object = MibScalar
hh3cCupmCpVbDestAddrType = _Hh3cCupmCpVbDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 1, 5),
    _Hh3cCupmCpVbDestAddrType_Type()
)
hh3cCupmCpVbDestAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmCpVbDestAddrType.setStatus("current")
_Hh3cCupmCpVbDestAddr_Type = InetAddress
_Hh3cCupmCpVbDestAddr_Object = MibScalar
hh3cCupmCpVbDestAddr = _Hh3cCupmCpVbDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 1, 6),
    _Hh3cCupmCpVbDestAddr_Type()
)
hh3cCupmCpVbDestAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmCpVbDestAddr.setStatus("current")


class _Hh3cCupmCpVbVpnName_Type(OctetString):
    """Custom type hh3cCupmCpVbVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cCupmCpVbVpnName_Type.__name__ = "OctetString"
_Hh3cCupmCpVbVpnName_Object = MibScalar
hh3cCupmCpVbVpnName = _Hh3cCupmCpVbVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 1, 7),
    _Hh3cCupmCpVbVpnName_Type()
)
hh3cCupmCpVbVpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmCpVbVpnName.setStatus("current")


class _Hh3cCupmCpVbVxlanState_Type(Integer32):
    """Custom type hh3cCupmCpVbVxlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2))
    )


_Hh3cCupmCpVbVxlanState_Type.__name__ = "Integer32"
_Hh3cCupmCpVbVxlanState_Object = MibScalar
hh3cCupmCpVbVxlanState = _Hh3cCupmCpVbVxlanState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 1, 8),
    _Hh3cCupmCpVbVxlanState_Type()
)
hh3cCupmCpVbVxlanState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmCpVbVxlanState.setStatus("current")
_Hh3cCupmCpScalarObjects_ObjectIdentity = ObjectIdentity
hh3cCupmCpScalarObjects = _Hh3cCupmCpScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 2)
)


class _Hh3cCupmUpNum_Type(Integer32):
    """Custom type hh3cCupmUpNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cCupmUpNum_Type.__name__ = "Integer32"
_Hh3cCupmUpNum_Object = MibScalar
hh3cCupmUpNum = _Hh3cCupmUpNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 2, 1),
    _Hh3cCupmUpNum_Type()
)
hh3cCupmUpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmUpNum.setStatus("current")
_Hh3cCupmCpTableObjects_ObjectIdentity = ObjectIdentity
hh3cCupmCpTableObjects = _Hh3cCupmCpTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3)
)
_Hh3cCupmUpListTable_Object = MibTable
hh3cCupmUpListTable = _Hh3cCupmUpListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cCupmUpListTable.setStatus("current")
_Hh3cCupmUpListEntry_Object = MibTableRow
hh3cCupmUpListEntry = _Hh3cCupmUpListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 1, 1)
)
hh3cCupmUpListEntry.setIndexNames(
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmUpID"),
)
if mibBuilder.loadTexts:
    hh3cCupmUpListEntry.setStatus("current")


class _Hh3cCupmUpID_Type(Integer32):
    """Custom type hh3cCupmUpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cCupmUpID_Type.__name__ = "Integer32"
_Hh3cCupmUpID_Object = MibTableColumn
hh3cCupmUpID = _Hh3cCupmUpID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 1, 1, 1),
    _Hh3cCupmUpID_Type()
)
hh3cCupmUpID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cCupmUpID.setStatus("current")


class _Hh3cCupmUpDescr_Type(OctetString):
    """Custom type hh3cCupmUpDescr based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cCupmUpDescr_Type.__name__ = "OctetString"
_Hh3cCupmUpDescr_Object = MibTableColumn
hh3cCupmUpDescr = _Hh3cCupmUpDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 1, 1, 2),
    _Hh3cCupmUpDescr_Type()
)
hh3cCupmUpDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCupmUpDescr.setStatus("current")
_Hh3cCupmUpListRowStatus_Type = RowStatus
_Hh3cCupmUpListRowStatus_Object = MibTableColumn
hh3cCupmUpListRowStatus = _Hh3cCupmUpListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 1, 1, 3),
    _Hh3cCupmUpListRowStatus_Type()
)
hh3cCupmUpListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCupmUpListRowStatus.setStatus("current")
_Hh3cCupmCpProtoTnlTable_Object = MibTable
hh3cCupmCpProtoTnlTable = _Hh3cCupmCpProtoTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlTable.setStatus("current")
_Hh3cCupmCpProtoTnlEntry_Object = MibTableRow
hh3cCupmCpProtoTnlEntry = _Hh3cCupmCpProtoTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 2, 1)
)
hh3cCupmCpProtoTnlEntry.setIndexNames(
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmUpID"),
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmCpProtoTnlVxlanID"),
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmCpProtoTnlSrcAddrType"),
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmCpProtoTnlSrcAddr"),
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmCpProtoTnlDstAddrType"),
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmCpProtoTnlDstAddr"),
)
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlEntry.setStatus("current")


class _Hh3cCupmCpProtoTnlVxlanID_Type(Integer32):
    """Custom type hh3cCupmCpProtoTnlVxlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_Hh3cCupmCpProtoTnlVxlanID_Type.__name__ = "Integer32"
_Hh3cCupmCpProtoTnlVxlanID_Object = MibTableColumn
hh3cCupmCpProtoTnlVxlanID = _Hh3cCupmCpProtoTnlVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 2, 1, 1),
    _Hh3cCupmCpProtoTnlVxlanID_Type()
)
hh3cCupmCpProtoTnlVxlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlVxlanID.setStatus("current")
_Hh3cCupmCpProtoTnlSrcAddrType_Type = InetAddressType
_Hh3cCupmCpProtoTnlSrcAddrType_Object = MibTableColumn
hh3cCupmCpProtoTnlSrcAddrType = _Hh3cCupmCpProtoTnlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 2, 1, 2),
    _Hh3cCupmCpProtoTnlSrcAddrType_Type()
)
hh3cCupmCpProtoTnlSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlSrcAddrType.setStatus("current")
_Hh3cCupmCpProtoTnlSrcAddr_Type = InetAddress
_Hh3cCupmCpProtoTnlSrcAddr_Object = MibTableColumn
hh3cCupmCpProtoTnlSrcAddr = _Hh3cCupmCpProtoTnlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 2, 1, 3),
    _Hh3cCupmCpProtoTnlSrcAddr_Type()
)
hh3cCupmCpProtoTnlSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlSrcAddr.setStatus("current")
_Hh3cCupmCpProtoTnlDstAddrType_Type = InetAddressType
_Hh3cCupmCpProtoTnlDstAddrType_Object = MibTableColumn
hh3cCupmCpProtoTnlDstAddrType = _Hh3cCupmCpProtoTnlDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 2, 1, 4),
    _Hh3cCupmCpProtoTnlDstAddrType_Type()
)
hh3cCupmCpProtoTnlDstAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlDstAddrType.setStatus("current")
_Hh3cCupmCpProtoTnlDstAddr_Type = InetAddress
_Hh3cCupmCpProtoTnlDstAddr_Object = MibTableColumn
hh3cCupmCpProtoTnlDstAddr = _Hh3cCupmCpProtoTnlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 2, 1, 5),
    _Hh3cCupmCpProtoTnlDstAddr_Type()
)
hh3cCupmCpProtoTnlDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlDstAddr.setStatus("current")


class _Hh3cCupmCpProtoTnlVpnName_Type(OctetString):
    """Custom type hh3cCupmCpProtoTnlVpnName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cCupmCpProtoTnlVpnName_Type.__name__ = "OctetString"
_Hh3cCupmCpProtoTnlVpnName_Object = MibTableColumn
hh3cCupmCpProtoTnlVpnName = _Hh3cCupmCpProtoTnlVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 2, 1, 6),
    _Hh3cCupmCpProtoTnlVpnName_Type()
)
hh3cCupmCpProtoTnlVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlVpnName.setStatus("current")


class _Hh3cCupmCpProtoTnlState_Type(Integer32):
    """Custom type hh3cCupmCpProtoTnlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2))
    )


_Hh3cCupmCpProtoTnlState_Type.__name__ = "Integer32"
_Hh3cCupmCpProtoTnlState_Object = MibTableColumn
hh3cCupmCpProtoTnlState = _Hh3cCupmCpProtoTnlState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 2, 1, 7),
    _Hh3cCupmCpProtoTnlState_Type()
)
hh3cCupmCpProtoTnlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlState.setStatus("current")
_Hh3cCupmCpProtoTnlRowStatus_Type = RowStatus
_Hh3cCupmCpProtoTnlRowStatus_Object = MibTableColumn
hh3cCupmCpProtoTnlRowStatus = _Hh3cCupmCpProtoTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 2, 1, 8),
    _Hh3cCupmCpProtoTnlRowStatus_Type()
)
hh3cCupmCpProtoTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlRowStatus.setStatus("current")
_Hh3cCupmAgtProtoTnlTable_Object = MibTable
hh3cCupmAgtProtoTnlTable = _Hh3cCupmAgtProtoTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cCupmAgtProtoTnlTable.setStatus("current")
_Hh3cCupmAgtProtoTnlEntry_Object = MibTableRow
hh3cCupmAgtProtoTnlEntry = _Hh3cCupmAgtProtoTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 3, 1)
)
hh3cCupmAgtProtoTnlEntry.setIndexNames(
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmUpID"),
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmAgtProtoTnlVxlanID"),
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmAgtProtoTnlSrcAddrType"),
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmAgtProtoTnlSrcAddr"),
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmAgtProtoTnlDstAddrType"),
    (0, "HH3C-CUPM-CP-MIB", "hh3cCupmAgtProtoTnlDstAddr"),
)
if mibBuilder.loadTexts:
    hh3cCupmAgtProtoTnlEntry.setStatus("current")


class _Hh3cCupmAgtProtoTnlVxlanID_Type(Integer32):
    """Custom type hh3cCupmAgtProtoTnlVxlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_Hh3cCupmAgtProtoTnlVxlanID_Type.__name__ = "Integer32"
_Hh3cCupmAgtProtoTnlVxlanID_Object = MibTableColumn
hh3cCupmAgtProtoTnlVxlanID = _Hh3cCupmAgtProtoTnlVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 3, 1, 1),
    _Hh3cCupmAgtProtoTnlVxlanID_Type()
)
hh3cCupmAgtProtoTnlVxlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmAgtProtoTnlVxlanID.setStatus("current")
_Hh3cCupmAgtProtoTnlSrcAddrType_Type = InetAddressType
_Hh3cCupmAgtProtoTnlSrcAddrType_Object = MibTableColumn
hh3cCupmAgtProtoTnlSrcAddrType = _Hh3cCupmAgtProtoTnlSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 3, 1, 2),
    _Hh3cCupmAgtProtoTnlSrcAddrType_Type()
)
hh3cCupmAgtProtoTnlSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmAgtProtoTnlSrcAddrType.setStatus("current")
_Hh3cCupmAgtProtoTnlSrcAddr_Type = InetAddress
_Hh3cCupmAgtProtoTnlSrcAddr_Object = MibTableColumn
hh3cCupmAgtProtoTnlSrcAddr = _Hh3cCupmAgtProtoTnlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 3, 1, 3),
    _Hh3cCupmAgtProtoTnlSrcAddr_Type()
)
hh3cCupmAgtProtoTnlSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmAgtProtoTnlSrcAddr.setStatus("current")
_Hh3cCupmAgtProtoTnlDstAddrType_Type = InetAddressType
_Hh3cCupmAgtProtoTnlDstAddrType_Object = MibTableColumn
hh3cCupmAgtProtoTnlDstAddrType = _Hh3cCupmAgtProtoTnlDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 3, 1, 4),
    _Hh3cCupmAgtProtoTnlDstAddrType_Type()
)
hh3cCupmAgtProtoTnlDstAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmAgtProtoTnlDstAddrType.setStatus("current")
_Hh3cCupmAgtProtoTnlDstAddr_Type = InetAddress
_Hh3cCupmAgtProtoTnlDstAddr_Object = MibTableColumn
hh3cCupmAgtProtoTnlDstAddr = _Hh3cCupmAgtProtoTnlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 3, 1, 5),
    _Hh3cCupmAgtProtoTnlDstAddr_Type()
)
hh3cCupmAgtProtoTnlDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCupmAgtProtoTnlDstAddr.setStatus("current")


class _Hh3cCupmAgtProtoTnlVpnName_Type(OctetString):
    """Custom type hh3cCupmAgtProtoTnlVpnName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cCupmAgtProtoTnlVpnName_Type.__name__ = "OctetString"
_Hh3cCupmAgtProtoTnlVpnName_Object = MibTableColumn
hh3cCupmAgtProtoTnlVpnName = _Hh3cCupmAgtProtoTnlVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 3, 1, 6),
    _Hh3cCupmAgtProtoTnlVpnName_Type()
)
hh3cCupmAgtProtoTnlVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCupmAgtProtoTnlVpnName.setStatus("current")
_Hh3cCupmAgtProtoTnlRowStatus_Type = RowStatus
_Hh3cCupmAgtProtoTnlRowStatus_Object = MibTableColumn
hh3cCupmAgtProtoTnlRowStatus = _Hh3cCupmAgtProtoTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 3, 3, 1, 7),
    _Hh3cCupmAgtProtoTnlRowStatus_Type()
)
hh3cCupmAgtProtoTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cCupmAgtProtoTnlRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cCupmCpProtoTnlUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 0, 1)
)
hh3cCupmCpProtoTnlUp.setObjects(
      *(("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbUpID"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbVxlanID"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbSrcAddrType"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbSrcAddr"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbDestAddrType"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbDestAddr"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbVpnName"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbVxlanState"))
)
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlUp.setStatus(
        "current"
    )

hh3cCupmCpProtoTnlDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 194, 0, 2)
)
hh3cCupmCpProtoTnlDown.setObjects(
      *(("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbUpID"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbVxlanID"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbSrcAddrType"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbSrcAddr"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbDestAddrType"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbDestAddr"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbVpnName"),
        ("HH3C-CUPM-CP-MIB", "hh3cCupmCpVbVxlanState"))
)
if mibBuilder.loadTexts:
    hh3cCupmCpProtoTnlDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-CUPM-CP-MIB",
    **{"hh3cCupmCp": hh3cCupmCp,
       "hh3cCupmCpNotifications": hh3cCupmCpNotifications,
       "hh3cCupmCpProtoTnlUp": hh3cCupmCpProtoTnlUp,
       "hh3cCupmCpProtoTnlDown": hh3cCupmCpProtoTnlDown,
       "hh3cCupmCpNotifyVarObjects": hh3cCupmCpNotifyVarObjects,
       "hh3cCupmCpVbUpID": hh3cCupmCpVbUpID,
       "hh3cCupmCpVbVxlanID": hh3cCupmCpVbVxlanID,
       "hh3cCupmCpVbSrcAddrType": hh3cCupmCpVbSrcAddrType,
       "hh3cCupmCpVbSrcAddr": hh3cCupmCpVbSrcAddr,
       "hh3cCupmCpVbDestAddrType": hh3cCupmCpVbDestAddrType,
       "hh3cCupmCpVbDestAddr": hh3cCupmCpVbDestAddr,
       "hh3cCupmCpVbVpnName": hh3cCupmCpVbVpnName,
       "hh3cCupmCpVbVxlanState": hh3cCupmCpVbVxlanState,
       "hh3cCupmCpScalarObjects": hh3cCupmCpScalarObjects,
       "hh3cCupmUpNum": hh3cCupmUpNum,
       "hh3cCupmCpTableObjects": hh3cCupmCpTableObjects,
       "hh3cCupmUpListTable": hh3cCupmUpListTable,
       "hh3cCupmUpListEntry": hh3cCupmUpListEntry,
       "hh3cCupmUpID": hh3cCupmUpID,
       "hh3cCupmUpDescr": hh3cCupmUpDescr,
       "hh3cCupmUpListRowStatus": hh3cCupmUpListRowStatus,
       "hh3cCupmCpProtoTnlTable": hh3cCupmCpProtoTnlTable,
       "hh3cCupmCpProtoTnlEntry": hh3cCupmCpProtoTnlEntry,
       "hh3cCupmCpProtoTnlVxlanID": hh3cCupmCpProtoTnlVxlanID,
       "hh3cCupmCpProtoTnlSrcAddrType": hh3cCupmCpProtoTnlSrcAddrType,
       "hh3cCupmCpProtoTnlSrcAddr": hh3cCupmCpProtoTnlSrcAddr,
       "hh3cCupmCpProtoTnlDstAddrType": hh3cCupmCpProtoTnlDstAddrType,
       "hh3cCupmCpProtoTnlDstAddr": hh3cCupmCpProtoTnlDstAddr,
       "hh3cCupmCpProtoTnlVpnName": hh3cCupmCpProtoTnlVpnName,
       "hh3cCupmCpProtoTnlState": hh3cCupmCpProtoTnlState,
       "hh3cCupmCpProtoTnlRowStatus": hh3cCupmCpProtoTnlRowStatus,
       "hh3cCupmAgtProtoTnlTable": hh3cCupmAgtProtoTnlTable,
       "hh3cCupmAgtProtoTnlEntry": hh3cCupmAgtProtoTnlEntry,
       "hh3cCupmAgtProtoTnlVxlanID": hh3cCupmAgtProtoTnlVxlanID,
       "hh3cCupmAgtProtoTnlSrcAddrType": hh3cCupmAgtProtoTnlSrcAddrType,
       "hh3cCupmAgtProtoTnlSrcAddr": hh3cCupmAgtProtoTnlSrcAddr,
       "hh3cCupmAgtProtoTnlDstAddrType": hh3cCupmAgtProtoTnlDstAddrType,
       "hh3cCupmAgtProtoTnlDstAddr": hh3cCupmAgtProtoTnlDstAddr,
       "hh3cCupmAgtProtoTnlVpnName": hh3cCupmAgtProtoTnlVpnName,
       "hh3cCupmAgtProtoTnlRowStatus": hh3cCupmAgtProtoTnlRowStatus}
)
