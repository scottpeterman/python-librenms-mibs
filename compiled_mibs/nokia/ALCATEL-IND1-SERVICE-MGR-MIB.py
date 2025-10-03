# SNMP MIB module (ALCATEL-IND1-SERVICE-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-SERVICE-MGR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:11 2025
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

(softentIND1serviceMgr,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1serviceMgr")

(AlaEServiceUNIProfileProtocolTreatment,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-E-SERVICE-MIB",
    "AlaEServiceUNIProfileProtocolTreatment")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(MplsLdpIdentifier,) = mibBuilder.importSymbols(
    "MPLS-LDP-MIB",
    "MplsLdpIdentifier")

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

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(sdpBindId,) = mibBuilder.importSymbols(
    "TIMETRA-SDP-MIB",
    "sdpBindId")

(SdpId,
 svcId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpId",
    "svcId")

(SdpBindId,
 TmnxEncapVal,
 TmnxPortID,
 TmnxServId,
 TmnxVcIdOrNone) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "SdpBindId",
    "TmnxEncapVal",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVcIdOrNone")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

alcatelIND1ServiceMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AluLocation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("sdp", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1ServiceMgrMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1ServiceMgrMIBObjects = _AlcatelIND1ServiceMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ServiceMgrMIBObjects.setStatus("current")
_AlaServiceMgr_ObjectIdentity = ObjectIdentity
alaServiceMgr = _AlaServiceMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1)
)
_AlaServiceMgrPortProfileTable_Object = MibTable
alaServiceMgrPortProfileTable = _AlaServiceMgrPortProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaServiceMgrPortProfileTable.setStatus("current")
_AlaServiceMgrPortProfileEntry_Object = MibTableRow
alaServiceMgrPortProfileEntry = _AlaServiceMgrPortProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 1, 1)
)
alaServiceMgrPortProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortProfileID"),
)
if mibBuilder.loadTexts:
    alaServiceMgrPortProfileEntry.setStatus("current")


class _AlaServiceMgrPortProfileID_Type(DisplayString):
    """Custom type alaServiceMgrPortProfileID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaServiceMgrPortProfileID_Type.__name__ = "DisplayString"
_AlaServiceMgrPortProfileID_Object = MibTableColumn
alaServiceMgrPortProfileID = _AlaServiceMgrPortProfileID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 1, 1, 1),
    _AlaServiceMgrPortProfileID_Type()
)
alaServiceMgrPortProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaServiceMgrPortProfileID.setStatus("current")


class _AlaServiceMgrPortProfileStpBpduTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaServiceMgrPortProfileStpBpduTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 1


_AlaServiceMgrPortProfileStpBpduTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaServiceMgrPortProfileStpBpduTreatment_Object = MibTableColumn
alaServiceMgrPortProfileStpBpduTreatment = _AlaServiceMgrPortProfileStpBpduTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 1, 1, 2),
    _AlaServiceMgrPortProfileStpBpduTreatment_Type()
)
alaServiceMgrPortProfileStpBpduTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaServiceMgrPortProfileStpBpduTreatment.setStatus("current")


class _AlaServiceMgrPortProfile8021xTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaServiceMgrPortProfile8021xTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaServiceMgrPortProfile8021xTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaServiceMgrPortProfile8021xTreatment_Object = MibTableColumn
alaServiceMgrPortProfile8021xTreatment = _AlaServiceMgrPortProfile8021xTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 1, 1, 3),
    _AlaServiceMgrPortProfile8021xTreatment_Type()
)
alaServiceMgrPortProfile8021xTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaServiceMgrPortProfile8021xTreatment.setStatus("current")


class _AlaServiceMgrPortProfile8021ABTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaServiceMgrPortProfile8021ABTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaServiceMgrPortProfile8021ABTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaServiceMgrPortProfile8021ABTreatment_Object = MibTableColumn
alaServiceMgrPortProfile8021ABTreatment = _AlaServiceMgrPortProfile8021ABTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 1, 1, 4),
    _AlaServiceMgrPortProfile8021ABTreatment_Type()
)
alaServiceMgrPortProfile8021ABTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaServiceMgrPortProfile8021ABTreatment.setStatus("current")


class _AlaServiceMgrPortProfile8023adTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaServiceMgrPortProfile8023adTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 3


_AlaServiceMgrPortProfile8023adTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaServiceMgrPortProfile8023adTreatment_Object = MibTableColumn
alaServiceMgrPortProfile8023adTreatment = _AlaServiceMgrPortProfile8023adTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 1, 1, 5),
    _AlaServiceMgrPortProfile8023adTreatment_Type()
)
alaServiceMgrPortProfile8023adTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaServiceMgrPortProfile8023adTreatment.setStatus("current")


class _AlaServiceMgrPortProfileGvrpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaServiceMgrPortProfileGvrpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 1


_AlaServiceMgrPortProfileGvrpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaServiceMgrPortProfileGvrpTreatment_Object = MibTableColumn
alaServiceMgrPortProfileGvrpTreatment = _AlaServiceMgrPortProfileGvrpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 1, 1, 6),
    _AlaServiceMgrPortProfileGvrpTreatment_Type()
)
alaServiceMgrPortProfileGvrpTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaServiceMgrPortProfileGvrpTreatment.setStatus("current")


class _AlaServiceMgrPortProfileAmapTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaServiceMgrPortProfileAmapTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaServiceMgrPortProfileAmapTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaServiceMgrPortProfileAmapTreatment_Object = MibTableColumn
alaServiceMgrPortProfileAmapTreatment = _AlaServiceMgrPortProfileAmapTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 1, 1, 7),
    _AlaServiceMgrPortProfileAmapTreatment_Type()
)
alaServiceMgrPortProfileAmapTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaServiceMgrPortProfileAmapTreatment.setStatus("current")
_AlaServiceMgrPortProfileRowStatus_Type = RowStatus
_AlaServiceMgrPortProfileRowStatus_Object = MibTableColumn
alaServiceMgrPortProfileRowStatus = _AlaServiceMgrPortProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 1, 1, 8),
    _AlaServiceMgrPortProfileRowStatus_Type()
)
alaServiceMgrPortProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaServiceMgrPortProfileRowStatus.setStatus("current")


class _AlaServiceMgrPortProfileMvrpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaServiceMgrPortProfileMvrpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 1


_AlaServiceMgrPortProfileMvrpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaServiceMgrPortProfileMvrpTreatment_Object = MibTableColumn
alaServiceMgrPortProfileMvrpTreatment = _AlaServiceMgrPortProfileMvrpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 1, 1, 9),
    _AlaServiceMgrPortProfileMvrpTreatment_Type()
)
alaServiceMgrPortProfileMvrpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaServiceMgrPortProfileMvrpTreatment.setStatus("current")
_AlaServiceMgrPortTable_Object = MibTable
alaServiceMgrPortTable = _AlaServiceMgrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaServiceMgrPortTable.setStatus("current")
_AlaServiceMgrPortEntry_Object = MibTableRow
alaServiceMgrPortEntry = _AlaServiceMgrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 2, 1)
)
alaServiceMgrPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortID"),
)
if mibBuilder.loadTexts:
    alaServiceMgrPortEntry.setStatus("current")
_AlaServiceMgrPortID_Type = InterfaceIndex
_AlaServiceMgrPortID_Object = MibTableColumn
alaServiceMgrPortID = _AlaServiceMgrPortID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 2, 1, 1),
    _AlaServiceMgrPortID_Type()
)
alaServiceMgrPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaServiceMgrPortID.setStatus("current")


class _AlaServiceMgrPortMode_Type(Integer32):
    """Custom type alaServiceMgrPortMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("access", 1),
          ("network", 2))
    )


_AlaServiceMgrPortMode_Type.__name__ = "Integer32"
_AlaServiceMgrPortMode_Object = MibTableColumn
alaServiceMgrPortMode = _AlaServiceMgrPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 2, 1, 2),
    _AlaServiceMgrPortMode_Type()
)
alaServiceMgrPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaServiceMgrPortMode.setStatus("current")


class _AlaServiceMgrPortEncapType_Type(Integer32):
    """Custom type alaServiceMgrPortEncapType based on Integer32"""
    defaultValue = 1

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
          ("nullEncap", 1),
          ("qEncap", 2))
    )


_AlaServiceMgrPortEncapType_Type.__name__ = "Integer32"
_AlaServiceMgrPortEncapType_Object = MibTableColumn
alaServiceMgrPortEncapType = _AlaServiceMgrPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 2, 1, 3),
    _AlaServiceMgrPortEncapType_Type()
)
alaServiceMgrPortEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaServiceMgrPortEncapType.setStatus("current")


class _AlaServiceMgrPortPortProfileID_Type(DisplayString):
    """Custom type alaServiceMgrPortPortProfileID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaServiceMgrPortPortProfileID_Type.__name__ = "DisplayString"
_AlaServiceMgrPortPortProfileID_Object = MibTableColumn
alaServiceMgrPortPortProfileID = _AlaServiceMgrPortPortProfileID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 2, 1, 4),
    _AlaServiceMgrPortPortProfileID_Type()
)
alaServiceMgrPortPortProfileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaServiceMgrPortPortProfileID.setStatus("current")
_AlaServiceMgrPortRowStatus_Type = RowStatus
_AlaServiceMgrPortRowStatus_Object = MibTableColumn
alaServiceMgrPortRowStatus = _AlaServiceMgrPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 2, 1, 5),
    _AlaServiceMgrPortRowStatus_Type()
)
alaServiceMgrPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaServiceMgrPortRowStatus.setStatus("current")
_AlaSapExtraInfoTable_Object = MibTable
alaSapExtraInfoTable = _AlaSapExtraInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaSapExtraInfoTable.setStatus("current")
_AlaSapExtraInfoEntry_Object = MibTableRow
alaSapExtraInfoEntry = _AlaSapExtraInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 3, 1)
)
alaSapExtraInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    alaSapExtraInfoEntry.setStatus("current")


class _AlaSapInfoTrusted_Type(Integer32):
    """Custom type alaSapInfoTrusted based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AlaSapInfoTrusted_Type.__name__ = "Integer32"
_AlaSapInfoTrusted_Object = MibTableColumn
alaSapInfoTrusted = _AlaSapInfoTrusted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 3, 1, 1),
    _AlaSapInfoTrusted_Type()
)
alaSapInfoTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaSapInfoTrusted.setStatus("current")


class _AlaSapInfoPriority_Type(Integer32):
    """Custom type alaSapInfoPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaSapInfoPriority_Type.__name__ = "Integer32"
_AlaSapInfoPriority_Object = MibTableColumn
alaSapInfoPriority = _AlaSapInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 1, 3, 1, 2),
    _AlaSapInfoPriority_Type()
)
alaSapInfoPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaSapInfoPriority.setStatus("current")
_AlaServiceMgrIgmp_ObjectIdentity = ObjectIdentity
alaServiceMgrIgmp = _AlaServiceMgrIgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2)
)
_AlaIgmpServiceTable_Object = MibTable
alaIgmpServiceTable = _AlaIgmpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaIgmpServiceTable.setStatus("current")
_AlaIgmpServiceEntry_Object = MibTableRow
alaIgmpServiceEntry = _AlaIgmpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1)
)
alaIgmpServiceEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    alaIgmpServiceEntry.setStatus("current")


class _AlaIgmpServiceStatus_Type(Integer32):
    """Custom type alaIgmpServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaIgmpServiceStatus_Type.__name__ = "Integer32"
_AlaIgmpServiceStatus_Object = MibTableColumn
alaIgmpServiceStatus = _AlaIgmpServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 1),
    _AlaIgmpServiceStatus_Type()
)
alaIgmpServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceStatus.setStatus("current")


class _AlaIgmpServiceQuerying_Type(Integer32):
    """Custom type alaIgmpServiceQuerying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaIgmpServiceQuerying_Type.__name__ = "Integer32"
_AlaIgmpServiceQuerying_Object = MibTableColumn
alaIgmpServiceQuerying = _AlaIgmpServiceQuerying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 2),
    _AlaIgmpServiceQuerying_Type()
)
alaIgmpServiceQuerying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceQuerying.setStatus("current")


class _AlaIgmpServiceSpoofing_Type(Integer32):
    """Custom type alaIgmpServiceSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaIgmpServiceSpoofing_Type.__name__ = "Integer32"
_AlaIgmpServiceSpoofing_Object = MibTableColumn
alaIgmpServiceSpoofing = _AlaIgmpServiceSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 3),
    _AlaIgmpServiceSpoofing_Type()
)
alaIgmpServiceSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceSpoofing.setStatus("current")


class _AlaIgmpServiceZapping_Type(Integer32):
    """Custom type alaIgmpServiceZapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaIgmpServiceZapping_Type.__name__ = "Integer32"
_AlaIgmpServiceZapping_Object = MibTableColumn
alaIgmpServiceZapping = _AlaIgmpServiceZapping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 4),
    _AlaIgmpServiceZapping_Type()
)
alaIgmpServiceZapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceZapping.setStatus("current")
_AlaIgmpServiceVersion_Type = Unsigned32
_AlaIgmpServiceVersion_Object = MibTableColumn
alaIgmpServiceVersion = _AlaIgmpServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 5),
    _AlaIgmpServiceVersion_Type()
)
alaIgmpServiceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceVersion.setStatus("current")
_AlaIgmpServiceRobustness_Type = Unsigned32
_AlaIgmpServiceRobustness_Object = MibTableColumn
alaIgmpServiceRobustness = _AlaIgmpServiceRobustness_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 6),
    _AlaIgmpServiceRobustness_Type()
)
alaIgmpServiceRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceRobustness.setStatus("current")
_AlaIgmpServiceQueryInterval_Type = Unsigned32
_AlaIgmpServiceQueryInterval_Object = MibTableColumn
alaIgmpServiceQueryInterval = _AlaIgmpServiceQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 7),
    _AlaIgmpServiceQueryInterval_Type()
)
alaIgmpServiceQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpServiceQueryInterval.setUnits("seconds")
_AlaIgmpServiceQueryResponseInterval_Type = Unsigned32
_AlaIgmpServiceQueryResponseInterval_Object = MibTableColumn
alaIgmpServiceQueryResponseInterval = _AlaIgmpServiceQueryResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 8),
    _AlaIgmpServiceQueryResponseInterval_Type()
)
alaIgmpServiceQueryResponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceQueryResponseInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpServiceQueryResponseInterval.setUnits("tenths of seconds")
_AlaIgmpServiceLastMemberQueryInterval_Type = Unsigned32
_AlaIgmpServiceLastMemberQueryInterval_Object = MibTableColumn
alaIgmpServiceLastMemberQueryInterval = _AlaIgmpServiceLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 9),
    _AlaIgmpServiceLastMemberQueryInterval_Type()
)
alaIgmpServiceLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpServiceLastMemberQueryInterval.setUnits("tenths of seconds")
_AlaIgmpServiceRouterTimeout_Type = Unsigned32
_AlaIgmpServiceRouterTimeout_Object = MibTableColumn
alaIgmpServiceRouterTimeout = _AlaIgmpServiceRouterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 10),
    _AlaIgmpServiceRouterTimeout_Type()
)
alaIgmpServiceRouterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceRouterTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpServiceRouterTimeout.setUnits("seconds")
_AlaIgmpServiceSourceTimeout_Type = Unsigned32
_AlaIgmpServiceSourceTimeout_Object = MibTableColumn
alaIgmpServiceSourceTimeout = _AlaIgmpServiceSourceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 11),
    _AlaIgmpServiceSourceTimeout_Type()
)
alaIgmpServiceSourceTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceTimeout.setUnits("seconds")


class _AlaIgmpServiceProxying_Type(Integer32):
    """Custom type alaIgmpServiceProxying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaIgmpServiceProxying_Type.__name__ = "Integer32"
_AlaIgmpServiceProxying_Object = MibTableColumn
alaIgmpServiceProxying = _AlaIgmpServiceProxying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 12),
    _AlaIgmpServiceProxying_Type()
)
alaIgmpServiceProxying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceProxying.setStatus("current")
_AlaIgmpServiceUnsolicitedReportInterval_Type = Unsigned32
_AlaIgmpServiceUnsolicitedReportInterval_Object = MibTableColumn
alaIgmpServiceUnsolicitedReportInterval = _AlaIgmpServiceUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 13),
    _AlaIgmpServiceUnsolicitedReportInterval_Type()
)
alaIgmpServiceUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceUnsolicitedReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpServiceUnsolicitedReportInterval.setUnits("seconds")


class _AlaIgmpServiceQuerierForwarding_Type(Integer32):
    """Custom type alaIgmpServiceQuerierForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaIgmpServiceQuerierForwarding_Type.__name__ = "Integer32"
_AlaIgmpServiceQuerierForwarding_Object = MibTableColumn
alaIgmpServiceQuerierForwarding = _AlaIgmpServiceQuerierForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 14),
    _AlaIgmpServiceQuerierForwarding_Type()
)
alaIgmpServiceQuerierForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceQuerierForwarding.setStatus("current")


class _AlaIgmpServiceMaxGroupLimit_Type(Unsigned32):
    """Custom type alaIgmpServiceMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaIgmpServiceMaxGroupLimit_Type.__name__ = "Unsigned32"
_AlaIgmpServiceMaxGroupLimit_Object = MibTableColumn
alaIgmpServiceMaxGroupLimit = _AlaIgmpServiceMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 15),
    _AlaIgmpServiceMaxGroupLimit_Type()
)
alaIgmpServiceMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceMaxGroupLimit.setStatus("current")


class _AlaIgmpServiceMaxGroupExceedAction_Type(Integer32):
    """Custom type alaIgmpServiceMaxGroupExceedAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("drop", 1),
          ("replace", 2))
    )


_AlaIgmpServiceMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaIgmpServiceMaxGroupExceedAction_Object = MibTableColumn
alaIgmpServiceMaxGroupExceedAction = _AlaIgmpServiceMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 1, 1, 16),
    _AlaIgmpServiceMaxGroupExceedAction_Type()
)
alaIgmpServiceMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceMaxGroupExceedAction.setStatus("current")
_AlaIgmpMemberServiceSapTable_Object = MibTable
alaIgmpMemberServiceSapTable = _AlaIgmpMemberServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSapTable.setStatus("current")
_AlaIgmpMemberServiceSapEntry_Object = MibTableRow
alaIgmpMemberServiceSapEntry = _AlaIgmpMemberServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 2, 1)
)
alaIgmpMemberServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSapGroupAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSapGroupAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSapSourceAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSapSourceAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSapEntry.setStatus("current")


class _AlaIgmpMemberServiceSapGroupAddressType_Type(InetAddressType):
    """Custom type alaIgmpMemberServiceSapGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpMemberServiceSapGroupAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpMemberServiceSapGroupAddressType_Object = MibTableColumn
alaIgmpMemberServiceSapGroupAddressType = _AlaIgmpMemberServiceSapGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 2, 1, 1),
    _AlaIgmpMemberServiceSapGroupAddressType_Type()
)
alaIgmpMemberServiceSapGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSapGroupAddressType.setStatus("current")


class _AlaIgmpMemberServiceSapGroupAddress_Type(InetAddress):
    """Custom type alaIgmpMemberServiceSapGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpMemberServiceSapGroupAddress_Type.__name__ = "InetAddress"
_AlaIgmpMemberServiceSapGroupAddress_Object = MibTableColumn
alaIgmpMemberServiceSapGroupAddress = _AlaIgmpMemberServiceSapGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 2, 1, 2),
    _AlaIgmpMemberServiceSapGroupAddress_Type()
)
alaIgmpMemberServiceSapGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSapGroupAddress.setStatus("current")


class _AlaIgmpMemberServiceSapSourceAddressType_Type(InetAddressType):
    """Custom type alaIgmpMemberServiceSapSourceAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpMemberServiceSapSourceAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpMemberServiceSapSourceAddressType_Object = MibTableColumn
alaIgmpMemberServiceSapSourceAddressType = _AlaIgmpMemberServiceSapSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 2, 1, 3),
    _AlaIgmpMemberServiceSapSourceAddressType_Type()
)
alaIgmpMemberServiceSapSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSapSourceAddressType.setStatus("current")


class _AlaIgmpMemberServiceSapSourceAddress_Type(InetAddress):
    """Custom type alaIgmpMemberServiceSapSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpMemberServiceSapSourceAddress_Type.__name__ = "InetAddress"
_AlaIgmpMemberServiceSapSourceAddress_Object = MibTableColumn
alaIgmpMemberServiceSapSourceAddress = _AlaIgmpMemberServiceSapSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 2, 1, 4),
    _AlaIgmpMemberServiceSapSourceAddress_Type()
)
alaIgmpMemberServiceSapSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSapSourceAddress.setStatus("current")


class _AlaIgmpMemberServiceSapMode_Type(Integer32):
    """Custom type alaIgmpMemberServiceSapMode based on Integer32"""
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


_AlaIgmpMemberServiceSapMode_Type.__name__ = "Integer32"
_AlaIgmpMemberServiceSapMode_Object = MibTableColumn
alaIgmpMemberServiceSapMode = _AlaIgmpMemberServiceSapMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 2, 1, 5),
    _AlaIgmpMemberServiceSapMode_Type()
)
alaIgmpMemberServiceSapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSapMode.setStatus("current")
_AlaIgmpMemberServiceSapCount_Type = Counter32
_AlaIgmpMemberServiceSapCount_Object = MibTableColumn
alaIgmpMemberServiceSapCount = _AlaIgmpMemberServiceSapCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 2, 1, 6),
    _AlaIgmpMemberServiceSapCount_Type()
)
alaIgmpMemberServiceSapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSapCount.setStatus("current")
_AlaIgmpMemberServiceSapTimeout_Type = TimeTicks
_AlaIgmpMemberServiceSapTimeout_Object = MibTableColumn
alaIgmpMemberServiceSapTimeout = _AlaIgmpMemberServiceSapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 2, 1, 7),
    _AlaIgmpMemberServiceSapTimeout_Type()
)
alaIgmpMemberServiceSapTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSapTimeout.setStatus("current")
_AlaIgmpMemberServiceSdpBindTable_Object = MibTable
alaIgmpMemberServiceSdpBindTable = _AlaIgmpMemberServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSdpBindTable.setStatus("current")
_AlaIgmpMemberServiceSdpBindEntry_Object = MibTableRow
alaIgmpMemberServiceSdpBindEntry = _AlaIgmpMemberServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 3, 1)
)
alaIgmpMemberServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSdpBindGroupAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSdpBindGroupAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSdpBindSourceAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSdpBindSourceAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSdpBindEntry.setStatus("current")


class _AlaIgmpMemberServiceSdpBindGroupAddressType_Type(InetAddressType):
    """Custom type alaIgmpMemberServiceSdpBindGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpMemberServiceSdpBindGroupAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpMemberServiceSdpBindGroupAddressType_Object = MibTableColumn
