# SNMP MIB module (HH3C-SRPOLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-SRPOLICY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:59 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cSrpolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186)
)
if mibBuilder.loadTexts:
    hh3cSrpolicy.setRevisions(
        ("2019-12-06 11:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSrpolicyNotifications_ObjectIdentity = ObjectIdentity
hh3cSrpolicyNotifications = _Hh3cSrpolicyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 0)
)
_Hh3cSrpolicyTable_Object = MibTable
hh3cSrpolicyTable = _Hh3cSrpolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1)
)
if mibBuilder.loadTexts:
    hh3cSrpolicyTable.setStatus("current")
_Hh3cSrpolicyEntry_Object = MibTableRow
hh3cSrpolicyEntry = _Hh3cSrpolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1)
)
hh3cSrpolicyEntry.setIndexNames(
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpolicyColor"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpolicyEndPoint"),
)
if mibBuilder.loadTexts:
    hh3cSrpolicyEntry.setStatus("current")


class _Hh3cSrpolicyColor_Type(Unsigned32):
    """Custom type hh3cSrpolicyColor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cSrpolicyColor_Type.__name__ = "Unsigned32"
_Hh3cSrpolicyColor_Object = MibTableColumn
hh3cSrpolicyColor = _Hh3cSrpolicyColor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 1),
    _Hh3cSrpolicyColor_Type()
)
hh3cSrpolicyColor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpolicyColor.setStatus("current")
_Hh3cSrpolicyEndPoint_Type = IpAddress
_Hh3cSrpolicyEndPoint_Object = MibTableColumn
hh3cSrpolicyEndPoint = _Hh3cSrpolicyEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 2),
    _Hh3cSrpolicyEndPoint_Type()
)
hh3cSrpolicyEndPoint.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpolicyEndPoint.setStatus("current")


class _Hh3cSrpolicyName_Type(OctetString):
    """Custom type hh3cSrpolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hh3cSrpolicyName_Type.__name__ = "OctetString"
_Hh3cSrpolicyName_Object = MibTableColumn
hh3cSrpolicyName = _Hh3cSrpolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 3),
    _Hh3cSrpolicyName_Type()
)
hh3cSrpolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyName.setStatus("current")


class _Hh3cSrpolicyBsid_Type(Integer32):
    """Custom type hh3cSrpolicyBsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_Hh3cSrpolicyBsid_Type.__name__ = "Integer32"
_Hh3cSrpolicyBsid_Object = MibTableColumn
hh3cSrpolicyBsid = _Hh3cSrpolicyBsid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 4),
    _Hh3cSrpolicyBsid_Type()
)
hh3cSrpolicyBsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyBsid.setStatus("current")
_Hh3cSrpolicyInPackets_Type = Counter64
_Hh3cSrpolicyInPackets_Object = MibTableColumn
hh3cSrpolicyInPackets = _Hh3cSrpolicyInPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 5),
    _Hh3cSrpolicyInPackets_Type()
)
hh3cSrpolicyInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyInPackets.setStatus("current")
_Hh3cSrpolicyInOctets_Type = Counter64
_Hh3cSrpolicyInOctets_Object = MibTableColumn
hh3cSrpolicyInOctets = _Hh3cSrpolicyInOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 6),
    _Hh3cSrpolicyInOctets_Type()
)
hh3cSrpolicyInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyInOctets.setStatus("current")
_Hh3cSrpolicyOutPackets_Type = Counter64
_Hh3cSrpolicyOutPackets_Object = MibTableColumn
hh3cSrpolicyOutPackets = _Hh3cSrpolicyOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 7),
    _Hh3cSrpolicyOutPackets_Type()
)
hh3cSrpolicyOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyOutPackets.setStatus("current")
_Hh3cSrpolicyOutOctets_Type = Counter64
_Hh3cSrpolicyOutOctets_Object = MibTableColumn
hh3cSrpolicyOutOctets = _Hh3cSrpolicyOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 8),
    _Hh3cSrpolicyOutOctets_Type()
)
hh3cSrpolicyOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyOutOctets.setStatus("current")


class _Hh3cSrpolicyStatus_Type(OctetString):
    """Custom type hh3cSrpolicyStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cSrpolicyStatus_Type.__name__ = "OctetString"
