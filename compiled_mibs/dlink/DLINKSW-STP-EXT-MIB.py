# SNMP MIB module (DLINKSW-STP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-STP-EXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:54 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(IEEE8021BridgePortNumber,
 IEEE8021MstIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021MstIdentifier")

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

dlinkSwStpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 15)
)
if mibBuilder.loadTexts:
    dlinkSwStpExtMIB.setRevisions(
        ("2013-03-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DStpExtMIBNotifications_ObjectIdentity = ObjectIdentity
dStpExtMIBNotifications = _DStpExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 0)
)
_DStpExtMIBObjects_ObjectIdentity = ObjectIdentity
dStpExtMIBObjects = _DStpExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1)
)
_DStpExtGblMgmt_ObjectIdentity = ObjectIdentity
dStpExtGblMgmt = _DStpExtGblMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 1)
)
_DStpExtStpGblStateEnabled_Type = TruthValue
_DStpExtStpGblStateEnabled_Object = MibScalar
dStpExtStpGblStateEnabled = _DStpExtStpGblStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 1, 1),
    _DStpExtStpGblStateEnabled_Type()
)
dStpExtStpGblStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStpExtStpGblStateEnabled.setStatus("current")


class _DStpExtNotificationEnable_Type(Bits):
    """Custom type dStpExtNotificationEnable based on Bits"""
    namedValues = NamedValues(
        *(("newRoot", 0),
          ("topologyChange", 1))
    )

_DStpExtNotificationEnable_Type.__name__ = "Bits"
_DStpExtNotificationEnable_Object = MibScalar
dStpExtNotificationEnable = _DStpExtNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 1, 2),
    _DStpExtNotificationEnable_Type()
)
dStpExtNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStpExtNotificationEnable.setStatus("current")


class _DStpExtStpNniBpduAddress_Type(Integer32):
    """Custom type dStpExtStpNniBpduAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 1),
          ("dot1ad", 2))
    )


_DStpExtStpNniBpduAddress_Type.__name__ = "Integer32"
_DStpExtStpNniBpduAddress_Object = MibScalar
dStpExtStpNniBpduAddress = _DStpExtStpNniBpduAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 1, 3),
    _DStpExtStpNniBpduAddress_Type()
)
dStpExtStpNniBpduAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStpExtStpNniBpduAddress.setStatus("current")
_DStpExtPortMgmt_ObjectIdentity = ObjectIdentity
dStpExtPortMgmt = _DStpExtPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 2)
)
_DStpExtPortTable_Object = MibTable
dStpExtPortTable = _DStpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dStpExtPortTable.setStatus("current")
_DStpExtPortEntry_Object = MibTableRow
dStpExtPortEntry = _DStpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 2, 1, 1)
)
dStpExtPortEntry.setIndexNames(
    (0, "DLINKSW-STP-EXT-MIB", "dStpExtPortNumber"),
)
if mibBuilder.loadTexts:
    dStpExtPortEntry.setStatus("current")
_DStpExtPortNumber_Type = IEEE8021BridgePortNumber
_DStpExtPortNumber_Object = MibTableColumn
dStpExtPortNumber = _DStpExtPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 2, 1, 1, 1),
    _DStpExtPortNumber_Type()
)
dStpExtPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dStpExtPortNumber.setStatus("current")
_DStpExtPortForwardBpduEnabled_Type = TruthValue
_DStpExtPortForwardBpduEnabled_Object = MibTableColumn
dStpExtPortForwardBpduEnabled = _DStpExtPortForwardBpduEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 2, 1, 1, 2),
    _DStpExtPortForwardBpduEnabled_Type()
)
dStpExtPortForwardBpduEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStpExtPortForwardBpduEnabled.setStatus("current")


class _DStpExtPortAdminHelloTime_Type(Unsigned32):
    """Custom type dStpExtPortAdminHelloTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DStpExtPortAdminHelloTime_Type.__name__ = "Unsigned32"
_DStpExtPortAdminHelloTime_Object = MibTableColumn
dStpExtPortAdminHelloTime = _DStpExtPortAdminHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 2, 1, 1, 3),
    _DStpExtPortAdminHelloTime_Type()
)
dStpExtPortAdminHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dStpExtPortAdminHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    dStpExtPortAdminHelloTime.setUnits("seconds")