alaIgmpMemberServiceSdpBindGroupAddressType = _AlaIgmpMemberServiceSdpBindGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 3, 1, 1),
    _AlaIgmpMemberServiceSdpBindGroupAddressType_Type()
)
alaIgmpMemberServiceSdpBindGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSdpBindGroupAddressType.setStatus("current")


class _AlaIgmpMemberServiceSdpBindGroupAddress_Type(InetAddress):
    """Custom type alaIgmpMemberServiceSdpBindGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpMemberServiceSdpBindGroupAddress_Type.__name__ = "InetAddress"
_AlaIgmpMemberServiceSdpBindGroupAddress_Object = MibTableColumn
alaIgmpMemberServiceSdpBindGroupAddress = _AlaIgmpMemberServiceSdpBindGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 3, 1, 2),
    _AlaIgmpMemberServiceSdpBindGroupAddress_Type()
)
alaIgmpMemberServiceSdpBindGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSdpBindGroupAddress.setStatus("current")


class _AlaIgmpMemberServiceSdpBindSourceAddressType_Type(InetAddressType):
    """Custom type alaIgmpMemberServiceSdpBindSourceAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpMemberServiceSdpBindSourceAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpMemberServiceSdpBindSourceAddressType_Object = MibTableColumn
alaIgmpMemberServiceSdpBindSourceAddressType = _AlaIgmpMemberServiceSdpBindSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 3, 1, 3),
    _AlaIgmpMemberServiceSdpBindSourceAddressType_Type()
)
alaIgmpMemberServiceSdpBindSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSdpBindSourceAddressType.setStatus("current")


class _AlaIgmpMemberServiceSdpBindSourceAddress_Type(InetAddress):
    """Custom type alaIgmpMemberServiceSdpBindSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpMemberServiceSdpBindSourceAddress_Type.__name__ = "InetAddress"
_AlaIgmpMemberServiceSdpBindSourceAddress_Object = MibTableColumn
alaIgmpMemberServiceSdpBindSourceAddress = _AlaIgmpMemberServiceSdpBindSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 3, 1, 4),
    _AlaIgmpMemberServiceSdpBindSourceAddress_Type()
)
alaIgmpMemberServiceSdpBindSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSdpBindSourceAddress.setStatus("current")


class _AlaIgmpMemberServiceSdpBindMode_Type(Integer32):
    """Custom type alaIgmpMemberServiceSdpBindMode based on Integer32"""
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


_AlaIgmpMemberServiceSdpBindMode_Type.__name__ = "Integer32"
_AlaIgmpMemberServiceSdpBindMode_Object = MibTableColumn
alaIgmpMemberServiceSdpBindMode = _AlaIgmpMemberServiceSdpBindMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 3, 1, 5),
    _AlaIgmpMemberServiceSdpBindMode_Type()
)
alaIgmpMemberServiceSdpBindMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSdpBindMode.setStatus("current")
_AlaIgmpMemberServiceSdpBindCount_Type = Counter32
_AlaIgmpMemberServiceSdpBindCount_Object = MibTableColumn
alaIgmpMemberServiceSdpBindCount = _AlaIgmpMemberServiceSdpBindCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 3, 1, 6),
    _AlaIgmpMemberServiceSdpBindCount_Type()
)
alaIgmpMemberServiceSdpBindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSdpBindCount.setStatus("current")
_AlaIgmpMemberServiceSdpBindTimeout_Type = TimeTicks
_AlaIgmpMemberServiceSdpBindTimeout_Object = MibTableColumn
alaIgmpMemberServiceSdpBindTimeout = _AlaIgmpMemberServiceSdpBindTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 3, 1, 7),
    _AlaIgmpMemberServiceSdpBindTimeout_Type()
)
alaIgmpMemberServiceSdpBindTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSdpBindTimeout.setStatus("current")
_AlaIgmpStaticMemberServiceSapTable_Object = MibTable
alaIgmpStaticMemberServiceSapTable = _AlaIgmpStaticMemberServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSapTable.setStatus("current")
_AlaIgmpStaticMemberServiceSapEntry_Object = MibTableRow
alaIgmpStaticMemberServiceSapEntry = _AlaIgmpStaticMemberServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 4, 1)
)
alaIgmpStaticMemberServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticMemberServiceSapGroupAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticMemberServiceSapGroupAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSapEntry.setStatus("current")


class _AlaIgmpStaticMemberServiceSapGroupAddressType_Type(InetAddressType):
    """Custom type alaIgmpStaticMemberServiceSapGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpStaticMemberServiceSapGroupAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpStaticMemberServiceSapGroupAddressType_Object = MibTableColumn
alaIgmpStaticMemberServiceSapGroupAddressType = _AlaIgmpStaticMemberServiceSapGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 4, 1, 1),
    _AlaIgmpStaticMemberServiceSapGroupAddressType_Type()
)
alaIgmpStaticMemberServiceSapGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSapGroupAddressType.setStatus("current")


class _AlaIgmpStaticMemberServiceSapGroupAddress_Type(InetAddress):
    """Custom type alaIgmpStaticMemberServiceSapGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpStaticMemberServiceSapGroupAddress_Type.__name__ = "InetAddress"
_AlaIgmpStaticMemberServiceSapGroupAddress_Object = MibTableColumn
alaIgmpStaticMemberServiceSapGroupAddress = _AlaIgmpStaticMemberServiceSapGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 4, 1, 2),
    _AlaIgmpStaticMemberServiceSapGroupAddress_Type()
)
alaIgmpStaticMemberServiceSapGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSapGroupAddress.setStatus("current")
_AlaIgmpStaticMemberServiceSapRowStatus_Type = RowStatus
_AlaIgmpStaticMemberServiceSapRowStatus_Object = MibTableColumn
alaIgmpStaticMemberServiceSapRowStatus = _AlaIgmpStaticMemberServiceSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 4, 1, 3),
    _AlaIgmpStaticMemberServiceSapRowStatus_Type()
)
alaIgmpStaticMemberServiceSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSapRowStatus.setStatus("current")
_AlaIgmpStaticMemberServiceSdpBindTable_Object = MibTable
alaIgmpStaticMemberServiceSdpBindTable = _AlaIgmpStaticMemberServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSdpBindTable.setStatus("current")
_AlaIgmpStaticMemberServiceSdpBindEntry_Object = MibTableRow
alaIgmpStaticMemberServiceSdpBindEntry = _AlaIgmpStaticMemberServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 5, 1)
)
alaIgmpStaticMemberServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticMemberServiceSdpBindGroupAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticMemberServiceSdpBindGroupAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSdpBindEntry.setStatus("current")


class _AlaIgmpStaticMemberServiceSdpBindGroupAddressType_Type(InetAddressType):
    """Custom type alaIgmpStaticMemberServiceSdpBindGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpStaticMemberServiceSdpBindGroupAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpStaticMemberServiceSdpBindGroupAddressType_Object = MibTableColumn
alaIgmpStaticMemberServiceSdpBindGroupAddressType = _AlaIgmpStaticMemberServiceSdpBindGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 5, 1, 1),
    _AlaIgmpStaticMemberServiceSdpBindGroupAddressType_Type()
)
alaIgmpStaticMemberServiceSdpBindGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSdpBindGroupAddressType.setStatus("current")


class _AlaIgmpStaticMemberServiceSdpBindGroupAddress_Type(InetAddress):
    """Custom type alaIgmpStaticMemberServiceSdpBindGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpStaticMemberServiceSdpBindGroupAddress_Type.__name__ = "InetAddress"
_AlaIgmpStaticMemberServiceSdpBindGroupAddress_Object = MibTableColumn
alaIgmpStaticMemberServiceSdpBindGroupAddress = _AlaIgmpStaticMemberServiceSdpBindGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 5, 1, 2),
    _AlaIgmpStaticMemberServiceSdpBindGroupAddress_Type()
)
alaIgmpStaticMemberServiceSdpBindGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSdpBindGroupAddress.setStatus("current")
_AlaIgmpStaticMemberServiceSdpBindRowStatus_Type = RowStatus
_AlaIgmpStaticMemberServiceSdpBindRowStatus_Object = MibTableColumn
alaIgmpStaticMemberServiceSdpBindRowStatus = _AlaIgmpStaticMemberServiceSdpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 5, 1, 3),
    _AlaIgmpStaticMemberServiceSdpBindRowStatus_Type()
)
alaIgmpStaticMemberServiceSdpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSdpBindRowStatus.setStatus("current")
_AlaIgmpNeighborServiceSapTable_Object = MibTable
alaIgmpNeighborServiceSapTable = _AlaIgmpNeighborServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSapTable.setStatus("current")
_AlaIgmpNeighborServiceSapEntry_Object = MibTableRow
alaIgmpNeighborServiceSapEntry = _AlaIgmpNeighborServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 6, 1)
)
alaIgmpNeighborServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpNeighborServiceSapHostAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpNeighborServiceSapHostAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSapEntry.setStatus("current")


class _AlaIgmpNeighborServiceSapHostAddressType_Type(InetAddressType):
    """Custom type alaIgmpNeighborServiceSapHostAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpNeighborServiceSapHostAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpNeighborServiceSapHostAddressType_Object = MibTableColumn
alaIgmpNeighborServiceSapHostAddressType = _AlaIgmpNeighborServiceSapHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 6, 1, 1),
    _AlaIgmpNeighborServiceSapHostAddressType_Type()
)
alaIgmpNeighborServiceSapHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSapHostAddressType.setStatus("current")


class _AlaIgmpNeighborServiceSapHostAddress_Type(InetAddress):
    """Custom type alaIgmpNeighborServiceSapHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpNeighborServiceSapHostAddress_Type.__name__ = "InetAddress"
_AlaIgmpNeighborServiceSapHostAddress_Object = MibTableColumn
alaIgmpNeighborServiceSapHostAddress = _AlaIgmpNeighborServiceSapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 6, 1, 2),
    _AlaIgmpNeighborServiceSapHostAddress_Type()
)
alaIgmpNeighborServiceSapHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSapHostAddress.setStatus("current")
_AlaIgmpNeighborServiceSapCount_Type = Counter32
_AlaIgmpNeighborServiceSapCount_Object = MibTableColumn
alaIgmpNeighborServiceSapCount = _AlaIgmpNeighborServiceSapCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 6, 1, 3),
    _AlaIgmpNeighborServiceSapCount_Type()
)
alaIgmpNeighborServiceSapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSapCount.setStatus("current")
_AlaIgmpNeighborServiceSapTimeout_Type = TimeTicks
_AlaIgmpNeighborServiceSapTimeout_Object = MibTableColumn
alaIgmpNeighborServiceSapTimeout = _AlaIgmpNeighborServiceSapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 6, 1, 4),
    _AlaIgmpNeighborServiceSapTimeout_Type()
)
alaIgmpNeighborServiceSapTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSapTimeout.setStatus("current")
_AlaIgmpNeighborServiceSdpBindTable_Object = MibTable
alaIgmpNeighborServiceSdpBindTable = _AlaIgmpNeighborServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSdpBindTable.setStatus("current")
_AlaIgmpNeighborServiceSdpBindEntry_Object = MibTableRow
alaIgmpNeighborServiceSdpBindEntry = _AlaIgmpNeighborServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 7, 1)
)
alaIgmpNeighborServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpNeighborServiceSdpBindHostAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpNeighborServiceSdpBindHostAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSdpBindEntry.setStatus("current")


class _AlaIgmpNeighborServiceSdpBindHostAddressType_Type(InetAddressType):
    """Custom type alaIgmpNeighborServiceSdpBindHostAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpNeighborServiceSdpBindHostAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpNeighborServiceSdpBindHostAddressType_Object = MibTableColumn
alaIgmpNeighborServiceSdpBindHostAddressType = _AlaIgmpNeighborServiceSdpBindHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 7, 1, 1),
    _AlaIgmpNeighborServiceSdpBindHostAddressType_Type()
)
alaIgmpNeighborServiceSdpBindHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSdpBindHostAddressType.setStatus("current")


class _AlaIgmpNeighborServiceSdpBindHostAddress_Type(InetAddress):
    """Custom type alaIgmpNeighborServiceSdpBindHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpNeighborServiceSdpBindHostAddress_Type.__name__ = "InetAddress"
_AlaIgmpNeighborServiceSdpBindHostAddress_Object = MibTableColumn
alaIgmpNeighborServiceSdpBindHostAddress = _AlaIgmpNeighborServiceSdpBindHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 7, 1, 2),
    _AlaIgmpNeighborServiceSdpBindHostAddress_Type()
)
alaIgmpNeighborServiceSdpBindHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSdpBindHostAddress.setStatus("current")
_AlaIgmpNeighborServiceSdpBindCount_Type = Counter32
_AlaIgmpNeighborServiceSdpBindCount_Object = MibTableColumn
alaIgmpNeighborServiceSdpBindCount = _AlaIgmpNeighborServiceSdpBindCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 7, 1, 3),
    _AlaIgmpNeighborServiceSdpBindCount_Type()
)
alaIgmpNeighborServiceSdpBindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSdpBindCount.setStatus("current")
_AlaIgmpNeighborServiceSdpBindTimeout_Type = TimeTicks
_AlaIgmpNeighborServiceSdpBindTimeout_Object = MibTableColumn
alaIgmpNeighborServiceSdpBindTimeout = _AlaIgmpNeighborServiceSdpBindTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 7, 1, 4),
    _AlaIgmpNeighborServiceSdpBindTimeout_Type()
)
alaIgmpNeighborServiceSdpBindTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSdpBindTimeout.setStatus("current")
_AlaIgmpStaticNeighborServiceSapTable_Object = MibTable
alaIgmpStaticNeighborServiceSapTable = _AlaIgmpStaticNeighborServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborServiceSapTable.setStatus("current")
_AlaIgmpStaticNeighborServiceSapEntry_Object = MibTableRow
alaIgmpStaticNeighborServiceSapEntry = _AlaIgmpStaticNeighborServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 8, 1)
)
alaIgmpStaticNeighborServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborServiceSapEntry.setStatus("current")
_AlaIgmpStaticNeighborServiceSapRowStatus_Type = RowStatus
_AlaIgmpStaticNeighborServiceSapRowStatus_Object = MibTableColumn
alaIgmpStaticNeighborServiceSapRowStatus = _AlaIgmpStaticNeighborServiceSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 8, 1, 1),
    _AlaIgmpStaticNeighborServiceSapRowStatus_Type()
)
alaIgmpStaticNeighborServiceSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborServiceSapRowStatus.setStatus("current")
_AlaIgmpStaticNeighborServiceSdpBindTable_Object = MibTable
alaIgmpStaticNeighborServiceSdpBindTable = _AlaIgmpStaticNeighborServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborServiceSdpBindTable.setStatus("current")
_AlaIgmpStaticNeighborServiceSdpBindEntry_Object = MibTableRow
alaIgmpStaticNeighborServiceSdpBindEntry = _AlaIgmpStaticNeighborServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 9, 1)
)
alaIgmpStaticNeighborServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborServiceSdpBindEntry.setStatus("current")
_AlaIgmpStaticNeighborServiceSdpBindRowStatus_Type = RowStatus
_AlaIgmpStaticNeighborServiceSdpBindRowStatus_Object = MibTableColumn
alaIgmpStaticNeighborServiceSdpBindRowStatus = _AlaIgmpStaticNeighborServiceSdpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 9, 1, 1),
    _AlaIgmpStaticNeighborServiceSdpBindRowStatus_Type()
)
alaIgmpStaticNeighborServiceSdpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborServiceSdpBindRowStatus.setStatus("current")
_AlaIgmpQuerierServiceSapTable_Object = MibTable
alaIgmpQuerierServiceSapTable = _AlaIgmpQuerierServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSapTable.setStatus("current")
_AlaIgmpQuerierServiceSapEntry_Object = MibTableRow
alaIgmpQuerierServiceSapEntry = _AlaIgmpQuerierServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 10, 1)
)
alaIgmpQuerierServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpQuerierServiceSapHostAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpQuerierServiceSapHostAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSapEntry.setStatus("current")


class _AlaIgmpQuerierServiceSapHostAddressType_Type(InetAddressType):
    """Custom type alaIgmpQuerierServiceSapHostAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpQuerierServiceSapHostAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpQuerierServiceSapHostAddressType_Object = MibTableColumn
alaIgmpQuerierServiceSapHostAddressType = _AlaIgmpQuerierServiceSapHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 10, 1, 1),
    _AlaIgmpQuerierServiceSapHostAddressType_Type()
)
alaIgmpQuerierServiceSapHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSapHostAddressType.setStatus("current")


class _AlaIgmpQuerierServiceSapHostAddress_Type(InetAddress):
    """Custom type alaIgmpQuerierServiceSapHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpQuerierServiceSapHostAddress_Type.__name__ = "InetAddress"
_AlaIgmpQuerierServiceSapHostAddress_Object = MibTableColumn
alaIgmpQuerierServiceSapHostAddress = _AlaIgmpQuerierServiceSapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 10, 1, 2),
    _AlaIgmpQuerierServiceSapHostAddress_Type()
)
alaIgmpQuerierServiceSapHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSapHostAddress.setStatus("current")
_AlaIgmpQuerierServiceSapCount_Type = Counter32
_AlaIgmpQuerierServiceSapCount_Object = MibTableColumn
alaIgmpQuerierServiceSapCount = _AlaIgmpQuerierServiceSapCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 10, 1, 3),
    _AlaIgmpQuerierServiceSapCount_Type()
)
alaIgmpQuerierServiceSapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSapCount.setStatus("current")
_AlaIgmpQuerierServiceSapTimeout_Type = TimeTicks
_AlaIgmpQuerierServiceSapTimeout_Object = MibTableColumn
alaIgmpQuerierServiceSapTimeout = _AlaIgmpQuerierServiceSapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 10, 1, 4),
    _AlaIgmpQuerierServiceSapTimeout_Type()
)
alaIgmpQuerierServiceSapTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSapTimeout.setStatus("current")
_AlaIgmpQuerierServiceSdpBindTable_Object = MibTable
alaIgmpQuerierServiceSdpBindTable = _AlaIgmpQuerierServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 11)
)
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSdpBindTable.setStatus("current")
_AlaIgmpQuerierServiceSdpBindEntry_Object = MibTableRow
alaIgmpQuerierServiceSdpBindEntry = _AlaIgmpQuerierServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 11, 1)
)
alaIgmpQuerierServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpQuerierServiceSdpBindHostAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpQuerierServiceSdpBindHostAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSdpBindEntry.setStatus("current")


class _AlaIgmpQuerierServiceSdpBindHostAddressType_Type(InetAddressType):
    """Custom type alaIgmpQuerierServiceSdpBindHostAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpQuerierServiceSdpBindHostAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpQuerierServiceSdpBindHostAddressType_Object = MibTableColumn
alaIgmpQuerierServiceSdpBindHostAddressType = _AlaIgmpQuerierServiceSdpBindHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 11, 1, 1),
    _AlaIgmpQuerierServiceSdpBindHostAddressType_Type()
)
alaIgmpQuerierServiceSdpBindHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSdpBindHostAddressType.setStatus("current")


class _AlaIgmpQuerierServiceSdpBindHostAddress_Type(InetAddress):
    """Custom type alaIgmpQuerierServiceSdpBindHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpQuerierServiceSdpBindHostAddress_Type.__name__ = "InetAddress"
_AlaIgmpQuerierServiceSdpBindHostAddress_Object = MibTableColumn
alaIgmpQuerierServiceSdpBindHostAddress = _AlaIgmpQuerierServiceSdpBindHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 11, 1, 2),
    _AlaIgmpQuerierServiceSdpBindHostAddress_Type()
)
alaIgmpQuerierServiceSdpBindHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSdpBindHostAddress.setStatus("current")
_AlaIgmpQuerierServiceSdpBindCount_Type = Counter32
_AlaIgmpQuerierServiceSdpBindCount_Object = MibTableColumn
alaIgmpQuerierServiceSdpBindCount = _AlaIgmpQuerierServiceSdpBindCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 11, 1, 3),
    _AlaIgmpQuerierServiceSdpBindCount_Type()
)
alaIgmpQuerierServiceSdpBindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSdpBindCount.setStatus("current")
_AlaIgmpQuerierServiceSdpBindTimeout_Type = TimeTicks
_AlaIgmpQuerierServiceSdpBindTimeout_Object = MibTableColumn
alaIgmpQuerierServiceSdpBindTimeout = _AlaIgmpQuerierServiceSdpBindTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 11, 1, 4),
    _AlaIgmpQuerierServiceSdpBindTimeout_Type()
)
alaIgmpQuerierServiceSdpBindTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSdpBindTimeout.setStatus("current")
_AlaIgmpStaticQuerierServiceSapTable_Object = MibTable
alaIgmpStaticQuerierServiceSapTable = _AlaIgmpStaticQuerierServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierServiceSapTable.setStatus("current")
_AlaIgmpStaticQuerierServiceSapEntry_Object = MibTableRow
alaIgmpStaticQuerierServiceSapEntry = _AlaIgmpStaticQuerierServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 12, 1)
)
alaIgmpStaticQuerierServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierServiceSapEntry.setStatus("current")
_AlaIgmpStaticQuerierServiceSapRowStatus_Type = RowStatus
_AlaIgmpStaticQuerierServiceSapRowStatus_Object = MibTableColumn
alaIgmpStaticQuerierServiceSapRowStatus = _AlaIgmpStaticQuerierServiceSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 12, 1, 1),
    _AlaIgmpStaticQuerierServiceSapRowStatus_Type()
)
alaIgmpStaticQuerierServiceSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierServiceSapRowStatus.setStatus("current")
_AlaIgmpStaticQuerierServiceSdpBindTable_Object = MibTable
alaIgmpStaticQuerierServiceSdpBindTable = _AlaIgmpStaticQuerierServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 13)
)
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierServiceSdpBindTable.setStatus("current")
_AlaIgmpStaticQuerierServiceSdpBindEntry_Object = MibTableRow
alaIgmpStaticQuerierServiceSdpBindEntry = _AlaIgmpStaticQuerierServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 13, 1)
)
alaIgmpStaticQuerierServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierServiceSdpBindEntry.setStatus("current")
_AlaIgmpStaticQuerierServiceSdpBindRowStatus_Type = RowStatus
_AlaIgmpStaticQuerierServiceSdpBindRowStatus_Object = MibTableColumn
alaIgmpStaticQuerierServiceSdpBindRowStatus = _AlaIgmpStaticQuerierServiceSdpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 13, 1, 1),
    _AlaIgmpStaticQuerierServiceSdpBindRowStatus_Type()
)
alaIgmpStaticQuerierServiceSdpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierServiceSdpBindRowStatus.setStatus("current")
_AlaIgmpServiceSourceTable_Object = MibTable
alaIgmpServiceSourceTable = _AlaIgmpServiceSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    alaIgmpServiceSourceTable.setStatus("current")
_AlaIgmpServiceSourceEntry_Object = MibTableRow
alaIgmpServiceSourceEntry = _AlaIgmpServiceSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1)
)
alaIgmpServiceSourceEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceGroupAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceGroupAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceHostAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceHostAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceDestAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceDestAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceOrigAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceOrigAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpServiceSourceEntry.setStatus("current")


class _AlaIgmpServiceSourceGroupAddressType_Type(InetAddressType):
    """Custom type alaIgmpServiceSourceGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpServiceSourceGroupAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpServiceSourceGroupAddressType_Object = MibTableColumn