_Hh3cSrpolicyStatus_Object = MibTableColumn
hh3cSrpolicyStatus = _Hh3cSrpolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 9),
    _Hh3cSrpolicyStatus_Type()
)
hh3cSrpolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyStatus.setStatus("current")


class _Hh3cSrpolicyDownReason_Type(OctetString):
    """Custom type hh3cSrpolicyDownReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_Hh3cSrpolicyDownReason_Type.__name__ = "OctetString"
_Hh3cSrpolicyDownReason_Object = MibTableColumn
hh3cSrpolicyDownReason = _Hh3cSrpolicyDownReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 10),
    _Hh3cSrpolicyDownReason_Type()
)
hh3cSrpolicyDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyDownReason.setStatus("current")


class _Hh3cSrpolicyBsidFailReason_Type(OctetString):
    """Custom type hh3cSrpolicyBsidFailReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSrpolicyBsidFailReason_Type.__name__ = "OctetString"
_Hh3cSrpolicyBsidFailReason_Object = MibTableColumn
hh3cSrpolicyBsidFailReason = _Hh3cSrpolicyBsidFailReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 11),
    _Hh3cSrpolicyBsidFailReason_Type()
)
hh3cSrpolicyBsidFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyBsidFailReason.setStatus("current")


class _Hh3cSrpolicyBsidConflictState_Type(Integer32):
    """Custom type hh3cSrpolicyBsidConflictState based on Integer32"""
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


_Hh3cSrpolicyBsidConflictState_Type.__name__ = "Integer32"
_Hh3cSrpolicyBsidConflictState_Object = MibTableColumn
hh3cSrpolicyBsidConflictState = _Hh3cSrpolicyBsidConflictState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 1, 1, 12),
    _Hh3cSrpolicyBsidConflictState_Type()
)
hh3cSrpolicyBsidConflictState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyBsidConflictState.setStatus("current")
_Hh3cSrpSeglistTable_Object = MibTable
hh3cSrpSeglistTable = _Hh3cSrpSeglistTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2)
)
if mibBuilder.loadTexts:
    hh3cSrpSeglistTable.setStatus("current")
_Hh3cSrpSeglistEntry_Object = MibTableRow
hh3cSrpSeglistEntry = _Hh3cSrpSeglistEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1)
)
hh3cSrpSeglistEntry.setIndexNames(
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpSeglistColor"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpSeglistEndPoint"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathProto"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathInst"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathOri"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathDis"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpSeglistId"),
)
if mibBuilder.loadTexts:
    hh3cSrpSeglistEntry.setStatus("current")


class _Hh3cSrpSeglistColor_Type(Unsigned32):
    """Custom type hh3cSrpSeglistColor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cSrpSeglistColor_Type.__name__ = "Unsigned32"
_Hh3cSrpSeglistColor_Object = MibTableColumn
hh3cSrpSeglistColor = _Hh3cSrpSeglistColor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 1),
    _Hh3cSrpSeglistColor_Type()
)
hh3cSrpSeglistColor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpSeglistColor.setStatus("current")
_Hh3cSrpSeglistEndPoint_Type = IpAddress
_Hh3cSrpSeglistEndPoint_Object = MibTableColumn
hh3cSrpSeglistEndPoint = _Hh3cSrpSeglistEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 2),
    _Hh3cSrpSeglistEndPoint_Type()
)
hh3cSrpSeglistEndPoint.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpSeglistEndPoint.setStatus("current")


class _Hh3cSrpSeglistPathProto_Type(Integer32):
    """Custom type hh3cSrpSeglistPathProto based on Integer32"""
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


_Hh3cSrpSeglistPathProto_Type.__name__ = "Integer32"
_Hh3cSrpSeglistPathProto_Object = MibTableColumn
hh3cSrpSeglistPathProto = _Hh3cSrpSeglistPathProto_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 3),
    _Hh3cSrpSeglistPathProto_Type()
)
hh3cSrpSeglistPathProto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpSeglistPathProto.setStatus("current")


class _Hh3cSrpSeglistPathInst_Type(Integer32):
    """Custom type hh3cSrpSeglistPathInst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cSrpSeglistPathInst_Type.__name__ = "Integer32"
