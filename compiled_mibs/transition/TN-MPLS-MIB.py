# SNMP MIB module (TN-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-MPLS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:00 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(TNDisplayString,
 TNInterfaceIndex,
 TNRowEditorState,
 TNUnsigned16,
 TNUnsigned8) = mibBuilder.importSymbols(
    "TN-TC",
    "TNDisplayString",
    "TNInterfaceIndex",
    "TNRowEditorState",
    "TNUnsigned16",
    "TNUnsigned8")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnMplsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144)
)
if mibBuilder.loadTexts:
    tnMplsMib.setRevisions(
        ("2015-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TNMplsStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unconfigured", 0),
          ("configured", 1),
          ("up", 2),
          ("down", 3))
    )



class TNMplsTagType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untagged", 0),
          ("ctagged", 1),
          ("stagged", 2))
    )



class TNMplsTunnelMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pipe", 0),
          ("shortpipe", 1),
          ("uniform", 2),
          ("useglobal", 3))
    )



class TNMplsVccvType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("vccv1", 1),
          ("vccv2", 2),
          ("vccv3", 3),
          ("vccv4", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TnMplsMibObjects_ObjectIdentity = ObjectIdentity
tnMplsMibObjects = _TnMplsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1)
)
_TnMplsCapabilities_ObjectIdentity = ObjectIdentity
tnMplsCapabilities = _TnMplsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 1)
)
_TnMplsCapabilitiesMaxLinks_Type = Unsigned32
_TnMplsCapabilitiesMaxLinks_Object = MibScalar
tnMplsCapabilitiesMaxLinks = _TnMplsCapabilitiesMaxLinks_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 1, 1),
    _TnMplsCapabilitiesMaxLinks_Type()
)
tnMplsCapabilitiesMaxLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsCapabilitiesMaxLinks.setStatus("current")
_TnMplsCapabilitiesMaxTunnels_Type = Unsigned32
_TnMplsCapabilitiesMaxTunnels_Object = MibScalar
tnMplsCapabilitiesMaxTunnels = _TnMplsCapabilitiesMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 1, 2),
    _TnMplsCapabilitiesMaxTunnels_Type()
)
tnMplsCapabilitiesMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsCapabilitiesMaxTunnels.setStatus("current")
_TnMplsCapabilitiesMaxPw_Type = Unsigned32
_TnMplsCapabilitiesMaxPw_Object = MibScalar
tnMplsCapabilitiesMaxPw = _TnMplsCapabilitiesMaxPw_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 1, 3),
    _TnMplsCapabilitiesMaxPw_Type()
)
tnMplsCapabilitiesMaxPw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsCapabilitiesMaxPw.setStatus("current")
_TnMplsCapabilitiesMaxLsp_Type = Unsigned32
_TnMplsCapabilitiesMaxLsp_Object = MibScalar
tnMplsCapabilitiesMaxLsp = _TnMplsCapabilitiesMaxLsp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 1, 4),
    _TnMplsCapabilitiesMaxLsp_Type()
)
tnMplsCapabilitiesMaxLsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsCapabilitiesMaxLsp.setStatus("current")
_TnMplsCapabilitiesMaxCosMap_Type = Unsigned32
_TnMplsCapabilitiesMaxCosMap_Object = MibScalar
tnMplsCapabilitiesMaxCosMap = _TnMplsCapabilitiesMaxCosMap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 1, 5),
    _TnMplsCapabilitiesMaxCosMap_Type()
)
tnMplsCapabilitiesMaxCosMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsCapabilitiesMaxCosMap.setStatus("current")
_TnMplsCapabilitiesMaxTunnelNameLen_Type = Unsigned32
_TnMplsCapabilitiesMaxTunnelNameLen_Object = MibScalar
tnMplsCapabilitiesMaxTunnelNameLen = _TnMplsCapabilitiesMaxTunnelNameLen_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 1, 6),
    _TnMplsCapabilitiesMaxTunnelNameLen_Type()
)
tnMplsCapabilitiesMaxTunnelNameLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsCapabilitiesMaxTunnelNameLen.setStatus("current")
_TnMplsConfig_ObjectIdentity = ObjectIdentity
tnMplsConfig = _TnMplsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2)
)
_TnMplsConfigGlobal_ObjectIdentity = ObjectIdentity
tnMplsConfigGlobal = _TnMplsConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 1)
)
_TnMplsConfigGlobalMain_ObjectIdentity = ObjectIdentity
tnMplsConfigGlobalMain = _TnMplsConfigGlobalMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 1, 1)
)
_TnMplsConfigGlobalMainTunnelMode_Type = TNMplsTunnelMode
_TnMplsConfigGlobalMainTunnelMode_Object = MibScalar
tnMplsConfigGlobalMainTunnelMode = _TnMplsConfigGlobalMainTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 1, 1, 1),
    _TnMplsConfigGlobalMainTunnelMode_Type()
)
tnMplsConfigGlobalMainTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigGlobalMainTunnelMode.setStatus("current")
_TnMplsConfigGlobalMainGlobalId_Type = Unsigned32
_TnMplsConfigGlobalMainGlobalId_Object = MibScalar
tnMplsConfigGlobalMainGlobalId = _TnMplsConfigGlobalMainGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 1, 1, 2),
    _TnMplsConfigGlobalMainGlobalId_Type()
)
tnMplsConfigGlobalMainGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigGlobalMainGlobalId.setStatus("current")
_TnMplsConfigGlobalMainNodeId_Type = IpAddress
_TnMplsConfigGlobalMainNodeId_Object = MibScalar
tnMplsConfigGlobalMainNodeId = _TnMplsConfigGlobalMainNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 1, 1, 3),
    _TnMplsConfigGlobalMainNodeId_Type()
)
tnMplsConfigGlobalMainNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigGlobalMainNodeId.setStatus("current")


class _TnMplsConfigGlobalMainIccCarrierCode_Type(TNDisplayString):
    """Custom type tnMplsConfigGlobalMainIccCarrierCode based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_TnMplsConfigGlobalMainIccCarrierCode_Type.__name__ = "TNDisplayString"
_TnMplsConfigGlobalMainIccCarrierCode_Object = MibScalar
tnMplsConfigGlobalMainIccCarrierCode = _TnMplsConfigGlobalMainIccCarrierCode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 1, 1, 4),
    _TnMplsConfigGlobalMainIccCarrierCode_Type()
)
tnMplsConfigGlobalMainIccCarrierCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigGlobalMainIccCarrierCode.setStatus("current")
_TnMplsConfigLink_ObjectIdentity = ObjectIdentity
tnMplsConfigLink = _TnMplsConfigLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2)
)
_TnMplsConfigLinkTable_Object = MibTable
tnMplsConfigLinkTable = _TnMplsConfigLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnMplsConfigLinkTable.setStatus("current")
_TnMplsConfigLinkEntry_Object = MibTableRow
tnMplsConfigLinkEntry = _TnMplsConfigLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1)
)
tnMplsConfigLinkEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsConfigLinkGroupIfIndex"),
)
if mibBuilder.loadTexts:
    tnMplsConfigLinkEntry.setStatus("current")
_TnMplsConfigLinkGroupIfIndex_Type = TNInterfaceIndex
_TnMplsConfigLinkGroupIfIndex_Object = MibTableColumn
tnMplsConfigLinkGroupIfIndex = _TnMplsConfigLinkGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 1),
    _TnMplsConfigLinkGroupIfIndex_Type()
)
tnMplsConfigLinkGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsConfigLinkGroupIfIndex.setStatus("current")
_TnMplsConfigLinkPort_Type = TNInterfaceIndex
_TnMplsConfigLinkPort_Object = MibTableColumn
tnMplsConfigLinkPort = _TnMplsConfigLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 2),
    _TnMplsConfigLinkPort_Type()
)
tnMplsConfigLinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkPort.setStatus("current")
_TnMplsConfigLinkMACAddressNextHop_Type = MacAddress
_TnMplsConfigLinkMACAddressNextHop_Object = MibTableColumn
tnMplsConfigLinkMACAddressNextHop = _TnMplsConfigLinkMACAddressNextHop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 3),
    _TnMplsConfigLinkMACAddressNextHop_Type()
)
tnMplsConfigLinkMACAddressNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkMACAddressNextHop.setStatus("current")
_TnMplsConfigLinkMACAddress_Type = MacAddress
_TnMplsConfigLinkMACAddress_Object = MibTableColumn
tnMplsConfigLinkMACAddress = _TnMplsConfigLinkMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 4),
    _TnMplsConfigLinkMACAddress_Type()
)
tnMplsConfigLinkMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkMACAddress.setStatus("current")
_TnMplsConfigLinkVLANTagType_Type = TNMplsTagType
_TnMplsConfigLinkVLANTagType_Object = MibTableColumn
tnMplsConfigLinkVLANTagType = _TnMplsConfigLinkVLANTagType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 5),
    _TnMplsConfigLinkVLANTagType_Type()
)
tnMplsConfigLinkVLANTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkVLANTagType.setStatus("current")
_TnMplsConfigLinkVLANId_Type = TNUnsigned16
_TnMplsConfigLinkVLANId_Object = MibTableColumn
tnMplsConfigLinkVLANId = _TnMplsConfigLinkVLANId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 6),
    _TnMplsConfigLinkVLANId_Type()
)
tnMplsConfigLinkVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkVLANId.setStatus("current")
_TnMplsConfigLinkVLANpcp_Type = Unsigned32
_TnMplsConfigLinkVLANpcp_Object = MibTableColumn
tnMplsConfigLinkVLANpcp = _TnMplsConfigLinkVLANpcp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 7),
    _TnMplsConfigLinkVLANpcp_Type()
)
tnMplsConfigLinkVLANpcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkVLANpcp.setStatus("current")
_TnMplsConfigLinkVLANdei_Type = TNUnsigned8
_TnMplsConfigLinkVLANdei_Object = MibTableColumn
tnMplsConfigLinkVLANdei = _TnMplsConfigLinkVLANdei_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 8),
    _TnMplsConfigLinkVLANdei_Type()
)
tnMplsConfigLinkVLANdei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkVLANdei.setStatus("current")
_TnMplsConfigLinkSrcNodeId_Type = IpAddress
_TnMplsConfigLinkSrcNodeId_Object = MibTableColumn
tnMplsConfigLinkSrcNodeId = _TnMplsConfigLinkSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 9),
    _TnMplsConfigLinkSrcNodeId_Type()
)
tnMplsConfigLinkSrcNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkSrcNodeId.setStatus("current")
_TnMplsConfigLinkSrcGlobalId_Type = Unsigned32
_TnMplsConfigLinkSrcGlobalId_Object = MibTableColumn
tnMplsConfigLinkSrcGlobalId = _TnMplsConfigLinkSrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 10),
    _TnMplsConfigLinkSrcGlobalId_Type()
)
tnMplsConfigLinkSrcGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkSrcGlobalId.setStatus("current")
_TnMplsConfigLinkDstNodeId_Type = IpAddress
_TnMplsConfigLinkDstNodeId_Object = MibTableColumn
tnMplsConfigLinkDstNodeId = _TnMplsConfigLinkDstNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 11),
    _TnMplsConfigLinkDstNodeId_Type()
)
tnMplsConfigLinkDstNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkDstNodeId.setStatus("current")
_TnMplsConfigLinkDstGlobalId_Type = Unsigned32
_TnMplsConfigLinkDstGlobalId_Object = MibTableColumn
tnMplsConfigLinkDstGlobalId = _TnMplsConfigLinkDstGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 12),
    _TnMplsConfigLinkDstGlobalId_Type()
)
tnMplsConfigLinkDstGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkDstGlobalId.setStatus("current")
_TnMplsConfigLinkDstIfNum_Type = Unsigned32
_TnMplsConfigLinkDstIfNum_Object = MibTableColumn
tnMplsConfigLinkDstIfNum = _TnMplsConfigLinkDstIfNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 13),
    _TnMplsConfigLinkDstIfNum_Type()
)
tnMplsConfigLinkDstIfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkDstIfNum.setStatus("current")
_TnMplsConfigLinkSrcNodeIdValid_Type = TruthValue
_TnMplsConfigLinkSrcNodeIdValid_Object = MibTableColumn
tnMplsConfigLinkSrcNodeIdValid = _TnMplsConfigLinkSrcNodeIdValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 14),
    _TnMplsConfigLinkSrcNodeIdValid_Type()
)
tnMplsConfigLinkSrcNodeIdValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkSrcNodeIdValid.setStatus("current")
_TnMplsConfigLinkSrcGlobalIdValid_Type = TruthValue
_TnMplsConfigLinkSrcGlobalIdValid_Object = MibTableColumn
tnMplsConfigLinkSrcGlobalIdValid = _TnMplsConfigLinkSrcGlobalIdValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 15),
    _TnMplsConfigLinkSrcGlobalIdValid_Type()
)
tnMplsConfigLinkSrcGlobalIdValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkSrcGlobalIdValid.setStatus("current")
_TnMplsConfigLinkDstGlobalIdValid_Type = TruthValue
_TnMplsConfigLinkDstGlobalIdValid_Object = MibTableColumn
tnMplsConfigLinkDstGlobalIdValid = _TnMplsConfigLinkDstGlobalIdValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 16),
    _TnMplsConfigLinkDstGlobalIdValid_Type()
)
tnMplsConfigLinkDstGlobalIdValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkDstGlobalIdValid.setStatus("current")
_TnMplsConfigLinkAction_Type = TNRowEditorState
_TnMplsConfigLinkAction_Object = MibTableColumn
tnMplsConfigLinkAction = _TnMplsConfigLinkAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 1, 1, 100),
    _TnMplsConfigLinkAction_Type()
)
tnMplsConfigLinkAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkAction.setStatus("current")
_TnMplsConfigLinkRowEditor_ObjectIdentity = ObjectIdentity
tnMplsConfigLinkRowEditor = _TnMplsConfigLinkRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2)
)
_TnMplsConfigLinkRowEditorGroupIfIndex_Type = TNInterfaceIndex
_TnMplsConfigLinkRowEditorGroupIfIndex_Object = MibScalar
tnMplsConfigLinkRowEditorGroupIfIndex = _TnMplsConfigLinkRowEditorGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 1),
    _TnMplsConfigLinkRowEditorGroupIfIndex_Type()
)
tnMplsConfigLinkRowEditorGroupIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorGroupIfIndex.setStatus("current")
_TnMplsConfigLinkRowEditorPort_Type = TNInterfaceIndex
_TnMplsConfigLinkRowEditorPort_Object = MibScalar
tnMplsConfigLinkRowEditorPort = _TnMplsConfigLinkRowEditorPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 2),
    _TnMplsConfigLinkRowEditorPort_Type()
)
tnMplsConfigLinkRowEditorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorPort.setStatus("current")
_TnMplsConfigLinkRowEditorMACAddressNextHop_Type = MacAddress
_TnMplsConfigLinkRowEditorMACAddressNextHop_Object = MibScalar
tnMplsConfigLinkRowEditorMACAddressNextHop = _TnMplsConfigLinkRowEditorMACAddressNextHop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 3),
    _TnMplsConfigLinkRowEditorMACAddressNextHop_Type()
)
tnMplsConfigLinkRowEditorMACAddressNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorMACAddressNextHop.setStatus("current")
_TnMplsConfigLinkRowEditorMACAddress_Type = MacAddress
_TnMplsConfigLinkRowEditorMACAddress_Object = MibScalar
tnMplsConfigLinkRowEditorMACAddress = _TnMplsConfigLinkRowEditorMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 4),
    _TnMplsConfigLinkRowEditorMACAddress_Type()
)
tnMplsConfigLinkRowEditorMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorMACAddress.setStatus("current")
_TnMplsConfigLinkRowEditorVLANTagType_Type = TNMplsTagType
_TnMplsConfigLinkRowEditorVLANTagType_Object = MibScalar
tnMplsConfigLinkRowEditorVLANTagType = _TnMplsConfigLinkRowEditorVLANTagType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 5),
    _TnMplsConfigLinkRowEditorVLANTagType_Type()
)
tnMplsConfigLinkRowEditorVLANTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorVLANTagType.setStatus("current")
_TnMplsConfigLinkRowEditorVLANId_Type = TNUnsigned16
_TnMplsConfigLinkRowEditorVLANId_Object = MibScalar
tnMplsConfigLinkRowEditorVLANId = _TnMplsConfigLinkRowEditorVLANId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 6),
    _TnMplsConfigLinkRowEditorVLANId_Type()
)
tnMplsConfigLinkRowEditorVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorVLANId.setStatus("current")
_TnMplsConfigLinkRowEditorVLANpcp_Type = Unsigned32
_TnMplsConfigLinkRowEditorVLANpcp_Object = MibScalar
tnMplsConfigLinkRowEditorVLANpcp = _TnMplsConfigLinkRowEditorVLANpcp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 7),
    _TnMplsConfigLinkRowEditorVLANpcp_Type()
)
tnMplsConfigLinkRowEditorVLANpcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorVLANpcp.setStatus("current")
_TnMplsConfigLinkRowEditorVLANdei_Type = TNUnsigned8
_TnMplsConfigLinkRowEditorVLANdei_Object = MibScalar
tnMplsConfigLinkRowEditorVLANdei = _TnMplsConfigLinkRowEditorVLANdei_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 8),
    _TnMplsConfigLinkRowEditorVLANdei_Type()
)
tnMplsConfigLinkRowEditorVLANdei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorVLANdei.setStatus("current")
_TnMplsConfigLinkRowEditorSrcNodeId_Type = IpAddress
_TnMplsConfigLinkRowEditorSrcNodeId_Object = MibScalar
tnMplsConfigLinkRowEditorSrcNodeId = _TnMplsConfigLinkRowEditorSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 9),
    _TnMplsConfigLinkRowEditorSrcNodeId_Type()
)
tnMplsConfigLinkRowEditorSrcNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorSrcNodeId.setStatus("current")
_TnMplsConfigLinkRowEditorSrcGlobalId_Type = Unsigned32
_TnMplsConfigLinkRowEditorSrcGlobalId_Object = MibScalar
tnMplsConfigLinkRowEditorSrcGlobalId = _TnMplsConfigLinkRowEditorSrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 10),
    _TnMplsConfigLinkRowEditorSrcGlobalId_Type()
)
tnMplsConfigLinkRowEditorSrcGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorSrcGlobalId.setStatus("current")
_TnMplsConfigLinkRowEditorDstNodeId_Type = IpAddress
_TnMplsConfigLinkRowEditorDstNodeId_Object = MibScalar
tnMplsConfigLinkRowEditorDstNodeId = _TnMplsConfigLinkRowEditorDstNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 11),
    _TnMplsConfigLinkRowEditorDstNodeId_Type()
)
tnMplsConfigLinkRowEditorDstNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorDstNodeId.setStatus("current")
_TnMplsConfigLinkRowEditorDstGlobalId_Type = Unsigned32
_TnMplsConfigLinkRowEditorDstGlobalId_Object = MibScalar
tnMplsConfigLinkRowEditorDstGlobalId = _TnMplsConfigLinkRowEditorDstGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 12),
    _TnMplsConfigLinkRowEditorDstGlobalId_Type()
)
tnMplsConfigLinkRowEditorDstGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorDstGlobalId.setStatus("current")
_TnMplsConfigLinkRowEditorDstIfNum_Type = Unsigned32
_TnMplsConfigLinkRowEditorDstIfNum_Object = MibScalar
tnMplsConfigLinkRowEditorDstIfNum = _TnMplsConfigLinkRowEditorDstIfNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 13),
    _TnMplsConfigLinkRowEditorDstIfNum_Type()
)
tnMplsConfigLinkRowEditorDstIfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorDstIfNum.setStatus("current")
_TnMplsConfigLinkRowEditorSrcNodeIdValid_Type = TruthValue
_TnMplsConfigLinkRowEditorSrcNodeIdValid_Object = MibScalar
tnMplsConfigLinkRowEditorSrcNodeIdValid = _TnMplsConfigLinkRowEditorSrcNodeIdValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 14),
    _TnMplsConfigLinkRowEditorSrcNodeIdValid_Type()
)
tnMplsConfigLinkRowEditorSrcNodeIdValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorSrcNodeIdValid.setStatus("current")
_TnMplsConfigLinkRowEditorSrcGlobalIdValid_Type = TruthValue
_TnMplsConfigLinkRowEditorSrcGlobalIdValid_Object = MibScalar
tnMplsConfigLinkRowEditorSrcGlobalIdValid = _TnMplsConfigLinkRowEditorSrcGlobalIdValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 15),
    _TnMplsConfigLinkRowEditorSrcGlobalIdValid_Type()
)
tnMplsConfigLinkRowEditorSrcGlobalIdValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorSrcGlobalIdValid.setStatus("current")
_TnMplsConfigLinkRowEditorDstGlobalIdValid_Type = TruthValue
_TnMplsConfigLinkRowEditorDstGlobalIdValid_Object = MibScalar
tnMplsConfigLinkRowEditorDstGlobalIdValid = _TnMplsConfigLinkRowEditorDstGlobalIdValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 16),
    _TnMplsConfigLinkRowEditorDstGlobalIdValid_Type()
)
tnMplsConfigLinkRowEditorDstGlobalIdValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorDstGlobalIdValid.setStatus("current")
_TnMplsConfigLinkRowEditorAction_Type = TNRowEditorState
_TnMplsConfigLinkRowEditorAction_Object = MibScalar
tnMplsConfigLinkRowEditorAction = _TnMplsConfigLinkRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 2, 2, 100),
    _TnMplsConfigLinkRowEditorAction_Type()
)
tnMplsConfigLinkRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorAction.setStatus("current")
_TnMplsConfigTunnel_ObjectIdentity = ObjectIdentity
tnMplsConfigTunnel = _TnMplsConfigTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3)
)
_TnMplsConfigTunnelTable_Object = MibTable
tnMplsConfigTunnelTable = _TnMplsConfigTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnMplsConfigTunnelTable.setStatus("current")
_TnMplsConfigTunnelEntry_Object = MibTableRow
tnMplsConfigTunnelEntry = _TnMplsConfigTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1)
)
tnMplsConfigTunnelEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsConfigTunnelGroupIfIndex"),
)
if mibBuilder.loadTexts:
    tnMplsConfigTunnelEntry.setStatus("current")
_TnMplsConfigTunnelGroupIfIndex_Type = TNInterfaceIndex
_TnMplsConfigTunnelGroupIfIndex_Object = MibTableColumn
tnMplsConfigTunnelGroupIfIndex = _TnMplsConfigTunnelGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 1),
    _TnMplsConfigTunnelGroupIfIndex_Type()
)
tnMplsConfigTunnelGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelGroupIfIndex.setStatus("current")


class _TnMplsConfigTunnelTunnelName_Type(TNDisplayString):
    """Custom type tnMplsConfigTunnelTunnelName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnMplsConfigTunnelTunnelName_Type.__name__ = "TNDisplayString"
_TnMplsConfigTunnelTunnelName_Object = MibTableColumn
tnMplsConfigTunnelTunnelName = _TnMplsConfigTunnelTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 2),
    _TnMplsConfigTunnelTunnelName_Type()
)
tnMplsConfigTunnelTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelTunnelName.setStatus("current")
_TnMplsConfigTunnelTunnelMode_Type = TNMplsTunnelMode
_TnMplsConfigTunnelTunnelMode_Object = MibTableColumn
tnMplsConfigTunnelTunnelMode = _TnMplsConfigTunnelTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 3),
    _TnMplsConfigTunnelTunnelMode_Type()
)
tnMplsConfigTunnelTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelTunnelMode.setStatus("current")
_TnMplsConfigTunnelSrcNodeId_Type = IpAddress
_TnMplsConfigTunnelSrcNodeId_Object = MibTableColumn
tnMplsConfigTunnelSrcNodeId = _TnMplsConfigTunnelSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 4),
    _TnMplsConfigTunnelSrcNodeId_Type()
)
tnMplsConfigTunnelSrcNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelSrcNodeId.setStatus("current")
_TnMplsConfigTunnelSrcGlobalId_Type = Unsigned32
_TnMplsConfigTunnelSrcGlobalId_Object = MibTableColumn
tnMplsConfigTunnelSrcGlobalId = _TnMplsConfigTunnelSrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 5),
    _TnMplsConfigTunnelSrcGlobalId_Type()
)
tnMplsConfigTunnelSrcGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelSrcGlobalId.setStatus("current")
_TnMplsConfigTunnelDstNodeId_Type = IpAddress
_TnMplsConfigTunnelDstNodeId_Object = MibTableColumn
tnMplsConfigTunnelDstNodeId = _TnMplsConfigTunnelDstNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 6),
    _TnMplsConfigTunnelDstNodeId_Type()
)
tnMplsConfigTunnelDstNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelDstNodeId.setStatus("current")
_TnMplsConfigTunnelDstGlobalId_Type = Unsigned32
_TnMplsConfigTunnelDstGlobalId_Object = MibTableColumn
tnMplsConfigTunnelDstGlobalId = _TnMplsConfigTunnelDstGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 7),
    _TnMplsConfigTunnelDstGlobalId_Type()
)
tnMplsConfigTunnelDstGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelDstGlobalId.setStatus("current")
_TnMplsConfigTunnelDstTunnelTpNum_Type = Unsigned32
_TnMplsConfigTunnelDstTunnelTpNum_Object = MibTableColumn
tnMplsConfigTunnelDstTunnelTpNum = _TnMplsConfigTunnelDstTunnelTpNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 8),
    _TnMplsConfigTunnelDstTunnelTpNum_Type()
)
tnMplsConfigTunnelDstTunnelTpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelDstTunnelTpNum.setStatus("current")
_TnMplsConfigTunnelSrcTunnelTpNum_Type = TNUnsigned16
_TnMplsConfigTunnelSrcTunnelTpNum_Object = MibTableColumn
tnMplsConfigTunnelSrcTunnelTpNum = _TnMplsConfigTunnelSrcTunnelTpNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 9),
    _TnMplsConfigTunnelSrcTunnelTpNum_Type()
)
tnMplsConfigTunnelSrcTunnelTpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelSrcTunnelTpNum.setStatus("current")
_TnMplsConfigTunnelSrcLspNum_Type = TNUnsigned16
_TnMplsConfigTunnelSrcLspNum_Object = MibTableColumn
tnMplsConfigTunnelSrcLspNum = _TnMplsConfigTunnelSrcLspNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 10),
    _TnMplsConfigTunnelSrcLspNum_Type()
)
tnMplsConfigTunnelSrcLspNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelSrcLspNum.setStatus("current")
_TnMplsConfigTunnelDstLspNum_Type = TNUnsigned16
_TnMplsConfigTunnelDstLspNum_Object = MibTableColumn
tnMplsConfigTunnelDstLspNum = _TnMplsConfigTunnelDstLspNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 11),
    _TnMplsConfigTunnelDstLspNum_Type()
)
tnMplsConfigTunnelDstLspNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelDstLspNum.setStatus("current")
_TnMplsConfigTunnelIsSpme_Type = TruthValue
_TnMplsConfigTunnelIsSpme_Object = MibTableColumn
tnMplsConfigTunnelIsSpme = _TnMplsConfigTunnelIsSpme_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 12),
    _TnMplsConfigTunnelIsSpme_Type()
)
tnMplsConfigTunnelIsSpme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelIsSpme.setStatus("current")
_TnMplsConfigTunnelSrcNodeIsValid_Type = TruthValue
_TnMplsConfigTunnelSrcNodeIsValid_Object = MibTableColumn
tnMplsConfigTunnelSrcNodeIsValid = _TnMplsConfigTunnelSrcNodeIsValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 13),
    _TnMplsConfigTunnelSrcNodeIsValid_Type()
)
tnMplsConfigTunnelSrcNodeIsValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelSrcNodeIsValid.setStatus("current")
_TnMplsConfigTunnelSrcGlobalIdValid_Type = TruthValue
_TnMplsConfigTunnelSrcGlobalIdValid_Object = MibTableColumn
tnMplsConfigTunnelSrcGlobalIdValid = _TnMplsConfigTunnelSrcGlobalIdValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 14),
    _TnMplsConfigTunnelSrcGlobalIdValid_Type()
)
tnMplsConfigTunnelSrcGlobalIdValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelSrcGlobalIdValid.setStatus("current")
_TnMplsConfigTunnelDstGlobalIdValid_Type = TruthValue
_TnMplsConfigTunnelDstGlobalIdValid_Object = MibTableColumn
tnMplsConfigTunnelDstGlobalIdValid = _TnMplsConfigTunnelDstGlobalIdValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 15),
    _TnMplsConfigTunnelDstGlobalIdValid_Type()
)
tnMplsConfigTunnelDstGlobalIdValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelDstGlobalIdValid.setStatus("current")


class _TnMplsConfigTunnelIngressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigTunnelIngressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigTunnelIngressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigTunnelIngressLabel_Object = MibTableColumn
tnMplsConfigTunnelIngressLabel = _TnMplsConfigTunnelIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 16),
    _TnMplsConfigTunnelIngressLabel_Type()
)
tnMplsConfigTunnelIngressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelIngressLabel.setStatus("current")


class _TnMplsConfigTunnelEgressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigTunnelEgressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigTunnelEgressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigTunnelEgressLabel_Object = MibTableColumn
tnMplsConfigTunnelEgressLabel = _TnMplsConfigTunnelEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 17),
    _TnMplsConfigTunnelEgressLabel_Type()
)
tnMplsConfigTunnelEgressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelEgressLabel.setStatus("current")
_TnMplsConfigTunnelAttachInterface_Type = TNInterfaceIndex
_TnMplsConfigTunnelAttachInterface_Object = MibTableColumn
tnMplsConfigTunnelAttachInterface = _TnMplsConfigTunnelAttachInterface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 18),
    _TnMplsConfigTunnelAttachInterface_Type()
)
tnMplsConfigTunnelAttachInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelAttachInterface.setStatus("current")


class _TnMplsConfigTunnelTrafficClass_Type(TNUnsigned8):
    """Custom type tnMplsConfigTunnelTrafficClass based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigTunnelTrafficClass_Type.__name__ = "TNUnsigned8"
_TnMplsConfigTunnelTrafficClass_Object = MibTableColumn
tnMplsConfigTunnelTrafficClass = _TnMplsConfigTunnelTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 19),
    _TnMplsConfigTunnelTrafficClass_Type()
)
tnMplsConfigTunnelTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelTrafficClass.setStatus("current")


class _TnMplsConfigTunnelTtl_Type(TNUnsigned8):
    """Custom type tnMplsConfigTunnelTtl based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnMplsConfigTunnelTtl_Type.__name__ = "TNUnsigned8"
_TnMplsConfigTunnelTtl_Object = MibTableColumn
tnMplsConfigTunnelTtl = _TnMplsConfigTunnelTtl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 20),
    _TnMplsConfigTunnelTtl_Type()
)
tnMplsConfigTunnelTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelTtl.setStatus("current")
_TnMplsConfigTunnelInCosMapId_Type = TNUnsigned8
_TnMplsConfigTunnelInCosMapId_Object = MibTableColumn
tnMplsConfigTunnelInCosMapId = _TnMplsConfigTunnelInCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 21),
    _TnMplsConfigTunnelInCosMapId_Type()
)
tnMplsConfigTunnelInCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelInCosMapId.setStatus("current")
_TnMplsConfigTunnelOutCosMapId_Type = TNUnsigned8
_TnMplsConfigTunnelOutCosMapId_Object = MibTableColumn
tnMplsConfigTunnelOutCosMapId = _TnMplsConfigTunnelOutCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 22),
    _TnMplsConfigTunnelOutCosMapId_Type()
)
tnMplsConfigTunnelOutCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelOutCosMapId.setStatus("current")
_TnMplsConfigTunnelIsLLsp_Type = TruthValue
_TnMplsConfigTunnelIsLLsp_Object = MibTableColumn
tnMplsConfigTunnelIsLLsp = _TnMplsConfigTunnelIsLLsp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 23),
    _TnMplsConfigTunnelIsLLsp_Type()
)
tnMplsConfigTunnelIsLLsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelIsLLsp.setStatus("current")


class _TnMplsConfigTunnelLLspCos_Type(TNUnsigned8):
    """Custom type tnMplsConfigTunnelLLspCos based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigTunnelLLspCos_Type.__name__ = "TNUnsigned8"
_TnMplsConfigTunnelLLspCos_Object = MibTableColumn
tnMplsConfigTunnelLLspCos = _TnMplsConfigTunnelLLspCos_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 24),
    _TnMplsConfigTunnelLLspCos_Type()
)
tnMplsConfigTunnelLLspCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelLLspCos.setStatus("current")
_TnMplsConfigTunnelAction_Type = TNRowEditorState
_TnMplsConfigTunnelAction_Object = MibTableColumn
tnMplsConfigTunnelAction = _TnMplsConfigTunnelAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 1, 1, 100),
    _TnMplsConfigTunnelAction_Type()
)
tnMplsConfigTunnelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelAction.setStatus("current")
_TnMplsConfigTunnelRowEditor_ObjectIdentity = ObjectIdentity
tnMplsConfigTunnelRowEditor = _TnMplsConfigTunnelRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2)
)
_TnMplsConfigTunnelRowEditorGroupIfIndex_Type = TNInterfaceIndex
_TnMplsConfigTunnelRowEditorGroupIfIndex_Object = MibScalar
tnMplsConfigTunnelRowEditorGroupIfIndex = _TnMplsConfigTunnelRowEditorGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 1),
    _TnMplsConfigTunnelRowEditorGroupIfIndex_Type()
)
tnMplsConfigTunnelRowEditorGroupIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorGroupIfIndex.setStatus("current")


class _TnMplsConfigTunnelRowEditorTunnelName_Type(TNDisplayString):
    """Custom type tnMplsConfigTunnelRowEditorTunnelName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnMplsConfigTunnelRowEditorTunnelName_Type.__name__ = "TNDisplayString"
_TnMplsConfigTunnelRowEditorTunnelName_Object = MibScalar
tnMplsConfigTunnelRowEditorTunnelName = _TnMplsConfigTunnelRowEditorTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 2),
    _TnMplsConfigTunnelRowEditorTunnelName_Type()
)
tnMplsConfigTunnelRowEditorTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorTunnelName.setStatus("current")
_TnMplsConfigTunnelRowEditorTunnelMode_Type = TNMplsTunnelMode
_TnMplsConfigTunnelRowEditorTunnelMode_Object = MibScalar
tnMplsConfigTunnelRowEditorTunnelMode = _TnMplsConfigTunnelRowEditorTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 3),
    _TnMplsConfigTunnelRowEditorTunnelMode_Type()
)
tnMplsConfigTunnelRowEditorTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorTunnelMode.setStatus("current")
_TnMplsConfigTunnelRowEditorSrcNodeId_Type = IpAddress
_TnMplsConfigTunnelRowEditorSrcNodeId_Object = MibScalar
tnMplsConfigTunnelRowEditorSrcNodeId = _TnMplsConfigTunnelRowEditorSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 4),
    _TnMplsConfigTunnelRowEditorSrcNodeId_Type()
)
tnMplsConfigTunnelRowEditorSrcNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorSrcNodeId.setStatus("current")
_TnMplsConfigTunnelRowEditorSrcGlobalId_Type = Unsigned32
_TnMplsConfigTunnelRowEditorSrcGlobalId_Object = MibScalar
tnMplsConfigTunnelRowEditorSrcGlobalId = _TnMplsConfigTunnelRowEditorSrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 5),
    _TnMplsConfigTunnelRowEditorSrcGlobalId_Type()
)
tnMplsConfigTunnelRowEditorSrcGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorSrcGlobalId.setStatus("current")
_TnMplsConfigTunnelRowEditorDstNodeId_Type = IpAddress
_TnMplsConfigTunnelRowEditorDstNodeId_Object = MibScalar
tnMplsConfigTunnelRowEditorDstNodeId = _TnMplsConfigTunnelRowEditorDstNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 6),
    _TnMplsConfigTunnelRowEditorDstNodeId_Type()
)
tnMplsConfigTunnelRowEditorDstNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorDstNodeId.setStatus("current")
_TnMplsConfigTunnelRowEditorDstGlobalId_Type = Unsigned32
_TnMplsConfigTunnelRowEditorDstGlobalId_Object = MibScalar
tnMplsConfigTunnelRowEditorDstGlobalId = _TnMplsConfigTunnelRowEditorDstGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 7),
    _TnMplsConfigTunnelRowEditorDstGlobalId_Type()
)
tnMplsConfigTunnelRowEditorDstGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorDstGlobalId.setStatus("current")
_TnMplsConfigTunnelRowEditorDstTunnelTpNum_Type = Unsigned32
_TnMplsConfigTunnelRowEditorDstTunnelTpNum_Object = MibScalar
tnMplsConfigTunnelRowEditorDstTunnelTpNum = _TnMplsConfigTunnelRowEditorDstTunnelTpNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 8),
    _TnMplsConfigTunnelRowEditorDstTunnelTpNum_Type()
)
tnMplsConfigTunnelRowEditorDstTunnelTpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorDstTunnelTpNum.setStatus("current")
_TnMplsConfigTunnelRowEditorSrcTunnelTpNum_Type = TNUnsigned16
_TnMplsConfigTunnelRowEditorSrcTunnelTpNum_Object = MibScalar
tnMplsConfigTunnelRowEditorSrcTunnelTpNum = _TnMplsConfigTunnelRowEditorSrcTunnelTpNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 9),
    _TnMplsConfigTunnelRowEditorSrcTunnelTpNum_Type()
)
tnMplsConfigTunnelRowEditorSrcTunnelTpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorSrcTunnelTpNum.setStatus("current")
_TnMplsConfigTunnelRowEditorSrcLspNum_Type = TNUnsigned16
_TnMplsConfigTunnelRowEditorSrcLspNum_Object = MibScalar
tnMplsConfigTunnelRowEditorSrcLspNum = _TnMplsConfigTunnelRowEditorSrcLspNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 10),
    _TnMplsConfigTunnelRowEditorSrcLspNum_Type()
)
tnMplsConfigTunnelRowEditorSrcLspNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorSrcLspNum.setStatus("current")
_TnMplsConfigTunnelRowEditorDstLspNum_Type = TNUnsigned16
_TnMplsConfigTunnelRowEditorDstLspNum_Object = MibScalar
tnMplsConfigTunnelRowEditorDstLspNum = _TnMplsConfigTunnelRowEditorDstLspNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 11),
    _TnMplsConfigTunnelRowEditorDstLspNum_Type()
)
tnMplsConfigTunnelRowEditorDstLspNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorDstLspNum.setStatus("current")
_TnMplsConfigTunnelRowEditorIsSpme_Type = TruthValue
_TnMplsConfigTunnelRowEditorIsSpme_Object = MibScalar
tnMplsConfigTunnelRowEditorIsSpme = _TnMplsConfigTunnelRowEditorIsSpme_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 12),
    _TnMplsConfigTunnelRowEditorIsSpme_Type()
)
tnMplsConfigTunnelRowEditorIsSpme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorIsSpme.setStatus("current")
_TnMplsConfigTunnelRowEditorSrcNodeIsValid_Type = TruthValue
_TnMplsConfigTunnelRowEditorSrcNodeIsValid_Object = MibScalar
tnMplsConfigTunnelRowEditorSrcNodeIsValid = _TnMplsConfigTunnelRowEditorSrcNodeIsValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 13),
    _TnMplsConfigTunnelRowEditorSrcNodeIsValid_Type()
)
tnMplsConfigTunnelRowEditorSrcNodeIsValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorSrcNodeIsValid.setStatus("current")
_TnMplsConfigTunnelRowEditorSrcGlobalIdValid_Type = TruthValue
_TnMplsConfigTunnelRowEditorSrcGlobalIdValid_Object = MibScalar
tnMplsConfigTunnelRowEditorSrcGlobalIdValid = _TnMplsConfigTunnelRowEditorSrcGlobalIdValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 14),
    _TnMplsConfigTunnelRowEditorSrcGlobalIdValid_Type()
)
tnMplsConfigTunnelRowEditorSrcGlobalIdValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorSrcGlobalIdValid.setStatus("current")
_TnMplsConfigTunnelRowEditorDstGlobalIdValid_Type = TruthValue
_TnMplsConfigTunnelRowEditorDstGlobalIdValid_Object = MibScalar
tnMplsConfigTunnelRowEditorDstGlobalIdValid = _TnMplsConfigTunnelRowEditorDstGlobalIdValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 15),
    _TnMplsConfigTunnelRowEditorDstGlobalIdValid_Type()
)
tnMplsConfigTunnelRowEditorDstGlobalIdValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorDstGlobalIdValid.setStatus("current")


class _TnMplsConfigTunnelRowEditorIngressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigTunnelRowEditorIngressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigTunnelRowEditorIngressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigTunnelRowEditorIngressLabel_Object = MibScalar
tnMplsConfigTunnelRowEditorIngressLabel = _TnMplsConfigTunnelRowEditorIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 16),
    _TnMplsConfigTunnelRowEditorIngressLabel_Type()
)
tnMplsConfigTunnelRowEditorIngressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorIngressLabel.setStatus("current")


class _TnMplsConfigTunnelRowEditorEgressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigTunnelRowEditorEgressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigTunnelRowEditorEgressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigTunnelRowEditorEgressLabel_Object = MibScalar
tnMplsConfigTunnelRowEditorEgressLabel = _TnMplsConfigTunnelRowEditorEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 17),
    _TnMplsConfigTunnelRowEditorEgressLabel_Type()
)
tnMplsConfigTunnelRowEditorEgressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorEgressLabel.setStatus("current")
_TnMplsConfigTunnelRowEditorAttachInterface_Type = TNInterfaceIndex
_TnMplsConfigTunnelRowEditorAttachInterface_Object = MibScalar
tnMplsConfigTunnelRowEditorAttachInterface = _TnMplsConfigTunnelRowEditorAttachInterface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 18),
    _TnMplsConfigTunnelRowEditorAttachInterface_Type()
)
tnMplsConfigTunnelRowEditorAttachInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorAttachInterface.setStatus("current")


class _TnMplsConfigTunnelRowEditorTrafficClass_Type(TNUnsigned8):
    """Custom type tnMplsConfigTunnelRowEditorTrafficClass based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigTunnelRowEditorTrafficClass_Type.__name__ = "TNUnsigned8"
_TnMplsConfigTunnelRowEditorTrafficClass_Object = MibScalar
tnMplsConfigTunnelRowEditorTrafficClass = _TnMplsConfigTunnelRowEditorTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 19),
    _TnMplsConfigTunnelRowEditorTrafficClass_Type()
)
tnMplsConfigTunnelRowEditorTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorTrafficClass.setStatus("current")


class _TnMplsConfigTunnelRowEditorTtl_Type(TNUnsigned8):
    """Custom type tnMplsConfigTunnelRowEditorTtl based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnMplsConfigTunnelRowEditorTtl_Type.__name__ = "TNUnsigned8"
_TnMplsConfigTunnelRowEditorTtl_Object = MibScalar
tnMplsConfigTunnelRowEditorTtl = _TnMplsConfigTunnelRowEditorTtl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 20),
    _TnMplsConfigTunnelRowEditorTtl_Type()
)
tnMplsConfigTunnelRowEditorTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorTtl.setStatus("current")
_TnMplsConfigTunnelRowEditorInCosMapId_Type = TNUnsigned8
_TnMplsConfigTunnelRowEditorInCosMapId_Object = MibScalar
tnMplsConfigTunnelRowEditorInCosMapId = _TnMplsConfigTunnelRowEditorInCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 21),
    _TnMplsConfigTunnelRowEditorInCosMapId_Type()
)
tnMplsConfigTunnelRowEditorInCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorInCosMapId.setStatus("current")
_TnMplsConfigTunnelRowEditorOutCosMapId_Type = TNUnsigned8
_TnMplsConfigTunnelRowEditorOutCosMapId_Object = MibScalar
tnMplsConfigTunnelRowEditorOutCosMapId = _TnMplsConfigTunnelRowEditorOutCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 22),
    _TnMplsConfigTunnelRowEditorOutCosMapId_Type()
)
tnMplsConfigTunnelRowEditorOutCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorOutCosMapId.setStatus("current")
_TnMplsConfigTunnelRowEditorIsLLsp_Type = TruthValue
_TnMplsConfigTunnelRowEditorIsLLsp_Object = MibScalar
tnMplsConfigTunnelRowEditorIsLLsp = _TnMplsConfigTunnelRowEditorIsLLsp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 23),
    _TnMplsConfigTunnelRowEditorIsLLsp_Type()
)
tnMplsConfigTunnelRowEditorIsLLsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorIsLLsp.setStatus("current")


class _TnMplsConfigTunnelRowEditorLLspCos_Type(TNUnsigned8):
    """Custom type tnMplsConfigTunnelRowEditorLLspCos based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigTunnelRowEditorLLspCos_Type.__name__ = "TNUnsigned8"
_TnMplsConfigTunnelRowEditorLLspCos_Object = MibScalar
tnMplsConfigTunnelRowEditorLLspCos = _TnMplsConfigTunnelRowEditorLLspCos_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 24),
    _TnMplsConfigTunnelRowEditorLLspCos_Type()
)
tnMplsConfigTunnelRowEditorLLspCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorLLspCos.setStatus("current")
_TnMplsConfigTunnelRowEditorAction_Type = TNRowEditorState
_TnMplsConfigTunnelRowEditorAction_Object = MibScalar
tnMplsConfigTunnelRowEditorAction = _TnMplsConfigTunnelRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 3, 2, 100),
    _TnMplsConfigTunnelRowEditorAction_Type()
)
tnMplsConfigTunnelRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorAction.setStatus("current")
_TnMplsConfigLsp_ObjectIdentity = ObjectIdentity
tnMplsConfigLsp = _TnMplsConfigLsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4)
)
_TnMplsConfigLspTable_Object = MibTable
tnMplsConfigLspTable = _TnMplsConfigLspTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnMplsConfigLspTable.setStatus("current")
_TnMplsConfigLspEntry_Object = MibTableRow
tnMplsConfigLspEntry = _TnMplsConfigLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1)
)
tnMplsConfigLspEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsConfigLspGroupIndex"),
)
if mibBuilder.loadTexts:
    tnMplsConfigLspEntry.setStatus("current")


class _TnMplsConfigLspGroupIndex_Type(Integer32):
    """Custom type tnMplsConfigLspGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnMplsConfigLspGroupIndex_Type.__name__ = "Integer32"
_TnMplsConfigLspGroupIndex_Object = MibTableColumn
tnMplsConfigLspGroupIndex = _TnMplsConfigLspGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 1),
    _TnMplsConfigLspGroupIndex_Type()
)
tnMplsConfigLspGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsConfigLspGroupIndex.setStatus("current")


class _TnMplsConfigLspXcName_Type(TNDisplayString):
    """Custom type tnMplsConfigLspXcName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnMplsConfigLspXcName_Type.__name__ = "TNDisplayString"
_TnMplsConfigLspXcName_Object = MibTableColumn
tnMplsConfigLspXcName = _TnMplsConfigLspXcName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 2),
    _TnMplsConfigLspXcName_Type()
)
tnMplsConfigLspXcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspXcName.setStatus("current")
_TnMplsConfigLspSrcNodeId_Type = IpAddress
_TnMplsConfigLspSrcNodeId_Object = MibTableColumn
tnMplsConfigLspSrcNodeId = _TnMplsConfigLspSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 3),
    _TnMplsConfigLspSrcNodeId_Type()
)
tnMplsConfigLspSrcNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspSrcNodeId.setStatus("current")
_TnMplsConfigLspSrcNodeIdIsDefined_Type = TruthValue
_TnMplsConfigLspSrcNodeIdIsDefined_Object = MibTableColumn
tnMplsConfigLspSrcNodeIdIsDefined = _TnMplsConfigLspSrcNodeIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 4),
    _TnMplsConfigLspSrcNodeIdIsDefined_Type()
)
tnMplsConfigLspSrcNodeIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspSrcNodeIdIsDefined.setStatus("current")
_TnMplsConfigLspSrcGlobalId_Type = Unsigned32
_TnMplsConfigLspSrcGlobalId_Object = MibTableColumn
tnMplsConfigLspSrcGlobalId = _TnMplsConfigLspSrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 5),
    _TnMplsConfigLspSrcGlobalId_Type()
)
tnMplsConfigLspSrcGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspSrcGlobalId.setStatus("current")
_TnMplsConfigLspSrcGlobalIdIsDefined_Type = TruthValue
_TnMplsConfigLspSrcGlobalIdIsDefined_Object = MibTableColumn
tnMplsConfigLspSrcGlobalIdIsDefined = _TnMplsConfigLspSrcGlobalIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 6),
    _TnMplsConfigLspSrcGlobalIdIsDefined_Type()
)
tnMplsConfigLspSrcGlobalIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspSrcGlobalIdIsDefined.setStatus("current")
_TnMplsConfigLspSrcTunnelTpNum_Type = TNUnsigned16
_TnMplsConfigLspSrcTunnelTpNum_Object = MibTableColumn
tnMplsConfigLspSrcTunnelTpNum = _TnMplsConfigLspSrcTunnelTpNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 7),
    _TnMplsConfigLspSrcTunnelTpNum_Type()
)
tnMplsConfigLspSrcTunnelTpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspSrcTunnelTpNum.setStatus("current")
_TnMplsConfigLspDstNodeId_Type = IpAddress
_TnMplsConfigLspDstNodeId_Object = MibTableColumn
tnMplsConfigLspDstNodeId = _TnMplsConfigLspDstNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 8),
    _TnMplsConfigLspDstNodeId_Type()
)
tnMplsConfigLspDstNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspDstNodeId.setStatus("current")
_TnMplsConfigLspDstGlobalId_Type = Unsigned32
_TnMplsConfigLspDstGlobalId_Object = MibTableColumn
tnMplsConfigLspDstGlobalId = _TnMplsConfigLspDstGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 9),
    _TnMplsConfigLspDstGlobalId_Type()
)
tnMplsConfigLspDstGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspDstGlobalId.setStatus("current")
_TnMplsConfigLspDstGlobalIdIsDefined_Type = TruthValue
_TnMplsConfigLspDstGlobalIdIsDefined_Object = MibTableColumn
tnMplsConfigLspDstGlobalIdIsDefined = _TnMplsConfigLspDstGlobalIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 10),
    _TnMplsConfigLspDstGlobalIdIsDefined_Type()
)
tnMplsConfigLspDstGlobalIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspDstGlobalIdIsDefined.setStatus("current")
_TnMplsConfigLspDstTunnelTpNum_Type = TNUnsigned16
_TnMplsConfigLspDstTunnelTpNum_Object = MibTableColumn
tnMplsConfigLspDstTunnelTpNum = _TnMplsConfigLspDstTunnelTpNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 11),
    _TnMplsConfigLspDstTunnelTpNum_Type()
)
tnMplsConfigLspDstTunnelTpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspDstTunnelTpNum.setStatus("current")
_TnMplsConfigLspSrcLspNumber_Type = TNUnsigned16
_TnMplsConfigLspSrcLspNumber_Object = MibTableColumn
tnMplsConfigLspSrcLspNumber = _TnMplsConfigLspSrcLspNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 12),
    _TnMplsConfigLspSrcLspNumber_Type()
)
tnMplsConfigLspSrcLspNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspSrcLspNumber.setStatus("current")
_TnMplsConfigLspDstLspNumber_Type = TNUnsigned16
_TnMplsConfigLspDstLspNumber_Object = MibTableColumn
tnMplsConfigLspDstLspNumber = _TnMplsConfigLspDstLspNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 13),
    _TnMplsConfigLspDstLspNumber_Type()
)
tnMplsConfigLspDstLspNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspDstLspNumber.setStatus("current")


class _TnMplsConfigLspForwardIngressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigLspForwardIngressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigLspForwardIngressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigLspForwardIngressLabel_Object = MibTableColumn
tnMplsConfigLspForwardIngressLabel = _TnMplsConfigLspForwardIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 14),
    _TnMplsConfigLspForwardIngressLabel_Type()
)
tnMplsConfigLspForwardIngressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspForwardIngressLabel.setStatus("current")


class _TnMplsConfigLspForwardEgressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigLspForwardEgressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigLspForwardEgressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigLspForwardEgressLabel_Object = MibTableColumn
tnMplsConfigLspForwardEgressLabel = _TnMplsConfigLspForwardEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 15),
    _TnMplsConfigLspForwardEgressLabel_Type()
)
tnMplsConfigLspForwardEgressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspForwardEgressLabel.setStatus("current")
_TnMplsConfigLspForwardAttachInterface_Type = TNInterfaceIndex
_TnMplsConfigLspForwardAttachInterface_Object = MibTableColumn
tnMplsConfigLspForwardAttachInterface = _TnMplsConfigLspForwardAttachInterface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 16),
    _TnMplsConfigLspForwardAttachInterface_Type()
)
tnMplsConfigLspForwardAttachInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspForwardAttachInterface.setStatus("current")
_TnMplsConfigLspForwardInCosMapId_Type = TNUnsigned8
_TnMplsConfigLspForwardInCosMapId_Object = MibTableColumn
tnMplsConfigLspForwardInCosMapId = _TnMplsConfigLspForwardInCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 17),
    _TnMplsConfigLspForwardInCosMapId_Type()
)
tnMplsConfigLspForwardInCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspForwardInCosMapId.setStatus("current")
_TnMplsConfigLspForwardOutCosMapId_Type = TNUnsigned8
_TnMplsConfigLspForwardOutCosMapId_Object = MibTableColumn
tnMplsConfigLspForwardOutCosMapId = _TnMplsConfigLspForwardOutCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 18),
    _TnMplsConfigLspForwardOutCosMapId_Type()
)
tnMplsConfigLspForwardOutCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspForwardOutCosMapId.setStatus("current")
_TnMplsConfigLspForwardIsLLsp_Type = TruthValue
_TnMplsConfigLspForwardIsLLsp_Object = MibTableColumn
tnMplsConfigLspForwardIsLLsp = _TnMplsConfigLspForwardIsLLsp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 19),
    _TnMplsConfigLspForwardIsLLsp_Type()
)
tnMplsConfigLspForwardIsLLsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspForwardIsLLsp.setStatus("current")


class _TnMplsConfigLspForwardHQoSId_Type(TNUnsigned16):
    """Custom type tnMplsConfigLspForwardHQoSId based on TNUnsigned16"""
    subtypeSpec = TNUnsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TnMplsConfigLspForwardHQoSId_Type.__name__ = "TNUnsigned16"
_TnMplsConfigLspForwardHQoSId_Object = MibTableColumn
tnMplsConfigLspForwardHQoSId = _TnMplsConfigLspForwardHQoSId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 20),
    _TnMplsConfigLspForwardHQoSId_Type()
)
tnMplsConfigLspForwardHQoSId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspForwardHQoSId.setStatus("current")


class _TnMplsConfigLspForwardLLspCos_Type(TNUnsigned8):
    """Custom type tnMplsConfigLspForwardLLspCos based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigLspForwardLLspCos_Type.__name__ = "TNUnsigned8"
_TnMplsConfigLspForwardLLspCos_Object = MibTableColumn
tnMplsConfigLspForwardLLspCos = _TnMplsConfigLspForwardLLspCos_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 21),
    _TnMplsConfigLspForwardLLspCos_Type()
)
tnMplsConfigLspForwardLLspCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspForwardLLspCos.setStatus("current")


class _TnMplsConfigLspReverseIngressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigLspReverseIngressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigLspReverseIngressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigLspReverseIngressLabel_Object = MibTableColumn
tnMplsConfigLspReverseIngressLabel = _TnMplsConfigLspReverseIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 22),
    _TnMplsConfigLspReverseIngressLabel_Type()
)
tnMplsConfigLspReverseIngressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspReverseIngressLabel.setStatus("current")


class _TnMplsConfigLspReverseEgressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigLspReverseEgressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigLspReverseEgressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigLspReverseEgressLabel_Object = MibTableColumn
tnMplsConfigLspReverseEgressLabel = _TnMplsConfigLspReverseEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 23),
    _TnMplsConfigLspReverseEgressLabel_Type()
)
tnMplsConfigLspReverseEgressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspReverseEgressLabel.setStatus("current")
_TnMplsConfigLspReverseAttachInterface_Type = TNInterfaceIndex
_TnMplsConfigLspReverseAttachInterface_Object = MibTableColumn
tnMplsConfigLspReverseAttachInterface = _TnMplsConfigLspReverseAttachInterface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 24),
    _TnMplsConfigLspReverseAttachInterface_Type()
)
tnMplsConfigLspReverseAttachInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspReverseAttachInterface.setStatus("current")
_TnMplsConfigLspReverseInCosMapId_Type = TNUnsigned8
_TnMplsConfigLspReverseInCosMapId_Object = MibTableColumn
tnMplsConfigLspReverseInCosMapId = _TnMplsConfigLspReverseInCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 25),
    _TnMplsConfigLspReverseInCosMapId_Type()
)
tnMplsConfigLspReverseInCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspReverseInCosMapId.setStatus("current")
_TnMplsConfigLspReverseOutCosMapId_Type = TNUnsigned8
_TnMplsConfigLspReverseOutCosMapId_Object = MibTableColumn
tnMplsConfigLspReverseOutCosMapId = _TnMplsConfigLspReverseOutCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 26),
    _TnMplsConfigLspReverseOutCosMapId_Type()
)
tnMplsConfigLspReverseOutCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspReverseOutCosMapId.setStatus("current")
_TnMplsConfigLspReverseIsLLsp_Type = TruthValue
_TnMplsConfigLspReverseIsLLsp_Object = MibTableColumn
tnMplsConfigLspReverseIsLLsp = _TnMplsConfigLspReverseIsLLsp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 27),
    _TnMplsConfigLspReverseIsLLsp_Type()
)
tnMplsConfigLspReverseIsLLsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspReverseIsLLsp.setStatus("current")