alaIgmpServiceSourceGroupAddressType = _AlaIgmpServiceSourceGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 1),
    _AlaIgmpServiceSourceGroupAddressType_Type()
)
alaIgmpServiceSourceGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceGroupAddressType.setStatus("current")


class _AlaIgmpServiceSourceGroupAddress_Type(InetAddress):
    """Custom type alaIgmpServiceSourceGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpServiceSourceGroupAddress_Type.__name__ = "InetAddress"
_AlaIgmpServiceSourceGroupAddress_Object = MibTableColumn
alaIgmpServiceSourceGroupAddress = _AlaIgmpServiceSourceGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 2),
    _AlaIgmpServiceSourceGroupAddress_Type()
)
alaIgmpServiceSourceGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceGroupAddress.setStatus("current")


class _AlaIgmpServiceSourceHostAddressType_Type(InetAddressType):
    """Custom type alaIgmpServiceSourceHostAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpServiceSourceHostAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpServiceSourceHostAddressType_Object = MibTableColumn
alaIgmpServiceSourceHostAddressType = _AlaIgmpServiceSourceHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 3),
    _AlaIgmpServiceSourceHostAddressType_Type()
)
alaIgmpServiceSourceHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceHostAddressType.setStatus("current")


class _AlaIgmpServiceSourceHostAddress_Type(InetAddress):
    """Custom type alaIgmpServiceSourceHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpServiceSourceHostAddress_Type.__name__ = "InetAddress"
_AlaIgmpServiceSourceHostAddress_Object = MibTableColumn
alaIgmpServiceSourceHostAddress = _AlaIgmpServiceSourceHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 4),
    _AlaIgmpServiceSourceHostAddress_Type()
)
alaIgmpServiceSourceHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceHostAddress.setStatus("current")


class _AlaIgmpServiceSourceDestAddressType_Type(InetAddressType):
    """Custom type alaIgmpServiceSourceDestAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpServiceSourceDestAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpServiceSourceDestAddressType_Object = MibTableColumn
alaIgmpServiceSourceDestAddressType = _AlaIgmpServiceSourceDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 5),
    _AlaIgmpServiceSourceDestAddressType_Type()
)
alaIgmpServiceSourceDestAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceDestAddressType.setStatus("current")


class _AlaIgmpServiceSourceDestAddress_Type(InetAddress):
    """Custom type alaIgmpServiceSourceDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpServiceSourceDestAddress_Type.__name__ = "InetAddress"
_AlaIgmpServiceSourceDestAddress_Object = MibTableColumn
alaIgmpServiceSourceDestAddress = _AlaIgmpServiceSourceDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 6),
    _AlaIgmpServiceSourceDestAddress_Type()
)
alaIgmpServiceSourceDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceDestAddress.setStatus("current")


class _AlaIgmpServiceSourceOrigAddressType_Type(InetAddressType):
    """Custom type alaIgmpServiceSourceOrigAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpServiceSourceOrigAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpServiceSourceOrigAddressType_Object = MibTableColumn
alaIgmpServiceSourceOrigAddressType = _AlaIgmpServiceSourceOrigAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 7),
    _AlaIgmpServiceSourceOrigAddressType_Type()
)
alaIgmpServiceSourceOrigAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceOrigAddressType.setStatus("current")


class _AlaIgmpServiceSourceOrigAddress_Type(InetAddress):
    """Custom type alaIgmpServiceSourceOrigAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaIgmpServiceSourceOrigAddress_Type.__name__ = "InetAddress"
_AlaIgmpServiceSourceOrigAddress_Object = MibTableColumn
alaIgmpServiceSourceOrigAddress = _AlaIgmpServiceSourceOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 8),
    _AlaIgmpServiceSourceOrigAddress_Type()
)
alaIgmpServiceSourceOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceOrigAddress.setStatus("current")
_AlaIgmpServiceSourceLocale_Type = AluLocation
_AlaIgmpServiceSourceLocale_Object = MibTableColumn
alaIgmpServiceSourceLocale = _AlaIgmpServiceSourceLocale_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 9),
    _AlaIgmpServiceSourceLocale_Type()
)
alaIgmpServiceSourceLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceLocale.setStatus("current")
_AlaIgmpServiceSourcePortId_Type = TmnxPortID
_AlaIgmpServiceSourcePortId_Object = MibTableColumn
alaIgmpServiceSourcePortId = _AlaIgmpServiceSourcePortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 10),
    _AlaIgmpServiceSourcePortId_Type()
)
alaIgmpServiceSourcePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSourcePortId.setStatus("current")
_AlaIgmpServiceSourceEncapValue_Type = TmnxEncapVal
_AlaIgmpServiceSourceEncapValue_Object = MibTableColumn
alaIgmpServiceSourceEncapValue = _AlaIgmpServiceSourceEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 11),
    _AlaIgmpServiceSourceEncapValue_Type()
)
alaIgmpServiceSourceEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceEncapValue.setStatus("current")
_AlaIgmpServiceSourceSdpId_Type = SdpId
_AlaIgmpServiceSourceSdpId_Object = MibTableColumn
alaIgmpServiceSourceSdpId = _AlaIgmpServiceSourceSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 12),
    _AlaIgmpServiceSourceSdpId_Type()
)
alaIgmpServiceSourceSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceSdpId.setStatus("current")
_AlaIgmpServiceSourceVcId_Type = TmnxVcIdOrNone
_AlaIgmpServiceSourceVcId_Object = MibTableColumn
alaIgmpServiceSourceVcId = _AlaIgmpServiceSourceVcId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 13),
    _AlaIgmpServiceSourceVcId_Type()
)
alaIgmpServiceSourceVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceVcId.setStatus("current")


class _AlaIgmpServiceSourceType_Type(Integer32):
    """Custom type alaIgmpServiceSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpServiceSourceType_Type.__name__ = "Integer32"
_AlaIgmpServiceSourceType_Object = MibTableColumn
alaIgmpServiceSourceType = _AlaIgmpServiceSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 14, 1, 14),
    _AlaIgmpServiceSourceType_Type()
)
alaIgmpServiceSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSourceType.setStatus("current")
_AlaIgmpServiceSapForwardTable_Object = MibTable
alaIgmpServiceSapForwardTable = _AlaIgmpServiceSapForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardTable.setStatus("current")
_AlaIgmpServiceSapForwardEntry_Object = MibTableRow
alaIgmpServiceSapForwardEntry = _AlaIgmpServiceSapForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1)
)
alaIgmpServiceSapForwardEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardGroupAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardHostAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardDestAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardOrigAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardNextSapPortId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardNextSapEncapValue"),
)
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardEntry.setStatus("current")
_AlaIgmpServiceSapForwardLocale_Type = AluLocation
_AlaIgmpServiceSapForwardLocale_Object = MibTableColumn
alaIgmpServiceSapForwardLocale = _AlaIgmpServiceSapForwardLocale_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 1),
    _AlaIgmpServiceSapForwardLocale_Type()
)
alaIgmpServiceSapForwardLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardLocale.setStatus("current")
_AlaIgmpServiceSapForwardPortId_Type = TmnxPortID
_AlaIgmpServiceSapForwardPortId_Object = MibTableColumn
alaIgmpServiceSapForwardPortId = _AlaIgmpServiceSapForwardPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 2),
    _AlaIgmpServiceSapForwardPortId_Type()
)
alaIgmpServiceSapForwardPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardPortId.setStatus("current")
_AlaIgmpServiceSapForwardEncapValue_Type = TmnxEncapVal
_AlaIgmpServiceSapForwardEncapValue_Object = MibTableColumn
alaIgmpServiceSapForwardEncapValue = _AlaIgmpServiceSapForwardEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 3),
    _AlaIgmpServiceSapForwardEncapValue_Type()
)
alaIgmpServiceSapForwardEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardEncapValue.setStatus("current")
_AlaIgmpServiceSapForwardSdpId_Type = SdpId
_AlaIgmpServiceSapForwardSdpId_Object = MibTableColumn
alaIgmpServiceSapForwardSdpId = _AlaIgmpServiceSapForwardSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 4),
    _AlaIgmpServiceSapForwardSdpId_Type()
)
alaIgmpServiceSapForwardSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardSdpId.setStatus("current")
_AlaIgmpServiceSapForwardVcId_Type = TmnxVcIdOrNone
_AlaIgmpServiceSapForwardVcId_Object = MibTableColumn
alaIgmpServiceSapForwardVcId = _AlaIgmpServiceSapForwardVcId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 5),
    _AlaIgmpServiceSapForwardVcId_Type()
)
alaIgmpServiceSapForwardVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardVcId.setStatus("current")
_AlaIgmpServiceSapForwardGroupAddress_Type = MacAddress
_AlaIgmpServiceSapForwardGroupAddress_Object = MibTableColumn
alaIgmpServiceSapForwardGroupAddress = _AlaIgmpServiceSapForwardGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 6),
    _AlaIgmpServiceSapForwardGroupAddress_Type()
)
alaIgmpServiceSapForwardGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardGroupAddress.setStatus("current")
_AlaIgmpServiceSapForwardHostAddress_Type = MacAddress
_AlaIgmpServiceSapForwardHostAddress_Object = MibTableColumn
alaIgmpServiceSapForwardHostAddress = _AlaIgmpServiceSapForwardHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 7),
    _AlaIgmpServiceSapForwardHostAddress_Type()
)
alaIgmpServiceSapForwardHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardHostAddress.setStatus("current")
_AlaIgmpServiceSapForwardDestAddress_Type = MacAddress
_AlaIgmpServiceSapForwardDestAddress_Object = MibTableColumn
alaIgmpServiceSapForwardDestAddress = _AlaIgmpServiceSapForwardDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 8),
    _AlaIgmpServiceSapForwardDestAddress_Type()
)
alaIgmpServiceSapForwardDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardDestAddress.setStatus("current")
_AlaIgmpServiceSapForwardOrigAddress_Type = MacAddress
_AlaIgmpServiceSapForwardOrigAddress_Object = MibTableColumn
alaIgmpServiceSapForwardOrigAddress = _AlaIgmpServiceSapForwardOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 9),
    _AlaIgmpServiceSapForwardOrigAddress_Type()
)
alaIgmpServiceSapForwardOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardOrigAddress.setStatus("current")


class _AlaIgmpServiceSapForwardType_Type(Integer32):
    """Custom type alaIgmpServiceSapForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpServiceSapForwardType_Type.__name__ = "Integer32"
_AlaIgmpServiceSapForwardType_Object = MibTableColumn
alaIgmpServiceSapForwardType = _AlaIgmpServiceSapForwardType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 10),
    _AlaIgmpServiceSapForwardType_Type()
)
alaIgmpServiceSapForwardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardType.setStatus("current")
_AlaIgmpServiceSapForwardNextSapPortId_Type = TmnxPortID
_AlaIgmpServiceSapForwardNextSapPortId_Object = MibTableColumn
alaIgmpServiceSapForwardNextSapPortId = _AlaIgmpServiceSapForwardNextSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 11),
    _AlaIgmpServiceSapForwardNextSapPortId_Type()
)
alaIgmpServiceSapForwardNextSapPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardNextSapPortId.setStatus("current")
_AlaIgmpServiceSapForwardNextSapEncapValue_Type = TmnxEncapVal
_AlaIgmpServiceSapForwardNextSapEncapValue_Object = MibTableColumn
alaIgmpServiceSapForwardNextSapEncapValue = _AlaIgmpServiceSapForwardNextSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 12),
    _AlaIgmpServiceSapForwardNextSapEncapValue_Type()
)
alaIgmpServiceSapForwardNextSapEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardNextSapEncapValue.setStatus("current")


class _AlaIgmpServiceSapForwardNextType_Type(Integer32):
    """Custom type alaIgmpServiceSapForwardNextType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpServiceSapForwardNextType_Type.__name__ = "Integer32"
_AlaIgmpServiceSapForwardNextType_Object = MibTableColumn
alaIgmpServiceSapForwardNextType = _AlaIgmpServiceSapForwardNextType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 15, 1, 13),
    _AlaIgmpServiceSapForwardNextType_Type()
)
alaIgmpServiceSapForwardNextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardNextType.setStatus("current")
_AlaIgmpServiceSdpBindForwardTable_Object = MibTable
alaIgmpServiceSdpBindForwardTable = _AlaIgmpServiceSdpBindForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16)
)
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardTable.setStatus("current")
_AlaIgmpServiceSdpBindForwardEntry_Object = MibTableRow
alaIgmpServiceSdpBindForwardEntry = _AlaIgmpServiceSdpBindForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1)
)
alaIgmpServiceSdpBindForwardEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardGroupAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardHostAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardDestAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardOrigAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardNextSdpBindId"),
)
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardEntry.setStatus("current")
_AlaIgmpServiceSdpBindForwardLocale_Type = AluLocation
_AlaIgmpServiceSdpBindForwardLocale_Object = MibTableColumn
alaIgmpServiceSdpBindForwardLocale = _AlaIgmpServiceSdpBindForwardLocale_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 1),
    _AlaIgmpServiceSdpBindForwardLocale_Type()
)
alaIgmpServiceSdpBindForwardLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardLocale.setStatus("current")
_AlaIgmpServiceSdpBindForwardPortId_Type = TmnxPortID
_AlaIgmpServiceSdpBindForwardPortId_Object = MibTableColumn
alaIgmpServiceSdpBindForwardPortId = _AlaIgmpServiceSdpBindForwardPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 2),
    _AlaIgmpServiceSdpBindForwardPortId_Type()
)
alaIgmpServiceSdpBindForwardPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardPortId.setStatus("current")
_AlaIgmpServiceSdpBindForwardEncapValue_Type = TmnxEncapVal
_AlaIgmpServiceSdpBindForwardEncapValue_Object = MibTableColumn
alaIgmpServiceSdpBindForwardEncapValue = _AlaIgmpServiceSdpBindForwardEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 3),
    _AlaIgmpServiceSdpBindForwardEncapValue_Type()
)
alaIgmpServiceSdpBindForwardEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardEncapValue.setStatus("current")
_AlaIgmpServiceSdpBindForwardSdpId_Type = SdpId
_AlaIgmpServiceSdpBindForwardSdpId_Object = MibTableColumn
alaIgmpServiceSdpBindForwardSdpId = _AlaIgmpServiceSdpBindForwardSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 4),
    _AlaIgmpServiceSdpBindForwardSdpId_Type()
)
alaIgmpServiceSdpBindForwardSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardSdpId.setStatus("current")
_AlaIgmpServiceSdpBindForwardVcId_Type = TmnxVcIdOrNone
_AlaIgmpServiceSdpBindForwardVcId_Object = MibTableColumn
alaIgmpServiceSdpBindForwardVcId = _AlaIgmpServiceSdpBindForwardVcId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 5),
    _AlaIgmpServiceSdpBindForwardVcId_Type()
)
alaIgmpServiceSdpBindForwardVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardVcId.setStatus("current")
_AlaIgmpServiceSdpBindForwardGroupAddress_Type = MacAddress
_AlaIgmpServiceSdpBindForwardGroupAddress_Object = MibTableColumn
alaIgmpServiceSdpBindForwardGroupAddress = _AlaIgmpServiceSdpBindForwardGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 6),
    _AlaIgmpServiceSdpBindForwardGroupAddress_Type()
)
alaIgmpServiceSdpBindForwardGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardGroupAddress.setStatus("current")
_AlaIgmpServiceSdpBindForwardHostAddress_Type = MacAddress
_AlaIgmpServiceSdpBindForwardHostAddress_Object = MibTableColumn
alaIgmpServiceSdpBindForwardHostAddress = _AlaIgmpServiceSdpBindForwardHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 7),
    _AlaIgmpServiceSdpBindForwardHostAddress_Type()
)
alaIgmpServiceSdpBindForwardHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardHostAddress.setStatus("current")
_AlaIgmpServiceSdpBindForwardDestAddress_Type = MacAddress
_AlaIgmpServiceSdpBindForwardDestAddress_Object = MibTableColumn
alaIgmpServiceSdpBindForwardDestAddress = _AlaIgmpServiceSdpBindForwardDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 8),
    _AlaIgmpServiceSdpBindForwardDestAddress_Type()
)
alaIgmpServiceSdpBindForwardDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardDestAddress.setStatus("current")
_AlaIgmpServiceSdpBindForwardOrigAddress_Type = MacAddress
_AlaIgmpServiceSdpBindForwardOrigAddress_Object = MibTableColumn
alaIgmpServiceSdpBindForwardOrigAddress = _AlaIgmpServiceSdpBindForwardOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 9),
    _AlaIgmpServiceSdpBindForwardOrigAddress_Type()
)
alaIgmpServiceSdpBindForwardOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardOrigAddress.setStatus("current")


class _AlaIgmpServiceSdpBindForwardType_Type(Integer32):
    """Custom type alaIgmpServiceSdpBindForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpServiceSdpBindForwardType_Type.__name__ = "Integer32"
_AlaIgmpServiceSdpBindForwardType_Object = MibTableColumn
alaIgmpServiceSdpBindForwardType = _AlaIgmpServiceSdpBindForwardType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 10),
    _AlaIgmpServiceSdpBindForwardType_Type()
)
alaIgmpServiceSdpBindForwardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardType.setStatus("current")
_AlaIgmpServiceSdpBindForwardNextSdpBindId_Type = SdpBindId
_AlaIgmpServiceSdpBindForwardNextSdpBindId_Object = MibTableColumn
alaIgmpServiceSdpBindForwardNextSdpBindId = _AlaIgmpServiceSdpBindForwardNextSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 11),
    _AlaIgmpServiceSdpBindForwardNextSdpBindId_Type()
)
alaIgmpServiceSdpBindForwardNextSdpBindId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardNextSdpBindId.setStatus("current")


class _AlaIgmpServiceSdpBindForwardNextType_Type(Integer32):
    """Custom type alaIgmpServiceSdpBindForwardNextType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpServiceSdpBindForwardNextType_Type.__name__ = "Integer32"
_AlaIgmpServiceSdpBindForwardNextType_Object = MibTableColumn
alaIgmpServiceSdpBindForwardNextType = _AlaIgmpServiceSdpBindForwardNextType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 16, 1, 12),
    _AlaIgmpServiceSdpBindForwardNextType_Type()
)
alaIgmpServiceSdpBindForwardNextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardNextType.setStatus("current")
_AlaIgmpServiceSapTable_Object = MibTable
alaIgmpServiceSapTable = _AlaIgmpServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 17)
)
if mibBuilder.loadTexts:
    alaIgmpServiceSapTable.setStatus("current")
_AlaIgmpServiceSapEntry_Object = MibTableRow
alaIgmpServiceSapEntry = _AlaIgmpServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 17, 1)
)
alaIgmpServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    alaIgmpServiceSapEntry.setStatus("current")


class _AlaIgmpServiceSapMaxGroupLimit_Type(Unsigned32):
    """Custom type alaIgmpServiceSapMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaIgmpServiceSapMaxGroupLimit_Type.__name__ = "Unsigned32"
_AlaIgmpServiceSapMaxGroupLimit_Object = MibTableColumn
alaIgmpServiceSapMaxGroupLimit = _AlaIgmpServiceSapMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 17, 1, 1),
    _AlaIgmpServiceSapMaxGroupLimit_Type()
)
alaIgmpServiceSapMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceSapMaxGroupLimit.setStatus("current")


class _AlaIgmpServiceSapMaxGroupExceedAction_Type(Integer32):
    """Custom type alaIgmpServiceSapMaxGroupExceedAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("drop", 1),
          ("replace", 2))
    )


_AlaIgmpServiceSapMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaIgmpServiceSapMaxGroupExceedAction_Object = MibTableColumn
alaIgmpServiceSapMaxGroupExceedAction = _AlaIgmpServiceSapMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 17, 1, 2),
    _AlaIgmpServiceSapMaxGroupExceedAction_Type()
)
alaIgmpServiceSapMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceSapMaxGroupExceedAction.setStatus("current")
_AlaIgmpServiceSapCurrentGroupCount_Type = Unsigned32
_AlaIgmpServiceSapCurrentGroupCount_Object = MibTableColumn
alaIgmpServiceSapCurrentGroupCount = _AlaIgmpServiceSapCurrentGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 17, 1, 3),
    _AlaIgmpServiceSapCurrentGroupCount_Type()
)
alaIgmpServiceSapCurrentGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSapCurrentGroupCount.setStatus("current")
_AlaIgmpServiceSdpBindTable_Object = MibTable
alaIgmpServiceSdpBindTable = _AlaIgmpServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 18)
)
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindTable.setStatus("current")
_AlaIgmpServiceSdpBindEntry_Object = MibTableRow
alaIgmpServiceSdpBindEntry = _AlaIgmpServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 18, 1)
)
alaIgmpServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindEntry.setStatus("current")


class _AlaIgmpServiceSdpBindMaxGroupLimit_Type(Unsigned32):
    """Custom type alaIgmpServiceSdpBindMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaIgmpServiceSdpBindMaxGroupLimit_Type.__name__ = "Unsigned32"
_AlaIgmpServiceSdpBindMaxGroupLimit_Object = MibTableColumn
alaIgmpServiceSdpBindMaxGroupLimit = _AlaIgmpServiceSdpBindMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 18, 1, 1),
    _AlaIgmpServiceSdpBindMaxGroupLimit_Type()
)
alaIgmpServiceSdpBindMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindMaxGroupLimit.setStatus("current")


class _AlaIgmpServiceSdpBindMaxGroupExceedAction_Type(Integer32):
    """Custom type alaIgmpServiceSdpBindMaxGroupExceedAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("drop", 1),
          ("replace", 2))
    )


_AlaIgmpServiceSdpBindMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaIgmpServiceSdpBindMaxGroupExceedAction_Object = MibTableColumn
alaIgmpServiceSdpBindMaxGroupExceedAction = _AlaIgmpServiceSdpBindMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 18, 1, 2),
    _AlaIgmpServiceSdpBindMaxGroupExceedAction_Type()
)
alaIgmpServiceSdpBindMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindMaxGroupExceedAction.setStatus("current")
_AlaIgmpServiceSdpBindCurrentGroupCount_Type = Unsigned32
_AlaIgmpServiceSdpBindCurrentGroupCount_Object = MibTableColumn
alaIgmpServiceSdpBindCurrentGroupCount = _AlaIgmpServiceSdpBindCurrentGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 2, 18, 1, 3),
    _AlaIgmpServiceSdpBindCurrentGroupCount_Type()
)
alaIgmpServiceSdpBindCurrentGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindCurrentGroupCount.setStatus("current")
_AlaServiceMgrMld_ObjectIdentity = ObjectIdentity
alaServiceMgrMld = _AlaServiceMgrMld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3)
)
_AlaMldServiceTable_Object = MibTable
alaMldServiceTable = _AlaMldServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaMldServiceTable.setStatus("current")
_AlaMldServiceEntry_Object = MibTableRow
alaMldServiceEntry = _AlaMldServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1)
)
alaMldServiceEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    alaMldServiceEntry.setStatus("current")


class _AlaMldServiceStatus_Type(Integer32):
    """Custom type alaMldServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaMldServiceStatus_Type.__name__ = "Integer32"
_AlaMldServiceStatus_Object = MibTableColumn
alaMldServiceStatus = _AlaMldServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 1),
    _AlaMldServiceStatus_Type()
)
alaMldServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceStatus.setStatus("current")


class _AlaMldServiceQuerying_Type(Integer32):
    """Custom type alaMldServiceQuerying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaMldServiceQuerying_Type.__name__ = "Integer32"
_AlaMldServiceQuerying_Object = MibTableColumn
alaMldServiceQuerying = _AlaMldServiceQuerying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 2),
    _AlaMldServiceQuerying_Type()
)
alaMldServiceQuerying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceQuerying.setStatus("current")


class _AlaMldServiceSpoofing_Type(Integer32):
    """Custom type alaMldServiceSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaMldServiceSpoofing_Type.__name__ = "Integer32"
_AlaMldServiceSpoofing_Object = MibTableColumn
alaMldServiceSpoofing = _AlaMldServiceSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 3),
    _AlaMldServiceSpoofing_Type()
)
alaMldServiceSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceSpoofing.setStatus("current")


class _AlaMldServiceZapping_Type(Integer32):
    """Custom type alaMldServiceZapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaMldServiceZapping_Type.__name__ = "Integer32"
_AlaMldServiceZapping_Object = MibTableColumn
alaMldServiceZapping = _AlaMldServiceZapping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 4),
    _AlaMldServiceZapping_Type()
)
alaMldServiceZapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceZapping.setStatus("current")
_AlaMldServiceVersion_Type = Unsigned32
_AlaMldServiceVersion_Object = MibTableColumn
alaMldServiceVersion = _AlaMldServiceVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 5),
    _AlaMldServiceVersion_Type()
)
alaMldServiceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceVersion.setStatus("current")
_AlaMldServiceRobustness_Type = Unsigned32
_AlaMldServiceRobustness_Object = MibTableColumn
alaMldServiceRobustness = _AlaMldServiceRobustness_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 6),
    _AlaMldServiceRobustness_Type()
)
alaMldServiceRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceRobustness.setStatus("current")
_AlaMldServiceQueryInterval_Type = Unsigned32
_AlaMldServiceQueryInterval_Object = MibTableColumn
alaMldServiceQueryInterval = _AlaMldServiceQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 7),
    _AlaMldServiceQueryInterval_Type()
)
alaMldServiceQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldServiceQueryInterval.setUnits("seconds")
_AlaMldServiceQueryResponseInterval_Type = Unsigned32
_AlaMldServiceQueryResponseInterval_Object = MibTableColumn
alaMldServiceQueryResponseInterval = _AlaMldServiceQueryResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 8),
    _AlaMldServiceQueryResponseInterval_Type()
)
alaMldServiceQueryResponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceQueryResponseInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldServiceQueryResponseInterval.setUnits("tenths of seconds")
_AlaMldServiceLastMemberQueryInterval_Type = Unsigned32
_AlaMldServiceLastMemberQueryInterval_Object = MibTableColumn
alaMldServiceLastMemberQueryInterval = _AlaMldServiceLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 9),
    _AlaMldServiceLastMemberQueryInterval_Type()
)
alaMldServiceLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldServiceLastMemberQueryInterval.setUnits("tenths of seconds")
_AlaMldServiceRouterTimeout_Type = Unsigned32
_AlaMldServiceRouterTimeout_Object = MibTableColumn
alaMldServiceRouterTimeout = _AlaMldServiceRouterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 10),
    _AlaMldServiceRouterTimeout_Type()
)
alaMldServiceRouterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceRouterTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaMldServiceRouterTimeout.setUnits("seconds")
_AlaMldServiceSourceTimeout_Type = Unsigned32
_AlaMldServiceSourceTimeout_Object = MibTableColumn
alaMldServiceSourceTimeout = _AlaMldServiceSourceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 11),
    _AlaMldServiceSourceTimeout_Type()
)
alaMldServiceSourceTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceSourceTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaMldServiceSourceTimeout.setUnits("seconds")


class _AlaMldServiceProxying_Type(Integer32):
    """Custom type alaMldServiceProxying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaMldServiceProxying_Type.__name__ = "Integer32"
_AlaMldServiceProxying_Object = MibTableColumn
alaMldServiceProxying = _AlaMldServiceProxying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 12),
    _AlaMldServiceProxying_Type()
)
alaMldServiceProxying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceProxying.setStatus("current")
_AlaMldServiceUnsolicitedReportInterval_Type = Unsigned32
_AlaMldServiceUnsolicitedReportInterval_Object = MibTableColumn
alaMldServiceUnsolicitedReportInterval = _AlaMldServiceUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 13),
    _AlaMldServiceUnsolicitedReportInterval_Type()
)
alaMldServiceUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceUnsolicitedReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaMldServiceUnsolicitedReportInterval.setUnits("seconds")


class _AlaMldServiceQuerierForwarding_Type(Integer32):
    """Custom type alaMldServiceQuerierForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaMldServiceQuerierForwarding_Type.__name__ = "Integer32"
_AlaMldServiceQuerierForwarding_Object = MibTableColumn
alaMldServiceQuerierForwarding = _AlaMldServiceQuerierForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 14),
    _AlaMldServiceQuerierForwarding_Type()
)
alaMldServiceQuerierForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceQuerierForwarding.setStatus("current")


class _AlaMldServiceMaxGroupLimit_Type(Unsigned32):
    """Custom type alaMldServiceMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaMldServiceMaxGroupLimit_Type.__name__ = "Unsigned32"
_AlaMldServiceMaxGroupLimit_Object = MibTableColumn
alaMldServiceMaxGroupLimit = _AlaMldServiceMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 15),
    _AlaMldServiceMaxGroupLimit_Type()
)
alaMldServiceMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceMaxGroupLimit.setStatus("current")


class _AlaMldServiceMaxGroupExceedAction_Type(Integer32):
    """Custom type alaMldServiceMaxGroupExceedAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("drop", 1),
          ("replace", 2))
    )


_AlaMldServiceMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaMldServiceMaxGroupExceedAction_Object = MibTableColumn
alaMldServiceMaxGroupExceedAction = _AlaMldServiceMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 1, 1, 16),
    _AlaMldServiceMaxGroupExceedAction_Type()
)
alaMldServiceMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceMaxGroupExceedAction.setStatus("current")
_AlaMldMemberServiceSapTable_Object = MibTable
alaMldMemberServiceSapTable = _AlaMldMemberServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    alaMldMemberServiceSapTable.setStatus("current")
_AlaMldMemberServiceSapEntry_Object = MibTableRow
alaMldMemberServiceSapEntry = _AlaMldMemberServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 2, 1)
)
alaMldMemberServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSapGroupAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSapGroupAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSapSourceAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSapSourceAddress"),
)
if mibBuilder.loadTexts:
    alaMldMemberServiceSapEntry.setStatus("current")


class _AlaMldMemberServiceSapGroupAddressType_Type(InetAddressType):
    """Custom type alaMldMemberServiceSapGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldMemberServiceSapGroupAddressType_Type.__name__ = "InetAddressType"
_AlaMldMemberServiceSapGroupAddressType_Object = MibTableColumn
alaMldMemberServiceSapGroupAddressType = _AlaMldMemberServiceSapGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 2, 1, 1),
    _AlaMldMemberServiceSapGroupAddressType_Type()
)
alaMldMemberServiceSapGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberServiceSapGroupAddressType.setStatus("current")


class _AlaMldMemberServiceSapGroupAddress_Type(InetAddress):
    """Custom type alaMldMemberServiceSapGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldMemberServiceSapGroupAddress_Type.__name__ = "InetAddress"
_AlaMldMemberServiceSapGroupAddress_Object = MibTableColumn
alaMldMemberServiceSapGroupAddress = _AlaMldMemberServiceSapGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 2, 1, 2),
    _AlaMldMemberServiceSapGroupAddress_Type()
)
alaMldMemberServiceSapGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberServiceSapGroupAddress.setStatus("current")


class _AlaMldMemberServiceSapSourceAddressType_Type(InetAddressType):
    """Custom type alaMldMemberServiceSapSourceAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldMemberServiceSapSourceAddressType_Type.__name__ = "InetAddressType"
_AlaMldMemberServiceSapSourceAddressType_Object = MibTableColumn
alaMldMemberServiceSapSourceAddressType = _AlaMldMemberServiceSapSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 2, 1, 3),
    _AlaMldMemberServiceSapSourceAddressType_Type()
)
alaMldMemberServiceSapSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberServiceSapSourceAddressType.setStatus("current")


class _AlaMldMemberServiceSapSourceAddress_Type(InetAddress):
    """Custom type alaMldMemberServiceSapSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldMemberServiceSapSourceAddress_Type.__name__ = "InetAddress"
_AlaMldMemberServiceSapSourceAddress_Object = MibTableColumn
alaMldMemberServiceSapSourceAddress = _AlaMldMemberServiceSapSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 2, 1, 4),
    _AlaMldMemberServiceSapSourceAddress_Type()
)
alaMldMemberServiceSapSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberServiceSapSourceAddress.setStatus("current")


class _AlaMldMemberServiceSapMode_Type(Integer32):
    """Custom type alaMldMemberServiceSapMode based on Integer32"""
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


_AlaMldMemberServiceSapMode_Type.__name__ = "Integer32"
_AlaMldMemberServiceSapMode_Object = MibTableColumn
alaMldMemberServiceSapMode = _AlaMldMemberServiceSapMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 2, 1, 5),
    _AlaMldMemberServiceSapMode_Type()
)
alaMldMemberServiceSapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldMemberServiceSapMode.setStatus("current")
_AlaMldMemberServiceSapCount_Type = Counter32
_AlaMldMemberServiceSapCount_Object = MibTableColumn
alaMldMemberServiceSapCount = _AlaMldMemberServiceSapCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 2, 1, 6),
    _AlaMldMemberServiceSapCount_Type()
)
alaMldMemberServiceSapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldMemberServiceSapCount.setStatus("current")
_AlaMldMemberServiceSapTimeout_Type = TimeTicks
_AlaMldMemberServiceSapTimeout_Object = MibTableColumn
alaMldMemberServiceSapTimeout = _AlaMldMemberServiceSapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 2, 1, 7),
    _AlaMldMemberServiceSapTimeout_Type()
)
alaMldMemberServiceSapTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldMemberServiceSapTimeout.setStatus("current")
_AlaMldMemberServiceSdpBindTable_Object = MibTable
alaMldMemberServiceSdpBindTable = _AlaMldMemberServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    alaMldMemberServiceSdpBindTable.setStatus("current")
_AlaMldMemberServiceSdpBindEntry_Object = MibTableRow
alaMldMemberServiceSdpBindEntry = _AlaMldMemberServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 3, 1)
)
alaMldMemberServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSdpBindGroupAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSdpBindGroupAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSdpBindSourceAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSdpBindSourceAddress"),
)
if mibBuilder.loadTexts:
    alaMldMemberServiceSdpBindEntry.setStatus("current")


class _AlaMldMemberServiceSdpBindGroupAddressType_Type(InetAddressType):
    """Custom type alaMldMemberServiceSdpBindGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldMemberServiceSdpBindGroupAddressType_Type.__name__ = "InetAddressType"
_AlaMldMemberServiceSdpBindGroupAddressType_Object = MibTableColumn
alaMldMemberServiceSdpBindGroupAddressType = _AlaMldMemberServiceSdpBindGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 3, 1, 1),
    _AlaMldMemberServiceSdpBindGroupAddressType_Type()
)
alaMldMemberServiceSdpBindGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberServiceSdpBindGroupAddressType.setStatus("current")


class _AlaMldMemberServiceSdpBindGroupAddress_Type(InetAddress):
    """Custom type alaMldMemberServiceSdpBindGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldMemberServiceSdpBindGroupAddress_Type.__name__ = "InetAddress"
_AlaMldMemberServiceSdpBindGroupAddress_Object = MibTableColumn
alaMldMemberServiceSdpBindGroupAddress = _AlaMldMemberServiceSdpBindGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 3, 1, 2),
    _AlaMldMemberServiceSdpBindGroupAddress_Type()
)
alaMldMemberServiceSdpBindGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberServiceSdpBindGroupAddress.setStatus("current")


class _AlaMldMemberServiceSdpBindSourceAddressType_Type(InetAddressType):
    """Custom type alaMldMemberServiceSdpBindSourceAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldMemberServiceSdpBindSourceAddressType_Type.__name__ = "InetAddressType"
_AlaMldMemberServiceSdpBindSourceAddressType_Object = MibTableColumn
alaMldMemberServiceSdpBindSourceAddressType = _AlaMldMemberServiceSdpBindSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 3, 1, 3),
    _AlaMldMemberServiceSdpBindSourceAddressType_Type()
)
alaMldMemberServiceSdpBindSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberServiceSdpBindSourceAddressType.setStatus("current")


class _AlaMldMemberServiceSdpBindSourceAddress_Type(InetAddress):
    """Custom type alaMldMemberServiceSdpBindSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldMemberServiceSdpBindSourceAddress_Type.__name__ = "InetAddress"
_AlaMldMemberServiceSdpBindSourceAddress_Object = MibTableColumn
alaMldMemberServiceSdpBindSourceAddress = _AlaMldMemberServiceSdpBindSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 3, 1, 4),
    _AlaMldMemberServiceSdpBindSourceAddress_Type()
)
alaMldMemberServiceSdpBindSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldMemberServiceSdpBindSourceAddress.setStatus("current")


class _AlaMldMemberServiceSdpBindMode_Type(Integer32):
    """Custom type alaMldMemberServiceSdpBindMode based on Integer32"""
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


_AlaMldMemberServiceSdpBindMode_Type.__name__ = "Integer32"
_AlaMldMemberServiceSdpBindMode_Object = MibTableColumn
alaMldMemberServiceSdpBindMode = _AlaMldMemberServiceSdpBindMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 3, 1, 5),
    _AlaMldMemberServiceSdpBindMode_Type()
)
alaMldMemberServiceSdpBindMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldMemberServiceSdpBindMode.setStatus("current")
_AlaMldMemberServiceSdpBindCount_Type = Counter32
_AlaMldMemberServiceSdpBindCount_Object = MibTableColumn
alaMldMemberServiceSdpBindCount = _AlaMldMemberServiceSdpBindCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 3, 1, 6),
    _AlaMldMemberServiceSdpBindCount_Type()
)
alaMldMemberServiceSdpBindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldMemberServiceSdpBindCount.setStatus("current")
_AlaMldMemberServiceSdpBindTimeout_Type = TimeTicks
_AlaMldMemberServiceSdpBindTimeout_Object = MibTableColumn
alaMldMemberServiceSdpBindTimeout = _AlaMldMemberServiceSdpBindTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 3, 1, 7),
    _AlaMldMemberServiceSdpBindTimeout_Type()
)
alaMldMemberServiceSdpBindTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldMemberServiceSdpBindTimeout.setStatus("current")
_AlaMldStaticMemberServiceSapTable_Object = MibTable
alaMldStaticMemberServiceSapTable = _AlaMldStaticMemberServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSapTable.setStatus("current")
_AlaMldStaticMemberServiceSapEntry_Object = MibTableRow
alaMldStaticMemberServiceSapEntry = _AlaMldStaticMemberServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 4, 1)
)
alaMldStaticMemberServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticMemberServiceSapGroupAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticMemberServiceSapGroupAddress"),
)
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSapEntry.setStatus("current")


class _AlaMldStaticMemberServiceSapGroupAddressType_Type(InetAddressType):
    """Custom type alaMldStaticMemberServiceSapGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldStaticMemberServiceSapGroupAddressType_Type.__name__ = "InetAddressType"
_AlaMldStaticMemberServiceSapGroupAddressType_Object = MibTableColumn
alaMldStaticMemberServiceSapGroupAddressType = _AlaMldStaticMemberServiceSapGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 4, 1, 1),
    _AlaMldStaticMemberServiceSapGroupAddressType_Type()
)
alaMldStaticMemberServiceSapGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSapGroupAddressType.setStatus("current")


class _AlaMldStaticMemberServiceSapGroupAddress_Type(InetAddress):
    """Custom type alaMldStaticMemberServiceSapGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldStaticMemberServiceSapGroupAddress_Type.__name__ = "InetAddress"
_AlaMldStaticMemberServiceSapGroupAddress_Object = MibTableColumn
alaMldStaticMemberServiceSapGroupAddress = _AlaMldStaticMemberServiceSapGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 4, 1, 2),
    _AlaMldStaticMemberServiceSapGroupAddress_Type()
)
alaMldStaticMemberServiceSapGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSapGroupAddress.setStatus("current")
_AlaMldStaticMemberServiceSapRowStatus_Type = RowStatus
_AlaMldStaticMemberServiceSapRowStatus_Object = MibTableColumn
alaMldStaticMemberServiceSapRowStatus = _AlaMldStaticMemberServiceSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 4, 1, 3),
    _AlaMldStaticMemberServiceSapRowStatus_Type()
)
alaMldStaticMemberServiceSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSapRowStatus.setStatus("current")
_AlaMldStaticMemberServiceSdpBindTable_Object = MibTable
alaMldStaticMemberServiceSdpBindTable = _AlaMldStaticMemberServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSdpBindTable.setStatus("current")
_AlaMldStaticMemberServiceSdpBindEntry_Object = MibTableRow
alaMldStaticMemberServiceSdpBindEntry = _AlaMldStaticMemberServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 5, 1)
)
alaMldStaticMemberServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticMemberServiceSapGroupAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticMemberServiceSapGroupAddress"),
)
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSdpBindEntry.setStatus("current")


class _AlaMldStaticMemberServiceSdpBindGroupAddressType_Type(InetAddressType):
    """Custom type alaMldStaticMemberServiceSdpBindGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldStaticMemberServiceSdpBindGroupAddressType_Type.__name__ = "InetAddressType"
_AlaMldStaticMemberServiceSdpBindGroupAddressType_Object = MibTableColumn
alaMldStaticMemberServiceSdpBindGroupAddressType = _AlaMldStaticMemberServiceSdpBindGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 5, 1, 1),
    _AlaMldStaticMemberServiceSdpBindGroupAddressType_Type()
)
alaMldStaticMemberServiceSdpBindGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSdpBindGroupAddressType.setStatus("current")


class _AlaMldStaticMemberServiceSdpBindGroupAddress_Type(InetAddress):
    """Custom type alaMldStaticMemberServiceSdpBindGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldStaticMemberServiceSdpBindGroupAddress_Type.__name__ = "InetAddress"
_AlaMldStaticMemberServiceSdpBindGroupAddress_Object = MibTableColumn
alaMldStaticMemberServiceSdpBindGroupAddress = _AlaMldStaticMemberServiceSdpBindGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 5, 1, 2),
    _AlaMldStaticMemberServiceSdpBindGroupAddress_Type()
)
alaMldStaticMemberServiceSdpBindGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSdpBindGroupAddress.setStatus("current")
_AlaMldStaticMemberServiceSdpBindRowStatus_Type = RowStatus
_AlaMldStaticMemberServiceSdpBindRowStatus_Object = MibTableColumn
alaMldStaticMemberServiceSdpBindRowStatus = _AlaMldStaticMemberServiceSdpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 5, 1, 3),
    _AlaMldStaticMemberServiceSdpBindRowStatus_Type()
)
alaMldStaticMemberServiceSdpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSdpBindRowStatus.setStatus("current")
_AlaMldNeighborServiceSapTable_Object = MibTable
alaMldNeighborServiceSapTable = _AlaMldNeighborServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    alaMldNeighborServiceSapTable.setStatus("current")
_AlaMldNeighborServiceSapEntry_Object = MibTableRow
alaMldNeighborServiceSapEntry = _AlaMldNeighborServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 6, 1)
)
alaMldNeighborServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldNeighborServiceSapHostAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldNeighborServiceSapHostAddress"),
)
if mibBuilder.loadTexts:
    alaMldNeighborServiceSapEntry.setStatus("current")


class _AlaMldNeighborServiceSapHostAddressType_Type(InetAddressType):
    """Custom type alaMldNeighborServiceSapHostAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldNeighborServiceSapHostAddressType_Type.__name__ = "InetAddressType"
_AlaMldNeighborServiceSapHostAddressType_Object = MibTableColumn
alaMldNeighborServiceSapHostAddressType = _AlaMldNeighborServiceSapHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 6, 1, 1),
    _AlaMldNeighborServiceSapHostAddressType_Type()
)
alaMldNeighborServiceSapHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldNeighborServiceSapHostAddressType.setStatus("current")


class _AlaMldNeighborServiceSapHostAddress_Type(InetAddress):
    """Custom type alaMldNeighborServiceSapHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldNeighborServiceSapHostAddress_Type.__name__ = "InetAddress"