_Hh3cSrpSeglistPathInst_Object = MibTableColumn
hh3cSrpSeglistPathInst = _Hh3cSrpSeglistPathInst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 4),
    _Hh3cSrpSeglistPathInst_Type()
)
hh3cSrpSeglistPathInst.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpSeglistPathInst.setStatus("current")


class _Hh3cSrpSeglistPathOri_Type(OctetString):
    """Custom type hh3cSrpSeglistPathOri based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cSrpSeglistPathOri_Type.__name__ = "OctetString"
_Hh3cSrpSeglistPathOri_Object = MibTableColumn
hh3cSrpSeglistPathOri = _Hh3cSrpSeglistPathOri_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 5),
    _Hh3cSrpSeglistPathOri_Type()
)
hh3cSrpSeglistPathOri.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpSeglistPathOri.setStatus("current")
_Hh3cSrpSeglistPathDis_Type = Unsigned32
_Hh3cSrpSeglistPathDis_Object = MibTableColumn
hh3cSrpSeglistPathDis = _Hh3cSrpSeglistPathDis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 6),
    _Hh3cSrpSeglistPathDis_Type()
)
hh3cSrpSeglistPathDis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpSeglistPathDis.setStatus("current")


class _Hh3cSrpSeglistId_Type(Unsigned32):
    """Custom type hh3cSrpSeglistId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cSrpSeglistId_Type.__name__ = "Unsigned32"
_Hh3cSrpSeglistId_Object = MibTableColumn
hh3cSrpSeglistId = _Hh3cSrpSeglistId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 7),
    _Hh3cSrpSeglistId_Type()
)
hh3cSrpSeglistId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpSeglistId.setStatus("current")


class _Hh3cSrpolicySeglistName_Type(OctetString):
    """Custom type hh3cSrpolicySeglistName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hh3cSrpolicySeglistName_Type.__name__ = "OctetString"
_Hh3cSrpolicySeglistName_Object = MibTableColumn
hh3cSrpolicySeglistName = _Hh3cSrpolicySeglistName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 8),
    _Hh3cSrpolicySeglistName_Type()
)
hh3cSrpolicySeglistName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicySeglistName.setStatus("current")
_Hh3cSrpSeglistOutPackets_Type = Counter64
_Hh3cSrpSeglistOutPackets_Object = MibTableColumn
hh3cSrpSeglistOutPackets = _Hh3cSrpSeglistOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 9),
    _Hh3cSrpSeglistOutPackets_Type()
)
hh3cSrpSeglistOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpSeglistOutPackets.setStatus("current")
_Hh3cSrpSeglistOutOctets_Type = Counter64
_Hh3cSrpSeglistOutOctets_Object = MibTableColumn
hh3cSrpSeglistOutOctets = _Hh3cSrpSeglistOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 10),
    _Hh3cSrpSeglistOutOctets_Type()
)
hh3cSrpSeglistOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpSeglistOutOctets.setStatus("current")


class _Hh3cSrpSeglistStatus_Type(OctetString):
    """Custom type hh3cSrpSeglistStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cSrpSeglistStatus_Type.__name__ = "OctetString"
_Hh3cSrpSeglistStatus_Object = MibTableColumn
hh3cSrpSeglistStatus = _Hh3cSrpSeglistStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 11),
    _Hh3cSrpSeglistStatus_Type()
)
hh3cSrpSeglistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpSeglistStatus.setStatus("current")