class _TnMplsConfigLspReverseLLspCos_Type(TNUnsigned8):
    """Custom type tnMplsConfigLspReverseLLspCos based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigLspReverseLLspCos_Type.__name__ = "TNUnsigned8"
_TnMplsConfigLspReverseLLspCos_Object = MibTableColumn
tnMplsConfigLspReverseLLspCos = _TnMplsConfigLspReverseLLspCos_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 28),
    _TnMplsConfigLspReverseLLspCos_Type()
)
tnMplsConfigLspReverseLLspCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspReverseLLspCos.setStatus("current")


class _TnMplsConfigLspReverseHQoSId_Type(TNUnsigned16):
    """Custom type tnMplsConfigLspReverseHQoSId based on TNUnsigned16"""
    subtypeSpec = TNUnsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TnMplsConfigLspReverseHQoSId_Type.__name__ = "TNUnsigned16"
_TnMplsConfigLspReverseHQoSId_Object = MibTableColumn
tnMplsConfigLspReverseHQoSId = _TnMplsConfigLspReverseHQoSId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 29),
    _TnMplsConfigLspReverseHQoSId_Type()
)
tnMplsConfigLspReverseHQoSId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspReverseHQoSId.setStatus("current")
_TnMplsConfigLspAction_Type = TNRowEditorState
_TnMplsConfigLspAction_Object = MibTableColumn
tnMplsConfigLspAction = _TnMplsConfigLspAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 1, 1, 100),
    _TnMplsConfigLspAction_Type()
)
tnMplsConfigLspAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspAction.setStatus("current")
_TnMplsConfigLspRowEditor_ObjectIdentity = ObjectIdentity
tnMplsConfigLspRowEditor = _TnMplsConfigLspRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2)
)


class _TnMplsConfigLspRowEditorGroupIndex_Type(Integer32):
    """Custom type tnMplsConfigLspRowEditorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnMplsConfigLspRowEditorGroupIndex_Type.__name__ = "Integer32"
_TnMplsConfigLspRowEditorGroupIndex_Object = MibScalar
tnMplsConfigLspRowEditorGroupIndex = _TnMplsConfigLspRowEditorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 1),
    _TnMplsConfigLspRowEditorGroupIndex_Type()
)
tnMplsConfigLspRowEditorGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorGroupIndex.setStatus("current")


class _TnMplsConfigLspRowEditorXcName_Type(TNDisplayString):
    """Custom type tnMplsConfigLspRowEditorXcName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnMplsConfigLspRowEditorXcName_Type.__name__ = "TNDisplayString"
_TnMplsConfigLspRowEditorXcName_Object = MibScalar
tnMplsConfigLspRowEditorXcName = _TnMplsConfigLspRowEditorXcName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 2),
    _TnMplsConfigLspRowEditorXcName_Type()
)
tnMplsConfigLspRowEditorXcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorXcName.setStatus("current")
_TnMplsConfigLspRowEditorSrcNodeId_Type = IpAddress
_TnMplsConfigLspRowEditorSrcNodeId_Object = MibScalar
tnMplsConfigLspRowEditorSrcNodeId = _TnMplsConfigLspRowEditorSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 3),
    _TnMplsConfigLspRowEditorSrcNodeId_Type()
)
tnMplsConfigLspRowEditorSrcNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorSrcNodeId.setStatus("current")
_TnMplsConfigLspRowEditorSrcNodeIdIsDefined_Type = TruthValue
_TnMplsConfigLspRowEditorSrcNodeIdIsDefined_Object = MibScalar
tnMplsConfigLspRowEditorSrcNodeIdIsDefined = _TnMplsConfigLspRowEditorSrcNodeIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 4),
    _TnMplsConfigLspRowEditorSrcNodeIdIsDefined_Type()
)
tnMplsConfigLspRowEditorSrcNodeIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorSrcNodeIdIsDefined.setStatus("current")
_TnMplsConfigLspRowEditorSrcGlobalId_Type = Unsigned32
_TnMplsConfigLspRowEditorSrcGlobalId_Object = MibScalar
tnMplsConfigLspRowEditorSrcGlobalId = _TnMplsConfigLspRowEditorSrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 5),
    _TnMplsConfigLspRowEditorSrcGlobalId_Type()
)
tnMplsConfigLspRowEditorSrcGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorSrcGlobalId.setStatus("current")
_TnMplsConfigLspRowEditorSrcGlobalIdIsDefined_Type = TruthValue
_TnMplsConfigLspRowEditorSrcGlobalIdIsDefined_Object = MibScalar
tnMplsConfigLspRowEditorSrcGlobalIdIsDefined = _TnMplsConfigLspRowEditorSrcGlobalIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 6),
    _TnMplsConfigLspRowEditorSrcGlobalIdIsDefined_Type()
)
tnMplsConfigLspRowEditorSrcGlobalIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorSrcGlobalIdIsDefined.setStatus("current")
_TnMplsConfigLspRowEditorSrcTunnelTpNum_Type = TNUnsigned16
_TnMplsConfigLspRowEditorSrcTunnelTpNum_Object = MibScalar
tnMplsConfigLspRowEditorSrcTunnelTpNum = _TnMplsConfigLspRowEditorSrcTunnelTpNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 7),
    _TnMplsConfigLspRowEditorSrcTunnelTpNum_Type()
)
tnMplsConfigLspRowEditorSrcTunnelTpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorSrcTunnelTpNum.setStatus("current")
_TnMplsConfigLspRowEditorDstNodeId_Type = IpAddress
_TnMplsConfigLspRowEditorDstNodeId_Object = MibScalar
tnMplsConfigLspRowEditorDstNodeId = _TnMplsConfigLspRowEditorDstNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 8),
    _TnMplsConfigLspRowEditorDstNodeId_Type()
)
tnMplsConfigLspRowEditorDstNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorDstNodeId.setStatus("current")
_TnMplsConfigLspRowEditorDstGlobalId_Type = Unsigned32
_TnMplsConfigLspRowEditorDstGlobalId_Object = MibScalar
tnMplsConfigLspRowEditorDstGlobalId = _TnMplsConfigLspRowEditorDstGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 9),
    _TnMplsConfigLspRowEditorDstGlobalId_Type()
)
tnMplsConfigLspRowEditorDstGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorDstGlobalId.setStatus("current")
_TnMplsConfigLspRowEditorDstGlobalIdIsDefined_Type = TruthValue
_TnMplsConfigLspRowEditorDstGlobalIdIsDefined_Object = MibScalar
tnMplsConfigLspRowEditorDstGlobalIdIsDefined = _TnMplsConfigLspRowEditorDstGlobalIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 10),
    _TnMplsConfigLspRowEditorDstGlobalIdIsDefined_Type()
)
tnMplsConfigLspRowEditorDstGlobalIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorDstGlobalIdIsDefined.setStatus("current")
_TnMplsConfigLspRowEditorDstTunnelTpNum_Type = TNUnsigned16
_TnMplsConfigLspRowEditorDstTunnelTpNum_Object = MibScalar
tnMplsConfigLspRowEditorDstTunnelTpNum = _TnMplsConfigLspRowEditorDstTunnelTpNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 11),
    _TnMplsConfigLspRowEditorDstTunnelTpNum_Type()
)
tnMplsConfigLspRowEditorDstTunnelTpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorDstTunnelTpNum.setStatus("current")
_TnMplsConfigLspRowEditorSrcLspNumber_Type = TNUnsigned16
_TnMplsConfigLspRowEditorSrcLspNumber_Object = MibScalar
tnMplsConfigLspRowEditorSrcLspNumber = _TnMplsConfigLspRowEditorSrcLspNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 12),
    _TnMplsConfigLspRowEditorSrcLspNumber_Type()
)
tnMplsConfigLspRowEditorSrcLspNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorSrcLspNumber.setStatus("current")
_TnMplsConfigLspRowEditorDstLspNumber_Type = TNUnsigned16
_TnMplsConfigLspRowEditorDstLspNumber_Object = MibScalar
tnMplsConfigLspRowEditorDstLspNumber = _TnMplsConfigLspRowEditorDstLspNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 13),
    _TnMplsConfigLspRowEditorDstLspNumber_Type()
)
tnMplsConfigLspRowEditorDstLspNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorDstLspNumber.setStatus("current")


class _TnMplsConfigLspRowEditorForwardIngressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigLspRowEditorForwardIngressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigLspRowEditorForwardIngressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigLspRowEditorForwardIngressLabel_Object = MibScalar
tnMplsConfigLspRowEditorForwardIngressLabel = _TnMplsConfigLspRowEditorForwardIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 14),
    _TnMplsConfigLspRowEditorForwardIngressLabel_Type()
)
tnMplsConfigLspRowEditorForwardIngressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorForwardIngressLabel.setStatus("current")


class _TnMplsConfigLspRowEditorForwardEgressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigLspRowEditorForwardEgressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigLspRowEditorForwardEgressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigLspRowEditorForwardEgressLabel_Object = MibScalar
tnMplsConfigLspRowEditorForwardEgressLabel = _TnMplsConfigLspRowEditorForwardEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 15),
    _TnMplsConfigLspRowEditorForwardEgressLabel_Type()
)
tnMplsConfigLspRowEditorForwardEgressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorForwardEgressLabel.setStatus("current")
_TnMplsConfigLspRowEditorForwardAttachInterface_Type = TNInterfaceIndex
_TnMplsConfigLspRowEditorForwardAttachInterface_Object = MibScalar
tnMplsConfigLspRowEditorForwardAttachInterface = _TnMplsConfigLspRowEditorForwardAttachInterface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 16),
    _TnMplsConfigLspRowEditorForwardAttachInterface_Type()
)
tnMplsConfigLspRowEditorForwardAttachInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorForwardAttachInterface.setStatus("current")
_TnMplsConfigLspRowEditorForwardInCosMapId_Type = TNUnsigned8
_TnMplsConfigLspRowEditorForwardInCosMapId_Object = MibScalar
tnMplsConfigLspRowEditorForwardInCosMapId = _TnMplsConfigLspRowEditorForwardInCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 17),
    _TnMplsConfigLspRowEditorForwardInCosMapId_Type()
)
tnMplsConfigLspRowEditorForwardInCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorForwardInCosMapId.setStatus("current")
_TnMplsConfigLspRowEditorForwardOutCosMapId_Type = TNUnsigned8
_TnMplsConfigLspRowEditorForwardOutCosMapId_Object = MibScalar
tnMplsConfigLspRowEditorForwardOutCosMapId = _TnMplsConfigLspRowEditorForwardOutCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 18),
    _TnMplsConfigLspRowEditorForwardOutCosMapId_Type()
)
tnMplsConfigLspRowEditorForwardOutCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorForwardOutCosMapId.setStatus("current")
_TnMplsConfigLspRowEditorForwardIsLLsp_Type = TruthValue
_TnMplsConfigLspRowEditorForwardIsLLsp_Object = MibScalar
tnMplsConfigLspRowEditorForwardIsLLsp = _TnMplsConfigLspRowEditorForwardIsLLsp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 19),
    _TnMplsConfigLspRowEditorForwardIsLLsp_Type()
)
tnMplsConfigLspRowEditorForwardIsLLsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorForwardIsLLsp.setStatus("current")


class _TnMplsConfigLspRowEditorForwardHQoSId_Type(TNUnsigned16):
    """Custom type tnMplsConfigLspRowEditorForwardHQoSId based on TNUnsigned16"""
    subtypeSpec = TNUnsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TnMplsConfigLspRowEditorForwardHQoSId_Type.__name__ = "TNUnsigned16"
_TnMplsConfigLspRowEditorForwardHQoSId_Object = MibScalar
tnMplsConfigLspRowEditorForwardHQoSId = _TnMplsConfigLspRowEditorForwardHQoSId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 20),
    _TnMplsConfigLspRowEditorForwardHQoSId_Type()
)
tnMplsConfigLspRowEditorForwardHQoSId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorForwardHQoSId.setStatus("current")


class _TnMplsConfigLspRowEditorForwardLLspCos_Type(TNUnsigned8):
    """Custom type tnMplsConfigLspRowEditorForwardLLspCos based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigLspRowEditorForwardLLspCos_Type.__name__ = "TNUnsigned8"
_TnMplsConfigLspRowEditorForwardLLspCos_Object = MibScalar
tnMplsConfigLspRowEditorForwardLLspCos = _TnMplsConfigLspRowEditorForwardLLspCos_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 21),
    _TnMplsConfigLspRowEditorForwardLLspCos_Type()
)
tnMplsConfigLspRowEditorForwardLLspCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorForwardLLspCos.setStatus("current")


class _TnMplsConfigLspRowEditorReverseIngressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigLspRowEditorReverseIngressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigLspRowEditorReverseIngressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigLspRowEditorReverseIngressLabel_Object = MibScalar
tnMplsConfigLspRowEditorReverseIngressLabel = _TnMplsConfigLspRowEditorReverseIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 22),
    _TnMplsConfigLspRowEditorReverseIngressLabel_Type()
)
tnMplsConfigLspRowEditorReverseIngressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorReverseIngressLabel.setStatus("current")


class _TnMplsConfigLspRowEditorReverseEgressLabel_Type(Unsigned32):
    """Custom type tnMplsConfigLspRowEditorReverseEgressLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigLspRowEditorReverseEgressLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigLspRowEditorReverseEgressLabel_Object = MibScalar
tnMplsConfigLspRowEditorReverseEgressLabel = _TnMplsConfigLspRowEditorReverseEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 23),
    _TnMplsConfigLspRowEditorReverseEgressLabel_Type()
)
tnMplsConfigLspRowEditorReverseEgressLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorReverseEgressLabel.setStatus("current")
_TnMplsConfigLspRowEditorReverseAttachInterface_Type = TNInterfaceIndex
_TnMplsConfigLspRowEditorReverseAttachInterface_Object = MibScalar
tnMplsConfigLspRowEditorReverseAttachInterface = _TnMplsConfigLspRowEditorReverseAttachInterface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 24),
    _TnMplsConfigLspRowEditorReverseAttachInterface_Type()
)
tnMplsConfigLspRowEditorReverseAttachInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorReverseAttachInterface.setStatus("current")
_TnMplsConfigLspRowEditorReverseInCosMapId_Type = TNUnsigned8
_TnMplsConfigLspRowEditorReverseInCosMapId_Object = MibScalar
tnMplsConfigLspRowEditorReverseInCosMapId = _TnMplsConfigLspRowEditorReverseInCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 25),
    _TnMplsConfigLspRowEditorReverseInCosMapId_Type()
)
tnMplsConfigLspRowEditorReverseInCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorReverseInCosMapId.setStatus("current")
_TnMplsConfigLspRowEditorReverseOutCosMapId_Type = TNUnsigned8
_TnMplsConfigLspRowEditorReverseOutCosMapId_Object = MibScalar
tnMplsConfigLspRowEditorReverseOutCosMapId = _TnMplsConfigLspRowEditorReverseOutCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 26),
    _TnMplsConfigLspRowEditorReverseOutCosMapId_Type()
)
tnMplsConfigLspRowEditorReverseOutCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorReverseOutCosMapId.setStatus("current")
_TnMplsConfigLspRowEditorReverseIsLLsp_Type = TruthValue
_TnMplsConfigLspRowEditorReverseIsLLsp_Object = MibScalar
tnMplsConfigLspRowEditorReverseIsLLsp = _TnMplsConfigLspRowEditorReverseIsLLsp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 27),
    _TnMplsConfigLspRowEditorReverseIsLLsp_Type()
)
tnMplsConfigLspRowEditorReverseIsLLsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorReverseIsLLsp.setStatus("current")


class _TnMplsConfigLspRowEditorReverseLLspCos_Type(TNUnsigned8):
    """Custom type tnMplsConfigLspRowEditorReverseLLspCos based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigLspRowEditorReverseLLspCos_Type.__name__ = "TNUnsigned8"
_TnMplsConfigLspRowEditorReverseLLspCos_Object = MibScalar
tnMplsConfigLspRowEditorReverseLLspCos = _TnMplsConfigLspRowEditorReverseLLspCos_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 28),
    _TnMplsConfigLspRowEditorReverseLLspCos_Type()
)
tnMplsConfigLspRowEditorReverseLLspCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorReverseLLspCos.setStatus("current")


class _TnMplsConfigLspRowEditorReverseHQoSId_Type(TNUnsigned16):
    """Custom type tnMplsConfigLspRowEditorReverseHQoSId based on TNUnsigned16"""
    subtypeSpec = TNUnsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TnMplsConfigLspRowEditorReverseHQoSId_Type.__name__ = "TNUnsigned16"
_TnMplsConfigLspRowEditorReverseHQoSId_Object = MibScalar
tnMplsConfigLspRowEditorReverseHQoSId = _TnMplsConfigLspRowEditorReverseHQoSId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 29),
    _TnMplsConfigLspRowEditorReverseHQoSId_Type()
)
tnMplsConfigLspRowEditorReverseHQoSId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorReverseHQoSId.setStatus("current")
_TnMplsConfigLspRowEditorAction_Type = TNRowEditorState
_TnMplsConfigLspRowEditorAction_Object = MibScalar
tnMplsConfigLspRowEditorAction = _TnMplsConfigLspRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 4, 2, 100),
    _TnMplsConfigLspRowEditorAction_Type()
)
tnMplsConfigLspRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorAction.setStatus("current")
_TnMplsConfigPw_ObjectIdentity = ObjectIdentity
tnMplsConfigPw = _TnMplsConfigPw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5)
)
_TnMplsConfigPwTable_Object = MibTable
tnMplsConfigPwTable = _TnMplsConfigPwTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tnMplsConfigPwTable.setStatus("current")
_TnMplsConfigPwEntry_Object = MibTableRow
tnMplsConfigPwEntry = _TnMplsConfigPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1)
)
tnMplsConfigPwEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsConfigPwGroupIfIndex"),
)
if mibBuilder.loadTexts:
    tnMplsConfigPwEntry.setStatus("current")
_TnMplsConfigPwGroupIfIndex_Type = TNInterfaceIndex
_TnMplsConfigPwGroupIfIndex_Object = MibTableColumn
tnMplsConfigPwGroupIfIndex = _TnMplsConfigPwGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 1),
    _TnMplsConfigPwGroupIfIndex_Type()
)
tnMplsConfigPwGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsConfigPwGroupIfIndex.setStatus("current")


class _TnMplsConfigPwInLabel_Type(Unsigned32):
    """Custom type tnMplsConfigPwInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigPwInLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigPwInLabel_Object = MibTableColumn
tnMplsConfigPwInLabel = _TnMplsConfigPwInLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 2),
    _TnMplsConfigPwInLabel_Type()
)
tnMplsConfigPwInLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwInLabel.setStatus("current")


class _TnMplsConfigPwOutLabel_Type(Unsigned32):
    """Custom type tnMplsConfigPwOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigPwOutLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigPwOutLabel_Object = MibTableColumn
tnMplsConfigPwOutLabel = _TnMplsConfigPwOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 3),
    _TnMplsConfigPwOutLabel_Type()
)
tnMplsConfigPwOutLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwOutLabel.setStatus("current")


class _TnMplsConfigPwControlWord_Type(Unsigned32):
    """Custom type tnMplsConfigPwControlWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_TnMplsConfigPwControlWord_Type.__name__ = "Unsigned32"
_TnMplsConfigPwControlWord_Object = MibTableColumn
tnMplsConfigPwControlWord = _TnMplsConfigPwControlWord_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 4),
    _TnMplsConfigPwControlWord_Type()
)
tnMplsConfigPwControlWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwControlWord.setStatus("current")
_TnMplsConfigPwUseControlWord_Type = TruthValue
_TnMplsConfigPwUseControlWord_Object = MibTableColumn
tnMplsConfigPwUseControlWord = _TnMplsConfigPwUseControlWord_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 5),
    _TnMplsConfigPwUseControlWord_Type()
)
tnMplsConfigPwUseControlWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwUseControlWord.setStatus("current")
_TnMplsConfigPwTunnelMode_Type = TNMplsTunnelMode
_TnMplsConfigPwTunnelMode_Object = MibTableColumn
tnMplsConfigPwTunnelMode = _TnMplsConfigPwTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 6),
    _TnMplsConfigPwTunnelMode_Type()
)
tnMplsConfigPwTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwTunnelMode.setStatus("current")


class _TnMplsConfigPwTrafficClass_Type(TNUnsigned8):
    """Custom type tnMplsConfigPwTrafficClass based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigPwTrafficClass_Type.__name__ = "TNUnsigned8"
_TnMplsConfigPwTrafficClass_Object = MibTableColumn
tnMplsConfigPwTrafficClass = _TnMplsConfigPwTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 7),
    _TnMplsConfigPwTrafficClass_Type()
)
tnMplsConfigPwTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwTrafficClass.setStatus("current")


class _TnMplsConfigPwTtl_Type(TNUnsigned8):
    """Custom type tnMplsConfigPwTtl based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnMplsConfigPwTtl_Type.__name__ = "TNUnsigned8"
_TnMplsConfigPwTtl_Object = MibTableColumn
tnMplsConfigPwTtl = _TnMplsConfigPwTtl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 8),
    _TnMplsConfigPwTtl_Type()
)
tnMplsConfigPwTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwTtl.setStatus("current")
_TnMplsConfigPwInCosMapId_Type = TNUnsigned8
_TnMplsConfigPwInCosMapId_Object = MibTableColumn
tnMplsConfigPwInCosMapId = _TnMplsConfigPwInCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 9),
    _TnMplsConfigPwInCosMapId_Type()
)
tnMplsConfigPwInCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwInCosMapId.setStatus("current")
_TnMplsConfigPwOutCosMapId_Type = TNUnsigned8
_TnMplsConfigPwOutCosMapId_Object = MibTableColumn
tnMplsConfigPwOutCosMapId = _TnMplsConfigPwOutCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 10),
    _TnMplsConfigPwOutCosMapId_Type()
)
tnMplsConfigPwOutCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwOutCosMapId.setStatus("current")
_TnMplsConfigPwIsLLsp_Type = TruthValue
_TnMplsConfigPwIsLLsp_Object = MibTableColumn
tnMplsConfigPwIsLLsp = _TnMplsConfigPwIsLLsp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 11),
    _TnMplsConfigPwIsLLsp_Type()
)
tnMplsConfigPwIsLLsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwIsLLsp.setStatus("current")


class _TnMplsConfigPwLLspCos_Type(TNUnsigned8):
    """Custom type tnMplsConfigPwLLspCos based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigPwLLspCos_Type.__name__ = "TNUnsigned8"
_TnMplsConfigPwLLspCos_Object = MibTableColumn
tnMplsConfigPwLLspCos = _TnMplsConfigPwLLspCos_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 12),
    _TnMplsConfigPwLLspCos_Type()
)
tnMplsConfigPwLLspCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwLLspCos.setStatus("current")
_TnMplsConfigPwAttachInterface_Type = TNInterfaceIndex
_TnMplsConfigPwAttachInterface_Object = MibTableColumn
tnMplsConfigPwAttachInterface = _TnMplsConfigPwAttachInterface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 13),
    _TnMplsConfigPwAttachInterface_Type()
)
tnMplsConfigPwAttachInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwAttachInterface.setStatus("current")
_TnMplsConfigPwStitchPwInterface_Type = TNInterfaceIndex
_TnMplsConfigPwStitchPwInterface_Object = MibTableColumn
tnMplsConfigPwStitchPwInterface = _TnMplsConfigPwStitchPwInterface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 14),
    _TnMplsConfigPwStitchPwInterface_Type()
)
tnMplsConfigPwStitchPwInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwStitchPwInterface.setStatus("current")
_TnMplsConfigPwVccvType_Type = TNMplsVccvType
_TnMplsConfigPwVccvType_Object = MibTableColumn
tnMplsConfigPwVccvType = _TnMplsConfigPwVccvType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 15),
    _TnMplsConfigPwVccvType_Type()
)
tnMplsConfigPwVccvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwVccvType.setStatus("current")


class _TnMplsConfigPwHQoSId_Type(TNUnsigned16):
    """Custom type tnMplsConfigPwHQoSId based on TNUnsigned16"""
    subtypeSpec = TNUnsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TnMplsConfigPwHQoSId_Type.__name__ = "TNUnsigned16"
_TnMplsConfigPwHQoSId_Object = MibTableColumn
tnMplsConfigPwHQoSId = _TnMplsConfigPwHQoSId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 16),
    _TnMplsConfigPwHQoSId_Type()
)
tnMplsConfigPwHQoSId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwHQoSId.setStatus("current")
_TnMplsConfigPwSrcNodeId_Type = IpAddress
_TnMplsConfigPwSrcNodeId_Object = MibTableColumn
tnMplsConfigPwSrcNodeId = _TnMplsConfigPwSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 17),
    _TnMplsConfigPwSrcNodeId_Type()
)
tnMplsConfigPwSrcNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwSrcNodeId.setStatus("current")
_TnMplsConfigPwSrcNodeIdIsDefined_Type = TruthValue
_TnMplsConfigPwSrcNodeIdIsDefined_Object = MibTableColumn
tnMplsConfigPwSrcNodeIdIsDefined = _TnMplsConfigPwSrcNodeIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 18),
    _TnMplsConfigPwSrcNodeIdIsDefined_Type()
)
tnMplsConfigPwSrcNodeIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwSrcNodeIdIsDefined.setStatus("current")
_TnMplsConfigPwSrcGlobalId_Type = Unsigned32
_TnMplsConfigPwSrcGlobalId_Object = MibTableColumn
tnMplsConfigPwSrcGlobalId = _TnMplsConfigPwSrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 19),
    _TnMplsConfigPwSrcGlobalId_Type()
)
tnMplsConfigPwSrcGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwSrcGlobalId.setStatus("current")
_TnMplsConfigPwSrcGlobalIdIsDefined_Type = TruthValue
_TnMplsConfigPwSrcGlobalIdIsDefined_Object = MibTableColumn
tnMplsConfigPwSrcGlobalIdIsDefined = _TnMplsConfigPwSrcGlobalIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 20),
    _TnMplsConfigPwSrcGlobalIdIsDefined_Type()
)
tnMplsConfigPwSrcGlobalIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwSrcGlobalIdIsDefined.setStatus("current")
_TnMplsConfigPwDstNodeId_Type = IpAddress
_TnMplsConfigPwDstNodeId_Object = MibTableColumn
tnMplsConfigPwDstNodeId = _TnMplsConfigPwDstNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 21),
    _TnMplsConfigPwDstNodeId_Type()
)
tnMplsConfigPwDstNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwDstNodeId.setStatus("current")
_TnMplsConfigPwDstGlobalId_Type = Unsigned32
_TnMplsConfigPwDstGlobalId_Object = MibTableColumn
tnMplsConfigPwDstGlobalId = _TnMplsConfigPwDstGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 22),
    _TnMplsConfigPwDstGlobalId_Type()
)
tnMplsConfigPwDstGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwDstGlobalId.setStatus("current")
_TnMplsConfigPwDstGlobalIdIsDefined_Type = TruthValue
_TnMplsConfigPwDstGlobalIdIsDefined_Object = MibTableColumn
tnMplsConfigPwDstGlobalIdIsDefined = _TnMplsConfigPwDstGlobalIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 23),
    _TnMplsConfigPwDstGlobalIdIsDefined_Type()
)
tnMplsConfigPwDstGlobalIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwDstGlobalIdIsDefined.setStatus("current")
_TnMplsConfigPwSrcAcId_Type = Unsigned32
_TnMplsConfigPwSrcAcId_Object = MibTableColumn
tnMplsConfigPwSrcAcId = _TnMplsConfigPwSrcAcId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 24),
    _TnMplsConfigPwSrcAcId_Type()
)
tnMplsConfigPwSrcAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwSrcAcId.setStatus("current")
_TnMplsConfigPwDstAcId_Type = Unsigned32
_TnMplsConfigPwDstAcId_Object = MibTableColumn
tnMplsConfigPwDstAcId = _TnMplsConfigPwDstAcId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 25),
    _TnMplsConfigPwDstAcId_Type()
)
tnMplsConfigPwDstAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwDstAcId.setStatus("current")