class _DStpExtPortState_Type(Integer32):
    """Custom type dStpExtPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("errDisabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6),
          ("nonStpForwarding", 7),
          ("nonStpOther", 8))
    )


_DStpExtPortState_Type.__name__ = "Integer32"
_DStpExtPortState_Object = MibTableColumn
dStpExtPortState = _DStpExtPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 2, 1, 1, 4),
    _DStpExtPortState_Type()
)
dStpExtPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStpExtPortState.setStatus("current")
_DStpExtMstpMgmt_ObjectIdentity = ObjectIdentity
dStpExtMstpMgmt = _DStpExtMstpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 3)
)
_DStpExtMstpPortTable_Object = MibTable
dStpExtMstpPortTable = _DStpExtMstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dStpExtMstpPortTable.setStatus("current")
_DStpExtMstpPortEntry_Object = MibTableRow
dStpExtMstpPortEntry = _DStpExtMstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 3, 1, 1)
)
dStpExtMstpPortEntry.setIndexNames(
    (0, "DLINKSW-STP-EXT-MIB", "dStpExtMstpPortMstId"),
    (0, "DLINKSW-STP-EXT-MIB", "dStpExtMstpPortNum"),
)
if mibBuilder.loadTexts:
    dStpExtMstpPortEntry.setStatus("current")
_DStpExtMstpPortMstId_Type = IEEE8021MstIdentifier
_DStpExtMstpPortMstId_Object = MibTableColumn
dStpExtMstpPortMstId = _DStpExtMstpPortMstId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 3, 1, 1, 1),
    _DStpExtMstpPortMstId_Type()
)
dStpExtMstpPortMstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dStpExtMstpPortMstId.setStatus("current")
_DStpExtMstpPortNum_Type = IEEE8021BridgePortNumber
_DStpExtMstpPortNum_Object = MibTableColumn
dStpExtMstpPortNum = _DStpExtMstpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 3, 1, 1, 2),
    _DStpExtMstpPortNum_Type()
)
dStpExtMstpPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dStpExtMstpPortNum.setStatus("current")


class _DStpExtMstpPortRole_Type(Integer32):
    """Custom type dStpExtMstpPortRole based on Integer32"""
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
        *(("root", 1),
          ("alternate", 2),
          ("designated", 3),
          ("backup", 4),
          ("master", 5))
    )


_DStpExtMstpPortRole_Type.__name__ = "Integer32"
_DStpExtMstpPortRole_Object = MibTableColumn
dStpExtMstpPortRole = _DStpExtMstpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 1, 3, 1, 1, 3),
    _DStpExtMstpPortRole_Type()
)
dStpExtMstpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dStpExtMstpPortRole.setStatus("current")
_DStpExtMIBConformance_ObjectIdentity = ObjectIdentity
dStpExtMIBConformance = _DStpExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 2)
)
_DStpExtMIBCompliances_ObjectIdentity = ObjectIdentity
dStpExtMIBCompliances = _DStpExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 2, 1)
)
_DStpExtGroups_ObjectIdentity = ObjectIdentity
dStpExtGroups = _DStpExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 2, 1, 2)
)

# Managed Objects groups

dStpExtBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 2, 1, 2, 1)
)
dStpExtBasicGroup.setObjects(
      *(("DLINKSW-STP-EXT-MIB", "dStpExtStpGblStateEnabled"),
        ("DLINKSW-STP-EXT-MIB", "dStpExtPortForwardBpduEnabled"),
        ("DLINKSW-STP-EXT-MIB", "dStpExtPortState"),
        ("DLINKSW-STP-EXT-MIB", "dStpExtNotificationEnable"))
)
if mibBuilder.loadTexts:
    dStpExtBasicGroup.setStatus("current")

dStpExtMstpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 2, 1, 2, 2)
)
dStpExtMstpGroup.setObjects(
      *(("DLINKSW-STP-EXT-MIB", "dStpExtPortAdminHelloTime"),
        ("DLINKSW-STP-EXT-MIB", "dStpExtMstpPortRole"))
)
if mibBuilder.loadTexts:
    dStpExtMstpGroup.setStatus("current")

dStpExtServiceProviderCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 2, 1, 2, 3)
)
dStpExtServiceProviderCfgGroup.setObjects(
    ("DLINKSW-STP-EXT-MIB", "dStpExtStpNniBpduAddress")
)
if mibBuilder.loadTexts:
    dStpExtServiceProviderCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dStpExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 15, 2, 1, 1)
)
dStpExtCompliance.setObjects(
      *(("DLINKSW-STP-EXT-MIB", "dStpExtBasicGroup"),
        ("DLINKSW-STP-EXT-MIB", "dStpExtMstpGroup"),
        ("DLINKSW-STP-EXT-MIB", "dStpExtServiceProviderCfgGroup"))
)
if mibBuilder.loadTexts:
    dStpExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-STP-EXT-MIB",
    **{"dlinkSwStpExtMIB": dlinkSwStpExtMIB,
       "dStpExtMIBNotifications": dStpExtMIBNotifications,
       "dStpExtMIBObjects": dStpExtMIBObjects,
       "dStpExtGblMgmt": dStpExtGblMgmt,
       "dStpExtStpGblStateEnabled": dStpExtStpGblStateEnabled,
       "dStpExtNotificationEnable": dStpExtNotificationEnable,
       "dStpExtStpNniBpduAddress": dStpExtStpNniBpduAddress,
       "dStpExtPortMgmt": dStpExtPortMgmt,
       "dStpExtPortTable": dStpExtPortTable,
       "dStpExtPortEntry": dStpExtPortEntry,
       "dStpExtPortNumber": dStpExtPortNumber,
       "dStpExtPortForwardBpduEnabled": dStpExtPortForwardBpduEnabled,
       "dStpExtPortAdminHelloTime": dStpExtPortAdminHelloTime,
       "dStpExtPortState": dStpExtPortState,
       "dStpExtMstpMgmt": dStpExtMstpMgmt,
       "dStpExtMstpPortTable": dStpExtMstpPortTable,
       "dStpExtMstpPortEntry": dStpExtMstpPortEntry,
       "dStpExtMstpPortMstId": dStpExtMstpPortMstId,
       "dStpExtMstpPortNum": dStpExtMstpPortNum,
       "dStpExtMstpPortRole": dStpExtMstpPortRole,
       "dStpExtMIBConformance": dStpExtMIBConformance,
       "dStpExtMIBCompliances": dStpExtMIBCompliances,
       "dStpExtCompliance": dStpExtCompliance,
       "dStpExtGroups": dStpExtGroups,
       "dStpExtBasicGroup": dStpExtBasicGroup,
       "dStpExtMstpGroup": dStpExtMstpGroup,
       "dStpExtServiceProviderCfgGroup": dStpExtServiceProviderCfgGroup}
)