_AlaMldNeighborServiceSapHostAddress_Object = MibTableColumn
alaMldNeighborServiceSapHostAddress = _AlaMldNeighborServiceSapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 6, 1, 2),
    _AlaMldNeighborServiceSapHostAddress_Type()
)
alaMldNeighborServiceSapHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldNeighborServiceSapHostAddress.setStatus("current")
_AlaMldNeighborServiceSapCount_Type = Counter32
_AlaMldNeighborServiceSapCount_Object = MibTableColumn
alaMldNeighborServiceSapCount = _AlaMldNeighborServiceSapCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 6, 1, 3),
    _AlaMldNeighborServiceSapCount_Type()
)
alaMldNeighborServiceSapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldNeighborServiceSapCount.setStatus("current")
_AlaMldNeighborServiceSapTimeout_Type = TimeTicks
_AlaMldNeighborServiceSapTimeout_Object = MibTableColumn
alaMldNeighborServiceSapTimeout = _AlaMldNeighborServiceSapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 6, 1, 4),
    _AlaMldNeighborServiceSapTimeout_Type()
)
alaMldNeighborServiceSapTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldNeighborServiceSapTimeout.setStatus("current")
_AlaMldNeighborServiceSdpBindTable_Object = MibTable
alaMldNeighborServiceSdpBindTable = _AlaMldNeighborServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    alaMldNeighborServiceSdpBindTable.setStatus("current")
_AlaMldNeighborServiceSdpBindEntry_Object = MibTableRow
alaMldNeighborServiceSdpBindEntry = _AlaMldNeighborServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 7, 1)
)
alaMldNeighborServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldNeighborServiceSdpBindHostAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldNeighborServiceSdpBindHostAddress"),
)
if mibBuilder.loadTexts:
    alaMldNeighborServiceSdpBindEntry.setStatus("current")


class _AlaMldNeighborServiceSdpBindHostAddressType_Type(InetAddressType):
    """Custom type alaMldNeighborServiceSdpBindHostAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldNeighborServiceSdpBindHostAddressType_Type.__name__ = "InetAddressType"
_AlaMldNeighborServiceSdpBindHostAddressType_Object = MibTableColumn
alaMldNeighborServiceSdpBindHostAddressType = _AlaMldNeighborServiceSdpBindHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 7, 1, 1),
    _AlaMldNeighborServiceSdpBindHostAddressType_Type()
)
alaMldNeighborServiceSdpBindHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldNeighborServiceSdpBindHostAddressType.setStatus("current")


class _AlaMldNeighborServiceSdpBindHostAddress_Type(InetAddress):
    """Custom type alaMldNeighborServiceSdpBindHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldNeighborServiceSdpBindHostAddress_Type.__name__ = "InetAddress"
_AlaMldNeighborServiceSdpBindHostAddress_Object = MibTableColumn
alaMldNeighborServiceSdpBindHostAddress = _AlaMldNeighborServiceSdpBindHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 7, 1, 2),
    _AlaMldNeighborServiceSdpBindHostAddress_Type()
)
alaMldNeighborServiceSdpBindHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldNeighborServiceSdpBindHostAddress.setStatus("current")
_AlaMldNeighborServiceSdpBindCount_Type = Counter32
_AlaMldNeighborServiceSdpBindCount_Object = MibTableColumn
alaMldNeighborServiceSdpBindCount = _AlaMldNeighborServiceSdpBindCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 7, 1, 3),
    _AlaMldNeighborServiceSdpBindCount_Type()
)
alaMldNeighborServiceSdpBindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldNeighborServiceSdpBindCount.setStatus("current")
_AlaMldNeighborServiceSdpBindTimeout_Type = TimeTicks
_AlaMldNeighborServiceSdpBindTimeout_Object = MibTableColumn
alaMldNeighborServiceSdpBindTimeout = _AlaMldNeighborServiceSdpBindTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 7, 1, 4),
    _AlaMldNeighborServiceSdpBindTimeout_Type()
)
alaMldNeighborServiceSdpBindTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldNeighborServiceSdpBindTimeout.setStatus("current")
_AlaMldStaticNeighborServiceSapTable_Object = MibTable
alaMldStaticNeighborServiceSapTable = _AlaMldStaticNeighborServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    alaMldStaticNeighborServiceSapTable.setStatus("current")
_AlaMldStaticNeighborServiceSapEntry_Object = MibTableRow
alaMldStaticNeighborServiceSapEntry = _AlaMldStaticNeighborServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 8, 1)
)
alaMldStaticNeighborServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    alaMldStaticNeighborServiceSapEntry.setStatus("current")
_AlaMldStaticNeighborServiceSapRowStatus_Type = RowStatus
_AlaMldStaticNeighborServiceSapRowStatus_Object = MibTableColumn
alaMldStaticNeighborServiceSapRowStatus = _AlaMldStaticNeighborServiceSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 8, 1, 1),
    _AlaMldStaticNeighborServiceSapRowStatus_Type()
)
alaMldStaticNeighborServiceSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaMldStaticNeighborServiceSapRowStatus.setStatus("current")
_AlaMldStaticNeighborServiceSdpBindTable_Object = MibTable
alaMldStaticNeighborServiceSdpBindTable = _AlaMldStaticNeighborServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    alaMldStaticNeighborServiceSdpBindTable.setStatus("current")
_AlaMldStaticNeighborServiceSdpBindEntry_Object = MibTableRow
alaMldStaticNeighborServiceSdpBindEntry = _AlaMldStaticNeighborServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 9, 1)
)
alaMldStaticNeighborServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    alaMldStaticNeighborServiceSdpBindEntry.setStatus("current")
_AlaMldStaticNeighborServiceSdpBindRowStatus_Type = RowStatus
_AlaMldStaticNeighborServiceSdpBindRowStatus_Object = MibTableColumn
alaMldStaticNeighborServiceSdpBindRowStatus = _AlaMldStaticNeighborServiceSdpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 9, 1, 1),
    _AlaMldStaticNeighborServiceSdpBindRowStatus_Type()
)
alaMldStaticNeighborServiceSdpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaMldStaticNeighborServiceSdpBindRowStatus.setStatus("current")
_AlaMldQuerierServiceSapTable_Object = MibTable
alaMldQuerierServiceSapTable = _AlaMldQuerierServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 10)
)
if mibBuilder.loadTexts:
    alaMldQuerierServiceSapTable.setStatus("current")
_AlaMldQuerierServiceSapEntry_Object = MibTableRow
alaMldQuerierServiceSapEntry = _AlaMldQuerierServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 10, 1)
)
alaMldQuerierServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldQuerierServiceSapHostAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldQuerierServiceSapHostAddress"),
)
if mibBuilder.loadTexts:
    alaMldQuerierServiceSapEntry.setStatus("current")


class _AlaMldQuerierServiceSapHostAddressType_Type(InetAddressType):
    """Custom type alaMldQuerierServiceSapHostAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldQuerierServiceSapHostAddressType_Type.__name__ = "InetAddressType"
_AlaMldQuerierServiceSapHostAddressType_Object = MibTableColumn
alaMldQuerierServiceSapHostAddressType = _AlaMldQuerierServiceSapHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 10, 1, 1),
    _AlaMldQuerierServiceSapHostAddressType_Type()
)
alaMldQuerierServiceSapHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldQuerierServiceSapHostAddressType.setStatus("current")


class _AlaMldQuerierServiceSapHostAddress_Type(InetAddress):
    """Custom type alaMldQuerierServiceSapHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldQuerierServiceSapHostAddress_Type.__name__ = "InetAddress"
_AlaMldQuerierServiceSapHostAddress_Object = MibTableColumn
alaMldQuerierServiceSapHostAddress = _AlaMldQuerierServiceSapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 10, 1, 2),
    _AlaMldQuerierServiceSapHostAddress_Type()
)
alaMldQuerierServiceSapHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldQuerierServiceSapHostAddress.setStatus("current")
_AlaMldQuerierServiceSapCount_Type = Counter32
_AlaMldQuerierServiceSapCount_Object = MibTableColumn
alaMldQuerierServiceSapCount = _AlaMldQuerierServiceSapCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 10, 1, 3),
    _AlaMldQuerierServiceSapCount_Type()
)
alaMldQuerierServiceSapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldQuerierServiceSapCount.setStatus("current")
_AlaMldQuerierServiceSapTimeout_Type = TimeTicks
_AlaMldQuerierServiceSapTimeout_Object = MibTableColumn
alaMldQuerierServiceSapTimeout = _AlaMldQuerierServiceSapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 10, 1, 4),
    _AlaMldQuerierServiceSapTimeout_Type()
)
alaMldQuerierServiceSapTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldQuerierServiceSapTimeout.setStatus("current")
_AlaMldQuerierServiceSdpBindTable_Object = MibTable
alaMldQuerierServiceSdpBindTable = _AlaMldQuerierServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    alaMldQuerierServiceSdpBindTable.setStatus("current")
_AlaMldQuerierServiceSdpBindEntry_Object = MibTableRow
alaMldQuerierServiceSdpBindEntry = _AlaMldQuerierServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 11, 1)
)
alaMldQuerierServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldQuerierServiceSdpBindHostAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldQuerierServiceSdpBindHostAddress"),
)
if mibBuilder.loadTexts:
    alaMldQuerierServiceSdpBindEntry.setStatus("current")


class _AlaMldQuerierServiceSdpBindHostAddressType_Type(InetAddressType):
    """Custom type alaMldQuerierServiceSdpBindHostAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldQuerierServiceSdpBindHostAddressType_Type.__name__ = "InetAddressType"
_AlaMldQuerierServiceSdpBindHostAddressType_Object = MibTableColumn
alaMldQuerierServiceSdpBindHostAddressType = _AlaMldQuerierServiceSdpBindHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 11, 1, 1),
    _AlaMldQuerierServiceSdpBindHostAddressType_Type()
)
alaMldQuerierServiceSdpBindHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldQuerierServiceSdpBindHostAddressType.setStatus("current")


class _AlaMldQuerierServiceSdpBindHostAddress_Type(InetAddress):
    """Custom type alaMldQuerierServiceSdpBindHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldQuerierServiceSdpBindHostAddress_Type.__name__ = "InetAddress"
_AlaMldQuerierServiceSdpBindHostAddress_Object = MibTableColumn
alaMldQuerierServiceSdpBindHostAddress = _AlaMldQuerierServiceSdpBindHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 11, 1, 2),
    _AlaMldQuerierServiceSdpBindHostAddress_Type()
)
alaMldQuerierServiceSdpBindHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldQuerierServiceSdpBindHostAddress.setStatus("current")
_AlaMldQuerierServiceSdpBindCount_Type = Counter32
_AlaMldQuerierServiceSdpBindCount_Object = MibTableColumn
alaMldQuerierServiceSdpBindCount = _AlaMldQuerierServiceSdpBindCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 11, 1, 3),
    _AlaMldQuerierServiceSdpBindCount_Type()
)
alaMldQuerierServiceSdpBindCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldQuerierServiceSdpBindCount.setStatus("current")
_AlaMldQuerierServiceSdpBindTimeout_Type = TimeTicks
_AlaMldQuerierServiceSdpBindTimeout_Object = MibTableColumn
alaMldQuerierServiceSdpBindTimeout = _AlaMldQuerierServiceSdpBindTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 11, 1, 4),
    _AlaMldQuerierServiceSdpBindTimeout_Type()
)
alaMldQuerierServiceSdpBindTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldQuerierServiceSdpBindTimeout.setStatus("current")
_AlaMldStaticQuerierServiceSapTable_Object = MibTable
alaMldStaticQuerierServiceSapTable = _AlaMldStaticQuerierServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 12)
)
if mibBuilder.loadTexts:
    alaMldStaticQuerierServiceSapTable.setStatus("current")
_AlaMldStaticQuerierServiceSapEntry_Object = MibTableRow
alaMldStaticQuerierServiceSapEntry = _AlaMldStaticQuerierServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 12, 1)
)
alaMldStaticQuerierServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    alaMldStaticQuerierServiceSapEntry.setStatus("current")
_AlaMldStaticQuerierServiceSapRowStatus_Type = RowStatus
_AlaMldStaticQuerierServiceSapRowStatus_Object = MibTableColumn
alaMldStaticQuerierServiceSapRowStatus = _AlaMldStaticQuerierServiceSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 12, 1, 1),
    _AlaMldStaticQuerierServiceSapRowStatus_Type()
)
alaMldStaticQuerierServiceSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaMldStaticQuerierServiceSapRowStatus.setStatus("current")
_AlaMldStaticQuerierServiceSdpBindTable_Object = MibTable
alaMldStaticQuerierServiceSdpBindTable = _AlaMldStaticQuerierServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 13)
)
if mibBuilder.loadTexts:
    alaMldStaticQuerierServiceSdpBindTable.setStatus("current")
_AlaMldStaticQuerierServiceSdpBindEntry_Object = MibTableRow
alaMldStaticQuerierServiceSdpBindEntry = _AlaMldStaticQuerierServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 13, 1)
)
alaMldStaticQuerierServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    alaMldStaticQuerierServiceSdpBindEntry.setStatus("current")
_AlaMldStaticQuerierServiceSdpBindRowStatus_Type = RowStatus
_AlaMldStaticQuerierServiceSdpBindRowStatus_Object = MibTableColumn
alaMldStaticQuerierServiceSdpBindRowStatus = _AlaMldStaticQuerierServiceSdpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 13, 1, 1),
    _AlaMldStaticQuerierServiceSdpBindRowStatus_Type()
)
alaMldStaticQuerierServiceSdpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaMldStaticQuerierServiceSdpBindRowStatus.setStatus("current")
_AlaMldServiceSourceTable_Object = MibTable
alaMldServiceSourceTable = _AlaMldServiceSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14)
)
if mibBuilder.loadTexts:
    alaMldServiceSourceTable.setStatus("current")
_AlaMldServiceSourceEntry_Object = MibTableRow
alaMldServiceSourceEntry = _AlaMldServiceSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1)
)
alaMldServiceSourceEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceGroupAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceGroupAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceHostAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceHostAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceDestAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceDestAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceOrigAddressType"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceOrigAddress"),
)
if mibBuilder.loadTexts:
    alaMldServiceSourceEntry.setStatus("current")


class _AlaMldServiceSourceGroupAddressType_Type(InetAddressType):
    """Custom type alaMldServiceSourceGroupAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldServiceSourceGroupAddressType_Type.__name__ = "InetAddressType"
_AlaMldServiceSourceGroupAddressType_Object = MibTableColumn
alaMldServiceSourceGroupAddressType = _AlaMldServiceSourceGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 1),
    _AlaMldServiceSourceGroupAddressType_Type()
)
alaMldServiceSourceGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSourceGroupAddressType.setStatus("current")


class _AlaMldServiceSourceGroupAddress_Type(InetAddress):
    """Custom type alaMldServiceSourceGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldServiceSourceGroupAddress_Type.__name__ = "InetAddress"
_AlaMldServiceSourceGroupAddress_Object = MibTableColumn
alaMldServiceSourceGroupAddress = _AlaMldServiceSourceGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 2),
    _AlaMldServiceSourceGroupAddress_Type()
)
alaMldServiceSourceGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSourceGroupAddress.setStatus("current")


class _AlaMldServiceSourceHostAddressType_Type(InetAddressType):
    """Custom type alaMldServiceSourceHostAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldServiceSourceHostAddressType_Type.__name__ = "InetAddressType"
_AlaMldServiceSourceHostAddressType_Object = MibTableColumn
alaMldServiceSourceHostAddressType = _AlaMldServiceSourceHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 3),
    _AlaMldServiceSourceHostAddressType_Type()
)
alaMldServiceSourceHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSourceHostAddressType.setStatus("current")


class _AlaMldServiceSourceHostAddress_Type(InetAddress):
    """Custom type alaMldServiceSourceHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldServiceSourceHostAddress_Type.__name__ = "InetAddress"
_AlaMldServiceSourceHostAddress_Object = MibTableColumn
alaMldServiceSourceHostAddress = _AlaMldServiceSourceHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 4),
    _AlaMldServiceSourceHostAddress_Type()
)
alaMldServiceSourceHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSourceHostAddress.setStatus("current")


class _AlaMldServiceSourceDestAddressType_Type(InetAddressType):
    """Custom type alaMldServiceSourceDestAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldServiceSourceDestAddressType_Type.__name__ = "InetAddressType"
_AlaMldServiceSourceDestAddressType_Object = MibTableColumn
alaMldServiceSourceDestAddressType = _AlaMldServiceSourceDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 5),
    _AlaMldServiceSourceDestAddressType_Type()
)
alaMldServiceSourceDestAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSourceDestAddressType.setStatus("current")


class _AlaMldServiceSourceDestAddress_Type(InetAddress):
    """Custom type alaMldServiceSourceDestAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldServiceSourceDestAddress_Type.__name__ = "InetAddress"
_AlaMldServiceSourceDestAddress_Object = MibTableColumn
alaMldServiceSourceDestAddress = _AlaMldServiceSourceDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 6),
    _AlaMldServiceSourceDestAddress_Type()
)
alaMldServiceSourceDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSourceDestAddress.setStatus("current")


class _AlaMldServiceSourceOrigAddressType_Type(InetAddressType):
    """Custom type alaMldServiceSourceOrigAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_AlaMldServiceSourceOrigAddressType_Type.__name__ = "InetAddressType"
_AlaMldServiceSourceOrigAddressType_Object = MibTableColumn
alaMldServiceSourceOrigAddressType = _AlaMldServiceSourceOrigAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 7),
    _AlaMldServiceSourceOrigAddressType_Type()
)
alaMldServiceSourceOrigAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSourceOrigAddressType.setStatus("current")


class _AlaMldServiceSourceOrigAddress_Type(InetAddress):
    """Custom type alaMldServiceSourceOrigAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaMldServiceSourceOrigAddress_Type.__name__ = "InetAddress"
_AlaMldServiceSourceOrigAddress_Object = MibTableColumn
alaMldServiceSourceOrigAddress = _AlaMldServiceSourceOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 8),
    _AlaMldServiceSourceOrigAddress_Type()
)
alaMldServiceSourceOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSourceOrigAddress.setStatus("current")
_AlaMldServiceSourceLocale_Type = AluLocation
_AlaMldServiceSourceLocale_Object = MibTableColumn
alaMldServiceSourceLocale = _AlaMldServiceSourceLocale_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 9),
    _AlaMldServiceSourceLocale_Type()
)
alaMldServiceSourceLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSourceLocale.setStatus("current")
_AlaMldServiceSourcePortId_Type = TmnxPortID
_AlaMldServiceSourcePortId_Object = MibTableColumn
alaMldServiceSourcePortId = _AlaMldServiceSourcePortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 10),
    _AlaMldServiceSourcePortId_Type()
)
alaMldServiceSourcePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSourcePortId.setStatus("current")
_AlaMldServiceSourceEncapValue_Type = TmnxEncapVal
_AlaMldServiceSourceEncapValue_Object = MibTableColumn
alaMldServiceSourceEncapValue = _AlaMldServiceSourceEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 11),
    _AlaMldServiceSourceEncapValue_Type()
)
alaMldServiceSourceEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSourceEncapValue.setStatus("current")
_AlaMldServiceSourceSdpId_Type = SdpId
_AlaMldServiceSourceSdpId_Object = MibTableColumn
alaMldServiceSourceSdpId = _AlaMldServiceSourceSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 12),
    _AlaMldServiceSourceSdpId_Type()
)
alaMldServiceSourceSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSourceSdpId.setStatus("current")
_AlaMldServiceSourceVcId_Type = TmnxVcIdOrNone
_AlaMldServiceSourceVcId_Object = MibTableColumn
alaMldServiceSourceVcId = _AlaMldServiceSourceVcId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 13),
    _AlaMldServiceSourceVcId_Type()
)
alaMldServiceSourceVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSourceVcId.setStatus("current")


class _AlaMldServiceSourceType_Type(Integer32):
    """Custom type alaMldServiceSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaMldServiceSourceType_Type.__name__ = "Integer32"
_AlaMldServiceSourceType_Object = MibTableColumn
alaMldServiceSourceType = _AlaMldServiceSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 14, 1, 14),
    _AlaMldServiceSourceType_Type()
)
alaMldServiceSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSourceType.setStatus("current")
_AlaMldServiceSapForwardTable_Object = MibTable
alaMldServiceSapForwardTable = _AlaMldServiceSapForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15)
)
if mibBuilder.loadTexts:
    alaMldServiceSapForwardTable.setStatus("current")
_AlaMldServiceSapForwardEntry_Object = MibTableRow
alaMldServiceSapForwardEntry = _AlaMldServiceSapForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1)
)
alaMldServiceSapForwardEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardGroupAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardHostAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardDestAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardOrigAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardNextSapPortId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardNextSapEncapValue"),
)
if mibBuilder.loadTexts:
    alaMldServiceSapForwardEntry.setStatus("current")
_AlaMldServiceSapForwardLocale_Type = AluLocation
_AlaMldServiceSapForwardLocale_Object = MibTableColumn
alaMldServiceSapForwardLocale = _AlaMldServiceSapForwardLocale_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 1),
    _AlaMldServiceSapForwardLocale_Type()
)
alaMldServiceSapForwardLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardLocale.setStatus("current")
_AlaMldServiceSapForwardPortId_Type = TmnxPortID
_AlaMldServiceSapForwardPortId_Object = MibTableColumn
alaMldServiceSapForwardPortId = _AlaMldServiceSapForwardPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 2),
    _AlaMldServiceSapForwardPortId_Type()
)
alaMldServiceSapForwardPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardPortId.setStatus("current")
_AlaMldServiceSapForwardEncapValue_Type = TmnxEncapVal
_AlaMldServiceSapForwardEncapValue_Object = MibTableColumn
alaMldServiceSapForwardEncapValue = _AlaMldServiceSapForwardEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 3),
    _AlaMldServiceSapForwardEncapValue_Type()
)
alaMldServiceSapForwardEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardEncapValue.setStatus("current")
_AlaMldServiceSapForwardSdpId_Type = SdpId
_AlaMldServiceSapForwardSdpId_Object = MibTableColumn
alaMldServiceSapForwardSdpId = _AlaMldServiceSapForwardSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 4),
    _AlaMldServiceSapForwardSdpId_Type()
)
alaMldServiceSapForwardSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardSdpId.setStatus("current")
_AlaMldServiceSapForwardVcId_Type = TmnxVcIdOrNone
_AlaMldServiceSapForwardVcId_Object = MibTableColumn
alaMldServiceSapForwardVcId = _AlaMldServiceSapForwardVcId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 5),
    _AlaMldServiceSapForwardVcId_Type()
)
alaMldServiceSapForwardVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardVcId.setStatus("current")
_AlaMldServiceSapForwardGroupAddress_Type = MacAddress
_AlaMldServiceSapForwardGroupAddress_Object = MibTableColumn
alaMldServiceSapForwardGroupAddress = _AlaMldServiceSapForwardGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 6),
    _AlaMldServiceSapForwardGroupAddress_Type()
)
alaMldServiceSapForwardGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardGroupAddress.setStatus("current")
_AlaMldServiceSapForwardHostAddress_Type = MacAddress
_AlaMldServiceSapForwardHostAddress_Object = MibTableColumn
alaMldServiceSapForwardHostAddress = _AlaMldServiceSapForwardHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 7),
    _AlaMldServiceSapForwardHostAddress_Type()
)
alaMldServiceSapForwardHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardHostAddress.setStatus("current")
_AlaMldServiceSapForwardDestAddress_Type = MacAddress
_AlaMldServiceSapForwardDestAddress_Object = MibTableColumn
alaMldServiceSapForwardDestAddress = _AlaMldServiceSapForwardDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 8),
    _AlaMldServiceSapForwardDestAddress_Type()
)
alaMldServiceSapForwardDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardDestAddress.setStatus("current")
_AlaMldServiceSapForwardOrigAddress_Type = MacAddress
_AlaMldServiceSapForwardOrigAddress_Object = MibTableColumn
alaMldServiceSapForwardOrigAddress = _AlaMldServiceSapForwardOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 9),
    _AlaMldServiceSapForwardOrigAddress_Type()
)
alaMldServiceSapForwardOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardOrigAddress.setStatus("current")


class _AlaMldServiceSapForwardType_Type(Integer32):
    """Custom type alaMldServiceSapForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaMldServiceSapForwardType_Type.__name__ = "Integer32"