class _Hh3cSrpSeglistDownReason_Type(OctetString):
    """Custom type hh3cSrpSeglistDownReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_Hh3cSrpSeglistDownReason_Type.__name__ = "OctetString"
_Hh3cSrpSeglistDownReason_Object = MibTableColumn
hh3cSrpSeglistDownReason = _Hh3cSrpSeglistDownReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 2, 1, 12),
    _Hh3cSrpSeglistDownReason_Type()
)
hh3cSrpSeglistDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpSeglistDownReason.setStatus("current")
_Hh3cSrpForwardingTable_Object = MibTable
hh3cSrpForwardingTable = _Hh3cSrpForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3)
)
if mibBuilder.loadTexts:
    hh3cSrpForwardingTable.setStatus("current")
_Hh3cSrpForwardingEntry_Object = MibTableRow
hh3cSrpForwardingEntry = _Hh3cSrpForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1)
)
hh3cSrpForwardingEntry.setIndexNames(
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpFwdColor"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpFwdEndPoint"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpFwdPathProto"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpFwdPathInst"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpFwdPathOri"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpFwdPathDis"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpFwdSeglistId"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpFwdOutIf"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpFwdNexthop"),
)
if mibBuilder.loadTexts:
    hh3cSrpForwardingEntry.setStatus("current")


class _Hh3cSrpFwdColor_Type(Unsigned32):
    """Custom type hh3cSrpFwdColor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cSrpFwdColor_Type.__name__ = "Unsigned32"
_Hh3cSrpFwdColor_Object = MibTableColumn
hh3cSrpFwdColor = _Hh3cSrpFwdColor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1, 1),
    _Hh3cSrpFwdColor_Type()
)
hh3cSrpFwdColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSrpFwdColor.setStatus("current")
_Hh3cSrpFwdEndPoint_Type = IpAddress
_Hh3cSrpFwdEndPoint_Object = MibTableColumn
hh3cSrpFwdEndPoint = _Hh3cSrpFwdEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1, 2),
    _Hh3cSrpFwdEndPoint_Type()
)
hh3cSrpFwdEndPoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSrpFwdEndPoint.setStatus("current")


class _Hh3cSrpFwdPathProto_Type(Integer32):
    """Custom type hh3cSrpFwdPathProto based on Integer32"""
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


_Hh3cSrpFwdPathProto_Type.__name__ = "Integer32"
_Hh3cSrpFwdPathProto_Object = MibTableColumn
hh3cSrpFwdPathProto = _Hh3cSrpFwdPathProto_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1, 3),
    _Hh3cSrpFwdPathProto_Type()
)
hh3cSrpFwdPathProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSrpFwdPathProto.setStatus("current")


class _Hh3cSrpFwdPathInst_Type(Integer32):
    """Custom type hh3cSrpFwdPathInst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cSrpFwdPathInst_Type.__name__ = "Integer32"
_Hh3cSrpFwdPathInst_Object = MibTableColumn
hh3cSrpFwdPathInst = _Hh3cSrpFwdPathInst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1, 4),
    _Hh3cSrpFwdPathInst_Type()
)
hh3cSrpFwdPathInst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSrpFwdPathInst.setStatus("current")


class _Hh3cSrpFwdPathOri_Type(OctetString):
    """Custom type hh3cSrpFwdPathOri based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cSrpFwdPathOri_Type.__name__ = "OctetString"
_Hh3cSrpFwdPathOri_Object = MibTableColumn
hh3cSrpFwdPathOri = _Hh3cSrpFwdPathOri_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1, 5),
    _Hh3cSrpFwdPathOri_Type()
)
hh3cSrpFwdPathOri.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSrpFwdPathOri.setStatus("current")
_Hh3cSrpFwdPathDis_Type = Unsigned32
_Hh3cSrpFwdPathDis_Object = MibTableColumn
hh3cSrpFwdPathDis = _Hh3cSrpFwdPathDis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1, 6),
    _Hh3cSrpFwdPathDis_Type()
)
hh3cSrpFwdPathDis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSrpFwdPathDis.setStatus("current")