class _TnMplsConfigPwSrcAgiValue_Type(OctetString):
    """Custom type tnMplsConfigPwSrcAgiValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TnMplsConfigPwSrcAgiValue_Type.__name__ = "OctetString"
_TnMplsConfigPwSrcAgiValue_Object = MibTableColumn
tnMplsConfigPwSrcAgiValue = _TnMplsConfigPwSrcAgiValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 26),
    _TnMplsConfigPwSrcAgiValue_Type()
)
tnMplsConfigPwSrcAgiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwSrcAgiValue.setStatus("current")


class _TnMplsConfigPwDstAgiValue_Type(OctetString):
    """Custom type tnMplsConfigPwDstAgiValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TnMplsConfigPwDstAgiValue_Type.__name__ = "OctetString"
_TnMplsConfigPwDstAgiValue_Object = MibTableColumn
tnMplsConfigPwDstAgiValue = _TnMplsConfigPwDstAgiValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 27),
    _TnMplsConfigPwDstAgiValue_Type()
)
tnMplsConfigPwDstAgiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwDstAgiValue.setStatus("current")
_TnMplsConfigPwSrcAgiType_Type = TNUnsigned8
_TnMplsConfigPwSrcAgiType_Object = MibTableColumn
tnMplsConfigPwSrcAgiType = _TnMplsConfigPwSrcAgiType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 28),
    _TnMplsConfigPwSrcAgiType_Type()
)
tnMplsConfigPwSrcAgiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwSrcAgiType.setStatus("current")


class _TnMplsConfigPwSrcAgiLength_Type(TNUnsigned8):
    """Custom type tnMplsConfigPwSrcAgiLength based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigPwSrcAgiLength_Type.__name__ = "TNUnsigned8"
_TnMplsConfigPwSrcAgiLength_Object = MibTableColumn
tnMplsConfigPwSrcAgiLength = _TnMplsConfigPwSrcAgiLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 29),
    _TnMplsConfigPwSrcAgiLength_Type()
)
tnMplsConfigPwSrcAgiLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwSrcAgiLength.setStatus("current")
_TnMplsConfigPwDstAgiType_Type = TNUnsigned8
_TnMplsConfigPwDstAgiType_Object = MibTableColumn
tnMplsConfigPwDstAgiType = _TnMplsConfigPwDstAgiType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 30),
    _TnMplsConfigPwDstAgiType_Type()
)
tnMplsConfigPwDstAgiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwDstAgiType.setStatus("current")


class _TnMplsConfigPwDstAgiLength_Type(TNUnsigned8):
    """Custom type tnMplsConfigPwDstAgiLength based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigPwDstAgiLength_Type.__name__ = "TNUnsigned8"
_TnMplsConfigPwDstAgiLength_Object = MibTableColumn
tnMplsConfigPwDstAgiLength = _TnMplsConfigPwDstAgiLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 31),
    _TnMplsConfigPwDstAgiLength_Type()
)
tnMplsConfigPwDstAgiLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwDstAgiLength.setStatus("current")
_TnMplsConfigPwAction_Type = TNRowEditorState
_TnMplsConfigPwAction_Object = MibTableColumn
tnMplsConfigPwAction = _TnMplsConfigPwAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 1, 1, 100),
    _TnMplsConfigPwAction_Type()
)
tnMplsConfigPwAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwAction.setStatus("current")
_TnMplsConfigPwRowEditor_ObjectIdentity = ObjectIdentity
tnMplsConfigPwRowEditor = _TnMplsConfigPwRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2)
)
_TnMplsConfigPwRowEditorGroupIfIndex_Type = TNInterfaceIndex
_TnMplsConfigPwRowEditorGroupIfIndex_Object = MibScalar
tnMplsConfigPwRowEditorGroupIfIndex = _TnMplsConfigPwRowEditorGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 1),
    _TnMplsConfigPwRowEditorGroupIfIndex_Type()
)
tnMplsConfigPwRowEditorGroupIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorGroupIfIndex.setStatus("current")


class _TnMplsConfigPwRowEditorInLabel_Type(Unsigned32):
    """Custom type tnMplsConfigPwRowEditorInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigPwRowEditorInLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigPwRowEditorInLabel_Object = MibScalar
tnMplsConfigPwRowEditorInLabel = _TnMplsConfigPwRowEditorInLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 2),
    _TnMplsConfigPwRowEditorInLabel_Type()
)
tnMplsConfigPwRowEditorInLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorInLabel.setStatus("current")


class _TnMplsConfigPwRowEditorOutLabel_Type(Unsigned32):
    """Custom type tnMplsConfigPwRowEditorOutLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_TnMplsConfigPwRowEditorOutLabel_Type.__name__ = "Unsigned32"
_TnMplsConfigPwRowEditorOutLabel_Object = MibScalar
tnMplsConfigPwRowEditorOutLabel = _TnMplsConfigPwRowEditorOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 3),
    _TnMplsConfigPwRowEditorOutLabel_Type()
)
tnMplsConfigPwRowEditorOutLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorOutLabel.setStatus("current")


class _TnMplsConfigPwRowEditorControlWord_Type(Unsigned32):
    """Custom type tnMplsConfigPwRowEditorControlWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_TnMplsConfigPwRowEditorControlWord_Type.__name__ = "Unsigned32"
_TnMplsConfigPwRowEditorControlWord_Object = MibScalar
tnMplsConfigPwRowEditorControlWord = _TnMplsConfigPwRowEditorControlWord_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 4),
    _TnMplsConfigPwRowEditorControlWord_Type()
)
tnMplsConfigPwRowEditorControlWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorControlWord.setStatus("current")
_TnMplsConfigPwRowEditorUseControlWord_Type = TruthValue
_TnMplsConfigPwRowEditorUseControlWord_Object = MibScalar
tnMplsConfigPwRowEditorUseControlWord = _TnMplsConfigPwRowEditorUseControlWord_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 5),
    _TnMplsConfigPwRowEditorUseControlWord_Type()
)
tnMplsConfigPwRowEditorUseControlWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorUseControlWord.setStatus("current")
_TnMplsConfigPwRowEditorTunnelMode_Type = TNMplsTunnelMode
_TnMplsConfigPwRowEditorTunnelMode_Object = MibScalar
tnMplsConfigPwRowEditorTunnelMode = _TnMplsConfigPwRowEditorTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 6),
    _TnMplsConfigPwRowEditorTunnelMode_Type()
)
tnMplsConfigPwRowEditorTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorTunnelMode.setStatus("current")


class _TnMplsConfigPwRowEditorTrafficClass_Type(TNUnsigned8):
    """Custom type tnMplsConfigPwRowEditorTrafficClass based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigPwRowEditorTrafficClass_Type.__name__ = "TNUnsigned8"
_TnMplsConfigPwRowEditorTrafficClass_Object = MibScalar
tnMplsConfigPwRowEditorTrafficClass = _TnMplsConfigPwRowEditorTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 7),
    _TnMplsConfigPwRowEditorTrafficClass_Type()
)
tnMplsConfigPwRowEditorTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorTrafficClass.setStatus("current")


class _TnMplsConfigPwRowEditorTtl_Type(TNUnsigned8):
    """Custom type tnMplsConfigPwRowEditorTtl based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnMplsConfigPwRowEditorTtl_Type.__name__ = "TNUnsigned8"
_TnMplsConfigPwRowEditorTtl_Object = MibScalar
tnMplsConfigPwRowEditorTtl = _TnMplsConfigPwRowEditorTtl_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 8),
    _TnMplsConfigPwRowEditorTtl_Type()
)
tnMplsConfigPwRowEditorTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorTtl.setStatus("current")
_TnMplsConfigPwRowEditorInCosMapId_Type = TNUnsigned8
_TnMplsConfigPwRowEditorInCosMapId_Object = MibScalar
tnMplsConfigPwRowEditorInCosMapId = _TnMplsConfigPwRowEditorInCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 9),
    _TnMplsConfigPwRowEditorInCosMapId_Type()
)
tnMplsConfigPwRowEditorInCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorInCosMapId.setStatus("current")
_TnMplsConfigPwRowEditorOutCosMapId_Type = TNUnsigned8
_TnMplsConfigPwRowEditorOutCosMapId_Object = MibScalar
tnMplsConfigPwRowEditorOutCosMapId = _TnMplsConfigPwRowEditorOutCosMapId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 10),
    _TnMplsConfigPwRowEditorOutCosMapId_Type()
)
tnMplsConfigPwRowEditorOutCosMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorOutCosMapId.setStatus("current")
_TnMplsConfigPwRowEditorIsLLsp_Type = TruthValue
_TnMplsConfigPwRowEditorIsLLsp_Object = MibScalar
tnMplsConfigPwRowEditorIsLLsp = _TnMplsConfigPwRowEditorIsLLsp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 11),
    _TnMplsConfigPwRowEditorIsLLsp_Type()
)
tnMplsConfigPwRowEditorIsLLsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorIsLLsp.setStatus("current")


class _TnMplsConfigPwRowEditorLLspCos_Type(TNUnsigned8):
    """Custom type tnMplsConfigPwRowEditorLLspCos based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigPwRowEditorLLspCos_Type.__name__ = "TNUnsigned8"
_TnMplsConfigPwRowEditorLLspCos_Object = MibScalar
tnMplsConfigPwRowEditorLLspCos = _TnMplsConfigPwRowEditorLLspCos_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 12),
    _TnMplsConfigPwRowEditorLLspCos_Type()
)
tnMplsConfigPwRowEditorLLspCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorLLspCos.setStatus("current")
_TnMplsConfigPwRowEditorAttachInterface_Type = TNInterfaceIndex
_TnMplsConfigPwRowEditorAttachInterface_Object = MibScalar
tnMplsConfigPwRowEditorAttachInterface = _TnMplsConfigPwRowEditorAttachInterface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 13),
    _TnMplsConfigPwRowEditorAttachInterface_Type()
)
tnMplsConfigPwRowEditorAttachInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorAttachInterface.setStatus("current")
_TnMplsConfigPwRowEditorStitchPwInterface_Type = TNInterfaceIndex
_TnMplsConfigPwRowEditorStitchPwInterface_Object = MibScalar
tnMplsConfigPwRowEditorStitchPwInterface = _TnMplsConfigPwRowEditorStitchPwInterface_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 14),
    _TnMplsConfigPwRowEditorStitchPwInterface_Type()
)
tnMplsConfigPwRowEditorStitchPwInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorStitchPwInterface.setStatus("current")
_TnMplsConfigPwRowEditorVccvType_Type = TNMplsVccvType
_TnMplsConfigPwRowEditorVccvType_Object = MibScalar
tnMplsConfigPwRowEditorVccvType = _TnMplsConfigPwRowEditorVccvType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 15),
    _TnMplsConfigPwRowEditorVccvType_Type()
)
tnMplsConfigPwRowEditorVccvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorVccvType.setStatus("current")


class _TnMplsConfigPwRowEditorHQoSId_Type(TNUnsigned16):
    """Custom type tnMplsConfigPwRowEditorHQoSId based on TNUnsigned16"""
    subtypeSpec = TNUnsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TnMplsConfigPwRowEditorHQoSId_Type.__name__ = "TNUnsigned16"
_TnMplsConfigPwRowEditorHQoSId_Object = MibScalar
tnMplsConfigPwRowEditorHQoSId = _TnMplsConfigPwRowEditorHQoSId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 16),
    _TnMplsConfigPwRowEditorHQoSId_Type()
)
tnMplsConfigPwRowEditorHQoSId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorHQoSId.setStatus("current")
_TnMplsConfigPwRowEditorSrcNodeId_Type = IpAddress
_TnMplsConfigPwRowEditorSrcNodeId_Object = MibScalar
tnMplsConfigPwRowEditorSrcNodeId = _TnMplsConfigPwRowEditorSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 17),
    _TnMplsConfigPwRowEditorSrcNodeId_Type()
)
tnMplsConfigPwRowEditorSrcNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorSrcNodeId.setStatus("current")
_TnMplsConfigPwRowEditorSrcNodeIdIsDefined_Type = TruthValue
_TnMplsConfigPwRowEditorSrcNodeIdIsDefined_Object = MibScalar
tnMplsConfigPwRowEditorSrcNodeIdIsDefined = _TnMplsConfigPwRowEditorSrcNodeIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 18),
    _TnMplsConfigPwRowEditorSrcNodeIdIsDefined_Type()
)
tnMplsConfigPwRowEditorSrcNodeIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorSrcNodeIdIsDefined.setStatus("current")
_TnMplsConfigPwRowEditorSrcGlobalId_Type = Unsigned32
_TnMplsConfigPwRowEditorSrcGlobalId_Object = MibScalar
tnMplsConfigPwRowEditorSrcGlobalId = _TnMplsConfigPwRowEditorSrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 19),
    _TnMplsConfigPwRowEditorSrcGlobalId_Type()
)
tnMplsConfigPwRowEditorSrcGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorSrcGlobalId.setStatus("current")
_TnMplsConfigPwRowEditorSrcGlobalIdIsDefined_Type = TruthValue
_TnMplsConfigPwRowEditorSrcGlobalIdIsDefined_Object = MibScalar
tnMplsConfigPwRowEditorSrcGlobalIdIsDefined = _TnMplsConfigPwRowEditorSrcGlobalIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 20),
    _TnMplsConfigPwRowEditorSrcGlobalIdIsDefined_Type()
)
tnMplsConfigPwRowEditorSrcGlobalIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorSrcGlobalIdIsDefined.setStatus("current")
_TnMplsConfigPwRowEditorDstNodeId_Type = IpAddress
_TnMplsConfigPwRowEditorDstNodeId_Object = MibScalar
tnMplsConfigPwRowEditorDstNodeId = _TnMplsConfigPwRowEditorDstNodeId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 21),
    _TnMplsConfigPwRowEditorDstNodeId_Type()
)
tnMplsConfigPwRowEditorDstNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorDstNodeId.setStatus("current")
_TnMplsConfigPwRowEditorDstGlobalId_Type = Unsigned32
_TnMplsConfigPwRowEditorDstGlobalId_Object = MibScalar
tnMplsConfigPwRowEditorDstGlobalId = _TnMplsConfigPwRowEditorDstGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 22),
    _TnMplsConfigPwRowEditorDstGlobalId_Type()
)
tnMplsConfigPwRowEditorDstGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorDstGlobalId.setStatus("current")
_TnMplsConfigPwRowEditorDstGlobalIdIsDefined_Type = TruthValue
_TnMplsConfigPwRowEditorDstGlobalIdIsDefined_Object = MibScalar
tnMplsConfigPwRowEditorDstGlobalIdIsDefined = _TnMplsConfigPwRowEditorDstGlobalIdIsDefined_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 23),
    _TnMplsConfigPwRowEditorDstGlobalIdIsDefined_Type()
)
tnMplsConfigPwRowEditorDstGlobalIdIsDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorDstGlobalIdIsDefined.setStatus("current")
_TnMplsConfigPwRowEditorSrcAcId_Type = Unsigned32
_TnMplsConfigPwRowEditorSrcAcId_Object = MibScalar
tnMplsConfigPwRowEditorSrcAcId = _TnMplsConfigPwRowEditorSrcAcId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 24),
    _TnMplsConfigPwRowEditorSrcAcId_Type()
)
tnMplsConfigPwRowEditorSrcAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorSrcAcId.setStatus("current")
_TnMplsConfigPwRowEditorDstAcId_Type = Unsigned32
_TnMplsConfigPwRowEditorDstAcId_Object = MibScalar
tnMplsConfigPwRowEditorDstAcId = _TnMplsConfigPwRowEditorDstAcId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 25),
    _TnMplsConfigPwRowEditorDstAcId_Type()
)
tnMplsConfigPwRowEditorDstAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorDstAcId.setStatus("current")


class _TnMplsConfigPwRowEditorSrcAgiValue_Type(OctetString):
    """Custom type tnMplsConfigPwRowEditorSrcAgiValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TnMplsConfigPwRowEditorSrcAgiValue_Type.__name__ = "OctetString"
_TnMplsConfigPwRowEditorSrcAgiValue_Object = MibScalar
tnMplsConfigPwRowEditorSrcAgiValue = _TnMplsConfigPwRowEditorSrcAgiValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 26),
    _TnMplsConfigPwRowEditorSrcAgiValue_Type()
)
tnMplsConfigPwRowEditorSrcAgiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorSrcAgiValue.setStatus("current")


class _TnMplsConfigPwRowEditorDstAgiValue_Type(OctetString):
    """Custom type tnMplsConfigPwRowEditorDstAgiValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TnMplsConfigPwRowEditorDstAgiValue_Type.__name__ = "OctetString"
_TnMplsConfigPwRowEditorDstAgiValue_Object = MibScalar
tnMplsConfigPwRowEditorDstAgiValue = _TnMplsConfigPwRowEditorDstAgiValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 27),
    _TnMplsConfigPwRowEditorDstAgiValue_Type()
)
tnMplsConfigPwRowEditorDstAgiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorDstAgiValue.setStatus("current")
_TnMplsConfigPwRowEditorSrcAgiType_Type = TNUnsigned8
_TnMplsConfigPwRowEditorSrcAgiType_Object = MibScalar
tnMplsConfigPwRowEditorSrcAgiType = _TnMplsConfigPwRowEditorSrcAgiType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 28),
    _TnMplsConfigPwRowEditorSrcAgiType_Type()
)
tnMplsConfigPwRowEditorSrcAgiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorSrcAgiType.setStatus("current")


class _TnMplsConfigPwRowEditorSrcAgiLength_Type(TNUnsigned8):
    """Custom type tnMplsConfigPwRowEditorSrcAgiLength based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigPwRowEditorSrcAgiLength_Type.__name__ = "TNUnsigned8"
_TnMplsConfigPwRowEditorSrcAgiLength_Object = MibScalar
tnMplsConfigPwRowEditorSrcAgiLength = _TnMplsConfigPwRowEditorSrcAgiLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 29),
    _TnMplsConfigPwRowEditorSrcAgiLength_Type()
)
tnMplsConfigPwRowEditorSrcAgiLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorSrcAgiLength.setStatus("current")
_TnMplsConfigPwRowEditorDstAgiType_Type = TNUnsigned8
_TnMplsConfigPwRowEditorDstAgiType_Object = MibScalar
tnMplsConfigPwRowEditorDstAgiType = _TnMplsConfigPwRowEditorDstAgiType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 30),
    _TnMplsConfigPwRowEditorDstAgiType_Type()
)
tnMplsConfigPwRowEditorDstAgiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorDstAgiType.setStatus("current")


class _TnMplsConfigPwRowEditorDstAgiLength_Type(TNUnsigned8):
    """Custom type tnMplsConfigPwRowEditorDstAgiLength based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigPwRowEditorDstAgiLength_Type.__name__ = "TNUnsigned8"
_TnMplsConfigPwRowEditorDstAgiLength_Object = MibScalar
tnMplsConfigPwRowEditorDstAgiLength = _TnMplsConfigPwRowEditorDstAgiLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 31),
    _TnMplsConfigPwRowEditorDstAgiLength_Type()
)
tnMplsConfigPwRowEditorDstAgiLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorDstAgiLength.setStatus("current")
_TnMplsConfigPwRowEditorAction_Type = TNRowEditorState
_TnMplsConfigPwRowEditorAction_Object = MibScalar
tnMplsConfigPwRowEditorAction = _TnMplsConfigPwRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 5, 2, 100),
    _TnMplsConfigPwRowEditorAction_Type()
)
tnMplsConfigPwRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorAction.setStatus("current")
_TnMplsConfigCosMap_ObjectIdentity = ObjectIdentity
tnMplsConfigCosMap = _TnMplsConfigCosMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6)
)
_TnMplsConfigCosMapTable_Object = MibTable
tnMplsConfigCosMapTable = _TnMplsConfigCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tnMplsConfigCosMapTable.setStatus("current")
_TnMplsConfigCosMapEntry_Object = MibTableRow
tnMplsConfigCosMapEntry = _TnMplsConfigCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1)
)
tnMplsConfigCosMapEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsConfigCosMapGroupIndex"),
)
if mibBuilder.loadTexts:
    tnMplsConfigCosMapEntry.setStatus("current")


class _TnMplsConfigCosMapGroupIndex_Type(Integer32):
    """Custom type tnMplsConfigCosMapGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnMplsConfigCosMapGroupIndex_Type.__name__ = "Integer32"
_TnMplsConfigCosMapGroupIndex_Object = MibTableColumn
tnMplsConfigCosMapGroupIndex = _TnMplsConfigCosMapGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 1),
    _TnMplsConfigCosMapGroupIndex_Type()
)
tnMplsConfigCosMapGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapGroupIndex.setStatus("current")


class _TnMplsConfigCosMapInTcToCos0_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToCos0 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToCos0_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToCos0_Object = MibTableColumn
tnMplsConfigCosMapInTcToCos0 = _TnMplsConfigCosMapInTcToCos0_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 10),
    _TnMplsConfigCosMapInTcToCos0_Type()
)
tnMplsConfigCosMapInTcToCos0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToCos0.setStatus("current")


class _TnMplsConfigCosMapInTcToCos1_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToCos1 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToCos1_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToCos1_Object = MibTableColumn
tnMplsConfigCosMapInTcToCos1 = _TnMplsConfigCosMapInTcToCos1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 11),
    _TnMplsConfigCosMapInTcToCos1_Type()
)
tnMplsConfigCosMapInTcToCos1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToCos1.setStatus("current")


class _TnMplsConfigCosMapInTcToCos2_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToCos2 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToCos2_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToCos2_Object = MibTableColumn
tnMplsConfigCosMapInTcToCos2 = _TnMplsConfigCosMapInTcToCos2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 12),
    _TnMplsConfigCosMapInTcToCos2_Type()
)
tnMplsConfigCosMapInTcToCos2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToCos2.setStatus("current")


class _TnMplsConfigCosMapInTcToCos3_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToCos3 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToCos3_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToCos3_Object = MibTableColumn
tnMplsConfigCosMapInTcToCos3 = _TnMplsConfigCosMapInTcToCos3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 13),
    _TnMplsConfigCosMapInTcToCos3_Type()
)
tnMplsConfigCosMapInTcToCos3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToCos3.setStatus("current")


class _TnMplsConfigCosMapInTcToCos4_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToCos4 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToCos4_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToCos4_Object = MibTableColumn
tnMplsConfigCosMapInTcToCos4 = _TnMplsConfigCosMapInTcToCos4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 14),
    _TnMplsConfigCosMapInTcToCos4_Type()
)
tnMplsConfigCosMapInTcToCos4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToCos4.setStatus("current")


class _TnMplsConfigCosMapInTcToCos5_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToCos5 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToCos5_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToCos5_Object = MibTableColumn
tnMplsConfigCosMapInTcToCos5 = _TnMplsConfigCosMapInTcToCos5_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 15),
    _TnMplsConfigCosMapInTcToCos5_Type()
)
tnMplsConfigCosMapInTcToCos5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToCos5.setStatus("current")


class _TnMplsConfigCosMapInTcToCos6_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToCos6 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToCos6_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToCos6_Object = MibTableColumn
tnMplsConfigCosMapInTcToCos6 = _TnMplsConfigCosMapInTcToCos6_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 16),
    _TnMplsConfigCosMapInTcToCos6_Type()
)
tnMplsConfigCosMapInTcToCos6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToCos6.setStatus("current")


class _TnMplsConfigCosMapInTcToCos7_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToCos7 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToCos7_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToCos7_Object = MibTableColumn
tnMplsConfigCosMapInTcToCos7 = _TnMplsConfigCosMapInTcToCos7_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 17),
    _TnMplsConfigCosMapInTcToCos7_Type()
)
tnMplsConfigCosMapInTcToCos7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToCos7.setStatus("current")


class _TnMplsConfigCosMapInTcToDp0_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToDp0 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToDp0_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToDp0_Object = MibTableColumn
tnMplsConfigCosMapInTcToDp0 = _TnMplsConfigCosMapInTcToDp0_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 20),
    _TnMplsConfigCosMapInTcToDp0_Type()
)
tnMplsConfigCosMapInTcToDp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToDp0.setStatus("current")


class _TnMplsConfigCosMapInTcToDp1_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToDp1 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToDp1_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToDp1_Object = MibTableColumn
tnMplsConfigCosMapInTcToDp1 = _TnMplsConfigCosMapInTcToDp1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 21),
    _TnMplsConfigCosMapInTcToDp1_Type()
)
tnMplsConfigCosMapInTcToDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToDp1.setStatus("current")


class _TnMplsConfigCosMapInTcToDp2_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToDp2 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToDp2_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToDp2_Object = MibTableColumn
tnMplsConfigCosMapInTcToDp2 = _TnMplsConfigCosMapInTcToDp2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 22),
    _TnMplsConfigCosMapInTcToDp2_Type()
)
tnMplsConfigCosMapInTcToDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToDp2.setStatus("current")


class _TnMplsConfigCosMapInTcToDp3_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToDp3 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToDp3_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToDp3_Object = MibTableColumn
tnMplsConfigCosMapInTcToDp3 = _TnMplsConfigCosMapInTcToDp3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 23),
    _TnMplsConfigCosMapInTcToDp3_Type()
)
tnMplsConfigCosMapInTcToDp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToDp3.setStatus("current")


class _TnMplsConfigCosMapInTcToDp4_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToDp4 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToDp4_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToDp4_Object = MibTableColumn
tnMplsConfigCosMapInTcToDp4 = _TnMplsConfigCosMapInTcToDp4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 24),
    _TnMplsConfigCosMapInTcToDp4_Type()
)
tnMplsConfigCosMapInTcToDp4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToDp4.setStatus("current")


class _TnMplsConfigCosMapInTcToDp5_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToDp5 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToDp5_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToDp5_Object = MibTableColumn
tnMplsConfigCosMapInTcToDp5 = _TnMplsConfigCosMapInTcToDp5_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 25),
    _TnMplsConfigCosMapInTcToDp5_Type()
)
tnMplsConfigCosMapInTcToDp5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToDp5.setStatus("current")


class _TnMplsConfigCosMapInTcToDp6_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToDp6 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToDp6_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToDp6_Object = MibTableColumn
tnMplsConfigCosMapInTcToDp6 = _TnMplsConfigCosMapInTcToDp6_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 26),
    _TnMplsConfigCosMapInTcToDp6_Type()
)
tnMplsConfigCosMapInTcToDp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToDp6.setStatus("current")


class _TnMplsConfigCosMapInTcToDp7_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapInTcToDp7 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapInTcToDp7_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapInTcToDp7_Object = MibTableColumn
tnMplsConfigCosMapInTcToDp7 = _TnMplsConfigCosMapInTcToDp7_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 27),
    _TnMplsConfigCosMapInTcToDp7_Type()
)
tnMplsConfigCosMapInTcToDp7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapInTcToDp7.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc00_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc00 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc00_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc00_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc00 = _TnMplsConfigCosMapOutCosDpToTc00_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 30),
    _TnMplsConfigCosMapOutCosDpToTc00_Type()
)
tnMplsConfigCosMapOutCosDpToTc00.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc00.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc10_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc10 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc10_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc10_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc10 = _TnMplsConfigCosMapOutCosDpToTc10_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 31),
    _TnMplsConfigCosMapOutCosDpToTc10_Type()
)
tnMplsConfigCosMapOutCosDpToTc10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc10.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc20_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc20 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc20_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc20_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc20 = _TnMplsConfigCosMapOutCosDpToTc20_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 32),
    _TnMplsConfigCosMapOutCosDpToTc20_Type()
)
tnMplsConfigCosMapOutCosDpToTc20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc20.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc30_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc30 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc30_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc30_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc30 = _TnMplsConfigCosMapOutCosDpToTc30_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 33),
    _TnMplsConfigCosMapOutCosDpToTc30_Type()
)
tnMplsConfigCosMapOutCosDpToTc30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc30.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc40_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc40 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc40_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc40_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc40 = _TnMplsConfigCosMapOutCosDpToTc40_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 34),
    _TnMplsConfigCosMapOutCosDpToTc40_Type()
)
tnMplsConfigCosMapOutCosDpToTc40.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc40.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc50_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc50 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc50_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc50_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc50 = _TnMplsConfigCosMapOutCosDpToTc50_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 35),
    _TnMplsConfigCosMapOutCosDpToTc50_Type()
)
tnMplsConfigCosMapOutCosDpToTc50.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc50.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc60_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc60 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc60_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc60_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc60 = _TnMplsConfigCosMapOutCosDpToTc60_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 36),
    _TnMplsConfigCosMapOutCosDpToTc60_Type()
)
tnMplsConfigCosMapOutCosDpToTc60.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc60.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc70_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc70 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc70_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc70_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc70 = _TnMplsConfigCosMapOutCosDpToTc70_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 37),
    _TnMplsConfigCosMapOutCosDpToTc70_Type()
)
tnMplsConfigCosMapOutCosDpToTc70.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc70.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc01_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc01 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc01_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc01_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc01 = _TnMplsConfigCosMapOutCosDpToTc01_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 40),
    _TnMplsConfigCosMapOutCosDpToTc01_Type()
)
tnMplsConfigCosMapOutCosDpToTc01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc01.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc11_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc11 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc11_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc11_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc11 = _TnMplsConfigCosMapOutCosDpToTc11_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 41),
    _TnMplsConfigCosMapOutCosDpToTc11_Type()
)
tnMplsConfigCosMapOutCosDpToTc11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc11.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc21_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc21 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc21_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc21_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc21 = _TnMplsConfigCosMapOutCosDpToTc21_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 42),
    _TnMplsConfigCosMapOutCosDpToTc21_Type()
)
tnMplsConfigCosMapOutCosDpToTc21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc21.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc31_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc31 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc31_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc31_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc31 = _TnMplsConfigCosMapOutCosDpToTc31_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 43),
    _TnMplsConfigCosMapOutCosDpToTc31_Type()
)
tnMplsConfigCosMapOutCosDpToTc31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc31.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc41_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc41 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc41_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc41_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc41 = _TnMplsConfigCosMapOutCosDpToTc41_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 44),
    _TnMplsConfigCosMapOutCosDpToTc41_Type()
)
tnMplsConfigCosMapOutCosDpToTc41.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc41.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc51_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc51 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc51_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc51_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc51 = _TnMplsConfigCosMapOutCosDpToTc51_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 45),
    _TnMplsConfigCosMapOutCosDpToTc51_Type()
)
tnMplsConfigCosMapOutCosDpToTc51.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc51.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc61_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc61 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc61_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc61_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc61 = _TnMplsConfigCosMapOutCosDpToTc61_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 46),
    _TnMplsConfigCosMapOutCosDpToTc61_Type()
)
tnMplsConfigCosMapOutCosDpToTc61.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc61.setStatus("current")


class _TnMplsConfigCosMapOutCosDpToTc71_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapOutCosDpToTc71 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapOutCosDpToTc71_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapOutCosDpToTc71_Object = MibTableColumn
tnMplsConfigCosMapOutCosDpToTc71 = _TnMplsConfigCosMapOutCosDpToTc71_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 47),
    _TnMplsConfigCosMapOutCosDpToTc71_Type()
)
tnMplsConfigCosMapOutCosDpToTc71.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapOutCosDpToTc71.setStatus("current")
_TnMplsConfigCosMapAction_Type = TNRowEditorState
_TnMplsConfigCosMapAction_Object = MibTableColumn
tnMplsConfigCosMapAction = _TnMplsConfigCosMapAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 1, 1, 100),
    _TnMplsConfigCosMapAction_Type()
)
tnMplsConfigCosMapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapAction.setStatus("current")
_TnMplsConfigCosMapRowEditor_ObjectIdentity = ObjectIdentity
tnMplsConfigCosMapRowEditor = _TnMplsConfigCosMapRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2)
)


class _TnMplsConfigCosMapRowEditorGroupIndex_Type(Integer32):
    """Custom type tnMplsConfigCosMapRowEditorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnMplsConfigCosMapRowEditorGroupIndex_Type.__name__ = "Integer32"