_AlaMldServiceSapForwardType_Object = MibTableColumn
alaMldServiceSapForwardType = _AlaMldServiceSapForwardType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 10),
    _AlaMldServiceSapForwardType_Type()
)
alaMldServiceSapForwardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardType.setStatus("current")
_AlaMldServiceSapForwardNextSapPortId_Type = TmnxPortID
_AlaMldServiceSapForwardNextSapPortId_Object = MibTableColumn
alaMldServiceSapForwardNextSapPortId = _AlaMldServiceSapForwardNextSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 11),
    _AlaMldServiceSapForwardNextSapPortId_Type()
)
alaMldServiceSapForwardNextSapPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardNextSapPortId.setStatus("current")
_AlaMldServiceSapForwardNextSapEncapValue_Type = TmnxEncapVal
_AlaMldServiceSapForwardNextSapEncapValue_Object = MibTableColumn
alaMldServiceSapForwardNextSapEncapValue = _AlaMldServiceSapForwardNextSapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 12),
    _AlaMldServiceSapForwardNextSapEncapValue_Type()
)
alaMldServiceSapForwardNextSapEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardNextSapEncapValue.setStatus("current")


class _AlaMldServiceSapForwardNextType_Type(Integer32):
    """Custom type alaMldServiceSapForwardNextType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaMldServiceSapForwardNextType_Type.__name__ = "Integer32"
_AlaMldServiceSapForwardNextType_Object = MibTableColumn
alaMldServiceSapForwardNextType = _AlaMldServiceSapForwardNextType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 15, 1, 13),
    _AlaMldServiceSapForwardNextType_Type()
)
alaMldServiceSapForwardNextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSapForwardNextType.setStatus("current")
_AlaMldServiceSdpBindForwardTable_Object = MibTable
alaMldServiceSdpBindForwardTable = _AlaMldServiceSdpBindForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16)
)
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardTable.setStatus("current")
_AlaMldServiceSdpBindForwardEntry_Object = MibTableRow
alaMldServiceSdpBindForwardEntry = _AlaMldServiceSdpBindForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1)
)
alaMldServiceSdpBindForwardEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardGroupAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardHostAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardDestAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardOrigAddress"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardNextSdpBindId"),
)
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardEntry.setStatus("current")
_AlaMldServiceSdpBindForwardLocale_Type = AluLocation
_AlaMldServiceSdpBindForwardLocale_Object = MibTableColumn
alaMldServiceSdpBindForwardLocale = _AlaMldServiceSdpBindForwardLocale_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 1),
    _AlaMldServiceSdpBindForwardLocale_Type()
)
alaMldServiceSdpBindForwardLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardLocale.setStatus("current")
_AlaMldServiceSdpBindForwardPortId_Type = TmnxPortID
_AlaMldServiceSdpBindForwardPortId_Object = MibTableColumn
alaMldServiceSdpBindForwardPortId = _AlaMldServiceSdpBindForwardPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 2),
    _AlaMldServiceSdpBindForwardPortId_Type()
)
alaMldServiceSdpBindForwardPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardPortId.setStatus("current")
_AlaMldServiceSdpBindForwardEncapValue_Type = TmnxEncapVal
_AlaMldServiceSdpBindForwardEncapValue_Object = MibTableColumn
alaMldServiceSdpBindForwardEncapValue = _AlaMldServiceSdpBindForwardEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 3),
    _AlaMldServiceSdpBindForwardEncapValue_Type()
)
alaMldServiceSdpBindForwardEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardEncapValue.setStatus("current")
_AlaMldServiceSdpBindForwardSdpId_Type = SdpId
_AlaMldServiceSdpBindForwardSdpId_Object = MibTableColumn
alaMldServiceSdpBindForwardSdpId = _AlaMldServiceSdpBindForwardSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 4),
    _AlaMldServiceSdpBindForwardSdpId_Type()
)
alaMldServiceSdpBindForwardSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardSdpId.setStatus("current")
_AlaMldServiceSdpBindForwardVcId_Type = TmnxVcIdOrNone
_AlaMldServiceSdpBindForwardVcId_Object = MibTableColumn
alaMldServiceSdpBindForwardVcId = _AlaMldServiceSdpBindForwardVcId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 5),
    _AlaMldServiceSdpBindForwardVcId_Type()
)
alaMldServiceSdpBindForwardVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardVcId.setStatus("current")
_AlaMldServiceSdpBindForwardGroupAddress_Type = MacAddress
_AlaMldServiceSdpBindForwardGroupAddress_Object = MibTableColumn
alaMldServiceSdpBindForwardGroupAddress = _AlaMldServiceSdpBindForwardGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 6),
    _AlaMldServiceSdpBindForwardGroupAddress_Type()
)
alaMldServiceSdpBindForwardGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardGroupAddress.setStatus("current")
_AlaMldServiceSdpBindForwardHostAddress_Type = MacAddress
_AlaMldServiceSdpBindForwardHostAddress_Object = MibTableColumn
alaMldServiceSdpBindForwardHostAddress = _AlaMldServiceSdpBindForwardHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 7),
    _AlaMldServiceSdpBindForwardHostAddress_Type()
)
alaMldServiceSdpBindForwardHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardHostAddress.setStatus("current")
_AlaMldServiceSdpBindForwardDestAddress_Type = MacAddress
_AlaMldServiceSdpBindForwardDestAddress_Object = MibTableColumn
alaMldServiceSdpBindForwardDestAddress = _AlaMldServiceSdpBindForwardDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 8),
    _AlaMldServiceSdpBindForwardDestAddress_Type()
)
alaMldServiceSdpBindForwardDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardDestAddress.setStatus("current")
_AlaMldServiceSdpBindForwardOrigAddress_Type = MacAddress
_AlaMldServiceSdpBindForwardOrigAddress_Object = MibTableColumn
alaMldServiceSdpBindForwardOrigAddress = _AlaMldServiceSdpBindForwardOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 9),
    _AlaMldServiceSdpBindForwardOrigAddress_Type()
)
alaMldServiceSdpBindForwardOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardOrigAddress.setStatus("current")


class _AlaMldServiceSdpBindForwardType_Type(Integer32):
    """Custom type alaMldServiceSdpBindForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaMldServiceSdpBindForwardType_Type.__name__ = "Integer32"
_AlaMldServiceSdpBindForwardType_Object = MibTableColumn
alaMldServiceSdpBindForwardType = _AlaMldServiceSdpBindForwardType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 10),
    _AlaMldServiceSdpBindForwardType_Type()
)
alaMldServiceSdpBindForwardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardType.setStatus("current")
_AlaMldServiceSdpBindForwardNextSdpBindId_Type = SdpBindId
_AlaMldServiceSdpBindForwardNextSdpBindId_Object = MibTableColumn
alaMldServiceSdpBindForwardNextSdpBindId = _AlaMldServiceSdpBindForwardNextSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 11),
    _AlaMldServiceSdpBindForwardNextSdpBindId_Type()
)
alaMldServiceSdpBindForwardNextSdpBindId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardNextSdpBindId.setStatus("current")


class _AlaMldServiceSdpBindForwardNextType_Type(Integer32):
    """Custom type alaMldServiceSdpBindForwardNextType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaMldServiceSdpBindForwardNextType_Type.__name__ = "Integer32"
_AlaMldServiceSdpBindForwardNextType_Object = MibTableColumn
alaMldServiceSdpBindForwardNextType = _AlaMldServiceSdpBindForwardNextType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 16, 1, 12),
    _AlaMldServiceSdpBindForwardNextType_Type()
)
alaMldServiceSdpBindForwardNextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardNextType.setStatus("current")
_AlaMldServiceSapTable_Object = MibTable
alaMldServiceSapTable = _AlaMldServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 17)
)
if mibBuilder.loadTexts:
    alaMldServiceSapTable.setStatus("current")
_AlaMldServiceSapEntry_Object = MibTableRow
alaMldServiceSapEntry = _AlaMldServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 17, 1)
)
alaMldServiceSapEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    alaMldServiceSapEntry.setStatus("current")


class _AlaMldServiceSapMaxGroupLimit_Type(Unsigned32):
    """Custom type alaMldServiceSapMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaMldServiceSapMaxGroupLimit_Type.__name__ = "Unsigned32"
_AlaMldServiceSapMaxGroupLimit_Object = MibTableColumn
alaMldServiceSapMaxGroupLimit = _AlaMldServiceSapMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 17, 1, 1),
    _AlaMldServiceSapMaxGroupLimit_Type()
)
alaMldServiceSapMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceSapMaxGroupLimit.setStatus("current")


class _AlaMldServiceSapMaxGroupExceedAction_Type(Integer32):
    """Custom type alaMldServiceSapMaxGroupExceedAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("drop", 1),
          ("replace", 2))
    )


_AlaMldServiceSapMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaMldServiceSapMaxGroupExceedAction_Object = MibTableColumn
alaMldServiceSapMaxGroupExceedAction = _AlaMldServiceSapMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 17, 1, 2),
    _AlaMldServiceSapMaxGroupExceedAction_Type()
)
alaMldServiceSapMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceSapMaxGroupExceedAction.setStatus("current")
_AlaMldServiceSapCurrentGroupCount_Type = Unsigned32
_AlaMldServiceSapCurrentGroupCount_Object = MibTableColumn
alaMldServiceSapCurrentGroupCount = _AlaMldServiceSapCurrentGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 17, 1, 3),
    _AlaMldServiceSapCurrentGroupCount_Type()
)
alaMldServiceSapCurrentGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSapCurrentGroupCount.setStatus("current")
_AlaMldServiceSdpBindTable_Object = MibTable
alaMldServiceSdpBindTable = _AlaMldServiceSdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 18)
)
if mibBuilder.loadTexts:
    alaMldServiceSdpBindTable.setStatus("current")
_AlaMldServiceSdpBindEntry_Object = MibTableRow
alaMldServiceSdpBindEntry = _AlaMldServiceSdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 18, 1)
)
alaMldServiceSdpBindEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    alaMldServiceSdpBindEntry.setStatus("current")


class _AlaMldServiceSdpBindMaxGroupLimit_Type(Unsigned32):
    """Custom type alaMldServiceSdpBindMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaMldServiceSdpBindMaxGroupLimit_Type.__name__ = "Unsigned32"
_AlaMldServiceSdpBindMaxGroupLimit_Object = MibTableColumn
alaMldServiceSdpBindMaxGroupLimit = _AlaMldServiceSdpBindMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 18, 1, 1),
    _AlaMldServiceSdpBindMaxGroupLimit_Type()
)
alaMldServiceSdpBindMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindMaxGroupLimit.setStatus("current")


class _AlaMldServiceSdpBindMaxGroupExceedAction_Type(Integer32):
    """Custom type alaMldServiceSdpBindMaxGroupExceedAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("drop", 1),
          ("replace", 2))
    )


_AlaMldServiceSdpBindMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaMldServiceSdpBindMaxGroupExceedAction_Object = MibTableColumn
alaMldServiceSdpBindMaxGroupExceedAction = _AlaMldServiceSdpBindMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 18, 1, 2),
    _AlaMldServiceSdpBindMaxGroupExceedAction_Type()
)
alaMldServiceSdpBindMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindMaxGroupExceedAction.setStatus("current")
_AlaMldServiceSdpBindCurrentGroupCount_Type = Unsigned32
_AlaMldServiceSdpBindCurrentGroupCount_Object = MibTableColumn
alaMldServiceSdpBindCurrentGroupCount = _AlaMldServiceSdpBindCurrentGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 3, 18, 1, 3),
    _AlaMldServiceSdpBindCurrentGroupCount_Type()
)
alaMldServiceSdpBindCurrentGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMldServiceSdpBindCurrentGroupCount.setStatus("current")
_AlaExtraLdp_ObjectIdentity = ObjectIdentity
alaExtraLdp = _AlaExtraLdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4)
)
_AlaVRtrExtendedLdpGeneralTable_Object = MibTable
alaVRtrExtendedLdpGeneralTable = _AlaVRtrExtendedLdpGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaVRtrExtendedLdpGeneralTable.setStatus("current")
_AlaVRtrExtendedLdpGeneralEntry_Object = MibTableRow
alaVRtrExtendedLdpGeneralEntry = _AlaVRtrExtendedLdpGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4, 1, 1)
)
alaVRtrExtendedLdpGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    alaVRtrExtendedLdpGeneralEntry.setStatus("current")


class _AlaVRtrLdpGenGracefulRestartSupport_Type(TruthValue):
    """Custom type alaVRtrLdpGenGracefulRestartSupport based on TruthValue"""
    defaultValue = 2


_AlaVRtrLdpGenGracefulRestartSupport_Type.__name__ = "TruthValue"
_AlaVRtrLdpGenGracefulRestartSupport_Object = MibTableColumn
alaVRtrLdpGenGracefulRestartSupport = _AlaVRtrLdpGenGracefulRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4, 1, 1, 1),
    _AlaVRtrLdpGenGracefulRestartSupport_Type()
)
alaVRtrLdpGenGracefulRestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVRtrLdpGenGracefulRestartSupport.setStatus("current")


class _AlaVRtrLdpGenGRReconnectTime_Type(Unsigned32):
    """Custom type alaVRtrLdpGenGRReconnectTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_AlaVRtrLdpGenGRReconnectTime_Type.__name__ = "Unsigned32"
_AlaVRtrLdpGenGRReconnectTime_Object = MibTableColumn
alaVRtrLdpGenGRReconnectTime = _AlaVRtrLdpGenGRReconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4, 1, 1, 2),
    _AlaVRtrLdpGenGRReconnectTime_Type()
)
alaVRtrLdpGenGRReconnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVRtrLdpGenGRReconnectTime.setStatus("current")
if mibBuilder.loadTexts:
    alaVRtrLdpGenGRReconnectTime.setUnits("seconds")