class _Hh3cSrpFwdSeglistId_Type(Unsigned32):
    """Custom type hh3cSrpFwdSeglistId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cSrpFwdSeglistId_Type.__name__ = "Unsigned32"
_Hh3cSrpFwdSeglistId_Object = MibTableColumn
hh3cSrpFwdSeglistId = _Hh3cSrpFwdSeglistId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1, 7),
    _Hh3cSrpFwdSeglistId_Type()
)
hh3cSrpFwdSeglistId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSrpFwdSeglistId.setStatus("current")
_Hh3cSrpFwdOutIf_Type = InterfaceIndex
_Hh3cSrpFwdOutIf_Object = MibTableColumn
hh3cSrpFwdOutIf = _Hh3cSrpFwdOutIf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1, 8),
    _Hh3cSrpFwdOutIf_Type()
)
hh3cSrpFwdOutIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSrpFwdOutIf.setStatus("current")
_Hh3cSrpFwdNexthop_Type = IpAddress
_Hh3cSrpFwdNexthop_Object = MibTableColumn
hh3cSrpFwdNexthop = _Hh3cSrpFwdNexthop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1, 9),
    _Hh3cSrpFwdNexthop_Type()
)
hh3cSrpFwdNexthop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSrpFwdNexthop.setStatus("current")
_Hh3cSrpFwdOutPackets_Type = Counter64
_Hh3cSrpFwdOutPackets_Object = MibTableColumn
hh3cSrpFwdOutPackets = _Hh3cSrpFwdOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1, 10),
    _Hh3cSrpFwdOutPackets_Type()
)
hh3cSrpFwdOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpFwdOutPackets.setStatus("current")
_Hh3cSrpFwdOutOctets_Type = Counter64
_Hh3cSrpFwdOutOctets_Object = MibTableColumn
hh3cSrpFwdOutOctets = _Hh3cSrpFwdOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 3, 1, 11),
    _Hh3cSrpFwdOutOctets_Type()
)
hh3cSrpFwdOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpFwdOutOctets.setStatus("current")
_Hh3cSrpolicyPathTable_Object = MibTable
hh3cSrpolicyPathTable = _Hh3cSrpolicyPathTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 4)
)
if mibBuilder.loadTexts:
    hh3cSrpolicyPathTable.setStatus("current")
_Hh3cSrpolicyPathEntry_Object = MibTableRow
hh3cSrpolicyPathEntry = _Hh3cSrpolicyPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 4, 1)
)
hh3cSrpolicyPathEntry.setIndexNames(
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathColor"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathEndPoint"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathProto"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathInst"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathOri"),
    (0, "HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathDis"),
)
if mibBuilder.loadTexts:
    hh3cSrpolicyPathEntry.setStatus("current")


class _Hh3cSrpolicyPathColor_Type(Unsigned32):
    """Custom type hh3cSrpolicyPathColor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cSrpolicyPathColor_Type.__name__ = "Unsigned32"
_Hh3cSrpolicyPathColor_Object = MibTableColumn
hh3cSrpolicyPathColor = _Hh3cSrpolicyPathColor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 4, 1, 1),
    _Hh3cSrpolicyPathColor_Type()
)
hh3cSrpolicyPathColor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpolicyPathColor.setStatus("current")
_Hh3cSrpolicyPathEndPoint_Type = IpAddress
_Hh3cSrpolicyPathEndPoint_Object = MibTableColumn
hh3cSrpolicyPathEndPoint = _Hh3cSrpolicyPathEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 4, 1, 2),
    _Hh3cSrpolicyPathEndPoint_Type()
)
hh3cSrpolicyPathEndPoint.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpolicyPathEndPoint.setStatus("current")