_TnMplsConfigCosMapRowEditorGroupIndex_Object = MibScalar
tnMplsConfigCosMapRowEditorGroupIndex = _TnMplsConfigCosMapRowEditorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 1),
    _TnMplsConfigCosMapRowEditorGroupIndex_Type()
)
tnMplsConfigCosMapRowEditorGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorGroupIndex.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToCos0_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToCos0 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToCos0_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToCos0_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToCos0 = _TnMplsConfigCosMapRowEditorInTcToCos0_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 10),
    _TnMplsConfigCosMapRowEditorInTcToCos0_Type()
)
tnMplsConfigCosMapRowEditorInTcToCos0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToCos0.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToCos1_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToCos1 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToCos1_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToCos1_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToCos1 = _TnMplsConfigCosMapRowEditorInTcToCos1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 11),
    _TnMplsConfigCosMapRowEditorInTcToCos1_Type()
)
tnMplsConfigCosMapRowEditorInTcToCos1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToCos1.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToCos2_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToCos2 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToCos2_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToCos2_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToCos2 = _TnMplsConfigCosMapRowEditorInTcToCos2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 12),
    _TnMplsConfigCosMapRowEditorInTcToCos2_Type()
)
tnMplsConfigCosMapRowEditorInTcToCos2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToCos2.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToCos3_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToCos3 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToCos3_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToCos3_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToCos3 = _TnMplsConfigCosMapRowEditorInTcToCos3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 13),
    _TnMplsConfigCosMapRowEditorInTcToCos3_Type()
)
tnMplsConfigCosMapRowEditorInTcToCos3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToCos3.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToCos4_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToCos4 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToCos4_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToCos4_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToCos4 = _TnMplsConfigCosMapRowEditorInTcToCos4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 14),
    _TnMplsConfigCosMapRowEditorInTcToCos4_Type()
)
tnMplsConfigCosMapRowEditorInTcToCos4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToCos4.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToCos5_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToCos5 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToCos5_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToCos5_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToCos5 = _TnMplsConfigCosMapRowEditorInTcToCos5_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 15),
    _TnMplsConfigCosMapRowEditorInTcToCos5_Type()
)
tnMplsConfigCosMapRowEditorInTcToCos5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToCos5.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToCos6_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToCos6 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToCos6_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToCos6_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToCos6 = _TnMplsConfigCosMapRowEditorInTcToCos6_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 16),
    _TnMplsConfigCosMapRowEditorInTcToCos6_Type()
)
tnMplsConfigCosMapRowEditorInTcToCos6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToCos6.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToCos7_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToCos7 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToCos7_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToCos7_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToCos7 = _TnMplsConfigCosMapRowEditorInTcToCos7_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 17),
    _TnMplsConfigCosMapRowEditorInTcToCos7_Type()
)
tnMplsConfigCosMapRowEditorInTcToCos7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToCos7.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToDp0_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToDp0 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToDp0_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToDp0_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToDp0 = _TnMplsConfigCosMapRowEditorInTcToDp0_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 20),
    _TnMplsConfigCosMapRowEditorInTcToDp0_Type()
)
tnMplsConfigCosMapRowEditorInTcToDp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToDp0.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToDp1_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToDp1 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToDp1_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToDp1_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToDp1 = _TnMplsConfigCosMapRowEditorInTcToDp1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 21),
    _TnMplsConfigCosMapRowEditorInTcToDp1_Type()
)
tnMplsConfigCosMapRowEditorInTcToDp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToDp1.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToDp2_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToDp2 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToDp2_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToDp2_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToDp2 = _TnMplsConfigCosMapRowEditorInTcToDp2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 22),
    _TnMplsConfigCosMapRowEditorInTcToDp2_Type()
)
tnMplsConfigCosMapRowEditorInTcToDp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToDp2.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToDp3_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToDp3 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToDp3_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToDp3_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToDp3 = _TnMplsConfigCosMapRowEditorInTcToDp3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 23),
    _TnMplsConfigCosMapRowEditorInTcToDp3_Type()
)
tnMplsConfigCosMapRowEditorInTcToDp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToDp3.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToDp4_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToDp4 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToDp4_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToDp4_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToDp4 = _TnMplsConfigCosMapRowEditorInTcToDp4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 24),
    _TnMplsConfigCosMapRowEditorInTcToDp4_Type()
)
tnMplsConfigCosMapRowEditorInTcToDp4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToDp4.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToDp5_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToDp5 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToDp5_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToDp5_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToDp5 = _TnMplsConfigCosMapRowEditorInTcToDp5_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 25),
    _TnMplsConfigCosMapRowEditorInTcToDp5_Type()
)
tnMplsConfigCosMapRowEditorInTcToDp5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToDp5.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToDp6_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToDp6 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToDp6_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToDp6_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToDp6 = _TnMplsConfigCosMapRowEditorInTcToDp6_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 26),
    _TnMplsConfigCosMapRowEditorInTcToDp6_Type()
)
tnMplsConfigCosMapRowEditorInTcToDp6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToDp6.setStatus("current")


class _TnMplsConfigCosMapRowEditorInTcToDp7_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorInTcToDp7 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorInTcToDp7_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorInTcToDp7_Object = MibScalar
tnMplsConfigCosMapRowEditorInTcToDp7 = _TnMplsConfigCosMapRowEditorInTcToDp7_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 27),
    _TnMplsConfigCosMapRowEditorInTcToDp7_Type()
)
tnMplsConfigCosMapRowEditorInTcToDp7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInTcToDp7.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc00_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc00 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc00_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc00_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc00 = _TnMplsConfigCosMapRowEditorOutCosDpToTc00_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 30),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc00_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc00.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc00.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc10_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc10 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc10_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc10_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc10 = _TnMplsConfigCosMapRowEditorOutCosDpToTc10_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 31),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc10_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc10.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc20_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc20 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc20_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc20_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc20 = _TnMplsConfigCosMapRowEditorOutCosDpToTc20_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 32),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc20_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc20.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc30_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc30 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc30_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc30_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc30 = _TnMplsConfigCosMapRowEditorOutCosDpToTc30_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 33),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc30_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc30.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc40_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc40 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc40_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc40_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc40 = _TnMplsConfigCosMapRowEditorOutCosDpToTc40_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 34),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc40_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc40.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc40.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc50_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc50 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc50_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc50_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc50 = _TnMplsConfigCosMapRowEditorOutCosDpToTc50_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 35),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc50_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc50.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc50.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc60_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc60 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc60_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc60_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc60 = _TnMplsConfigCosMapRowEditorOutCosDpToTc60_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 36),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc60_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc60.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc60.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc70_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc70 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc70_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc70_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc70 = _TnMplsConfigCosMapRowEditorOutCosDpToTc70_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 37),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc70_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc70.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc70.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc01_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc01 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc01_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc01_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc01 = _TnMplsConfigCosMapRowEditorOutCosDpToTc01_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 40),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc01_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc01.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc11_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc11 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc11_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc11_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc11 = _TnMplsConfigCosMapRowEditorOutCosDpToTc11_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 41),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc11_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc11.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc21_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc21 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc21_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc21_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc21 = _TnMplsConfigCosMapRowEditorOutCosDpToTc21_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 42),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc21_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc21.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc31_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc31 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc31_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc31_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc31 = _TnMplsConfigCosMapRowEditorOutCosDpToTc31_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 43),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc31_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc31.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc41_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc41 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc41_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc41_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc41 = _TnMplsConfigCosMapRowEditorOutCosDpToTc41_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 44),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc41_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc41.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc41.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc51_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc51 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc51_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc51_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc51 = _TnMplsConfigCosMapRowEditorOutCosDpToTc51_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 45),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc51_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc51.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc51.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc61_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc61 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc61_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc61_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc61 = _TnMplsConfigCosMapRowEditorOutCosDpToTc61_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 46),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc61_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc61.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc61.setStatus("current")


class _TnMplsConfigCosMapRowEditorOutCosDpToTc71_Type(TNUnsigned8):
    """Custom type tnMplsConfigCosMapRowEditorOutCosDpToTc71 based on TNUnsigned8"""
    subtypeSpec = TNUnsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnMplsConfigCosMapRowEditorOutCosDpToTc71_Type.__name__ = "TNUnsigned8"
_TnMplsConfigCosMapRowEditorOutCosDpToTc71_Object = MibScalar
tnMplsConfigCosMapRowEditorOutCosDpToTc71 = _TnMplsConfigCosMapRowEditorOutCosDpToTc71_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 47),
    _TnMplsConfigCosMapRowEditorOutCosDpToTc71_Type()
)
tnMplsConfigCosMapRowEditorOutCosDpToTc71.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorOutCosDpToTc71.setStatus("current")
_TnMplsConfigCosMapRowEditorAction_Type = TNRowEditorState
_TnMplsConfigCosMapRowEditorAction_Object = MibScalar
tnMplsConfigCosMapRowEditorAction = _TnMplsConfigCosMapRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 2, 6, 2, 100),
    _TnMplsConfigCosMapRowEditorAction_Type()
)
tnMplsConfigCosMapRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorAction.setStatus("current")
_TnMplsStatus_ObjectIdentity = ObjectIdentity
tnMplsStatus = _TnMplsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3)
)
_TnMplsStatusGlobal_ObjectIdentity = ObjectIdentity
tnMplsStatusGlobal = _TnMplsStatusGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 1)
)
_TnMplsStatusLink_ObjectIdentity = ObjectIdentity
tnMplsStatusLink = _TnMplsStatusLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 2)
)
_TnMplsStatusLinkTable_Object = MibTable
tnMplsStatusLinkTable = _TnMplsStatusLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tnMplsStatusLinkTable.setStatus("current")
_TnMplsStatusLinkEntry_Object = MibTableRow
tnMplsStatusLinkEntry = _TnMplsStatusLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 2, 1, 1)
)
tnMplsStatusLinkEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsStatusLinkGroupIfIndex"),
)
if mibBuilder.loadTexts:
    tnMplsStatusLinkEntry.setStatus("current")
_TnMplsStatusLinkGroupIfIndex_Type = TNInterfaceIndex
_TnMplsStatusLinkGroupIfIndex_Object = MibTableColumn
tnMplsStatusLinkGroupIfIndex = _TnMplsStatusLinkGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 2, 1, 1, 1),
    _TnMplsStatusLinkGroupIfIndex_Type()
)
tnMplsStatusLinkGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsStatusLinkGroupIfIndex.setStatus("current")
_TnMplsStatusLinkOamActive_Type = TruthValue
_TnMplsStatusLinkOamActive_Object = MibTableColumn
tnMplsStatusLinkOamActive = _TnMplsStatusLinkOamActive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 2, 1, 1, 2),
    _TnMplsStatusLinkOamActive_Type()
)
tnMplsStatusLinkOamActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatusLinkOamActive.setStatus("current")
_TnMplsStatusTunnel_ObjectIdentity = ObjectIdentity
tnMplsStatusTunnel = _TnMplsStatusTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 3)
)
_TnMplsStatusTunnelTable_Object = MibTable
tnMplsStatusTunnelTable = _TnMplsStatusTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tnMplsStatusTunnelTable.setStatus("current")
_TnMplsStatusTunnelEntry_Object = MibTableRow
tnMplsStatusTunnelEntry = _TnMplsStatusTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 3, 1, 1)
)
tnMplsStatusTunnelEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsStatusTunnelGroupIfIndex"),
)
if mibBuilder.loadTexts:
    tnMplsStatusTunnelEntry.setStatus("current")
_TnMplsStatusTunnelGroupIfIndex_Type = TNInterfaceIndex
_TnMplsStatusTunnelGroupIfIndex_Object = MibTableColumn
tnMplsStatusTunnelGroupIfIndex = _TnMplsStatusTunnelGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 3, 1, 1, 1),
    _TnMplsStatusTunnelGroupIfIndex_Type()
)
tnMplsStatusTunnelGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsStatusTunnelGroupIfIndex.setStatus("current")
_TnMplsStatusTunnelOamActive_Type = TruthValue
_TnMplsStatusTunnelOamActive_Object = MibTableColumn
tnMplsStatusTunnelOamActive = _TnMplsStatusTunnelOamActive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 3, 1, 1, 2),
    _TnMplsStatusTunnelOamActive_Type()
)
tnMplsStatusTunnelOamActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatusTunnelOamActive.setStatus("current")
_TnMplsStatusTunnelState_Type = TNMplsStateType
_TnMplsStatusTunnelState_Object = MibTableColumn
tnMplsStatusTunnelState = _TnMplsStatusTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 3, 1, 1, 3),
    _TnMplsStatusTunnelState_Type()
)
tnMplsStatusTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatusTunnelState.setStatus("current")
_TnMplsStatusTunnelIngressLabel_Type = Unsigned32
_TnMplsStatusTunnelIngressLabel_Object = MibTableColumn
tnMplsStatusTunnelIngressLabel = _TnMplsStatusTunnelIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 3, 1, 1, 4),
    _TnMplsStatusTunnelIngressLabel_Type()
)
tnMplsStatusTunnelIngressLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatusTunnelIngressLabel.setStatus("current")
_TnMplsStatusTunnelEgressLabel_Type = Unsigned32
_TnMplsStatusTunnelEgressLabel_Object = MibTableColumn
tnMplsStatusTunnelEgressLabel = _TnMplsStatusTunnelEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 3, 1, 1, 5),
    _TnMplsStatusTunnelEgressLabel_Type()
)
tnMplsStatusTunnelEgressLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatusTunnelEgressLabel.setStatus("current")
_TnMplsStatusTunnelWorkingActive_Type = TruthValue
_TnMplsStatusTunnelWorkingActive_Object = MibTableColumn
tnMplsStatusTunnelWorkingActive = _TnMplsStatusTunnelWorkingActive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 3, 1, 1, 6),
    _TnMplsStatusTunnelWorkingActive_Type()
)
tnMplsStatusTunnelWorkingActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatusTunnelWorkingActive.setStatus("current")
_TnMplsStatusLsp_ObjectIdentity = ObjectIdentity
tnMplsStatusLsp = _TnMplsStatusLsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 4)
)
_TnMplsStatusLspTable_Object = MibTable
tnMplsStatusLspTable = _TnMplsStatusLspTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tnMplsStatusLspTable.setStatus("current")
_TnMplsStatusLspEntry_Object = MibTableRow
tnMplsStatusLspEntry = _TnMplsStatusLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 4, 1, 1)
)
tnMplsStatusLspEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsStatusLspGroupIndex"),
)
if mibBuilder.loadTexts:
    tnMplsStatusLspEntry.setStatus("current")


class _TnMplsStatusLspGroupIndex_Type(Integer32):
    """Custom type tnMplsStatusLspGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnMplsStatusLspGroupIndex_Type.__name__ = "Integer32"
_TnMplsStatusLspGroupIndex_Object = MibTableColumn
tnMplsStatusLspGroupIndex = _TnMplsStatusLspGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 4, 1, 1, 1),
    _TnMplsStatusLspGroupIndex_Type()
)
tnMplsStatusLspGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsStatusLspGroupIndex.setStatus("current")
_TnMplsStatusLspOamActive_Type = TruthValue
_TnMplsStatusLspOamActive_Object = MibTableColumn
tnMplsStatusLspOamActive = _TnMplsStatusLspOamActive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 4, 1, 1, 2),
    _TnMplsStatusLspOamActive_Type()
)
tnMplsStatusLspOamActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatusLspOamActive.setStatus("current")
_TnMplsStatusLspState_Type = TNMplsStateType
_TnMplsStatusLspState_Object = MibTableColumn
tnMplsStatusLspState = _TnMplsStatusLspState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 4, 1, 1, 3),
    _TnMplsStatusLspState_Type()
)
tnMplsStatusLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatusLspState.setStatus("current")
_TnMplsStatusPw_ObjectIdentity = ObjectIdentity
tnMplsStatusPw = _TnMplsStatusPw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 5)
)
_TnMplsStatusPwTable_Object = MibTable
tnMplsStatusPwTable = _TnMplsStatusPwTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    tnMplsStatusPwTable.setStatus("current")
_TnMplsStatusPwEntry_Object = MibTableRow
tnMplsStatusPwEntry = _TnMplsStatusPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 5, 1, 1)
)
tnMplsStatusPwEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsStatusPwGroupIfIndex"),
)
if mibBuilder.loadTexts:
    tnMplsStatusPwEntry.setStatus("current")
_TnMplsStatusPwGroupIfIndex_Type = TNInterfaceIndex
_TnMplsStatusPwGroupIfIndex_Object = MibTableColumn
tnMplsStatusPwGroupIfIndex = _TnMplsStatusPwGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 5, 1, 1, 1),
    _TnMplsStatusPwGroupIfIndex_Type()
)
tnMplsStatusPwGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsStatusPwGroupIfIndex.setStatus("current")
_TnMplsStatusPwOamActive_Type = TruthValue
_TnMplsStatusPwOamActive_Object = MibTableColumn
tnMplsStatusPwOamActive = _TnMplsStatusPwOamActive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 5, 1, 1, 2),
    _TnMplsStatusPwOamActive_Type()
)
tnMplsStatusPwOamActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatusPwOamActive.setStatus("current")
_TnMplsStatusPwState_Type = TNMplsStateType
_TnMplsStatusPwState_Object = MibTableColumn
tnMplsStatusPwState = _TnMplsStatusPwState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 3, 5, 1, 1, 3),
    _TnMplsStatusPwState_Type()
)
tnMplsStatusPwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatusPwState.setStatus("current")
_TnMplsControl_ObjectIdentity = ObjectIdentity
tnMplsControl = _TnMplsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4)
)
_TnMplsControlGlobal_ObjectIdentity = ObjectIdentity
tnMplsControlGlobal = _TnMplsControlGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4, 1)
)
_TnMplsControlLsp_ObjectIdentity = ObjectIdentity
tnMplsControlLsp = _TnMplsControlLsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4, 2)
)
_TnMplsControlLspTable_Object = MibTable
tnMplsControlLspTable = _TnMplsControlLspTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tnMplsControlLspTable.setStatus("current")
_TnMplsControlLspEntry_Object = MibTableRow
tnMplsControlLspEntry = _TnMplsControlLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4, 2, 1, 1)
)
tnMplsControlLspEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsControlLspGroupIndex"),
)
if mibBuilder.loadTexts:
    tnMplsControlLspEntry.setStatus("current")


class _TnMplsControlLspGroupIndex_Type(Integer32):
    """Custom type tnMplsControlLspGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnMplsControlLspGroupIndex_Type.__name__ = "Integer32"
_TnMplsControlLspGroupIndex_Object = MibTableColumn
tnMplsControlLspGroupIndex = _TnMplsControlLspGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4, 2, 1, 1, 1),
    _TnMplsControlLspGroupIndex_Type()
)
tnMplsControlLspGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsControlLspGroupIndex.setStatus("current")
_TnMplsControlLspClear_Type = TruthValue
_TnMplsControlLspClear_Object = MibTableColumn
tnMplsControlLspClear = _TnMplsControlLspClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4, 2, 1, 1, 2),
    _TnMplsControlLspClear_Type()
)
tnMplsControlLspClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsControlLspClear.setStatus("current")
_TnMplsControlIf_ObjectIdentity = ObjectIdentity
tnMplsControlIf = _TnMplsControlIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4, 3)
)
_TnMplsControlIfTable_Object = MibTable
tnMplsControlIfTable = _TnMplsControlIfTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    tnMplsControlIfTable.setStatus("current")
_TnMplsControlIfEntry_Object = MibTableRow
tnMplsControlIfEntry = _TnMplsControlIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4, 3, 1, 1)
)
tnMplsControlIfEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsControlIfGroupIfIndex"),
)
if mibBuilder.loadTexts:
    tnMplsControlIfEntry.setStatus("current")
_TnMplsControlIfGroupIfIndex_Type = TNInterfaceIndex
_TnMplsControlIfGroupIfIndex_Object = MibTableColumn
tnMplsControlIfGroupIfIndex = _TnMplsControlIfGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4, 3, 1, 1, 1),
    _TnMplsControlIfGroupIfIndex_Type()
)
tnMplsControlIfGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsControlIfGroupIfIndex.setStatus("current")
_TnMplsControlIfClear_Type = TruthValue
_TnMplsControlIfClear_Object = MibTableColumn
tnMplsControlIfClear = _TnMplsControlIfClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 4, 3, 1, 1, 2),
    _TnMplsControlIfClear_Type()
)
tnMplsControlIfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnMplsControlIfClear.setStatus("current")
_TnMplsStatistics_ObjectIdentity = ObjectIdentity
tnMplsStatistics = _TnMplsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5)
)
_TnMplsStatisticsGlobal_ObjectIdentity = ObjectIdentity
tnMplsStatisticsGlobal = _TnMplsStatisticsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 1)
)
_TnMplsStatisticsLink_ObjectIdentity = ObjectIdentity
tnMplsStatisticsLink = _TnMplsStatisticsLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 2)
)
_TnMplsStatisticsTunnel_ObjectIdentity = ObjectIdentity
tnMplsStatisticsTunnel = _TnMplsStatisticsTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3)
)
_TnMplsStatisticsTunnelTable_Object = MibTable
tnMplsStatisticsTunnelTable = _TnMplsStatisticsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelTable.setStatus("current")
_TnMplsStatisticsTunnelEntry_Object = MibTableRow
tnMplsStatisticsTunnelEntry = _TnMplsStatisticsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1)
)
tnMplsStatisticsTunnelEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsStatisticsTunnelGroupIfIndex"),
)
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelEntry.setStatus("current")
_TnMplsStatisticsTunnelGroupIfIndex_Type = TNInterfaceIndex
_TnMplsStatisticsTunnelGroupIfIndex_Object = MibTableColumn
tnMplsStatisticsTunnelGroupIfIndex = _TnMplsStatisticsTunnelGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 1),
    _TnMplsStatisticsTunnelGroupIfIndex_Type()
)
tnMplsStatisticsTunnelGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelGroupIfIndex.setStatus("current")
_TnMplsStatisticsTunnelRxGreenFrames_Type = Counter64
_TnMplsStatisticsTunnelRxGreenFrames_Object = MibTableColumn
tnMplsStatisticsTunnelRxGreenFrames = _TnMplsStatisticsTunnelRxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 3),
    _TnMplsStatisticsTunnelRxGreenFrames_Type()
)
tnMplsStatisticsTunnelRxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelRxGreenFrames.setStatus("current")
_TnMplsStatisticsTunnelRxGreenBytes_Type = Counter64
_TnMplsStatisticsTunnelRxGreenBytes_Object = MibTableColumn
tnMplsStatisticsTunnelRxGreenBytes = _TnMplsStatisticsTunnelRxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 4),
    _TnMplsStatisticsTunnelRxGreenBytes_Type()
)
tnMplsStatisticsTunnelRxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelRxGreenBytes.setStatus("current")
_TnMplsStatisticsTunnelRxYellowFrames_Type = Counter64
_TnMplsStatisticsTunnelRxYellowFrames_Object = MibTableColumn
tnMplsStatisticsTunnelRxYellowFrames = _TnMplsStatisticsTunnelRxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 5),
    _TnMplsStatisticsTunnelRxYellowFrames_Type()
)
tnMplsStatisticsTunnelRxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelRxYellowFrames.setStatus("current")
_TnMplsStatisticsTunnelRxYellowBytes_Type = Counter64
_TnMplsStatisticsTunnelRxYellowBytes_Object = MibTableColumn
tnMplsStatisticsTunnelRxYellowBytes = _TnMplsStatisticsTunnelRxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 6),
    _TnMplsStatisticsTunnelRxYellowBytes_Type()
)
tnMplsStatisticsTunnelRxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelRxYellowBytes.setStatus("current")
_TnMplsStatisticsTunnelRxRedFrames_Type = Counter64
_TnMplsStatisticsTunnelRxRedFrames_Object = MibTableColumn
tnMplsStatisticsTunnelRxRedFrames = _TnMplsStatisticsTunnelRxRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 7),
    _TnMplsStatisticsTunnelRxRedFrames_Type()
)
tnMplsStatisticsTunnelRxRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelRxRedFrames.setStatus("current")
_TnMplsStatisticsTunnelRxRedBytes_Type = Counter64
_TnMplsStatisticsTunnelRxRedBytes_Object = MibTableColumn
tnMplsStatisticsTunnelRxRedBytes = _TnMplsStatisticsTunnelRxRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 8),
    _TnMplsStatisticsTunnelRxRedBytes_Type()
)
tnMplsStatisticsTunnelRxRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelRxRedBytes.setStatus("current")
_TnMplsStatisticsTunnelRxDiscardFrames_Type = Counter64
_TnMplsStatisticsTunnelRxDiscardFrames_Object = MibTableColumn
tnMplsStatisticsTunnelRxDiscardFrames = _TnMplsStatisticsTunnelRxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 9),
    _TnMplsStatisticsTunnelRxDiscardFrames_Type()
)
tnMplsStatisticsTunnelRxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelRxDiscardFrames.setStatus("current")
_TnMplsStatisticsTunnelRxDiscardBytes_Type = Counter64
_TnMplsStatisticsTunnelRxDiscardBytes_Object = MibTableColumn
tnMplsStatisticsTunnelRxDiscardBytes = _TnMplsStatisticsTunnelRxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 10),
    _TnMplsStatisticsTunnelRxDiscardBytes_Type()
)
tnMplsStatisticsTunnelRxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelRxDiscardBytes.setStatus("current")
_TnMplsStatisticsTunnelTxGreenFrames_Type = Counter64
_TnMplsStatisticsTunnelTxGreenFrames_Object = MibTableColumn
tnMplsStatisticsTunnelTxGreenFrames = _TnMplsStatisticsTunnelTxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 11),
    _TnMplsStatisticsTunnelTxGreenFrames_Type()
)
tnMplsStatisticsTunnelTxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelTxGreenFrames.setStatus("current")
_TnMplsStatisticsTunnelTxGreenBytes_Type = Counter64
_TnMplsStatisticsTunnelTxGreenBytes_Object = MibTableColumn
tnMplsStatisticsTunnelTxGreenBytes = _TnMplsStatisticsTunnelTxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 12),
    _TnMplsStatisticsTunnelTxGreenBytes_Type()
)
tnMplsStatisticsTunnelTxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelTxGreenBytes.setStatus("current")
_TnMplsStatisticsTunnelTxYellowFrames_Type = Counter64
_TnMplsStatisticsTunnelTxYellowFrames_Object = MibTableColumn
tnMplsStatisticsTunnelTxYellowFrames = _TnMplsStatisticsTunnelTxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 13),
    _TnMplsStatisticsTunnelTxYellowFrames_Type()
)
tnMplsStatisticsTunnelTxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelTxYellowFrames.setStatus("current")
_TnMplsStatisticsTunnelTxYellowBytes_Type = Counter64
_TnMplsStatisticsTunnelTxYellowBytes_Object = MibTableColumn
tnMplsStatisticsTunnelTxYellowBytes = _TnMplsStatisticsTunnelTxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 14),
    _TnMplsStatisticsTunnelTxYellowBytes_Type()
)
tnMplsStatisticsTunnelTxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelTxYellowBytes.setStatus("current")
_TnMplsStatisticsTunnelTxDiscardFrames_Type = Counter64
_TnMplsStatisticsTunnelTxDiscardFrames_Object = MibTableColumn
tnMplsStatisticsTunnelTxDiscardFrames = _TnMplsStatisticsTunnelTxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 15),
    _TnMplsStatisticsTunnelTxDiscardFrames_Type()
)
tnMplsStatisticsTunnelTxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelTxDiscardFrames.setStatus("current")
_TnMplsStatisticsTunnelTxDiscardBytes_Type = Counter64
_TnMplsStatisticsTunnelTxDiscardBytes_Object = MibTableColumn
tnMplsStatisticsTunnelTxDiscardBytes = _TnMplsStatisticsTunnelTxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 3, 1, 1, 16),
    _TnMplsStatisticsTunnelTxDiscardBytes_Type()
)
tnMplsStatisticsTunnelTxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelTxDiscardBytes.setStatus("current")
_TnMplsStatisticsLsp_ObjectIdentity = ObjectIdentity
tnMplsStatisticsLsp = _TnMplsStatisticsLsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4)
)
_TnMplsStatisticsLspTable_Object = MibTable
tnMplsStatisticsLspTable = _TnMplsStatisticsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    tnMplsStatisticsLspTable.setStatus("current")
_TnMplsStatisticsLspEntry_Object = MibTableRow
tnMplsStatisticsLspEntry = _TnMplsStatisticsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1)
)
tnMplsStatisticsLspEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsStatisticsLspGroupIndex"),
)
if mibBuilder.loadTexts:
    tnMplsStatisticsLspEntry.setStatus("current")