class _AlaVRtrLdpGenGRFwdStateHoldTime_Type(Unsigned32):
    """Custom type alaVRtrLdpGenGRFwdStateHoldTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1800),
    )


_AlaVRtrLdpGenGRFwdStateHoldTime_Type.__name__ = "Unsigned32"
_AlaVRtrLdpGenGRFwdStateHoldTime_Object = MibTableColumn
alaVRtrLdpGenGRFwdStateHoldTime = _AlaVRtrLdpGenGRFwdStateHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4, 1, 1, 3),
    _AlaVRtrLdpGenGRFwdStateHoldTime_Type()
)
alaVRtrLdpGenGRFwdStateHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVRtrLdpGenGRFwdStateHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    alaVRtrLdpGenGRFwdStateHoldTime.setUnits("seconds")
_AlaVRtrLdpExtendedSessionTable_Object = MibTable
alaVRtrLdpExtendedSessionTable = _AlaVRtrLdpExtendedSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    alaVRtrLdpExtendedSessionTable.setStatus("current")
_AlaVRtrLdpExtendedSessionEntry_Object = MibTableRow
alaVRtrLdpExtendedSessionEntry = _AlaVRtrLdpExtendedSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4, 2, 1)
)
alaVRtrLdpExtendedSessionEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-SERVICE-MGR-MIB", "alaVRtrLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    alaVRtrLdpExtendedSessionEntry.setStatus("current")
_AlaVRtrLdpPeerLdpId_Type = MplsLdpIdentifier
_AlaVRtrLdpPeerLdpId_Object = MibTableColumn
alaVRtrLdpPeerLdpId = _AlaVRtrLdpPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4, 2, 1, 1),
    _AlaVRtrLdpPeerLdpId_Type()
)
alaVRtrLdpPeerLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVRtrLdpPeerLdpId.setStatus("current")
_AlaVRtrLdpSessRestartInProgress_Type = TruthValue
_AlaVRtrLdpSessRestartInProgress_Object = MibTableColumn
alaVRtrLdpSessRestartInProgress = _AlaVRtrLdpSessRestartInProgress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4, 2, 1, 2),
    _AlaVRtrLdpSessRestartInProgress_Type()
)
alaVRtrLdpSessRestartInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVRtrLdpSessRestartInProgress.setStatus("current")
_AlaVRtrLdpSessFtReconTimeAdvertised_Type = Unsigned32
_AlaVRtrLdpSessFtReconTimeAdvertised_Object = MibTableColumn
alaVRtrLdpSessFtReconTimeAdvertised = _AlaVRtrLdpSessFtReconTimeAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4, 2, 1, 3),
    _AlaVRtrLdpSessFtReconTimeAdvertised_Type()
)
alaVRtrLdpSessFtReconTimeAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVRtrLdpSessFtReconTimeAdvertised.setStatus("current")
if mibBuilder.loadTexts:
    alaVRtrLdpSessFtReconTimeAdvertised.setUnits("seconds")
_AlaVRtrLdpSessFtRecoveryTimeAdvertised_Type = Unsigned32
_AlaVRtrLdpSessFtRecoveryTimeAdvertised_Object = MibTableColumn
alaVRtrLdpSessFtRecoveryTimeAdvertised = _AlaVRtrLdpSessFtRecoveryTimeAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 1, 4, 2, 1, 4),
    _AlaVRtrLdpSessFtRecoveryTimeAdvertised_Type()
)
alaVRtrLdpSessFtRecoveryTimeAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVRtrLdpSessFtRecoveryTimeAdvertised.setStatus("current")
if mibBuilder.loadTexts:
    alaVRtrLdpSessFtRecoveryTimeAdvertised.setUnits("seconds")
_AlcatelIND1ServiceMgrMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1ServiceMgrMIBConformance = _AlcatelIND1ServiceMgrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ServiceMgrMIBConformance.setStatus("current")
_AlcatelIND1ServiceMgrMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1ServiceMgrMIBGroups = _AlcatelIND1ServiceMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ServiceMgrMIBGroups.setStatus("current")
_AlcatelIND1ServiceMgrMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1ServiceMgrMIBCompliances = _AlcatelIND1ServiceMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ServiceMgrMIBCompliances.setStatus("current")

# Managed Objects groups

alaServiceMgrPortProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 1)
)
alaServiceMgrPortProfileGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortProfileStpBpduTreatment"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortProfile8021xTreatment"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortProfile8021ABTreatment"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortProfile8023adTreatment"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortProfileGvrpTreatment"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortProfileAmapTreatment"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortProfileRowStatus"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortProfileMvrpTreatment"))
)
if mibBuilder.loadTexts:
    alaServiceMgrPortProfileGroup.setStatus("current")

alaServiceMgrPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 2)
)
alaServiceMgrPortGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortMode"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortEncapType"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortPortProfileID"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortRowStatus"))
)
if mibBuilder.loadTexts:
    alaServiceMgrPortGroup.setStatus("current")

alaSapExtraInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 3)
)
alaSapExtraInfoGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaSapInfoTrusted"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaSapInfoPriority"))
)
if mibBuilder.loadTexts:
    alaSapExtraInfoGroup.setStatus("current")

alaIgmpServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 4)
)
alaIgmpServiceGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceStatus"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceQuerying"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSpoofing"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceZapping"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceVersion"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceRobustness"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceQueryInterval"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceQueryResponseInterval"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceLastMemberQueryInterval"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceRouterTimeout"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceTimeout"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceProxying"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceUnsolicitedReportInterval"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceQuerierForwarding"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceMaxGroupLimit"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceMaxGroupExceedAction"))
)
if mibBuilder.loadTexts:
    alaIgmpServiceGroup.setStatus("current")

alaIgmpMemberServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 5)
)
alaIgmpMemberServiceSapGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSapMode"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSapCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSapTimeout"))
)
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSapGroup.setStatus("current")

alaIgmpMemberServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 6)
)
alaIgmpMemberServiceSdpBindGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSdpBindMode"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSdpBindCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSdpBindTimeout"))
)
if mibBuilder.loadTexts:
    alaIgmpMemberServiceSdpBindGroup.setStatus("current")

alaIgmpStaticMemberServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 7)
)
alaIgmpStaticMemberServiceSapGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticMemberServiceSapRowStatus")
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSapGroup.setStatus("current")

alaIgmpStaticMemberServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 8)
)
alaIgmpStaticMemberServiceSdpBindGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticMemberServiceSdpBindRowStatus")
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberServiceSdpBindGroup.setStatus("current")

alaIgmpNeighborServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 9)
)
alaIgmpNeighborServiceSapGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpNeighborServiceSapCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpNeighborServiceSapTimeout"))
)
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSapGroup.setStatus("current")

alaIgmpNeighborServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 10)
)
alaIgmpNeighborServiceSdpBindGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpNeighborServiceSdpBindCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpNeighborServiceSdpBindTimeout"))
)
if mibBuilder.loadTexts:
    alaIgmpNeighborServiceSdpBindGroup.setStatus("current")

alaIgmpStaticNeighborServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 11)
)
alaIgmpStaticNeighborServiceSapGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticNeighborServiceSapRowStatus")
)
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborServiceSapGroup.setStatus("current")

alaIgmpStaticNeighborServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 12)
)
alaIgmpStaticNeighborServiceSdpBindGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticNeighborServiceSdpBindRowStatus")
)
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborServiceSdpBindGroup.setStatus("current")

alaIgmpQuerierServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 13)
)
alaIgmpQuerierServiceSapGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpQuerierServiceSapCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpQuerierServiceSapTimeout"))
)
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSapGroup.setStatus("current")

alaIgmpQuerierServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 14)
)
alaIgmpQuerierServiceSdpBindGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpQuerierServiceSdpBindCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpQuerierServiceSdpBindTimeout"))
)
if mibBuilder.loadTexts:
    alaIgmpQuerierServiceSdpBindGroup.setStatus("current")

alaIgmpStaticQuerierServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 15)
)
alaIgmpStaticQuerierServiceSapGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticQuerierServiceSapRowStatus")
)
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierServiceSapGroup.setStatus("current")

alaIgmpStaticQuerierServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 16)
)
alaIgmpStaticQuerierServiceSdpBindGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticQuerierServiceSdpBindRowStatus")
)
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierServiceSdpBindGroup.setStatus("current")

alaIgmpServiceSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 17)
)
alaIgmpServiceSourceGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceLocale"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourcePortId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceEncapValue"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceSdpId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceVcId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceType"))
)
if mibBuilder.loadTexts:
    alaIgmpServiceSourceGroup.setStatus("current")

alaIgmpServiceSapForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 18)
)
alaIgmpServiceSapForwardGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardLocale"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardPortId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardEncapValue"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardSdpId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardVcId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardType"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardNextType"))
)
if mibBuilder.loadTexts:
    alaIgmpServiceSapForwardGroup.setStatus("current")

alaIgmpServiceSdpBindForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 19)
)
alaIgmpServiceSdpBindForwardGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardLocale"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardPortId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardEncapValue"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardSdpId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardVcId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardType"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardNextType"))
)
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindForwardGroup.setStatus("current")

alaIgmpServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 20)
)
alaIgmpServiceSapGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapMaxGroupLimit"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapMaxGroupExceedAction"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapCurrentGroupCount"))
)
if mibBuilder.loadTexts:
    alaIgmpServiceSapGroup.setStatus("current")

alaIgmpServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 21)
)
alaIgmpServiceSdpBindGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindMaxGroupLimit"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindMaxGroupExceedAction"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindCurrentGroupCount"))
)
if mibBuilder.loadTexts:
    alaIgmpServiceSdpBindGroup.setStatus("current")

alaMldServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 22)
)
alaMldServiceGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceStatus"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceQuerying"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSpoofing"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceZapping"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceVersion"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceRobustness"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceQueryInterval"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceQueryResponseInterval"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceLastMemberQueryInterval"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceRouterTimeout"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceTimeout"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceProxying"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceUnsolicitedReportInterval"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceQuerierForwarding"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceMaxGroupLimit"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceMaxGroupExceedAction"))
)
if mibBuilder.loadTexts:
    alaMldServiceGroup.setStatus("current")

alaMldMemberServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 23)
)
alaMldMemberServiceSapGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSapMode"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSapCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSapTimeout"))
)
if mibBuilder.loadTexts:
    alaMldMemberServiceSapGroup.setStatus("current")

alaMldMemberServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 24)
)
alaMldMemberServiceSdpBindGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSdpBindMode"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSdpBindCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSdpBindTimeout"))
)
if mibBuilder.loadTexts:
    alaMldMemberServiceSdpBindGroup.setStatus("current")

alaMldStaticMemberServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 25)
)
alaMldStaticMemberServiceSapGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticMemberServiceSapRowStatus")
)
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSapGroup.setStatus("current")

alaMldStaticMemberServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 26)
)
alaMldStaticMemberServiceSdpBindGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticMemberServiceSdpBindRowStatus")
)
if mibBuilder.loadTexts:
    alaMldStaticMemberServiceSdpBindGroup.setStatus("current")

alaMldNeighborServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 27)
)
alaMldNeighborServiceSapGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldNeighborServiceSapCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldNeighborServiceSapTimeout"))
)
if mibBuilder.loadTexts:
    alaMldNeighborServiceSapGroup.setStatus("current")

alaMldNeighborServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 28)
)
alaMldNeighborServiceSdpBindGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldNeighborServiceSdpBindCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldNeighborServiceSdpBindTimeout"))
)
if mibBuilder.loadTexts:
    alaMldNeighborServiceSdpBindGroup.setStatus("current")

alaMldStaticNeighborServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 29)
)
alaMldStaticNeighborServiceSapGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticNeighborServiceSapRowStatus")
)
if mibBuilder.loadTexts:
    alaMldStaticNeighborServiceSapGroup.setStatus("current")

alaMldStaticNeighborServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 30)
)
alaMldStaticNeighborServiceSdpBindGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticNeighborServiceSdpBindRowStatus")
)
if mibBuilder.loadTexts:
    alaMldStaticNeighborServiceSdpBindGroup.setStatus("current")

alaMldQuerierServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 31)
)
alaMldQuerierServiceSapGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldQuerierServiceSapCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldQuerierServiceSapTimeout"))
)
if mibBuilder.loadTexts:
    alaMldQuerierServiceSapGroup.setStatus("current")

alaMldQuerierServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 32)
)
alaMldQuerierServiceSdpBindGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldQuerierServiceSdpBindCount"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldQuerierServiceSdpBindTimeout"))
)
if mibBuilder.loadTexts:
    alaMldQuerierServiceSdpBindGroup.setStatus("current")

alaMldStaticQuerierServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 33)
)
alaMldStaticQuerierServiceSapGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticQuerierServiceSapRowStatus")
)
if mibBuilder.loadTexts:
    alaMldStaticQuerierServiceSapGroup.setStatus("current")

alaMldStaticQuerierServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 34)
)
alaMldStaticQuerierServiceSdpBindGroup.setObjects(
    ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticQuerierServiceSdpBindRowStatus")
)
if mibBuilder.loadTexts:
    alaMldStaticQuerierServiceSdpBindGroup.setStatus("current")

alaMldServiceSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 35)
)
alaMldServiceSourceGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceLocale"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourcePortId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceEncapValue"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceSdpId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceVcId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceType"))
)
if mibBuilder.loadTexts:
    alaMldServiceSourceGroup.setStatus("current")

alaMldServiceSapForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 36)
)
alaMldServiceSapForwardGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardLocale"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardPortId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardEncapValue"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardSdpId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardVcId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardType"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardNextType"))
)
if mibBuilder.loadTexts:
    alaMldServiceSapForwardGroup.setStatus("current")

alaMldServiceSdpBindForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 37)
)
alaMldServiceSdpBindForwardGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardLocale"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardPortId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardEncapValue"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardSdpId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardVcId"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardType"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardNextType"))
)
if mibBuilder.loadTexts:
    alaMldServiceSdpBindForwardGroup.setStatus("current")

alaMldServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 38)
)
alaMldServiceSapGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapMaxGroupLimit"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapMaxGroupExceedAction"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapCurrentGroupCount"))
)
if mibBuilder.loadTexts:
    alaMldServiceSapGroup.setStatus("current")

alaMldServiceSdpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 39)
)
alaMldServiceSdpBindGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindMaxGroupLimit"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindMaxGroupExceedAction"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindCurrentGroupCount"))
)
if mibBuilder.loadTexts:
    alaMldServiceSdpBindGroup.setStatus("current")

alaVRtrExtendedLdpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 40)
)
alaVRtrExtendedLdpGeneralGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaVRtrLdpGenGracefulRestartSupport"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaVRtrLdpGenGRReconnectTime"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaVRtrLdpGenGRFwdStateHoldTime"))
)
if mibBuilder.loadTexts:
    alaVRtrExtendedLdpGeneralGroup.setStatus("current")

alaVRtrLdpExtendedSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 1, 41)
)
alaVRtrLdpExtendedSessionGroup.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaVRtrLdpSessRestartInProgress"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaVRtrLdpSessFtReconTimeAdvertised"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaVRtrLdpSessFtRecoveryTimeAdvertised"))
)
if mibBuilder.loadTexts:
    alaVRtrLdpExtendedSessionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1ServiceMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 51, 1, 2, 2, 1)
)
alcatelIND1ServiceMgrMIBCompliance.setObjects(
      *(("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortProfileGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaServiceMgrPortGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaSapExtraInfoGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpMemberServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticMemberServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticMemberServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpNeighborServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpNeighborServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticNeighborServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticNeighborServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpQuerierServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpQuerierServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticQuerierServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpStaticQuerierServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSourceGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapForwardGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindForwardGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaIgmpServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldMemberServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticMemberServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticMemberServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldNeighborServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldNeighborServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticNeighborServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticNeighborServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldQuerierServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldQuerierServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticQuerierServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldStaticQuerierServiceSdpBindGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSourceGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapForwardGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindForwardGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSapGroup"),
        ("ALCATEL-IND1-SERVICE-MGR-MIB", "alaMldServiceSdpBindGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1ServiceMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-SERVICE-MGR-MIB",
    **{"AluLocation": AluLocation,
       "alcatelIND1ServiceMgrMIB": alcatelIND1ServiceMgrMIB,
       "alcatelIND1ServiceMgrMIBObjects": alcatelIND1ServiceMgrMIBObjects,
       "alaServiceMgr": alaServiceMgr,
       "alaServiceMgrPortProfileTable": alaServiceMgrPortProfileTable,
       "alaServiceMgrPortProfileEntry": alaServiceMgrPortProfileEntry,
       "alaServiceMgrPortProfileID": alaServiceMgrPortProfileID,
       "alaServiceMgrPortProfileStpBpduTreatment": alaServiceMgrPortProfileStpBpduTreatment,
       "alaServiceMgrPortProfile8021xTreatment": alaServiceMgrPortProfile8021xTreatment,
       "alaServiceMgrPortProfile8021ABTreatment": alaServiceMgrPortProfile8021ABTreatment,
       "alaServiceMgrPortProfile8023adTreatment": alaServiceMgrPortProfile8023adTreatment,
       "alaServiceMgrPortProfileGvrpTreatment": alaServiceMgrPortProfileGvrpTreatment,
       "alaServiceMgrPortProfileAmapTreatment": alaServiceMgrPortProfileAmapTreatment,
       "alaServiceMgrPortProfileRowStatus": alaServiceMgrPortProfileRowStatus,
       "alaServiceMgrPortProfileMvrpTreatment": alaServiceMgrPortProfileMvrpTreatment,
       "alaServiceMgrPortTable": alaServiceMgrPortTable,
       "alaServiceMgrPortEntry": alaServiceMgrPortEntry,
       "alaServiceMgrPortID": alaServiceMgrPortID,
       "alaServiceMgrPortMode": alaServiceMgrPortMode,
       "alaServiceMgrPortEncapType": alaServiceMgrPortEncapType,
       "alaServiceMgrPortPortProfileID": alaServiceMgrPortPortProfileID,
       "alaServiceMgrPortRowStatus": alaServiceMgrPortRowStatus,
       "alaSapExtraInfoTable": alaSapExtraInfoTable,
       "alaSapExtraInfoEntry": alaSapExtraInfoEntry,
       "alaSapInfoTrusted": alaSapInfoTrusted,
       "alaSapInfoPriority": alaSapInfoPriority,
       "alaServiceMgrIgmp": alaServiceMgrIgmp,
       "alaIgmpServiceTable": alaIgmpServiceTable,
       "alaIgmpServiceEntry": alaIgmpServiceEntry,
       "alaIgmpServiceStatus": alaIgmpServiceStatus,
       "alaIgmpServiceQuerying": alaIgmpServiceQuerying,
       "alaIgmpServiceSpoofing": alaIgmpServiceSpoofing,
       "alaIgmpServiceZapping": alaIgmpServiceZapping,
       "alaIgmpServiceVersion": alaIgmpServiceVersion,
       "alaIgmpServiceRobustness": alaIgmpServiceRobustness,
       "alaIgmpServiceQueryInterval": alaIgmpServiceQueryInterval,
       "alaIgmpServiceQueryResponseInterval": alaIgmpServiceQueryResponseInterval,
       "alaIgmpServiceLastMemberQueryInterval": alaIgmpServiceLastMemberQueryInterval,
       "alaIgmpServiceRouterTimeout": alaIgmpServiceRouterTimeout,
       "alaIgmpServiceSourceTimeout": alaIgmpServiceSourceTimeout,
       "alaIgmpServiceProxying": alaIgmpServiceProxying,
       "alaIgmpServiceUnsolicitedReportInterval": alaIgmpServiceUnsolicitedReportInterval,
       "alaIgmpServiceQuerierForwarding": alaIgmpServiceQuerierForwarding,
       "alaIgmpServiceMaxGroupLimit": alaIgmpServiceMaxGroupLimit,
       "alaIgmpServiceMaxGroupExceedAction": alaIgmpServiceMaxGroupExceedAction,
       "alaIgmpMemberServiceSapTable": alaIgmpMemberServiceSapTable,
       "alaIgmpMemberServiceSapEntry": alaIgmpMemberServiceSapEntry,
       "alaIgmpMemberServiceSapGroupAddressType": alaIgmpMemberServiceSapGroupAddressType,
       "alaIgmpMemberServiceSapGroupAddress": alaIgmpMemberServiceSapGroupAddress,
       "alaIgmpMemberServiceSapSourceAddressType": alaIgmpMemberServiceSapSourceAddressType,
       "alaIgmpMemberServiceSapSourceAddress": alaIgmpMemberServiceSapSourceAddress,
       "alaIgmpMemberServiceSapMode": alaIgmpMemberServiceSapMode,
       "alaIgmpMemberServiceSapCount": alaIgmpMemberServiceSapCount,
       "alaIgmpMemberServiceSapTimeout": alaIgmpMemberServiceSapTimeout,
       "alaIgmpMemberServiceSdpBindTable": alaIgmpMemberServiceSdpBindTable,
       "alaIgmpMemberServiceSdpBindEntry": alaIgmpMemberServiceSdpBindEntry,
       "alaIgmpMemberServiceSdpBindGroupAddressType": alaIgmpMemberServiceSdpBindGroupAddressType,
       "alaIgmpMemberServiceSdpBindGroupAddress": alaIgmpMemberServiceSdpBindGroupAddress,
       "alaIgmpMemberServiceSdpBindSourceAddressType": alaIgmpMemberServiceSdpBindSourceAddressType,
       "alaIgmpMemberServiceSdpBindSourceAddress": alaIgmpMemberServiceSdpBindSourceAddress,
       "alaIgmpMemberServiceSdpBindMode": alaIgmpMemberServiceSdpBindMode,
       "alaIgmpMemberServiceSdpBindCount": alaIgmpMemberServiceSdpBindCount,
       "alaIgmpMemberServiceSdpBindTimeout": alaIgmpMemberServiceSdpBindTimeout,
       "alaIgmpStaticMemberServiceSapTable": alaIgmpStaticMemberServiceSapTable,
       "alaIgmpStaticMemberServiceSapEntry": alaIgmpStaticMemberServiceSapEntry,
       "alaIgmpStaticMemberServiceSapGroupAddressType": alaIgmpStaticMemberServiceSapGroupAddressType,
       "alaIgmpStaticMemberServiceSapGroupAddress": alaIgmpStaticMemberServiceSapGroupAddress,
       "alaIgmpStaticMemberServiceSapRowStatus": alaIgmpStaticMemberServiceSapRowStatus,
       "alaIgmpStaticMemberServiceSdpBindTable": alaIgmpStaticMemberServiceSdpBindTable,
       "alaIgmpStaticMemberServiceSdpBindEntry": alaIgmpStaticMemberServiceSdpBindEntry,
       "alaIgmpStaticMemberServiceSdpBindGroupAddressType": alaIgmpStaticMemberServiceSdpBindGroupAddressType,
       "alaIgmpStaticMemberServiceSdpBindGroupAddress": alaIgmpStaticMemberServiceSdpBindGroupAddress,
       "alaIgmpStaticMemberServiceSdpBindRowStatus": alaIgmpStaticMemberServiceSdpBindRowStatus,
       "alaIgmpNeighborServiceSapTable": alaIgmpNeighborServiceSapTable,
       "alaIgmpNeighborServiceSapEntry": alaIgmpNeighborServiceSapEntry,
       "alaIgmpNeighborServiceSapHostAddressType": alaIgmpNeighborServiceSapHostAddressType,
       "alaIgmpNeighborServiceSapHostAddress": alaIgmpNeighborServiceSapHostAddress,
       "alaIgmpNeighborServiceSapCount": alaIgmpNeighborServiceSapCount,
       "alaIgmpNeighborServiceSapTimeout": alaIgmpNeighborServiceSapTimeout,
       "alaIgmpNeighborServiceSdpBindTable": alaIgmpNeighborServiceSdpBindTable,
       "alaIgmpNeighborServiceSdpBindEntry": alaIgmpNeighborServiceSdpBindEntry,
       "alaIgmpNeighborServiceSdpBindHostAddressType": alaIgmpNeighborServiceSdpBindHostAddressType,
       "alaIgmpNeighborServiceSdpBindHostAddress": alaIgmpNeighborServiceSdpBindHostAddress,
       "alaIgmpNeighborServiceSdpBindCount": alaIgmpNeighborServiceSdpBindCount,
       "alaIgmpNeighborServiceSdpBindTimeout": alaIgmpNeighborServiceSdpBindTimeout,
       "alaIgmpStaticNeighborServiceSapTable": alaIgmpStaticNeighborServiceSapTable,
       "alaIgmpStaticNeighborServiceSapEntry": alaIgmpStaticNeighborServiceSapEntry,
       "alaIgmpStaticNeighborServiceSapRowStatus": alaIgmpStaticNeighborServiceSapRowStatus,
       "alaIgmpStaticNeighborServiceSdpBindTable": alaIgmpStaticNeighborServiceSdpBindTable,
       "alaIgmpStaticNeighborServiceSdpBindEntry": alaIgmpStaticNeighborServiceSdpBindEntry,
       "alaIgmpStaticNeighborServiceSdpBindRowStatus": alaIgmpStaticNeighborServiceSdpBindRowStatus,
       "alaIgmpQuerierServiceSapTable": alaIgmpQuerierServiceSapTable,
       "alaIgmpQuerierServiceSapEntry": alaIgmpQuerierServiceSapEntry,
       "alaIgmpQuerierServiceSapHostAddressType": alaIgmpQuerierServiceSapHostAddressType,
       "alaIgmpQuerierServiceSapHostAddress": alaIgmpQuerierServiceSapHostAddress,
       "alaIgmpQuerierServiceSapCount": alaIgmpQuerierServiceSapCount,
       "alaIgmpQuerierServiceSapTimeout": alaIgmpQuerierServiceSapTimeout,
       "alaIgmpQuerierServiceSdpBindTable": alaIgmpQuerierServiceSdpBindTable,
       "alaIgmpQuerierServiceSdpBindEntry": alaIgmpQuerierServiceSdpBindEntry,
       "alaIgmpQuerierServiceSdpBindHostAddressType": alaIgmpQuerierServiceSdpBindHostAddressType,
       "alaIgmpQuerierServiceSdpBindHostAddress": alaIgmpQuerierServiceSdpBindHostAddress,
       "alaIgmpQuerierServiceSdpBindCount": alaIgmpQuerierServiceSdpBindCount,
       "alaIgmpQuerierServiceSdpBindTimeout": alaIgmpQuerierServiceSdpBindTimeout,
       "alaIgmpStaticQuerierServiceSapTable": alaIgmpStaticQuerierServiceSapTable,
       "alaIgmpStaticQuerierServiceSapEntry": alaIgmpStaticQuerierServiceSapEntry,
       "alaIgmpStaticQuerierServiceSapRowStatus": alaIgmpStaticQuerierServiceSapRowStatus,
       "alaIgmpStaticQuerierServiceSdpBindTable": alaIgmpStaticQuerierServiceSdpBindTable,
       "alaIgmpStaticQuerierServiceSdpBindEntry": alaIgmpStaticQuerierServiceSdpBindEntry,
       "alaIgmpStaticQuerierServiceSdpBindRowStatus": alaIgmpStaticQuerierServiceSdpBindRowStatus,
       "alaIgmpServiceSourceTable": alaIgmpServiceSourceTable,
       "alaIgmpServiceSourceEntry": alaIgmpServiceSourceEntry,
       "alaIgmpServiceSourceGroupAddressType": alaIgmpServiceSourceGroupAddressType,
       "alaIgmpServiceSourceGroupAddress": alaIgmpServiceSourceGroupAddress,
       "alaIgmpServiceSourceHostAddressType": alaIgmpServiceSourceHostAddressType,
       "alaIgmpServiceSourceHostAddress": alaIgmpServiceSourceHostAddress,
       "alaIgmpServiceSourceDestAddressType": alaIgmpServiceSourceDestAddressType,
       "alaIgmpServiceSourceDestAddress": alaIgmpServiceSourceDestAddress,
       "alaIgmpServiceSourceOrigAddressType": alaIgmpServiceSourceOrigAddressType,
       "alaIgmpServiceSourceOrigAddress": alaIgmpServiceSourceOrigAddress,
       "alaIgmpServiceSourceLocale": alaIgmpServiceSourceLocale,
       "alaIgmpServiceSourcePortId": alaIgmpServiceSourcePortId,
       "alaIgmpServiceSourceEncapValue": alaIgmpServiceSourceEncapValue,
       "alaIgmpServiceSourceSdpId": alaIgmpServiceSourceSdpId,
       "alaIgmpServiceSourceVcId": alaIgmpServiceSourceVcId,
       "alaIgmpServiceSourceType": alaIgmpServiceSourceType,
       "alaIgmpServiceSapForwardTable": alaIgmpServiceSapForwardTable,
       "alaIgmpServiceSapForwardEntry": alaIgmpServiceSapForwardEntry,
       "alaIgmpServiceSapForwardLocale": alaIgmpServiceSapForwardLocale,
       "alaIgmpServiceSapForwardPortId": alaIgmpServiceSapForwardPortId,
       "alaIgmpServiceSapForwardEncapValue": alaIgmpServiceSapForwardEncapValue,
       "alaIgmpServiceSapForwardSdpId": alaIgmpServiceSapForwardSdpId,
       "alaIgmpServiceSapForwardVcId": alaIgmpServiceSapForwardVcId,
       "alaIgmpServiceSapForwardGroupAddress": alaIgmpServiceSapForwardGroupAddress,
       "alaIgmpServiceSapForwardHostAddress": alaIgmpServiceSapForwardHostAddress,
       "alaIgmpServiceSapForwardDestAddress": alaIgmpServiceSapForwardDestAddress,
       "alaIgmpServiceSapForwardOrigAddress": alaIgmpServiceSapForwardOrigAddress,
       "alaIgmpServiceSapForwardType": alaIgmpServiceSapForwardType,
       "alaIgmpServiceSapForwardNextSapPortId": alaIgmpServiceSapForwardNextSapPortId,
       "alaIgmpServiceSapForwardNextSapEncapValue": alaIgmpServiceSapForwardNextSapEncapValue,
       "alaIgmpServiceSapForwardNextType": alaIgmpServiceSapForwardNextType,
       "alaIgmpServiceSdpBindForwardTable": alaIgmpServiceSdpBindForwardTable,
       "alaIgmpServiceSdpBindForwardEntry": alaIgmpServiceSdpBindForwardEntry,
       "alaIgmpServiceSdpBindForwardLocale": alaIgmpServiceSdpBindForwardLocale,
       "alaIgmpServiceSdpBindForwardPortId": alaIgmpServiceSdpBindForwardPortId,
       "alaIgmpServiceSdpBindForwardEncapValue": alaIgmpServiceSdpBindForwardEncapValue,
       "alaIgmpServiceSdpBindForwardSdpId": alaIgmpServiceSdpBindForwardSdpId,
       "alaIgmpServiceSdpBindForwardVcId": alaIgmpServiceSdpBindForwardVcId,
       "alaIgmpServiceSdpBindForwardGroupAddress": alaIgmpServiceSdpBindForwardGroupAddress,
       "alaIgmpServiceSdpBindForwardHostAddress": alaIgmpServiceSdpBindForwardHostAddress,
       "alaIgmpServiceSdpBindForwardDestAddress": alaIgmpServiceSdpBindForwardDestAddress,
       "alaIgmpServiceSdpBindForwardOrigAddress": alaIgmpServiceSdpBindForwardOrigAddress,
       "alaIgmpServiceSdpBindForwardType": alaIgmpServiceSdpBindForwardType,
       "alaIgmpServiceSdpBindForwardNextSdpBindId": alaIgmpServiceSdpBindForwardNextSdpBindId,
       "alaIgmpServiceSdpBindForwardNextType": alaIgmpServiceSdpBindForwardNextType,
       "alaIgmpServiceSapTable": alaIgmpServiceSapTable,
       "alaIgmpServiceSapEntry": alaIgmpServiceSapEntry,
       "alaIgmpServiceSapMaxGroupLimit": alaIgmpServiceSapMaxGroupLimit,
       "alaIgmpServiceSapMaxGroupExceedAction": alaIgmpServiceSapMaxGroupExceedAction,
       "alaIgmpServiceSapCurrentGroupCount": alaIgmpServiceSapCurrentGroupCount,
       "alaIgmpServiceSdpBindTable": alaIgmpServiceSdpBindTable,
       "alaIgmpServiceSdpBindEntry": alaIgmpServiceSdpBindEntry,
       "alaIgmpServiceSdpBindMaxGroupLimit": alaIgmpServiceSdpBindMaxGroupLimit,
       "alaIgmpServiceSdpBindMaxGroupExceedAction": alaIgmpServiceSdpBindMaxGroupExceedAction,
       "alaIgmpServiceSdpBindCurrentGroupCount": alaIgmpServiceSdpBindCurrentGroupCount,
       "alaServiceMgrMld": alaServiceMgrMld,
       "alaMldServiceTable": alaMldServiceTable,
       "alaMldServiceEntry": alaMldServiceEntry,
       "alaMldServiceStatus": alaMldServiceStatus,
       "alaMldServiceQuerying": alaMldServiceQuerying,
       "alaMldServiceSpoofing": alaMldServiceSpoofing,
       "alaMldServiceZapping": alaMldServiceZapping,
       "alaMldServiceVersion": alaMldServiceVersion,
       "alaMldServiceRobustness": alaMldServiceRobustness,
       "alaMldServiceQueryInterval": alaMldServiceQueryInterval,
       "alaMldServiceQueryResponseInterval": alaMldServiceQueryResponseInterval,
       "alaMldServiceLastMemberQueryInterval": alaMldServiceLastMemberQueryInterval,
       "alaMldServiceRouterTimeout": alaMldServiceRouterTimeout,
       "alaMldServiceSourceTimeout": alaMldServiceSourceTimeout,
       "alaMldServiceProxying": alaMldServiceProxying,
       "alaMldServiceUnsolicitedReportInterval": alaMldServiceUnsolicitedReportInterval,
       "alaMldServiceQuerierForwarding": alaMldServiceQuerierForwarding,
       "alaMldServiceMaxGroupLimit": alaMldServiceMaxGroupLimit,
       "alaMldServiceMaxGroupExceedAction": alaMldServiceMaxGroupExceedAction,
       "alaMldMemberServiceSapTable": alaMldMemberServiceSapTable,
       "alaMldMemberServiceSapEntry": alaMldMemberServiceSapEntry,
       "alaMldMemberServiceSapGroupAddressType": alaMldMemberServiceSapGroupAddressType,
       "alaMldMemberServiceSapGroupAddress": alaMldMemberServiceSapGroupAddress,
       "alaMldMemberServiceSapSourceAddressType": alaMldMemberServiceSapSourceAddressType,
       "alaMldMemberServiceSapSourceAddress": alaMldMemberServiceSapSourceAddress,
       "alaMldMemberServiceSapMode": alaMldMemberServiceSapMode,
       "alaMldMemberServiceSapCount": alaMldMemberServiceSapCount,
       "alaMldMemberServiceSapTimeout": alaMldMemberServiceSapTimeout,
       "alaMldMemberServiceSdpBindTable": alaMldMemberServiceSdpBindTable,
       "alaMldMemberServiceSdpBindEntry": alaMldMemberServiceSdpBindEntry,
       "alaMldMemberServiceSdpBindGroupAddressType": alaMldMemberServiceSdpBindGroupAddressType,
       "alaMldMemberServiceSdpBindGroupAddress": alaMldMemberServiceSdpBindGroupAddress,
       "alaMldMemberServiceSdpBindSourceAddressType": alaMldMemberServiceSdpBindSourceAddressType,
       "alaMldMemberServiceSdpBindSourceAddress": alaMldMemberServiceSdpBindSourceAddress,
       "alaMldMemberServiceSdpBindMode": alaMldMemberServiceSdpBindMode,
       "alaMldMemberServiceSdpBindCount": alaMldMemberServiceSdpBindCount,
       "alaMldMemberServiceSdpBindTimeout": alaMldMemberServiceSdpBindTimeout,
       "alaMldStaticMemberServiceSapTable": alaMldStaticMemberServiceSapTable,
       "alaMldStaticMemberServiceSapEntry": alaMldStaticMemberServiceSapEntry,
       "alaMldStaticMemberServiceSapGroupAddressType": alaMldStaticMemberServiceSapGroupAddressType,
       "alaMldStaticMemberServiceSapGroupAddress": alaMldStaticMemberServiceSapGroupAddress,
       "alaMldStaticMemberServiceSapRowStatus": alaMldStaticMemberServiceSapRowStatus,
       "alaMldStaticMemberServiceSdpBindTable": alaMldStaticMemberServiceSdpBindTable,
       "alaMldStaticMemberServiceSdpBindEntry": alaMldStaticMemberServiceSdpBindEntry,
       "alaMldStaticMemberServiceSdpBindGroupAddressType": alaMldStaticMemberServiceSdpBindGroupAddressType,
       "alaMldStaticMemberServiceSdpBindGroupAddress": alaMldStaticMemberServiceSdpBindGroupAddress,
       "alaMldStaticMemberServiceSdpBindRowStatus": alaMldStaticMemberServiceSdpBindRowStatus,
       "alaMldNeighborServiceSapTable": alaMldNeighborServiceSapTable,
       "alaMldNeighborServiceSapEntry": alaMldNeighborServiceSapEntry,
       "alaMldNeighborServiceSapHostAddressType": alaMldNeighborServiceSapHostAddressType,
       "alaMldNeighborServiceSapHostAddress": alaMldNeighborServiceSapHostAddress,
       "alaMldNeighborServiceSapCount": alaMldNeighborServiceSapCount,
       "alaMldNeighborServiceSapTimeout": alaMldNeighborServiceSapTimeout,
       "alaMldNeighborServiceSdpBindTable": alaMldNeighborServiceSdpBindTable,
       "alaMldNeighborServiceSdpBindEntry": alaMldNeighborServiceSdpBindEntry,
       "alaMldNeighborServiceSdpBindHostAddressType": alaMldNeighborServiceSdpBindHostAddressType,
       "alaMldNeighborServiceSdpBindHostAddress": alaMldNeighborServiceSdpBindHostAddress,
       "alaMldNeighborServiceSdpBindCount": alaMldNeighborServiceSdpBindCount,
       "alaMldNeighborServiceSdpBindTimeout": alaMldNeighborServiceSdpBindTimeout,
       "alaMldStaticNeighborServiceSapTable": alaMldStaticNeighborServiceSapTable,
       "alaMldStaticNeighborServiceSapEntry": alaMldStaticNeighborServiceSapEntry,
       "alaMldStaticNeighborServiceSapRowStatus": alaMldStaticNeighborServiceSapRowStatus,
       "alaMldStaticNeighborServiceSdpBindTable": alaMldStaticNeighborServiceSdpBindTable,
       "alaMldStaticNeighborServiceSdpBindEntry": alaMldStaticNeighborServiceSdpBindEntry,
       "alaMldStaticNeighborServiceSdpBindRowStatus": alaMldStaticNeighborServiceSdpBindRowStatus,
       "alaMldQuerierServiceSapTable": alaMldQuerierServiceSapTable,
       "alaMldQuerierServiceSapEntry": alaMldQuerierServiceSapEntry,
       "alaMldQuerierServiceSapHostAddressType": alaMldQuerierServiceSapHostAddressType,
       "alaMldQuerierServiceSapHostAddress": alaMldQuerierServiceSapHostAddress,
       "alaMldQuerierServiceSapCount": alaMldQuerierServiceSapCount,
       "alaMldQuerierServiceSapTimeout": alaMldQuerierServiceSapTimeout,
       "alaMldQuerierServiceSdpBindTable": alaMldQuerierServiceSdpBindTable,
       "alaMldQuerierServiceSdpBindEntry": alaMldQuerierServiceSdpBindEntry,
       "alaMldQuerierServiceSdpBindHostAddressType": alaMldQuerierServiceSdpBindHostAddressType,
       "alaMldQuerierServiceSdpBindHostAddress": alaMldQuerierServiceSdpBindHostAddress,
       "alaMldQuerierServiceSdpBindCount": alaMldQuerierServiceSdpBindCount,
       "alaMldQuerierServiceSdpBindTimeout": alaMldQuerierServiceSdpBindTimeout,
       "alaMldStaticQuerierServiceSapTable": alaMldStaticQuerierServiceSapTable,
       "alaMldStaticQuerierServiceSapEntry": alaMldStaticQuerierServiceSapEntry,
       "alaMldStaticQuerierServiceSapRowStatus": alaMldStaticQuerierServiceSapRowStatus,
       "alaMldStaticQuerierServiceSdpBindTable": alaMldStaticQuerierServiceSdpBindTable,
       "alaMldStaticQuerierServiceSdpBindEntry": alaMldStaticQuerierServiceSdpBindEntry,
       "alaMldStaticQuerierServiceSdpBindRowStatus": alaMldStaticQuerierServiceSdpBindRowStatus,
       "alaMldServiceSourceTable": alaMldServiceSourceTable,
       "alaMldServiceSourceEntry": alaMldServiceSourceEntry,
       "alaMldServiceSourceGroupAddressType": alaMldServiceSourceGroupAddressType,
       "alaMldServiceSourceGroupAddress": alaMldServiceSourceGroupAddress,
       "alaMldServiceSourceHostAddressType": alaMldServiceSourceHostAddressType,
       "alaMldServiceSourceHostAddress": alaMldServiceSourceHostAddress,
       "alaMldServiceSourceDestAddressType": alaMldServiceSourceDestAddressType,
       "alaMldServiceSourceDestAddress": alaMldServiceSourceDestAddress,
       "alaMldServiceSourceOrigAddressType": alaMldServiceSourceOrigAddressType,
       "alaMldServiceSourceOrigAddress": alaMldServiceSourceOrigAddress,
       "alaMldServiceSourceLocale": alaMldServiceSourceLocale,
       "alaMldServiceSourcePortId": alaMldServiceSourcePortId,
       "alaMldServiceSourceEncapValue": alaMldServiceSourceEncapValue,
       "alaMldServiceSourceSdpId": alaMldServiceSourceSdpId,
       "alaMldServiceSourceVcId": alaMldServiceSourceVcId,
       "alaMldServiceSourceType": alaMldServiceSourceType,
       "alaMldServiceSapForwardTable": alaMldServiceSapForwardTable,
       "alaMldServiceSapForwardEntry": alaMldServiceSapForwardEntry,
       "alaMldServiceSapForwardLocale": alaMldServiceSapForwardLocale,
       "alaMldServiceSapForwardPortId": alaMldServiceSapForwardPortId,
       "alaMldServiceSapForwardEncapValue": alaMldServiceSapForwardEncapValue,
       "alaMldServiceSapForwardSdpId": alaMldServiceSapForwardSdpId,
       "alaMldServiceSapForwardVcId": alaMldServiceSapForwardVcId,
       "alaMldServiceSapForwardGroupAddress": alaMldServiceSapForwardGroupAddress,
       "alaMldServiceSapForwardHostAddress": alaMldServiceSapForwardHostAddress,
       "alaMldServiceSapForwardDestAddress": alaMldServiceSapForwardDestAddress,
       "alaMldServiceSapForwardOrigAddress": alaMldServiceSapForwardOrigAddress,
       "alaMldServiceSapForwardType": alaMldServiceSapForwardType,
       "alaMldServiceSapForwardNextSapPortId": alaMldServiceSapForwardNextSapPortId,
       "alaMldServiceSapForwardNextSapEncapValue": alaMldServiceSapForwardNextSapEncapValue,
       "alaMldServiceSapForwardNextType": alaMldServiceSapForwardNextType,
       "alaMldServiceSdpBindForwardTable": alaMldServiceSdpBindForwardTable,
       "alaMldServiceSdpBindForwardEntry": alaMldServiceSdpBindForwardEntry,
       "alaMldServiceSdpBindForwardLocale": alaMldServiceSdpBindForwardLocale,
       "alaMldServiceSdpBindForwardPortId": alaMldServiceSdpBindForwardPortId,
       "alaMldServiceSdpBindForwardEncapValue": alaMldServiceSdpBindForwardEncapValue,
       "alaMldServiceSdpBindForwardSdpId": alaMldServiceSdpBindForwardSdpId,
       "alaMldServiceSdpBindForwardVcId": alaMldServiceSdpBindForwardVcId,
       "alaMldServiceSdpBindForwardGroupAddress": alaMldServiceSdpBindForwardGroupAddress,
       "alaMldServiceSdpBindForwardHostAddress": alaMldServiceSdpBindForwardHostAddress,
       "alaMldServiceSdpBindForwardDestAddress": alaMldServiceSdpBindForwardDestAddress,
       "alaMldServiceSdpBindForwardOrigAddress": alaMldServiceSdpBindForwardOrigAddress,
       "alaMldServiceSdpBindForwardType": alaMldServiceSdpBindForwardType,
       "alaMldServiceSdpBindForwardNextSdpBindId": alaMldServiceSdpBindForwardNextSdpBindId,
       "alaMldServiceSdpBindForwardNextType": alaMldServiceSdpBindForwardNextType,
       "alaMldServiceSapTable": alaMldServiceSapTable,
       "alaMldServiceSapEntry": alaMldServiceSapEntry,
       "alaMldServiceSapMaxGroupLimit": alaMldServiceSapMaxGroupLimit,
       "alaMldServiceSapMaxGroupExceedAction": alaMldServiceSapMaxGroupExceedAction,
       "alaMldServiceSapCurrentGroupCount": alaMldServiceSapCurrentGroupCount,
       "alaMldServiceSdpBindTable": alaMldServiceSdpBindTable,
       "alaMldServiceSdpBindEntry": alaMldServiceSdpBindEntry,
       "alaMldServiceSdpBindMaxGroupLimit": alaMldServiceSdpBindMaxGroupLimit,
       "alaMldServiceSdpBindMaxGroupExceedAction": alaMldServiceSdpBindMaxGroupExceedAction,
       "alaMldServiceSdpBindCurrentGroupCount": alaMldServiceSdpBindCurrentGroupCount,
       "alaExtraLdp": alaExtraLdp,
       "alaVRtrExtendedLdpGeneralTable": alaVRtrExtendedLdpGeneralTable,
       "alaVRtrExtendedLdpGeneralEntry": alaVRtrExtendedLdpGeneralEntry,
       "alaVRtrLdpGenGracefulRestartSupport": alaVRtrLdpGenGracefulRestartSupport,
       "alaVRtrLdpGenGRReconnectTime": alaVRtrLdpGenGRReconnectTime,
       "alaVRtrLdpGenGRFwdStateHoldTime": alaVRtrLdpGenGRFwdStateHoldTime,
       "alaVRtrLdpExtendedSessionTable": alaVRtrLdpExtendedSessionTable,
       "alaVRtrLdpExtendedSessionEntry": alaVRtrLdpExtendedSessionEntry,
       "alaVRtrLdpPeerLdpId": alaVRtrLdpPeerLdpId,
       "alaVRtrLdpSessRestartInProgress": alaVRtrLdpSessRestartInProgress,
       "alaVRtrLdpSessFtReconTimeAdvertised": alaVRtrLdpSessFtReconTimeAdvertised,
       "alaVRtrLdpSessFtRecoveryTimeAdvertised": alaVRtrLdpSessFtRecoveryTimeAdvertised,
       "alcatelIND1ServiceMgrMIBConformance": alcatelIND1ServiceMgrMIBConformance,
       "alcatelIND1ServiceMgrMIBGroups": alcatelIND1ServiceMgrMIBGroups,
       "alaServiceMgrPortProfileGroup": alaServiceMgrPortProfileGroup,
       "alaServiceMgrPortGroup": alaServiceMgrPortGroup,
       "alaSapExtraInfoGroup": alaSapExtraInfoGroup,
       "alaIgmpServiceGroup": alaIgmpServiceGroup,
       "alaIgmpMemberServiceSapGroup": alaIgmpMemberServiceSapGroup,
       "alaIgmpMemberServiceSdpBindGroup": alaIgmpMemberServiceSdpBindGroup,
       "alaIgmpStaticMemberServiceSapGroup": alaIgmpStaticMemberServiceSapGroup,
       "alaIgmpStaticMemberServiceSdpBindGroup": alaIgmpStaticMemberServiceSdpBindGroup,
       "alaIgmpNeighborServiceSapGroup": alaIgmpNeighborServiceSapGroup,
       "alaIgmpNeighborServiceSdpBindGroup": alaIgmpNeighborServiceSdpBindGroup,
       "alaIgmpStaticNeighborServiceSapGroup": alaIgmpStaticNeighborServiceSapGroup,
       "alaIgmpStaticNeighborServiceSdpBindGroup": alaIgmpStaticNeighborServiceSdpBindGroup,
       "alaIgmpQuerierServiceSapGroup": alaIgmpQuerierServiceSapGroup,
       "alaIgmpQuerierServiceSdpBindGroup": alaIgmpQuerierServiceSdpBindGroup,
       "alaIgmpStaticQuerierServiceSapGroup": alaIgmpStaticQuerierServiceSapGroup,
       "alaIgmpStaticQuerierServiceSdpBindGroup": alaIgmpStaticQuerierServiceSdpBindGroup,
       "alaIgmpServiceSourceGroup": alaIgmpServiceSourceGroup,
       "alaIgmpServiceSapForwardGroup": alaIgmpServiceSapForwardGroup,
       "alaIgmpServiceSdpBindForwardGroup": alaIgmpServiceSdpBindForwardGroup,
       "alaIgmpServiceSapGroup": alaIgmpServiceSapGroup,
       "alaIgmpServiceSdpBindGroup": alaIgmpServiceSdpBindGroup,
       "alaMldServiceGroup": alaMldServiceGroup,
       "alaMldMemberServiceSapGroup": alaMldMemberServiceSapGroup,
       "alaMldMemberServiceSdpBindGroup": alaMldMemberServiceSdpBindGroup,
       "alaMldStaticMemberServiceSapGroup": alaMldStaticMemberServiceSapGroup,
       "alaMldStaticMemberServiceSdpBindGroup": alaMldStaticMemberServiceSdpBindGroup,
       "alaMldNeighborServiceSapGroup": alaMldNeighborServiceSapGroup,
       "alaMldNeighborServiceSdpBindGroup": alaMldNeighborServiceSdpBindGroup,
       "alaMldStaticNeighborServiceSapGroup": alaMldStaticNeighborServiceSapGroup,
       "alaMldStaticNeighborServiceSdpBindGroup": alaMldStaticNeighborServiceSdpBindGroup,
       "alaMldQuerierServiceSapGroup": alaMldQuerierServiceSapGroup,
       "alaMldQuerierServiceSdpBindGroup": alaMldQuerierServiceSdpBindGroup,
       "alaMldStaticQuerierServiceSapGroup": alaMldStaticQuerierServiceSapGroup,
       "alaMldStaticQuerierServiceSdpBindGroup": alaMldStaticQuerierServiceSdpBindGroup,
       "alaMldServiceSourceGroup": alaMldServiceSourceGroup,
       "alaMldServiceSapForwardGroup": alaMldServiceSapForwardGroup,
       "alaMldServiceSdpBindForwardGroup": alaMldServiceSdpBindForwardGroup,
       "alaMldServiceSapGroup": alaMldServiceSapGroup,
       "alaMldServiceSdpBindGroup": alaMldServiceSdpBindGroup,
       "alaVRtrExtendedLdpGeneralGroup": alaVRtrExtendedLdpGeneralGroup,
       "alaVRtrLdpExtendedSessionGroup": alaVRtrLdpExtendedSessionGroup,
       "alcatelIND1ServiceMgrMIBCompliances": alcatelIND1ServiceMgrMIBCompliances,
       "alcatelIND1ServiceMgrMIBCompliance": alcatelIND1ServiceMgrMIBCompliance}
)