class _Hh3cSrpolicyPathProto_Type(Integer32):
    """Custom type hh3cSrpolicyPathProto based on Integer32"""
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


_Hh3cSrpolicyPathProto_Type.__name__ = "Integer32"
_Hh3cSrpolicyPathProto_Object = MibTableColumn
hh3cSrpolicyPathProto = _Hh3cSrpolicyPathProto_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 4, 1, 3),
    _Hh3cSrpolicyPathProto_Type()
)
hh3cSrpolicyPathProto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpolicyPathProto.setStatus("current")


class _Hh3cSrpolicyPathInst_Type(Integer32):
    """Custom type hh3cSrpolicyPathInst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cSrpolicyPathInst_Type.__name__ = "Integer32"
_Hh3cSrpolicyPathInst_Object = MibTableColumn
hh3cSrpolicyPathInst = _Hh3cSrpolicyPathInst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 4, 1, 4),
    _Hh3cSrpolicyPathInst_Type()
)
hh3cSrpolicyPathInst.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpolicyPathInst.setStatus("current")


class _Hh3cSrpolicyPathOri_Type(OctetString):
    """Custom type hh3cSrpolicyPathOri based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cSrpolicyPathOri_Type.__name__ = "OctetString"
_Hh3cSrpolicyPathOri_Object = MibTableColumn
hh3cSrpolicyPathOri = _Hh3cSrpolicyPathOri_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 4, 1, 5),
    _Hh3cSrpolicyPathOri_Type()
)
hh3cSrpolicyPathOri.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpolicyPathOri.setStatus("current")
_Hh3cSrpolicyPathDis_Type = Unsigned32
_Hh3cSrpolicyPathDis_Object = MibTableColumn
hh3cSrpolicyPathDis = _Hh3cSrpolicyPathDis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 4, 1, 6),
    _Hh3cSrpolicyPathDis_Type()
)
hh3cSrpolicyPathDis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSrpolicyPathDis.setStatus("current")
_Hh3cSrpolicyPathPref_Type = Unsigned32
_Hh3cSrpolicyPathPref_Object = MibTableColumn
hh3cSrpolicyPathPref = _Hh3cSrpolicyPathPref_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 4, 1, 7),
    _Hh3cSrpolicyPathPref_Type()
)
hh3cSrpolicyPathPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyPathPref.setStatus("current")


class _Hh3cSrpolicyPathPreviousRole_Type(OctetString):
    """Custom type hh3cSrpolicyPathPreviousRole based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cSrpolicyPathPreviousRole_Type.__name__ = "OctetString"
_Hh3cSrpolicyPathPreviousRole_Object = MibTableColumn
hh3cSrpolicyPathPreviousRole = _Hh3cSrpolicyPathPreviousRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 4, 1, 8),
    _Hh3cSrpolicyPathPreviousRole_Type()
)
hh3cSrpolicyPathPreviousRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyPathPreviousRole.setStatus("current")


class _Hh3cSrpolicyPathDownReason_Type(OctetString):
    """Custom type hh3cSrpolicyPathDownReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_Hh3cSrpolicyPathDownReason_Type.__name__ = "OctetString"
_Hh3cSrpolicyPathDownReason_Object = MibTableColumn
hh3cSrpolicyPathDownReason = _Hh3cSrpolicyPathDownReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 4, 1, 9),
    _Hh3cSrpolicyPathDownReason_Type()
)
hh3cSrpolicyPathDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSrpolicyPathDownReason.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cSrpolicyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 0, 1)
)
hh3cSrpolicyStatusChange.setObjects(
      *(("HH3C-SRPOLICY-MIB", "hh3cSrpolicyColor"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyEndPoint"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyStatus"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyDownReason"))
)
if mibBuilder.loadTexts:
    hh3cSrpolicyStatusChange.setStatus(
        "current"
    )

hh3cSrpolicyBsidConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 0, 2)
)
hh3cSrpolicyBsidConflict.setObjects(
      *(("HH3C-SRPOLICY-MIB", "hh3cSrpolicyColor"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyEndPoint"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyBsid"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyBsidFailReason"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyBsidConflictState"))
)
if mibBuilder.loadTexts:
    hh3cSrpolicyBsidConflict.setStatus(
        "current"
    )

hh3cSrpolicyBsidConflictClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 0, 3)
)
hh3cSrpolicyBsidConflictClear.setObjects(
      *(("HH3C-SRPOLICY-MIB", "hh3cSrpolicyColor"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyEndPoint"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyBsid"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyBsidFailReason"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyBsidConflictState"))
)
if mibBuilder.loadTexts:
    hh3cSrpolicyBsidConflictClear.setStatus(
        "current"
    )

hh3cSrpolicyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 0, 4)
)
hh3cSrpolicyDown.setObjects(
      *(("HH3C-SRPOLICY-MIB", "hh3cSrpolicyColor"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyEndPoint"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyDownReason"))
)
if mibBuilder.loadTexts:
    hh3cSrpolicyDown.setStatus(
        "current"
    )

hh3cSrpolicyDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 0, 5)
)
hh3cSrpolicyDownClear.setObjects(
      *(("HH3C-SRPOLICY-MIB", "hh3cSrpolicyColor"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyEndPoint"))
)
if mibBuilder.loadTexts:
    hh3cSrpolicyDownClear.setStatus(
        "current"
    )

hh3cSrpolicyPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 0, 6)
)
hh3cSrpolicyPathDown.setObjects(
      *(("HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathColor"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathEndPoint"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathProto"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathInst"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathOri"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathDis"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathPref"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathPreviousRole"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpolicyPathDownReason"))
)
if mibBuilder.loadTexts:
    hh3cSrpolicyPathDown.setStatus(
        "current"
    )

hh3cSrpolicySeglistDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 0, 7)
)
hh3cSrpolicySeglistDown.setObjects(
      *(("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistColor"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistEndPoint"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathProto"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathInst"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathOri"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathDis"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistId"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistStatus"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistDownReason"))
)
if mibBuilder.loadTexts:
    hh3cSrpolicySeglistDown.setStatus(
        "current"
    )