class _TnMplsStatisticsLspGroupIndex_Type(Integer32):
    """Custom type tnMplsStatisticsLspGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnMplsStatisticsLspGroupIndex_Type.__name__ = "Integer32"
_TnMplsStatisticsLspGroupIndex_Object = MibTableColumn
tnMplsStatisticsLspGroupIndex = _TnMplsStatisticsLspGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 1),
    _TnMplsStatisticsLspGroupIndex_Type()
)
tnMplsStatisticsLspGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspGroupIndex.setStatus("current")
_TnMplsStatisticsLspFwdRxGreenFrames_Type = Counter64
_TnMplsStatisticsLspFwdRxGreenFrames_Object = MibTableColumn
tnMplsStatisticsLspFwdRxGreenFrames = _TnMplsStatisticsLspFwdRxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 3),
    _TnMplsStatisticsLspFwdRxGreenFrames_Type()
)
tnMplsStatisticsLspFwdRxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdRxGreenFrames.setStatus("current")
_TnMplsStatisticsLspFwdRxGreenBytes_Type = Counter64
_TnMplsStatisticsLspFwdRxGreenBytes_Object = MibTableColumn
tnMplsStatisticsLspFwdRxGreenBytes = _TnMplsStatisticsLspFwdRxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 4),
    _TnMplsStatisticsLspFwdRxGreenBytes_Type()
)
tnMplsStatisticsLspFwdRxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdRxGreenBytes.setStatus("current")
_TnMplsStatisticsLspFwdRxYellowFrames_Type = Counter64
_TnMplsStatisticsLspFwdRxYellowFrames_Object = MibTableColumn
tnMplsStatisticsLspFwdRxYellowFrames = _TnMplsStatisticsLspFwdRxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 5),
    _TnMplsStatisticsLspFwdRxYellowFrames_Type()
)
tnMplsStatisticsLspFwdRxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdRxYellowFrames.setStatus("current")
_TnMplsStatisticsLspFwdRxYellowBytes_Type = Counter64
_TnMplsStatisticsLspFwdRxYellowBytes_Object = MibTableColumn
tnMplsStatisticsLspFwdRxYellowBytes = _TnMplsStatisticsLspFwdRxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 6),
    _TnMplsStatisticsLspFwdRxYellowBytes_Type()
)
tnMplsStatisticsLspFwdRxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdRxYellowBytes.setStatus("current")
_TnMplsStatisticsLspFwdRxRedFrames_Type = Counter64
_TnMplsStatisticsLspFwdRxRedFrames_Object = MibTableColumn
tnMplsStatisticsLspFwdRxRedFrames = _TnMplsStatisticsLspFwdRxRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 7),
    _TnMplsStatisticsLspFwdRxRedFrames_Type()
)
tnMplsStatisticsLspFwdRxRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdRxRedFrames.setStatus("current")
_TnMplsStatisticsLspFwdRxRedBytes_Type = Counter64
_TnMplsStatisticsLspFwdRxRedBytes_Object = MibTableColumn
tnMplsStatisticsLspFwdRxRedBytes = _TnMplsStatisticsLspFwdRxRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 8),
    _TnMplsStatisticsLspFwdRxRedBytes_Type()
)
tnMplsStatisticsLspFwdRxRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdRxRedBytes.setStatus("current")
_TnMplsStatisticsLspFwdRxDiscardFrames_Type = Counter64
_TnMplsStatisticsLspFwdRxDiscardFrames_Object = MibTableColumn
tnMplsStatisticsLspFwdRxDiscardFrames = _TnMplsStatisticsLspFwdRxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 9),
    _TnMplsStatisticsLspFwdRxDiscardFrames_Type()
)
tnMplsStatisticsLspFwdRxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdRxDiscardFrames.setStatus("current")
_TnMplsStatisticsLspFwdRxDiscardBytes_Type = Counter64
_TnMplsStatisticsLspFwdRxDiscardBytes_Object = MibTableColumn
tnMplsStatisticsLspFwdRxDiscardBytes = _TnMplsStatisticsLspFwdRxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 10),
    _TnMplsStatisticsLspFwdRxDiscardBytes_Type()
)
tnMplsStatisticsLspFwdRxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdRxDiscardBytes.setStatus("current")
_TnMplsStatisticsLspFwdTxGreenFrames_Type = Counter64
_TnMplsStatisticsLspFwdTxGreenFrames_Object = MibTableColumn
tnMplsStatisticsLspFwdTxGreenFrames = _TnMplsStatisticsLspFwdTxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 11),
    _TnMplsStatisticsLspFwdTxGreenFrames_Type()
)
tnMplsStatisticsLspFwdTxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdTxGreenFrames.setStatus("current")
_TnMplsStatisticsLspFwdTxGreenBytes_Type = Counter64
_TnMplsStatisticsLspFwdTxGreenBytes_Object = MibTableColumn
tnMplsStatisticsLspFwdTxGreenBytes = _TnMplsStatisticsLspFwdTxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 12),
    _TnMplsStatisticsLspFwdTxGreenBytes_Type()
)
tnMplsStatisticsLspFwdTxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdTxGreenBytes.setStatus("current")
_TnMplsStatisticsLspFwdTxYellowFrames_Type = Counter64
_TnMplsStatisticsLspFwdTxYellowFrames_Object = MibTableColumn
tnMplsStatisticsLspFwdTxYellowFrames = _TnMplsStatisticsLspFwdTxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 13),
    _TnMplsStatisticsLspFwdTxYellowFrames_Type()
)
tnMplsStatisticsLspFwdTxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdTxYellowFrames.setStatus("current")
_TnMplsStatisticsLspFwdTxYellowBytes_Type = Counter64
_TnMplsStatisticsLspFwdTxYellowBytes_Object = MibTableColumn
tnMplsStatisticsLspFwdTxYellowBytes = _TnMplsStatisticsLspFwdTxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 14),
    _TnMplsStatisticsLspFwdTxYellowBytes_Type()
)
tnMplsStatisticsLspFwdTxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdTxYellowBytes.setStatus("current")
_TnMplsStatisticsLspFwdTxDiscardFrames_Type = Counter64
_TnMplsStatisticsLspFwdTxDiscardFrames_Object = MibTableColumn
tnMplsStatisticsLspFwdTxDiscardFrames = _TnMplsStatisticsLspFwdTxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 15),
    _TnMplsStatisticsLspFwdTxDiscardFrames_Type()
)
tnMplsStatisticsLspFwdTxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdTxDiscardFrames.setStatus("current")
_TnMplsStatisticsLspFwdTxDiscardBytes_Type = Counter64
_TnMplsStatisticsLspFwdTxDiscardBytes_Object = MibTableColumn
tnMplsStatisticsLspFwdTxDiscardBytes = _TnMplsStatisticsLspFwdTxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 16),
    _TnMplsStatisticsLspFwdTxDiscardBytes_Type()
)
tnMplsStatisticsLspFwdTxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspFwdTxDiscardBytes.setStatus("current")
_TnMplsStatisticsLspRewRxGreenFrames_Type = Counter64
_TnMplsStatisticsLspRewRxGreenFrames_Object = MibTableColumn
tnMplsStatisticsLspRewRxGreenFrames = _TnMplsStatisticsLspRewRxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 17),
    _TnMplsStatisticsLspRewRxGreenFrames_Type()
)
tnMplsStatisticsLspRewRxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewRxGreenFrames.setStatus("current")
_TnMplsStatisticsLspRewRxGreenBytes_Type = Counter64
_TnMplsStatisticsLspRewRxGreenBytes_Object = MibTableColumn
tnMplsStatisticsLspRewRxGreenBytes = _TnMplsStatisticsLspRewRxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 18),
    _TnMplsStatisticsLspRewRxGreenBytes_Type()
)
tnMplsStatisticsLspRewRxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewRxGreenBytes.setStatus("current")
_TnMplsStatisticsLspRewRxYellowFrames_Type = Counter64
_TnMplsStatisticsLspRewRxYellowFrames_Object = MibTableColumn
tnMplsStatisticsLspRewRxYellowFrames = _TnMplsStatisticsLspRewRxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 19),
    _TnMplsStatisticsLspRewRxYellowFrames_Type()
)
tnMplsStatisticsLspRewRxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewRxYellowFrames.setStatus("current")
_TnMplsStatisticsLspRewRxYellowBytes_Type = Counter64
_TnMplsStatisticsLspRewRxYellowBytes_Object = MibTableColumn
tnMplsStatisticsLspRewRxYellowBytes = _TnMplsStatisticsLspRewRxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 20),
    _TnMplsStatisticsLspRewRxYellowBytes_Type()
)
tnMplsStatisticsLspRewRxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewRxYellowBytes.setStatus("current")
_TnMplsStatisticsLspRewRxRedFrames_Type = Counter64
_TnMplsStatisticsLspRewRxRedFrames_Object = MibTableColumn
tnMplsStatisticsLspRewRxRedFrames = _TnMplsStatisticsLspRewRxRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 21),
    _TnMplsStatisticsLspRewRxRedFrames_Type()
)
tnMplsStatisticsLspRewRxRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewRxRedFrames.setStatus("current")
_TnMplsStatisticsLspRewRxRedBytes_Type = Counter64
_TnMplsStatisticsLspRewRxRedBytes_Object = MibTableColumn
tnMplsStatisticsLspRewRxRedBytes = _TnMplsStatisticsLspRewRxRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 22),
    _TnMplsStatisticsLspRewRxRedBytes_Type()
)
tnMplsStatisticsLspRewRxRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewRxRedBytes.setStatus("current")
_TnMplsStatisticsLspRewRxDiscardFrames_Type = Counter64
_TnMplsStatisticsLspRewRxDiscardFrames_Object = MibTableColumn
tnMplsStatisticsLspRewRxDiscardFrames = _TnMplsStatisticsLspRewRxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 23),
    _TnMplsStatisticsLspRewRxDiscardFrames_Type()
)
tnMplsStatisticsLspRewRxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewRxDiscardFrames.setStatus("current")
_TnMplsStatisticsLspRewRxDiscardBytes_Type = Counter64
_TnMplsStatisticsLspRewRxDiscardBytes_Object = MibTableColumn
tnMplsStatisticsLspRewRxDiscardBytes = _TnMplsStatisticsLspRewRxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 24),
    _TnMplsStatisticsLspRewRxDiscardBytes_Type()
)
tnMplsStatisticsLspRewRxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewRxDiscardBytes.setStatus("current")
_TnMplsStatisticsLspRewTxGreenFrames_Type = Counter64
_TnMplsStatisticsLspRewTxGreenFrames_Object = MibTableColumn
tnMplsStatisticsLspRewTxGreenFrames = _TnMplsStatisticsLspRewTxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 25),
    _TnMplsStatisticsLspRewTxGreenFrames_Type()
)
tnMplsStatisticsLspRewTxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewTxGreenFrames.setStatus("current")
_TnMplsStatisticsLspRewTxGreenBytes_Type = Counter64
_TnMplsStatisticsLspRewTxGreenBytes_Object = MibTableColumn
tnMplsStatisticsLspRewTxGreenBytes = _TnMplsStatisticsLspRewTxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 26),
    _TnMplsStatisticsLspRewTxGreenBytes_Type()
)
tnMplsStatisticsLspRewTxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewTxGreenBytes.setStatus("current")
_TnMplsStatisticsLspRewTxYellowFrames_Type = Counter64
_TnMplsStatisticsLspRewTxYellowFrames_Object = MibTableColumn
tnMplsStatisticsLspRewTxYellowFrames = _TnMplsStatisticsLspRewTxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 27),
    _TnMplsStatisticsLspRewTxYellowFrames_Type()
)
tnMplsStatisticsLspRewTxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewTxYellowFrames.setStatus("current")
_TnMplsStatisticsLspRewTxYellowBytes_Type = Counter64
_TnMplsStatisticsLspRewTxYellowBytes_Object = MibTableColumn
tnMplsStatisticsLspRewTxYellowBytes = _TnMplsStatisticsLspRewTxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 28),
    _TnMplsStatisticsLspRewTxYellowBytes_Type()
)
tnMplsStatisticsLspRewTxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewTxYellowBytes.setStatus("current")
_TnMplsStatisticsLspRewTxDiscardFrames_Type = Counter64
_TnMplsStatisticsLspRewTxDiscardFrames_Object = MibTableColumn
tnMplsStatisticsLspRewTxDiscardFrames = _TnMplsStatisticsLspRewTxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 29),
    _TnMplsStatisticsLspRewTxDiscardFrames_Type()
)
tnMplsStatisticsLspRewTxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewTxDiscardFrames.setStatus("current")
_TnMplsStatisticsLspRewTxDiscardBytes_Type = Counter64
_TnMplsStatisticsLspRewTxDiscardBytes_Object = MibTableColumn
tnMplsStatisticsLspRewTxDiscardBytes = _TnMplsStatisticsLspRewTxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 4, 1, 1, 30),
    _TnMplsStatisticsLspRewTxDiscardBytes_Type()
)
tnMplsStatisticsLspRewTxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsLspRewTxDiscardBytes.setStatus("current")
_TnMplsStatisticsPw_ObjectIdentity = ObjectIdentity
tnMplsStatisticsPw = _TnMplsStatisticsPw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5)
)
_TnMplsStatisticsPwTable_Object = MibTable
tnMplsStatisticsPwTable = _TnMplsStatisticsPwTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    tnMplsStatisticsPwTable.setStatus("current")
_TnMplsStatisticsPwEntry_Object = MibTableRow
tnMplsStatisticsPwEntry = _TnMplsStatisticsPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1)
)
tnMplsStatisticsPwEntry.setIndexNames(
    (0, "TN-MPLS-MIB", "tnMplsStatisticsPwGroupIfIndex"),
)
if mibBuilder.loadTexts:
    tnMplsStatisticsPwEntry.setStatus("current")
_TnMplsStatisticsPwGroupIfIndex_Type = TNInterfaceIndex
_TnMplsStatisticsPwGroupIfIndex_Object = MibTableColumn
tnMplsStatisticsPwGroupIfIndex = _TnMplsStatisticsPwGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 1),
    _TnMplsStatisticsPwGroupIfIndex_Type()
)
tnMplsStatisticsPwGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwGroupIfIndex.setStatus("current")
_TnMplsStatisticsPwRxGreenFrames_Type = Counter64
_TnMplsStatisticsPwRxGreenFrames_Object = MibTableColumn
tnMplsStatisticsPwRxGreenFrames = _TnMplsStatisticsPwRxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 3),
    _TnMplsStatisticsPwRxGreenFrames_Type()
)
tnMplsStatisticsPwRxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwRxGreenFrames.setStatus("current")
_TnMplsStatisticsPwRxGreenBytes_Type = Counter64
_TnMplsStatisticsPwRxGreenBytes_Object = MibTableColumn
tnMplsStatisticsPwRxGreenBytes = _TnMplsStatisticsPwRxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 4),
    _TnMplsStatisticsPwRxGreenBytes_Type()
)
tnMplsStatisticsPwRxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwRxGreenBytes.setStatus("current")
_TnMplsStatisticsPwRxYellowFrames_Type = Counter64
_TnMplsStatisticsPwRxYellowFrames_Object = MibTableColumn
tnMplsStatisticsPwRxYellowFrames = _TnMplsStatisticsPwRxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 5),
    _TnMplsStatisticsPwRxYellowFrames_Type()
)
tnMplsStatisticsPwRxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwRxYellowFrames.setStatus("current")
_TnMplsStatisticsPwRxYellowBytes_Type = Counter64
_TnMplsStatisticsPwRxYellowBytes_Object = MibTableColumn
tnMplsStatisticsPwRxYellowBytes = _TnMplsStatisticsPwRxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 6),
    _TnMplsStatisticsPwRxYellowBytes_Type()
)
tnMplsStatisticsPwRxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwRxYellowBytes.setStatus("current")
_TnMplsStatisticsPwRxRedFrames_Type = Counter64
_TnMplsStatisticsPwRxRedFrames_Object = MibTableColumn
tnMplsStatisticsPwRxRedFrames = _TnMplsStatisticsPwRxRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 7),
    _TnMplsStatisticsPwRxRedFrames_Type()
)
tnMplsStatisticsPwRxRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwRxRedFrames.setStatus("current")
_TnMplsStatisticsPwRxRedBytes_Type = Counter64
_TnMplsStatisticsPwRxRedBytes_Object = MibTableColumn
tnMplsStatisticsPwRxRedBytes = _TnMplsStatisticsPwRxRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 8),
    _TnMplsStatisticsPwRxRedBytes_Type()
)
tnMplsStatisticsPwRxRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwRxRedBytes.setStatus("current")
_TnMplsStatisticsPwRxDiscardFrames_Type = Counter64
_TnMplsStatisticsPwRxDiscardFrames_Object = MibTableColumn
tnMplsStatisticsPwRxDiscardFrames = _TnMplsStatisticsPwRxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 9),
    _TnMplsStatisticsPwRxDiscardFrames_Type()
)
tnMplsStatisticsPwRxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwRxDiscardFrames.setStatus("current")
_TnMplsStatisticsPwRxDiscardBytes_Type = Counter64
_TnMplsStatisticsPwRxDiscardBytes_Object = MibTableColumn
tnMplsStatisticsPwRxDiscardBytes = _TnMplsStatisticsPwRxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 10),
    _TnMplsStatisticsPwRxDiscardBytes_Type()
)
tnMplsStatisticsPwRxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwRxDiscardBytes.setStatus("current")
_TnMplsStatisticsPwTxGreenFrames_Type = Counter64
_TnMplsStatisticsPwTxGreenFrames_Object = MibTableColumn
tnMplsStatisticsPwTxGreenFrames = _TnMplsStatisticsPwTxGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 11),
    _TnMplsStatisticsPwTxGreenFrames_Type()
)
tnMplsStatisticsPwTxGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwTxGreenFrames.setStatus("current")
_TnMplsStatisticsPwTxGreenBytes_Type = Counter64
_TnMplsStatisticsPwTxGreenBytes_Object = MibTableColumn
tnMplsStatisticsPwTxGreenBytes = _TnMplsStatisticsPwTxGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 12),
    _TnMplsStatisticsPwTxGreenBytes_Type()
)
tnMplsStatisticsPwTxGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwTxGreenBytes.setStatus("current")
_TnMplsStatisticsPwTxYellowFrames_Type = Counter64
_TnMplsStatisticsPwTxYellowFrames_Object = MibTableColumn
tnMplsStatisticsPwTxYellowFrames = _TnMplsStatisticsPwTxYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 13),
    _TnMplsStatisticsPwTxYellowFrames_Type()
)
tnMplsStatisticsPwTxYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwTxYellowFrames.setStatus("current")
_TnMplsStatisticsPwTxYellowBytes_Type = Counter64
_TnMplsStatisticsPwTxYellowBytes_Object = MibTableColumn
tnMplsStatisticsPwTxYellowBytes = _TnMplsStatisticsPwTxYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 14),
    _TnMplsStatisticsPwTxYellowBytes_Type()
)
tnMplsStatisticsPwTxYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwTxYellowBytes.setStatus("current")
_TnMplsStatisticsPwTxDiscardFrames_Type = Counter64
_TnMplsStatisticsPwTxDiscardFrames_Object = MibTableColumn
tnMplsStatisticsPwTxDiscardFrames = _TnMplsStatisticsPwTxDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 15),
    _TnMplsStatisticsPwTxDiscardFrames_Type()
)
tnMplsStatisticsPwTxDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwTxDiscardFrames.setStatus("current")
_TnMplsStatisticsPwTxDiscardBytes_Type = Counter64
_TnMplsStatisticsPwTxDiscardBytes_Object = MibTableColumn
tnMplsStatisticsPwTxDiscardBytes = _TnMplsStatisticsPwTxDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 1, 5, 5, 1, 1, 16),
    _TnMplsStatisticsPwTxDiscardBytes_Type()
)
tnMplsStatisticsPwTxDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMplsStatisticsPwTxDiscardBytes.setStatus("current")
_TnMplsMibConformance_ObjectIdentity = ObjectIdentity
tnMplsMibConformance = _TnMplsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2)
)
_TnMplsMibCompliances_ObjectIdentity = ObjectIdentity
tnMplsMibCompliances = _TnMplsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 1)
)
_TnMplsMibGroups_ObjectIdentity = ObjectIdentity
tnMplsMibGroups = _TnMplsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2)
)

# Managed Objects groups

tnMplsCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 1)
)
tnMplsCapabilitiesInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsCapabilitiesMaxLinks"),
        ("TN-MPLS-MIB", "tnMplsCapabilitiesMaxTunnels"),
        ("TN-MPLS-MIB", "tnMplsCapabilitiesMaxPw"),
        ("TN-MPLS-MIB", "tnMplsCapabilitiesMaxLsp"),
        ("TN-MPLS-MIB", "tnMplsCapabilitiesMaxCosMap"),
        ("TN-MPLS-MIB", "tnMplsCapabilitiesMaxTunnelNameLen"))
)
if mibBuilder.loadTexts:
    tnMplsCapabilitiesInfoGroup.setStatus("current")

tnMplsConfigGlobalMainInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 2)
)
tnMplsConfigGlobalMainInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsConfigGlobalMainTunnelMode"),
        ("TN-MPLS-MIB", "tnMplsConfigGlobalMainGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigGlobalMainNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigGlobalMainIccCarrierCode"))
)
if mibBuilder.loadTexts:
    tnMplsConfigGlobalMainInfoGroup.setStatus("current")

tnMplsConfigLinkTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 3)
)
tnMplsConfigLinkTableInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsConfigLinkPort"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkMACAddressNextHop"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkMACAddress"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkVLANTagType"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkVLANId"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkVLANpcp"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkVLANdei"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkSrcNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkSrcGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkDstNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkDstGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkDstIfNum"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkSrcNodeIdValid"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkSrcGlobalIdValid"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkDstGlobalIdValid"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkAction"))
)
if mibBuilder.loadTexts:
    tnMplsConfigLinkTableInfoGroup.setStatus("current")

tnMplsConfigLinkRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 4)
)
tnMplsConfigLinkRowEditorInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorGroupIfIndex"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorPort"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorMACAddressNextHop"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorMACAddress"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorVLANTagType"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorVLANId"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorVLANpcp"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorVLANdei"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorSrcNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorSrcGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorDstNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorDstGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorDstIfNum"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorSrcNodeIdValid"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorSrcGlobalIdValid"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorDstGlobalIdValid"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorAction"))
)
if mibBuilder.loadTexts:
    tnMplsConfigLinkRowEditorInfoGroup.setStatus("current")

tnMplsConfigTunnelTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 5)
)
tnMplsConfigTunnelTableInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsConfigTunnelTunnelName"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelTunnelMode"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelSrcNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelSrcGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelDstNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelDstGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelDstTunnelTpNum"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelSrcTunnelTpNum"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelSrcLspNum"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelDstLspNum"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelIsSpme"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelSrcNodeIsValid"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelSrcGlobalIdValid"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelDstGlobalIdValid"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelIngressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelEgressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelAttachInterface"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelTrafficClass"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelTtl"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelInCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelOutCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelIsLLsp"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelLLspCos"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelAction"))
)
if mibBuilder.loadTexts:
    tnMplsConfigTunnelTableInfoGroup.setStatus("current")

tnMplsConfigTunnelRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 6)
)
tnMplsConfigTunnelRowEditorInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorGroupIfIndex"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorTunnelName"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorTunnelMode"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorSrcNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorSrcGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorDstNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorDstGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorDstTunnelTpNum"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorSrcTunnelTpNum"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorSrcLspNum"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorDstLspNum"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorIsSpme"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorSrcNodeIsValid"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorSrcGlobalIdValid"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorDstGlobalIdValid"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorIngressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorEgressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorAttachInterface"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorTrafficClass"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorTtl"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorInCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorOutCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorIsLLsp"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorLLspCos"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorAction"))
)
if mibBuilder.loadTexts:
    tnMplsConfigTunnelRowEditorInfoGroup.setStatus("current")

tnMplsConfigLspTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 7)
)
tnMplsConfigLspTableInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsConfigLspXcName"),
        ("TN-MPLS-MIB", "tnMplsConfigLspSrcNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspSrcNodeIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigLspSrcGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspSrcGlobalIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigLspSrcTunnelTpNum"),
        ("TN-MPLS-MIB", "tnMplsConfigLspDstNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspDstGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspDstGlobalIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigLspDstTunnelTpNum"),
        ("TN-MPLS-MIB", "tnMplsConfigLspSrcLspNumber"),
        ("TN-MPLS-MIB", "tnMplsConfigLspDstLspNumber"),
        ("TN-MPLS-MIB", "tnMplsConfigLspForwardIngressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigLspForwardEgressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigLspForwardAttachInterface"),
        ("TN-MPLS-MIB", "tnMplsConfigLspForwardInCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspForwardOutCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspForwardIsLLsp"),
        ("TN-MPLS-MIB", "tnMplsConfigLspForwardHQoSId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspForwardLLspCos"),
        ("TN-MPLS-MIB", "tnMplsConfigLspReverseIngressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigLspReverseEgressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigLspReverseAttachInterface"),
        ("TN-MPLS-MIB", "tnMplsConfigLspReverseInCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspReverseOutCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspReverseIsLLsp"),
        ("TN-MPLS-MIB", "tnMplsConfigLspReverseLLspCos"),
        ("TN-MPLS-MIB", "tnMplsConfigLspReverseHQoSId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspAction"))
)
if mibBuilder.loadTexts:
    tnMplsConfigLspTableInfoGroup.setStatus("current")

tnMplsConfigLspRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 8)
)
tnMplsConfigLspRowEditorInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsConfigLspRowEditorGroupIndex"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorXcName"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorSrcNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorSrcNodeIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorSrcGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorSrcGlobalIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorSrcTunnelTpNum"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorDstNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorDstGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorDstGlobalIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorDstTunnelTpNum"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorSrcLspNumber"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorDstLspNumber"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorForwardIngressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorForwardEgressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorForwardAttachInterface"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorForwardInCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorForwardOutCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorForwardIsLLsp"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorForwardHQoSId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorForwardLLspCos"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorReverseIngressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorReverseEgressLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorReverseAttachInterface"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorReverseInCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorReverseOutCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorReverseIsLLsp"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorReverseLLspCos"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorReverseHQoSId"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorAction"))
)
if mibBuilder.loadTexts:
    tnMplsConfigLspRowEditorInfoGroup.setStatus("current")

tnMplsConfigPwTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 9)
)
tnMplsConfigPwTableInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsConfigPwInLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigPwOutLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigPwControlWord"),
        ("TN-MPLS-MIB", "tnMplsConfigPwUseControlWord"),
        ("TN-MPLS-MIB", "tnMplsConfigPwTunnelMode"),
        ("TN-MPLS-MIB", "tnMplsConfigPwTrafficClass"),
        ("TN-MPLS-MIB", "tnMplsConfigPwTtl"),
        ("TN-MPLS-MIB", "tnMplsConfigPwInCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwOutCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwIsLLsp"),
        ("TN-MPLS-MIB", "tnMplsConfigPwLLspCos"),
        ("TN-MPLS-MIB", "tnMplsConfigPwAttachInterface"),
        ("TN-MPLS-MIB", "tnMplsConfigPwStitchPwInterface"),
        ("TN-MPLS-MIB", "tnMplsConfigPwVccvType"),
        ("TN-MPLS-MIB", "tnMplsConfigPwHQoSId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwSrcNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwSrcNodeIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigPwSrcGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwSrcGlobalIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigPwDstNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwDstGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwDstGlobalIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigPwSrcAcId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwDstAcId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwSrcAgiValue"),
        ("TN-MPLS-MIB", "tnMplsConfigPwDstAgiValue"),
        ("TN-MPLS-MIB", "tnMplsConfigPwSrcAgiType"),
        ("TN-MPLS-MIB", "tnMplsConfigPwSrcAgiLength"),
        ("TN-MPLS-MIB", "tnMplsConfigPwDstAgiType"),
        ("TN-MPLS-MIB", "tnMplsConfigPwDstAgiLength"),
        ("TN-MPLS-MIB", "tnMplsConfigPwAction"))
)
if mibBuilder.loadTexts:
    tnMplsConfigPwTableInfoGroup.setStatus("current")

tnMplsConfigPwRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 10)
)
tnMplsConfigPwRowEditorInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsConfigPwRowEditorGroupIfIndex"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorInLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorOutLabel"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorControlWord"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorUseControlWord"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorTunnelMode"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorTrafficClass"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorTtl"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorInCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorOutCosMapId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorIsLLsp"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorLLspCos"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorAttachInterface"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorStitchPwInterface"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorVccvType"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorHQoSId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorSrcNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorSrcNodeIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorSrcGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorSrcGlobalIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorDstNodeId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorDstGlobalId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorDstGlobalIdIsDefined"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorSrcAcId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorDstAcId"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorSrcAgiValue"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorDstAgiValue"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorSrcAgiType"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorSrcAgiLength"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorDstAgiType"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorDstAgiLength"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorAction"))
)
if mibBuilder.loadTexts:
    tnMplsConfigPwRowEditorInfoGroup.setStatus("current")

tnMplsConfigCosMapTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 11)
)
tnMplsConfigCosMapTableInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToCos0"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToCos1"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToCos2"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToCos3"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToCos4"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToCos5"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToCos6"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToCos7"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToDp0"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToDp1"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToDp2"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToDp3"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToDp4"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToDp5"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToDp6"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapInTcToDp7"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc00"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc10"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc20"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc30"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc40"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc50"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc60"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc70"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc01"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc11"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc21"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc31"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc41"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc51"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc61"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapOutCosDpToTc71"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapAction"))
)
if mibBuilder.loadTexts:
    tnMplsConfigCosMapTableInfoGroup.setStatus("current")

tnMplsConfigCosMapRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 12)
)
tnMplsConfigCosMapRowEditorInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorGroupIndex"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToCos0"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToCos1"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToCos2"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToCos3"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToCos4"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToCos5"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToCos6"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToCos7"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToDp0"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToDp1"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToDp2"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToDp3"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToDp4"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToDp5"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToDp6"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInTcToDp7"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc00"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc10"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc20"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc30"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc40"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc50"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc60"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc70"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc01"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc11"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc21"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc31"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc41"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc51"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc61"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorOutCosDpToTc71"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorAction"))
)
if mibBuilder.loadTexts:
    tnMplsConfigCosMapRowEditorInfoGroup.setStatus("current")

tnMplsStatusLinkTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 13)
)
tnMplsStatusLinkTableInfoGroup.setObjects(
    ("TN-MPLS-MIB", "tnMplsStatusLinkOamActive")
)
if mibBuilder.loadTexts:
    tnMplsStatusLinkTableInfoGroup.setStatus("current")

tnMplsStatusTunnelTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 14)
)
tnMplsStatusTunnelTableInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsStatusTunnelOamActive"),
        ("TN-MPLS-MIB", "tnMplsStatusTunnelState"),
        ("TN-MPLS-MIB", "tnMplsStatusTunnelIngressLabel"),
        ("TN-MPLS-MIB", "tnMplsStatusTunnelEgressLabel"),
        ("TN-MPLS-MIB", "tnMplsStatusTunnelWorkingActive"))
)
if mibBuilder.loadTexts:
    tnMplsStatusTunnelTableInfoGroup.setStatus("current")

tnMplsStatusLspTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 15)
)
tnMplsStatusLspTableInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsStatusLspOamActive"),
        ("TN-MPLS-MIB", "tnMplsStatusLspState"))
)
if mibBuilder.loadTexts:
    tnMplsStatusLspTableInfoGroup.setStatus("current")

tnMplsStatusPwTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 16)
)
tnMplsStatusPwTableInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsStatusPwOamActive"),
        ("TN-MPLS-MIB", "tnMplsStatusPwState"))
)
if mibBuilder.loadTexts:
    tnMplsStatusPwTableInfoGroup.setStatus("current")

tnMplsControlLspTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 17)
)
tnMplsControlLspTableInfoGroup.setObjects(
    ("TN-MPLS-MIB", "tnMplsControlLspClear")
)
if mibBuilder.loadTexts:
    tnMplsControlLspTableInfoGroup.setStatus("current")

tnMplsControlIfTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 18)
)
tnMplsControlIfTableInfoGroup.setObjects(
    ("TN-MPLS-MIB", "tnMplsControlIfClear")
)
if mibBuilder.loadTexts:
    tnMplsControlIfTableInfoGroup.setStatus("current")

tnMplsStatisticsTunnelTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 19)
)
tnMplsStatisticsTunnelTableInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsStatisticsTunnelRxGreenFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelRxGreenBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelRxYellowFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelRxYellowBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelRxRedFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelRxRedBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelRxDiscardFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelRxDiscardBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelTxGreenFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelTxGreenBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelTxYellowFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelTxYellowBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelTxDiscardFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelTxDiscardBytes"))
)
if mibBuilder.loadTexts:
    tnMplsStatisticsTunnelTableInfoGroup.setStatus("current")

tnMplsStatisticsLspTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 20)
)
tnMplsStatisticsLspTableInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsStatisticsLspFwdRxGreenFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdRxGreenBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdRxYellowFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdRxYellowBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdRxRedFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdRxRedBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdRxDiscardFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdRxDiscardBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdTxGreenFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdTxGreenBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdTxYellowFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdTxYellowBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdTxDiscardFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspFwdTxDiscardBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewRxGreenFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewRxGreenBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewRxYellowFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewRxYellowBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewRxRedFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewRxRedBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewRxDiscardFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewRxDiscardBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewTxGreenFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewTxGreenBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewTxYellowFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewTxYellowBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewTxDiscardFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspRewTxDiscardBytes"))
)
if mibBuilder.loadTexts:
    tnMplsStatisticsLspTableInfoGroup.setStatus("current")

tnMplsStatisticsPwTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 2, 21)
)
tnMplsStatisticsPwTableInfoGroup.setObjects(
      *(("TN-MPLS-MIB", "tnMplsStatisticsPwRxGreenFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwRxGreenBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwRxYellowFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwRxYellowBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwRxRedFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwRxRedBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwRxDiscardFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwRxDiscardBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwTxGreenFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwTxGreenBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwTxYellowFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwTxYellowBytes"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwTxDiscardFrames"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwTxDiscardBytes"))
)
if mibBuilder.loadTexts:
    tnMplsStatisticsPwTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnMplsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 144, 2, 1, 1)
)
tnMplsMibCompliance.setObjects(
      *(("TN-MPLS-MIB", "tnMplsCapabilitiesInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsConfigGlobalMainInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsConfigLinkRowEditorInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsConfigTunnelRowEditorInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsConfigLspTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsConfigLspRowEditorInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsConfigPwTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsConfigPwRowEditorInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsConfigCosMapRowEditorInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsStatusLinkTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsStatusTunnelTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsStatusLspTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsStatusPwTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsControlLspTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsControlIfTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsStatisticsTunnelTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsStatisticsLspTableInfoGroup"),
        ("TN-MPLS-MIB", "tnMplsStatisticsPwTableInfoGroup"))
)
if mibBuilder.loadTexts:
    tnMplsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-MPLS-MIB",
    **{"TNMplsStateType": TNMplsStateType,
       "TNMplsTagType": TNMplsTagType,
       "TNMplsTunnelMode": TNMplsTunnelMode,
       "TNMplsVccvType": TNMplsVccvType,
       "tnMplsMib": tnMplsMib,
       "tnMplsMibObjects": tnMplsMibObjects,
       "tnMplsCapabilities": tnMplsCapabilities,
       "tnMplsCapabilitiesMaxLinks": tnMplsCapabilitiesMaxLinks,
       "tnMplsCapabilitiesMaxTunnels": tnMplsCapabilitiesMaxTunnels,
       "tnMplsCapabilitiesMaxPw": tnMplsCapabilitiesMaxPw,
       "tnMplsCapabilitiesMaxLsp": tnMplsCapabilitiesMaxLsp,
       "tnMplsCapabilitiesMaxCosMap": tnMplsCapabilitiesMaxCosMap,
       "tnMplsCapabilitiesMaxTunnelNameLen": tnMplsCapabilitiesMaxTunnelNameLen,
       "tnMplsConfig": tnMplsConfig,
       "tnMplsConfigGlobal": tnMplsConfigGlobal,
       "tnMplsConfigGlobalMain": tnMplsConfigGlobalMain,
       "tnMplsConfigGlobalMainTunnelMode": tnMplsConfigGlobalMainTunnelMode,
       "tnMplsConfigGlobalMainGlobalId": tnMplsConfigGlobalMainGlobalId,
       "tnMplsConfigGlobalMainNodeId": tnMplsConfigGlobalMainNodeId,
       "tnMplsConfigGlobalMainIccCarrierCode": tnMplsConfigGlobalMainIccCarrierCode,
       "tnMplsConfigLink": tnMplsConfigLink,
       "tnMplsConfigLinkTable": tnMplsConfigLinkTable,
       "tnMplsConfigLinkEntry": tnMplsConfigLinkEntry,
       "tnMplsConfigLinkGroupIfIndex": tnMplsConfigLinkGroupIfIndex,
       "tnMplsConfigLinkPort": tnMplsConfigLinkPort,
       "tnMplsConfigLinkMACAddressNextHop": tnMplsConfigLinkMACAddressNextHop,
       "tnMplsConfigLinkMACAddress": tnMplsConfigLinkMACAddress,
       "tnMplsConfigLinkVLANTagType": tnMplsConfigLinkVLANTagType,
       "tnMplsConfigLinkVLANId": tnMplsConfigLinkVLANId,
       "tnMplsConfigLinkVLANpcp": tnMplsConfigLinkVLANpcp,
       "tnMplsConfigLinkVLANdei": tnMplsConfigLinkVLANdei,
       "tnMplsConfigLinkSrcNodeId": tnMplsConfigLinkSrcNodeId,
       "tnMplsConfigLinkSrcGlobalId": tnMplsConfigLinkSrcGlobalId,
       "tnMplsConfigLinkDstNodeId": tnMplsConfigLinkDstNodeId,
       "tnMplsConfigLinkDstGlobalId": tnMplsConfigLinkDstGlobalId,
       "tnMplsConfigLinkDstIfNum": tnMplsConfigLinkDstIfNum,
       "tnMplsConfigLinkSrcNodeIdValid": tnMplsConfigLinkSrcNodeIdValid,
       "tnMplsConfigLinkSrcGlobalIdValid": tnMplsConfigLinkSrcGlobalIdValid,
       "tnMplsConfigLinkDstGlobalIdValid": tnMplsConfigLinkDstGlobalIdValid,
       "tnMplsConfigLinkAction": tnMplsConfigLinkAction,
       "tnMplsConfigLinkRowEditor": tnMplsConfigLinkRowEditor,
       "tnMplsConfigLinkRowEditorGroupIfIndex": tnMplsConfigLinkRowEditorGroupIfIndex,
       "tnMplsConfigLinkRowEditorPort": tnMplsConfigLinkRowEditorPort,
       "tnMplsConfigLinkRowEditorMACAddressNextHop": tnMplsConfigLinkRowEditorMACAddressNextHop,
       "tnMplsConfigLinkRowEditorMACAddress": tnMplsConfigLinkRowEditorMACAddress,
       "tnMplsConfigLinkRowEditorVLANTagType": tnMplsConfigLinkRowEditorVLANTagType,
       "tnMplsConfigLinkRowEditorVLANId": tnMplsConfigLinkRowEditorVLANId,
       "tnMplsConfigLinkRowEditorVLANpcp": tnMplsConfigLinkRowEditorVLANpcp,
       "tnMplsConfigLinkRowEditorVLANdei": tnMplsConfigLinkRowEditorVLANdei,
       "tnMplsConfigLinkRowEditorSrcNodeId": tnMplsConfigLinkRowEditorSrcNodeId,
       "tnMplsConfigLinkRowEditorSrcGlobalId": tnMplsConfigLinkRowEditorSrcGlobalId,
       "tnMplsConfigLinkRowEditorDstNodeId": tnMplsConfigLinkRowEditorDstNodeId,
       "tnMplsConfigLinkRowEditorDstGlobalId": tnMplsConfigLinkRowEditorDstGlobalId,
       "tnMplsConfigLinkRowEditorDstIfNum": tnMplsConfigLinkRowEditorDstIfNum,
       "tnMplsConfigLinkRowEditorSrcNodeIdValid": tnMplsConfigLinkRowEditorSrcNodeIdValid,
       "tnMplsConfigLinkRowEditorSrcGlobalIdValid": tnMplsConfigLinkRowEditorSrcGlobalIdValid,
       "tnMplsConfigLinkRowEditorDstGlobalIdValid": tnMplsConfigLinkRowEditorDstGlobalIdValid,
       "tnMplsConfigLinkRowEditorAction": tnMplsConfigLinkRowEditorAction,
       "tnMplsConfigTunnel": tnMplsConfigTunnel,
       "tnMplsConfigTunnelTable": tnMplsConfigTunnelTable,
       "tnMplsConfigTunnelEntry": tnMplsConfigTunnelEntry,
       "tnMplsConfigTunnelGroupIfIndex": tnMplsConfigTunnelGroupIfIndex,
       "tnMplsConfigTunnelTunnelName": tnMplsConfigTunnelTunnelName,
       "tnMplsConfigTunnelTunnelMode": tnMplsConfigTunnelTunnelMode,
       "tnMplsConfigTunnelSrcNodeId": tnMplsConfigTunnelSrcNodeId,
       "tnMplsConfigTunnelSrcGlobalId": tnMplsConfigTunnelSrcGlobalId,
       "tnMplsConfigTunnelDstNodeId": tnMplsConfigTunnelDstNodeId,
       "tnMplsConfigTunnelDstGlobalId": tnMplsConfigTunnelDstGlobalId,
       "tnMplsConfigTunnelDstTunnelTpNum": tnMplsConfigTunnelDstTunnelTpNum,
       "tnMplsConfigTunnelSrcTunnelTpNum": tnMplsConfigTunnelSrcTunnelTpNum,
       "tnMplsConfigTunnelSrcLspNum": tnMplsConfigTunnelSrcLspNum,
       "tnMplsConfigTunnelDstLspNum": tnMplsConfigTunnelDstLspNum,
       "tnMplsConfigTunnelIsSpme": tnMplsConfigTunnelIsSpme,
       "tnMplsConfigTunnelSrcNodeIsValid": tnMplsConfigTunnelSrcNodeIsValid,
       "tnMplsConfigTunnelSrcGlobalIdValid": tnMplsConfigTunnelSrcGlobalIdValid,
       "tnMplsConfigTunnelDstGlobalIdValid": tnMplsConfigTunnelDstGlobalIdValid,
       "tnMplsConfigTunnelIngressLabel": tnMplsConfigTunnelIngressLabel,
       "tnMplsConfigTunnelEgressLabel": tnMplsConfigTunnelEgressLabel,
       "tnMplsConfigTunnelAttachInterface": tnMplsConfigTunnelAttachInterface,
       "tnMplsConfigTunnelTrafficClass": tnMplsConfigTunnelTrafficClass,
       "tnMplsConfigTunnelTtl": tnMplsConfigTunnelTtl,
       "tnMplsConfigTunnelInCosMapId": tnMplsConfigTunnelInCosMapId,
       "tnMplsConfigTunnelOutCosMapId": tnMplsConfigTunnelOutCosMapId,
       "tnMplsConfigTunnelIsLLsp": tnMplsConfigTunnelIsLLsp,
       "tnMplsConfigTunnelLLspCos": tnMplsConfigTunnelLLspCos,
       "tnMplsConfigTunnelAction": tnMplsConfigTunnelAction,
       "tnMplsConfigTunnelRowEditor": tnMplsConfigTunnelRowEditor,
       "tnMplsConfigTunnelRowEditorGroupIfIndex": tnMplsConfigTunnelRowEditorGroupIfIndex,
       "tnMplsConfigTunnelRowEditorTunnelName": tnMplsConfigTunnelRowEditorTunnelName,
       "tnMplsConfigTunnelRowEditorTunnelMode": tnMplsConfigTunnelRowEditorTunnelMode,
       "tnMplsConfigTunnelRowEditorSrcNodeId": tnMplsConfigTunnelRowEditorSrcNodeId,
       "tnMplsConfigTunnelRowEditorSrcGlobalId": tnMplsConfigTunnelRowEditorSrcGlobalId,
       "tnMplsConfigTunnelRowEditorDstNodeId": tnMplsConfigTunnelRowEditorDstNodeId,
       "tnMplsConfigTunnelRowEditorDstGlobalId": tnMplsConfigTunnelRowEditorDstGlobalId,
       "tnMplsConfigTunnelRowEditorDstTunnelTpNum": tnMplsConfigTunnelRowEditorDstTunnelTpNum,
       "tnMplsConfigTunnelRowEditorSrcTunnelTpNum": tnMplsConfigTunnelRowEditorSrcTunnelTpNum,
       "tnMplsConfigTunnelRowEditorSrcLspNum": tnMplsConfigTunnelRowEditorSrcLspNum,
       "tnMplsConfigTunnelRowEditorDstLspNum": tnMplsConfigTunnelRowEditorDstLspNum,
       "tnMplsConfigTunnelRowEditorIsSpme": tnMplsConfigTunnelRowEditorIsSpme,
       "tnMplsConfigTunnelRowEditorSrcNodeIsValid": tnMplsConfigTunnelRowEditorSrcNodeIsValid,
       "tnMplsConfigTunnelRowEditorSrcGlobalIdValid": tnMplsConfigTunnelRowEditorSrcGlobalIdValid,
       "tnMplsConfigTunnelRowEditorDstGlobalIdValid": tnMplsConfigTunnelRowEditorDstGlobalIdValid,
       "tnMplsConfigTunnelRowEditorIngressLabel": tnMplsConfigTunnelRowEditorIngressLabel,
       "tnMplsConfigTunnelRowEditorEgressLabel": tnMplsConfigTunnelRowEditorEgressLabel,
       "tnMplsConfigTunnelRowEditorAttachInterface": tnMplsConfigTunnelRowEditorAttachInterface,
       "tnMplsConfigTunnelRowEditorTrafficClass": tnMplsConfigTunnelRowEditorTrafficClass,
       "tnMplsConfigTunnelRowEditorTtl": tnMplsConfigTunnelRowEditorTtl,
       "tnMplsConfigTunnelRowEditorInCosMapId": tnMplsConfigTunnelRowEditorInCosMapId,
       "tnMplsConfigTunnelRowEditorOutCosMapId": tnMplsConfigTunnelRowEditorOutCosMapId,
       "tnMplsConfigTunnelRowEditorIsLLsp": tnMplsConfigTunnelRowEditorIsLLsp,
       "tnMplsConfigTunnelRowEditorLLspCos": tnMplsConfigTunnelRowEditorLLspCos,
       "tnMplsConfigTunnelRowEditorAction": tnMplsConfigTunnelRowEditorAction,
       "tnMplsConfigLsp": tnMplsConfigLsp,
       "tnMplsConfigLspTable": tnMplsConfigLspTable,
       "tnMplsConfigLspEntry": tnMplsConfigLspEntry,
       "tnMplsConfigLspGroupIndex": tnMplsConfigLspGroupIndex,
       "tnMplsConfigLspXcName": tnMplsConfigLspXcName,
       "tnMplsConfigLspSrcNodeId": tnMplsConfigLspSrcNodeId,
       "tnMplsConfigLspSrcNodeIdIsDefined": tnMplsConfigLspSrcNodeIdIsDefined,
       "tnMplsConfigLspSrcGlobalId": tnMplsConfigLspSrcGlobalId,
       "tnMplsConfigLspSrcGlobalIdIsDefined": tnMplsConfigLspSrcGlobalIdIsDefined,
       "tnMplsConfigLspSrcTunnelTpNum": tnMplsConfigLspSrcTunnelTpNum,
       "tnMplsConfigLspDstNodeId": tnMplsConfigLspDstNodeId,
       "tnMplsConfigLspDstGlobalId": tnMplsConfigLspDstGlobalId,
       "tnMplsConfigLspDstGlobalIdIsDefined": tnMplsConfigLspDstGlobalIdIsDefined,
       "tnMplsConfigLspDstTunnelTpNum": tnMplsConfigLspDstTunnelTpNum,
       "tnMplsConfigLspSrcLspNumber": tnMplsConfigLspSrcLspNumber,
       "tnMplsConfigLspDstLspNumber": tnMplsConfigLspDstLspNumber,
       "tnMplsConfigLspForwardIngressLabel": tnMplsConfigLspForwardIngressLabel,
       "tnMplsConfigLspForwardEgressLabel": tnMplsConfigLspForwardEgressLabel,
       "tnMplsConfigLspForwardAttachInterface": tnMplsConfigLspForwardAttachInterface,
       "tnMplsConfigLspForwardInCosMapId": tnMplsConfigLspForwardInCosMapId,
       "tnMplsConfigLspForwardOutCosMapId": tnMplsConfigLspForwardOutCosMapId,
       "tnMplsConfigLspForwardIsLLsp": tnMplsConfigLspForwardIsLLsp,
       "tnMplsConfigLspForwardHQoSId": tnMplsConfigLspForwardHQoSId,
       "tnMplsConfigLspForwardLLspCos": tnMplsConfigLspForwardLLspCos,
       "tnMplsConfigLspReverseIngressLabel": tnMplsConfigLspReverseIngressLabel,
       "tnMplsConfigLspReverseEgressLabel": tnMplsConfigLspReverseEgressLabel,
       "tnMplsConfigLspReverseAttachInterface": tnMplsConfigLspReverseAttachInterface,
       "tnMplsConfigLspReverseInCosMapId": tnMplsConfigLspReverseInCosMapId,
       "tnMplsConfigLspReverseOutCosMapId": tnMplsConfigLspReverseOutCosMapId,
       "tnMplsConfigLspReverseIsLLsp": tnMplsConfigLspReverseIsLLsp,
       "tnMplsConfigLspReverseLLspCos": tnMplsConfigLspReverseLLspCos,
       "tnMplsConfigLspReverseHQoSId": tnMplsConfigLspReverseHQoSId,
       "tnMplsConfigLspAction": tnMplsConfigLspAction,
       "tnMplsConfigLspRowEditor": tnMplsConfigLspRowEditor,
       "tnMplsConfigLspRowEditorGroupIndex": tnMplsConfigLspRowEditorGroupIndex,
       "tnMplsConfigLspRowEditorXcName": tnMplsConfigLspRowEditorXcName,
       "tnMplsConfigLspRowEditorSrcNodeId": tnMplsConfigLspRowEditorSrcNodeId,
       "tnMplsConfigLspRowEditorSrcNodeIdIsDefined": tnMplsConfigLspRowEditorSrcNodeIdIsDefined,
       "tnMplsConfigLspRowEditorSrcGlobalId": tnMplsConfigLspRowEditorSrcGlobalId,
       "tnMplsConfigLspRowEditorSrcGlobalIdIsDefined": tnMplsConfigLspRowEditorSrcGlobalIdIsDefined,
       "tnMplsConfigLspRowEditorSrcTunnelTpNum": tnMplsConfigLspRowEditorSrcTunnelTpNum,
       "tnMplsConfigLspRowEditorDstNodeId": tnMplsConfigLspRowEditorDstNodeId,
       "tnMplsConfigLspRowEditorDstGlobalId": tnMplsConfigLspRowEditorDstGlobalId,
       "tnMplsConfigLspRowEditorDstGlobalIdIsDefined": tnMplsConfigLspRowEditorDstGlobalIdIsDefined,
       "tnMplsConfigLspRowEditorDstTunnelTpNum": tnMplsConfigLspRowEditorDstTunnelTpNum,
       "tnMplsConfigLspRowEditorSrcLspNumber": tnMplsConfigLspRowEditorSrcLspNumber,
       "tnMplsConfigLspRowEditorDstLspNumber": tnMplsConfigLspRowEditorDstLspNumber,
       "tnMplsConfigLspRowEditorForwardIngressLabel": tnMplsConfigLspRowEditorForwardIngressLabel,
       "tnMplsConfigLspRowEditorForwardEgressLabel": tnMplsConfigLspRowEditorForwardEgressLabel,
       "tnMplsConfigLspRowEditorForwardAttachInterface": tnMplsConfigLspRowEditorForwardAttachInterface,
       "tnMplsConfigLspRowEditorForwardInCosMapId": tnMplsConfigLspRowEditorForwardInCosMapId,
       "tnMplsConfigLspRowEditorForwardOutCosMapId": tnMplsConfigLspRowEditorForwardOutCosMapId,
       "tnMplsConfigLspRowEditorForwardIsLLsp": tnMplsConfigLspRowEditorForwardIsLLsp,
       "tnMplsConfigLspRowEditorForwardHQoSId": tnMplsConfigLspRowEditorForwardHQoSId,
       "tnMplsConfigLspRowEditorForwardLLspCos": tnMplsConfigLspRowEditorForwardLLspCos,
       "tnMplsConfigLspRowEditorReverseIngressLabel": tnMplsConfigLspRowEditorReverseIngressLabel,
       "tnMplsConfigLspRowEditorReverseEgressLabel": tnMplsConfigLspRowEditorReverseEgressLabel,
       "tnMplsConfigLspRowEditorReverseAttachInterface": tnMplsConfigLspRowEditorReverseAttachInterface,
       "tnMplsConfigLspRowEditorReverseInCosMapId": tnMplsConfigLspRowEditorReverseInCosMapId,
       "tnMplsConfigLspRowEditorReverseOutCosMapId": tnMplsConfigLspRowEditorReverseOutCosMapId,
       "tnMplsConfigLspRowEditorReverseIsLLsp": tnMplsConfigLspRowEditorReverseIsLLsp,
       "tnMplsConfigLspRowEditorReverseLLspCos": tnMplsConfigLspRowEditorReverseLLspCos,
       "tnMplsConfigLspRowEditorReverseHQoSId": tnMplsConfigLspRowEditorReverseHQoSId,
       "tnMplsConfigLspRowEditorAction": tnMplsConfigLspRowEditorAction,
       "tnMplsConfigPw": tnMplsConfigPw,
       "tnMplsConfigPwTable": tnMplsConfigPwTable,
       "tnMplsConfigPwEntry": tnMplsConfigPwEntry,
       "tnMplsConfigPwGroupIfIndex": tnMplsConfigPwGroupIfIndex,
       "tnMplsConfigPwInLabel": tnMplsConfigPwInLabel,
       "tnMplsConfigPwOutLabel": tnMplsConfigPwOutLabel,
       "tnMplsConfigPwControlWord": tnMplsConfigPwControlWord,
       "tnMplsConfigPwUseControlWord": tnMplsConfigPwUseControlWord,
       "tnMplsConfigPwTunnelMode": tnMplsConfigPwTunnelMode,
       "tnMplsConfigPwTrafficClass": tnMplsConfigPwTrafficClass,
       "tnMplsConfigPwTtl": tnMplsConfigPwTtl,
       "tnMplsConfigPwInCosMapId": tnMplsConfigPwInCosMapId,
       "tnMplsConfigPwOutCosMapId": tnMplsConfigPwOutCosMapId,
       "tnMplsConfigPwIsLLsp": tnMplsConfigPwIsLLsp,
       "tnMplsConfigPwLLspCos": tnMplsConfigPwLLspCos,
       "tnMplsConfigPwAttachInterface": tnMplsConfigPwAttachInterface,
       "tnMplsConfigPwStitchPwInterface": tnMplsConfigPwStitchPwInterface,
       "tnMplsConfigPwVccvType": tnMplsConfigPwVccvType,
       "tnMplsConfigPwHQoSId": tnMplsConfigPwHQoSId,
       "tnMplsConfigPwSrcNodeId": tnMplsConfigPwSrcNodeId,
       "tnMplsConfigPwSrcNodeIdIsDefined": tnMplsConfigPwSrcNodeIdIsDefined,
       "tnMplsConfigPwSrcGlobalId": tnMplsConfigPwSrcGlobalId,
       "tnMplsConfigPwSrcGlobalIdIsDefined": tnMplsConfigPwSrcGlobalIdIsDefined,
       "tnMplsConfigPwDstNodeId": tnMplsConfigPwDstNodeId,
       "tnMplsConfigPwDstGlobalId": tnMplsConfigPwDstGlobalId,
       "tnMplsConfigPwDstGlobalIdIsDefined": tnMplsConfigPwDstGlobalIdIsDefined,
       "tnMplsConfigPwSrcAcId": tnMplsConfigPwSrcAcId,
       "tnMplsConfigPwDstAcId": tnMplsConfigPwDstAcId,
       "tnMplsConfigPwSrcAgiValue": tnMplsConfigPwSrcAgiValue,
       "tnMplsConfigPwDstAgiValue": tnMplsConfigPwDstAgiValue,
       "tnMplsConfigPwSrcAgiType": tnMplsConfigPwSrcAgiType,
       "tnMplsConfigPwSrcAgiLength": tnMplsConfigPwSrcAgiLength,
       "tnMplsConfigPwDstAgiType": tnMplsConfigPwDstAgiType,
       "tnMplsConfigPwDstAgiLength": tnMplsConfigPwDstAgiLength,
       "tnMplsConfigPwAction": tnMplsConfigPwAction,
       "tnMplsConfigPwRowEditor": tnMplsConfigPwRowEditor,
       "tnMplsConfigPwRowEditorGroupIfIndex": tnMplsConfigPwRowEditorGroupIfIndex,
       "tnMplsConfigPwRowEditorInLabel": tnMplsConfigPwRowEditorInLabel,
       "tnMplsConfigPwRowEditorOutLabel": tnMplsConfigPwRowEditorOutLabel,
       "tnMplsConfigPwRowEditorControlWord": tnMplsConfigPwRowEditorControlWord,
       "tnMplsConfigPwRowEditorUseControlWord": tnMplsConfigPwRowEditorUseControlWord,
       "tnMplsConfigPwRowEditorTunnelMode": tnMplsConfigPwRowEditorTunnelMode,
       "tnMplsConfigPwRowEditorTrafficClass": tnMplsConfigPwRowEditorTrafficClass,
       "tnMplsConfigPwRowEditorTtl": tnMplsConfigPwRowEditorTtl,
       "tnMplsConfigPwRowEditorInCosMapId": tnMplsConfigPwRowEditorInCosMapId,
       "tnMplsConfigPwRowEditorOutCosMapId": tnMplsConfigPwRowEditorOutCosMapId,
       "tnMplsConfigPwRowEditorIsLLsp": tnMplsConfigPwRowEditorIsLLsp,
       "tnMplsConfigPwRowEditorLLspCos": tnMplsConfigPwRowEditorLLspCos,
       "tnMplsConfigPwRowEditorAttachInterface": tnMplsConfigPwRowEditorAttachInterface,
       "tnMplsConfigPwRowEditorStitchPwInterface": tnMplsConfigPwRowEditorStitchPwInterface,
       "tnMplsConfigPwRowEditorVccvType": tnMplsConfigPwRowEditorVccvType,
       "tnMplsConfigPwRowEditorHQoSId": tnMplsConfigPwRowEditorHQoSId,
       "tnMplsConfigPwRowEditorSrcNodeId": tnMplsConfigPwRowEditorSrcNodeId,
       "tnMplsConfigPwRowEditorSrcNodeIdIsDefined": tnMplsConfigPwRowEditorSrcNodeIdIsDefined,
       "tnMplsConfigPwRowEditorSrcGlobalId": tnMplsConfigPwRowEditorSrcGlobalId,
       "tnMplsConfigPwRowEditorSrcGlobalIdIsDefined": tnMplsConfigPwRowEditorSrcGlobalIdIsDefined,
       "tnMplsConfigPwRowEditorDstNodeId": tnMplsConfigPwRowEditorDstNodeId,
       "tnMplsConfigPwRowEditorDstGlobalId": tnMplsConfigPwRowEditorDstGlobalId,
       "tnMplsConfigPwRowEditorDstGlobalIdIsDefined": tnMplsConfigPwRowEditorDstGlobalIdIsDefined,
       "tnMplsConfigPwRowEditorSrcAcId": tnMplsConfigPwRowEditorSrcAcId,
       "tnMplsConfigPwRowEditorDstAcId": tnMplsConfigPwRowEditorDstAcId,
       "tnMplsConfigPwRowEditorSrcAgiValue": tnMplsConfigPwRowEditorSrcAgiValue,
       "tnMplsConfigPwRowEditorDstAgiValue": tnMplsConfigPwRowEditorDstAgiValue,
       "tnMplsConfigPwRowEditorSrcAgiType": tnMplsConfigPwRowEditorSrcAgiType,
       "tnMplsConfigPwRowEditorSrcAgiLength": tnMplsConfigPwRowEditorSrcAgiLength,
       "tnMplsConfigPwRowEditorDstAgiType": tnMplsConfigPwRowEditorDstAgiType,
       "tnMplsConfigPwRowEditorDstAgiLength": tnMplsConfigPwRowEditorDstAgiLength,
       "tnMplsConfigPwRowEditorAction": tnMplsConfigPwRowEditorAction,
       "tnMplsConfigCosMap": tnMplsConfigCosMap,
       "tnMplsConfigCosMapTable": tnMplsConfigCosMapTable,
       "tnMplsConfigCosMapEntry": tnMplsConfigCosMapEntry,
       "tnMplsConfigCosMapGroupIndex": tnMplsConfigCosMapGroupIndex,
       "tnMplsConfigCosMapInTcToCos0": tnMplsConfigCosMapInTcToCos0,
       "tnMplsConfigCosMapInTcToCos1": tnMplsConfigCosMapInTcToCos1,
       "tnMplsConfigCosMapInTcToCos2": tnMplsConfigCosMapInTcToCos2,
       "tnMplsConfigCosMapInTcToCos3": tnMplsConfigCosMapInTcToCos3,
       "tnMplsConfigCosMapInTcToCos4": tnMplsConfigCosMapInTcToCos4,
       "tnMplsConfigCosMapInTcToCos5": tnMplsConfigCosMapInTcToCos5,
       "tnMplsConfigCosMapInTcToCos6": tnMplsConfigCosMapInTcToCos6,
       "tnMplsConfigCosMapInTcToCos7": tnMplsConfigCosMapInTcToCos7,
       "tnMplsConfigCosMapInTcToDp0": tnMplsConfigCosMapInTcToDp0,
       "tnMplsConfigCosMapInTcToDp1": tnMplsConfigCosMapInTcToDp1,
       "tnMplsConfigCosMapInTcToDp2": tnMplsConfigCosMapInTcToDp2,
       "tnMplsConfigCosMapInTcToDp3": tnMplsConfigCosMapInTcToDp3,
       "tnMplsConfigCosMapInTcToDp4": tnMplsConfigCosMapInTcToDp4,
       "tnMplsConfigCosMapInTcToDp5": tnMplsConfigCosMapInTcToDp5,
       "tnMplsConfigCosMapInTcToDp6": tnMplsConfigCosMapInTcToDp6,
       "tnMplsConfigCosMapInTcToDp7": tnMplsConfigCosMapInTcToDp7,
       "tnMplsConfigCosMapOutCosDpToTc00": tnMplsConfigCosMapOutCosDpToTc00,
       "tnMplsConfigCosMapOutCosDpToTc10": tnMplsConfigCosMapOutCosDpToTc10,
       "tnMplsConfigCosMapOutCosDpToTc20": tnMplsConfigCosMapOutCosDpToTc20,
       "tnMplsConfigCosMapOutCosDpToTc30": tnMplsConfigCosMapOutCosDpToTc30,
       "tnMplsConfigCosMapOutCosDpToTc40": tnMplsConfigCosMapOutCosDpToTc40,
       "tnMplsConfigCosMapOutCosDpToTc50": tnMplsConfigCosMapOutCosDpToTc50,
       "tnMplsConfigCosMapOutCosDpToTc60": tnMplsConfigCosMapOutCosDpToTc60,
       "tnMplsConfigCosMapOutCosDpToTc70": tnMplsConfigCosMapOutCosDpToTc70,
       "tnMplsConfigCosMapOutCosDpToTc01": tnMplsConfigCosMapOutCosDpToTc01,
       "tnMplsConfigCosMapOutCosDpToTc11": tnMplsConfigCosMapOutCosDpToTc11,
       "tnMplsConfigCosMapOutCosDpToTc21": tnMplsConfigCosMapOutCosDpToTc21,
       "tnMplsConfigCosMapOutCosDpToTc31": tnMplsConfigCosMapOutCosDpToTc31,
       "tnMplsConfigCosMapOutCosDpToTc41": tnMplsConfigCosMapOutCosDpToTc41,
       "tnMplsConfigCosMapOutCosDpToTc51": tnMplsConfigCosMapOutCosDpToTc51,
       "tnMplsConfigCosMapOutCosDpToTc61": tnMplsConfigCosMapOutCosDpToTc61,
       "tnMplsConfigCosMapOutCosDpToTc71": tnMplsConfigCosMapOutCosDpToTc71,
       "tnMplsConfigCosMapAction": tnMplsConfigCosMapAction,
       "tnMplsConfigCosMapRowEditor": tnMplsConfigCosMapRowEditor,
       "tnMplsConfigCosMapRowEditorGroupIndex": tnMplsConfigCosMapRowEditorGroupIndex,
       "tnMplsConfigCosMapRowEditorInTcToCos0": tnMplsConfigCosMapRowEditorInTcToCos0,
       "tnMplsConfigCosMapRowEditorInTcToCos1": tnMplsConfigCosMapRowEditorInTcToCos1,
       "tnMplsConfigCosMapRowEditorInTcToCos2": tnMplsConfigCosMapRowEditorInTcToCos2,
       "tnMplsConfigCosMapRowEditorInTcToCos3": tnMplsConfigCosMapRowEditorInTcToCos3,
       "tnMplsConfigCosMapRowEditorInTcToCos4": tnMplsConfigCosMapRowEditorInTcToCos4,
       "tnMplsConfigCosMapRowEditorInTcToCos5": tnMplsConfigCosMapRowEditorInTcToCos5,
       "tnMplsConfigCosMapRowEditorInTcToCos6": tnMplsConfigCosMapRowEditorInTcToCos6,
       "tnMplsConfigCosMapRowEditorInTcToCos7": tnMplsConfigCosMapRowEditorInTcToCos7,
       "tnMplsConfigCosMapRowEditorInTcToDp0": tnMplsConfigCosMapRowEditorInTcToDp0,
       "tnMplsConfigCosMapRowEditorInTcToDp1": tnMplsConfigCosMapRowEditorInTcToDp1,
       "tnMplsConfigCosMapRowEditorInTcToDp2": tnMplsConfigCosMapRowEditorInTcToDp2,
       "tnMplsConfigCosMapRowEditorInTcToDp3": tnMplsConfigCosMapRowEditorInTcToDp3,
       "tnMplsConfigCosMapRowEditorInTcToDp4": tnMplsConfigCosMapRowEditorInTcToDp4,
       "tnMplsConfigCosMapRowEditorInTcToDp5": tnMplsConfigCosMapRowEditorInTcToDp5,
       "tnMplsConfigCosMapRowEditorInTcToDp6": tnMplsConfigCosMapRowEditorInTcToDp6,
       "tnMplsConfigCosMapRowEditorInTcToDp7": tnMplsConfigCosMapRowEditorInTcToDp7,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc00": tnMplsConfigCosMapRowEditorOutCosDpToTc00,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc10": tnMplsConfigCosMapRowEditorOutCosDpToTc10,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc20": tnMplsConfigCosMapRowEditorOutCosDpToTc20,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc30": tnMplsConfigCosMapRowEditorOutCosDpToTc30,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc40": tnMplsConfigCosMapRowEditorOutCosDpToTc40,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc50": tnMplsConfigCosMapRowEditorOutCosDpToTc50,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc60": tnMplsConfigCosMapRowEditorOutCosDpToTc60,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc70": tnMplsConfigCosMapRowEditorOutCosDpToTc70,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc01": tnMplsConfigCosMapRowEditorOutCosDpToTc01,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc11": tnMplsConfigCosMapRowEditorOutCosDpToTc11,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc21": tnMplsConfigCosMapRowEditorOutCosDpToTc21,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc31": tnMplsConfigCosMapRowEditorOutCosDpToTc31,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc41": tnMplsConfigCosMapRowEditorOutCosDpToTc41,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc51": tnMplsConfigCosMapRowEditorOutCosDpToTc51,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc61": tnMplsConfigCosMapRowEditorOutCosDpToTc61,
       "tnMplsConfigCosMapRowEditorOutCosDpToTc71": tnMplsConfigCosMapRowEditorOutCosDpToTc71,
       "tnMplsConfigCosMapRowEditorAction": tnMplsConfigCosMapRowEditorAction,
       "tnMplsStatus": tnMplsStatus,
       "tnMplsStatusGlobal": tnMplsStatusGlobal,
       "tnMplsStatusLink": tnMplsStatusLink,
       "tnMplsStatusLinkTable": tnMplsStatusLinkTable,
       "tnMplsStatusLinkEntry": tnMplsStatusLinkEntry,
       "tnMplsStatusLinkGroupIfIndex": tnMplsStatusLinkGroupIfIndex,
       "tnMplsStatusLinkOamActive": tnMplsStatusLinkOamActive,
       "tnMplsStatusTunnel": tnMplsStatusTunnel,
       "tnMplsStatusTunnelTable": tnMplsStatusTunnelTable,
       "tnMplsStatusTunnelEntry": tnMplsStatusTunnelEntry,
       "tnMplsStatusTunnelGroupIfIndex": tnMplsStatusTunnelGroupIfIndex,
       "tnMplsStatusTunnelOamActive": tnMplsStatusTunnelOamActive,
       "tnMplsStatusTunnelState": tnMplsStatusTunnelState,
       "tnMplsStatusTunnelIngressLabel": tnMplsStatusTunnelIngressLabel,
       "tnMplsStatusTunnelEgressLabel": tnMplsStatusTunnelEgressLabel,
       "tnMplsStatusTunnelWorkingActive": tnMplsStatusTunnelWorkingActive,
       "tnMplsStatusLsp": tnMplsStatusLsp,
       "tnMplsStatusLspTable": tnMplsStatusLspTable,
       "tnMplsStatusLspEntry": tnMplsStatusLspEntry,
       "tnMplsStatusLspGroupIndex": tnMplsStatusLspGroupIndex,
       "tnMplsStatusLspOamActive": tnMplsStatusLspOamActive,
       "tnMplsStatusLspState": tnMplsStatusLspState,
       "tnMplsStatusPw": tnMplsStatusPw,
       "tnMplsStatusPwTable": tnMplsStatusPwTable,
       "tnMplsStatusPwEntry": tnMplsStatusPwEntry,
       "tnMplsStatusPwGroupIfIndex": tnMplsStatusPwGroupIfIndex,
       "tnMplsStatusPwOamActive": tnMplsStatusPwOamActive,
       "tnMplsStatusPwState": tnMplsStatusPwState,
       "tnMplsControl": tnMplsControl,
       "tnMplsControlGlobal": tnMplsControlGlobal,
       "tnMplsControlLsp": tnMplsControlLsp,
       "tnMplsControlLspTable": tnMplsControlLspTable,
       "tnMplsControlLspEntry": tnMplsControlLspEntry,
       "tnMplsControlLspGroupIndex": tnMplsControlLspGroupIndex,
       "tnMplsControlLspClear": tnMplsControlLspClear,
       "tnMplsControlIf": tnMplsControlIf,
       "tnMplsControlIfTable": tnMplsControlIfTable,
       "tnMplsControlIfEntry": tnMplsControlIfEntry,
       "tnMplsControlIfGroupIfIndex": tnMplsControlIfGroupIfIndex,
       "tnMplsControlIfClear": tnMplsControlIfClear,
       "tnMplsStatistics": tnMplsStatistics,
       "tnMplsStatisticsGlobal": tnMplsStatisticsGlobal,
       "tnMplsStatisticsLink": tnMplsStatisticsLink,
       "tnMplsStatisticsTunnel": tnMplsStatisticsTunnel,
       "tnMplsStatisticsTunnelTable": tnMplsStatisticsTunnelTable,
       "tnMplsStatisticsTunnelEntry": tnMplsStatisticsTunnelEntry,
       "tnMplsStatisticsTunnelGroupIfIndex": tnMplsStatisticsTunnelGroupIfIndex,
       "tnMplsStatisticsTunnelRxGreenFrames": tnMplsStatisticsTunnelRxGreenFrames,
       "tnMplsStatisticsTunnelRxGreenBytes": tnMplsStatisticsTunnelRxGreenBytes,
       "tnMplsStatisticsTunnelRxYellowFrames": tnMplsStatisticsTunnelRxYellowFrames,
       "tnMplsStatisticsTunnelRxYellowBytes": tnMplsStatisticsTunnelRxYellowBytes,
       "tnMplsStatisticsTunnelRxRedFrames": tnMplsStatisticsTunnelRxRedFrames,
       "tnMplsStatisticsTunnelRxRedBytes": tnMplsStatisticsTunnelRxRedBytes,
       "tnMplsStatisticsTunnelRxDiscardFrames": tnMplsStatisticsTunnelRxDiscardFrames,
       "tnMplsStatisticsTunnelRxDiscardBytes": tnMplsStatisticsTunnelRxDiscardBytes,
       "tnMplsStatisticsTunnelTxGreenFrames": tnMplsStatisticsTunnelTxGreenFrames,
       "tnMplsStatisticsTunnelTxGreenBytes": tnMplsStatisticsTunnelTxGreenBytes,
       "tnMplsStatisticsTunnelTxYellowFrames": tnMplsStatisticsTunnelTxYellowFrames,
       "tnMplsStatisticsTunnelTxYellowBytes": tnMplsStatisticsTunnelTxYellowBytes,
       "tnMplsStatisticsTunnelTxDiscardFrames": tnMplsStatisticsTunnelTxDiscardFrames,
       "tnMplsStatisticsTunnelTxDiscardBytes": tnMplsStatisticsTunnelTxDiscardBytes,
       "tnMplsStatisticsLsp": tnMplsStatisticsLsp,
       "tnMplsStatisticsLspTable": tnMplsStatisticsLspTable,
       "tnMplsStatisticsLspEntry": tnMplsStatisticsLspEntry,
       "tnMplsStatisticsLspGroupIndex": tnMplsStatisticsLspGroupIndex,
       "tnMplsStatisticsLspFwdRxGreenFrames": tnMplsStatisticsLspFwdRxGreenFrames,
       "tnMplsStatisticsLspFwdRxGreenBytes": tnMplsStatisticsLspFwdRxGreenBytes,
       "tnMplsStatisticsLspFwdRxYellowFrames": tnMplsStatisticsLspFwdRxYellowFrames,
       "tnMplsStatisticsLspFwdRxYellowBytes": tnMplsStatisticsLspFwdRxYellowBytes,
       "tnMplsStatisticsLspFwdRxRedFrames": tnMplsStatisticsLspFwdRxRedFrames,
       "tnMplsStatisticsLspFwdRxRedBytes": tnMplsStatisticsLspFwdRxRedBytes,
       "tnMplsStatisticsLspFwdRxDiscardFrames": tnMplsStatisticsLspFwdRxDiscardFrames,
       "tnMplsStatisticsLspFwdRxDiscardBytes": tnMplsStatisticsLspFwdRxDiscardBytes,
       "tnMplsStatisticsLspFwdTxGreenFrames": tnMplsStatisticsLspFwdTxGreenFrames,
       "tnMplsStatisticsLspFwdTxGreenBytes": tnMplsStatisticsLspFwdTxGreenBytes,
       "tnMplsStatisticsLspFwdTxYellowFrames": tnMplsStatisticsLspFwdTxYellowFrames,
       "tnMplsStatisticsLspFwdTxYellowBytes": tnMplsStatisticsLspFwdTxYellowBytes,
       "tnMplsStatisticsLspFwdTxDiscardFrames": tnMplsStatisticsLspFwdTxDiscardFrames,
       "tnMplsStatisticsLspFwdTxDiscardBytes": tnMplsStatisticsLspFwdTxDiscardBytes,
       "tnMplsStatisticsLspRewRxGreenFrames": tnMplsStatisticsLspRewRxGreenFrames,
       "tnMplsStatisticsLspRewRxGreenBytes": tnMplsStatisticsLspRewRxGreenBytes,
       "tnMplsStatisticsLspRewRxYellowFrames": tnMplsStatisticsLspRewRxYellowFrames,
       "tnMplsStatisticsLspRewRxYellowBytes": tnMplsStatisticsLspRewRxYellowBytes,
       "tnMplsStatisticsLspRewRxRedFrames": tnMplsStatisticsLspRewRxRedFrames,
       "tnMplsStatisticsLspRewRxRedBytes": tnMplsStatisticsLspRewRxRedBytes,
       "tnMplsStatisticsLspRewRxDiscardFrames": tnMplsStatisticsLspRewRxDiscardFrames,
       "tnMplsStatisticsLspRewRxDiscardBytes": tnMplsStatisticsLspRewRxDiscardBytes,
       "tnMplsStatisticsLspRewTxGreenFrames": tnMplsStatisticsLspRewTxGreenFrames,
       "tnMplsStatisticsLspRewTxGreenBytes": tnMplsStatisticsLspRewTxGreenBytes,
       "tnMplsStatisticsLspRewTxYellowFrames": tnMplsStatisticsLspRewTxYellowFrames,
       "tnMplsStatisticsLspRewTxYellowBytes": tnMplsStatisticsLspRewTxYellowBytes,
       "tnMplsStatisticsLspRewTxDiscardFrames": tnMplsStatisticsLspRewTxDiscardFrames,
       "tnMplsStatisticsLspRewTxDiscardBytes": tnMplsStatisticsLspRewTxDiscardBytes,
       "tnMplsStatisticsPw": tnMplsStatisticsPw,
       "tnMplsStatisticsPwTable": tnMplsStatisticsPwTable,
       "tnMplsStatisticsPwEntry": tnMplsStatisticsPwEntry,
       "tnMplsStatisticsPwGroupIfIndex": tnMplsStatisticsPwGroupIfIndex,
       "tnMplsStatisticsPwRxGreenFrames": tnMplsStatisticsPwRxGreenFrames,
       "tnMplsStatisticsPwRxGreenBytes": tnMplsStatisticsPwRxGreenBytes,
       "tnMplsStatisticsPwRxYellowFrames": tnMplsStatisticsPwRxYellowFrames,
       "tnMplsStatisticsPwRxYellowBytes": tnMplsStatisticsPwRxYellowBytes,
       "tnMplsStatisticsPwRxRedFrames": tnMplsStatisticsPwRxRedFrames,
       "tnMplsStatisticsPwRxRedBytes": tnMplsStatisticsPwRxRedBytes,
       "tnMplsStatisticsPwRxDiscardFrames": tnMplsStatisticsPwRxDiscardFrames,
       "tnMplsStatisticsPwRxDiscardBytes": tnMplsStatisticsPwRxDiscardBytes,
       "tnMplsStatisticsPwTxGreenFrames": tnMplsStatisticsPwTxGreenFrames,
       "tnMplsStatisticsPwTxGreenBytes": tnMplsStatisticsPwTxGreenBytes,
       "tnMplsStatisticsPwTxYellowFrames": tnMplsStatisticsPwTxYellowFrames,
       "tnMplsStatisticsPwTxYellowBytes": tnMplsStatisticsPwTxYellowBytes,
       "tnMplsStatisticsPwTxDiscardFrames": tnMplsStatisticsPwTxDiscardFrames,
       "tnMplsStatisticsPwTxDiscardBytes": tnMplsStatisticsPwTxDiscardBytes,
       "tnMplsMibConformance": tnMplsMibConformance,
       "tnMplsMibCompliances": tnMplsMibCompliances,
       "tnMplsMibCompliance": tnMplsMibCompliance,
       "tnMplsMibGroups": tnMplsMibGroups,
       "tnMplsCapabilitiesInfoGroup": tnMplsCapabilitiesInfoGroup,
       "tnMplsConfigGlobalMainInfoGroup": tnMplsConfigGlobalMainInfoGroup,
       "tnMplsConfigLinkTableInfoGroup": tnMplsConfigLinkTableInfoGroup,
       "tnMplsConfigLinkRowEditorInfoGroup": tnMplsConfigLinkRowEditorInfoGroup,
       "tnMplsConfigTunnelTableInfoGroup": tnMplsConfigTunnelTableInfoGroup,
       "tnMplsConfigTunnelRowEditorInfoGroup": tnMplsConfigTunnelRowEditorInfoGroup,
       "tnMplsConfigLspTableInfoGroup": tnMplsConfigLspTableInfoGroup,
       "tnMplsConfigLspRowEditorInfoGroup": tnMplsConfigLspRowEditorInfoGroup,
       "tnMplsConfigPwTableInfoGroup": tnMplsConfigPwTableInfoGroup,
       "tnMplsConfigPwRowEditorInfoGroup": tnMplsConfigPwRowEditorInfoGroup,
       "tnMplsConfigCosMapTableInfoGroup": tnMplsConfigCosMapTableInfoGroup,
       "tnMplsConfigCosMapRowEditorInfoGroup": tnMplsConfigCosMapRowEditorInfoGroup,
       "tnMplsStatusLinkTableInfoGroup": tnMplsStatusLinkTableInfoGroup,
       "tnMplsStatusTunnelTableInfoGroup": tnMplsStatusTunnelTableInfoGroup,
       "tnMplsStatusLspTableInfoGroup": tnMplsStatusLspTableInfoGroup,
       "tnMplsStatusPwTableInfoGroup": tnMplsStatusPwTableInfoGroup,
       "tnMplsControlLspTableInfoGroup": tnMplsControlLspTableInfoGroup,
       "tnMplsControlIfTableInfoGroup": tnMplsControlIfTableInfoGroup,
       "tnMplsStatisticsTunnelTableInfoGroup": tnMplsStatisticsTunnelTableInfoGroup,
       "tnMplsStatisticsLspTableInfoGroup": tnMplsStatisticsLspTableInfoGroup,
       "tnMplsStatisticsPwTableInfoGroup": tnMplsStatisticsPwTableInfoGroup}
)