hh3cSrpolicySeglistDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 186, 0, 8)
)
hh3cSrpolicySeglistDownClear.setObjects(
      *(("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistColor"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistEndPoint"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathProto"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathInst"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathOri"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistPathDis"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistId"),
        ("HH3C-SRPOLICY-MIB", "hh3cSrpSeglistStatus"))
)
if mibBuilder.loadTexts:
    hh3cSrpolicySeglistDownClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SRPOLICY-MIB",
    **{"hh3cSrpolicy": hh3cSrpolicy,
       "hh3cSrpolicyNotifications": hh3cSrpolicyNotifications,
       "hh3cSrpolicyStatusChange": hh3cSrpolicyStatusChange,
       "hh3cSrpolicyBsidConflict": hh3cSrpolicyBsidConflict,
       "hh3cSrpolicyBsidConflictClear": hh3cSrpolicyBsidConflictClear,
       "hh3cSrpolicyDown": hh3cSrpolicyDown,
       "hh3cSrpolicyDownClear": hh3cSrpolicyDownClear,
       "hh3cSrpolicyPathDown": hh3cSrpolicyPathDown,
       "hh3cSrpolicySeglistDown": hh3cSrpolicySeglistDown,
       "hh3cSrpolicySeglistDownClear": hh3cSrpolicySeglistDownClear,
       "hh3cSrpolicyTable": hh3cSrpolicyTable,
       "hh3cSrpolicyEntry": hh3cSrpolicyEntry,
       "hh3cSrpolicyColor": hh3cSrpolicyColor,
       "hh3cSrpolicyEndPoint": hh3cSrpolicyEndPoint,
       "hh3cSrpolicyName": hh3cSrpolicyName,
       "hh3cSrpolicyBsid": hh3cSrpolicyBsid,
       "hh3cSrpolicyInPackets": hh3cSrpolicyInPackets,
       "hh3cSrpolicyInOctets": hh3cSrpolicyInOctets,
       "hh3cSrpolicyOutPackets": hh3cSrpolicyOutPackets,
       "hh3cSrpolicyOutOctets": hh3cSrpolicyOutOctets,
       "hh3cSrpolicyStatus": hh3cSrpolicyStatus,
       "hh3cSrpolicyDownReason": hh3cSrpolicyDownReason,
       "hh3cSrpolicyBsidFailReason": hh3cSrpolicyBsidFailReason,
       "hh3cSrpolicyBsidConflictState": hh3cSrpolicyBsidConflictState,
       "hh3cSrpSeglistTable": hh3cSrpSeglistTable,
       "hh3cSrpSeglistEntry": hh3cSrpSeglistEntry,
       "hh3cSrpSeglistColor": hh3cSrpSeglistColor,
       "hh3cSrpSeglistEndPoint": hh3cSrpSeglistEndPoint,
       "hh3cSrpSeglistPathProto": hh3cSrpSeglistPathProto,
       "hh3cSrpSeglistPathInst": hh3cSrpSeglistPathInst,
       "hh3cSrpSeglistPathOri": hh3cSrpSeglistPathOri,
       "hh3cSrpSeglistPathDis": hh3cSrpSeglistPathDis,
       "hh3cSrpSeglistId": hh3cSrpSeglistId,
       "hh3cSrpolicySeglistName": hh3cSrpolicySeglistName,
       "hh3cSrpSeglistOutPackets": hh3cSrpSeglistOutPackets,
       "hh3cSrpSeglistOutOctets": hh3cSrpSeglistOutOctets,
       "hh3cSrpSeglistStatus": hh3cSrpSeglistStatus,
       "hh3cSrpSeglistDownReason": hh3cSrpSeglistDownReason,
       "hh3cSrpForwardingTable": hh3cSrpForwardingTable,
       "hh3cSrpForwardingEntry": hh3cSrpForwardingEntry,
       "hh3cSrpFwdColor": hh3cSrpFwdColor,
       "hh3cSrpFwdEndPoint": hh3cSrpFwdEndPoint,
       "hh3cSrpFwdPathProto": hh3cSrpFwdPathProto,
       "hh3cSrpFwdPathInst": hh3cSrpFwdPathInst,
       "hh3cSrpFwdPathOri": hh3cSrpFwdPathOri,
       "hh3cSrpFwdPathDis": hh3cSrpFwdPathDis,
       "hh3cSrpFwdSeglistId": hh3cSrpFwdSeglistId,
       "hh3cSrpFwdOutIf": hh3cSrpFwdOutIf,
       "hh3cSrpFwdNexthop": hh3cSrpFwdNexthop,
       "hh3cSrpFwdOutPackets": hh3cSrpFwdOutPackets,
       "hh3cSrpFwdOutOctets": hh3cSrpFwdOutOctets,
       "hh3cSrpolicyPathTable": hh3cSrpolicyPathTable,
       "hh3cSrpolicyPathEntry": hh3cSrpolicyPathEntry,
       "hh3cSrpolicyPathColor": hh3cSrpolicyPathColor,
       "hh3cSrpolicyPathEndPoint": hh3cSrpolicyPathEndPoint,
       "hh3cSrpolicyPathProto": hh3cSrpolicyPathProto,
       "hh3cSrpolicyPathInst": hh3cSrpolicyPathInst,
       "hh3cSrpolicyPathOri": hh3cSrpolicyPathOri,
       "hh3cSrpolicyPathDis": hh3cSrpolicyPathDis,
       "hh3cSrpolicyPathPref": hh3cSrpolicyPathPref,
       "hh3cSrpolicyPathPreviousRole": hh3cSrpolicyPathPreviousRole,
       "hh3cSrpolicyPathDownReason": hh3cSrpolicyPathDownReason}
)
