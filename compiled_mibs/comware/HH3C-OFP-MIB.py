# SNMP MIB module (HH3C-OFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-OFP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:27 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cOfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167)
)
if mibBuilder.loadTexts:
    hh3cOfp.setRevisions(
        ("2019-04-11 13:00",
         "2017-02-28 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cOfpInstanceObjects_ObjectIdentity = ObjectIdentity
hh3cOfpInstanceObjects = _Hh3cOfpInstanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1)
)
_Hh3cOfpInstanceControllerTable_Object = MibTable
hh3cOfpInstanceControllerTable = _Hh3cOfpInstanceControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cOfpInstanceControllerTable.setStatus("current")
_Hh3cOfpInstanceControllerEntry_Object = MibTableRow
hh3cOfpInstanceControllerEntry = _Hh3cOfpInstanceControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1, 1)
)
hh3cOfpInstanceControllerEntry.setIndexNames(
    (0, "HH3C-OFP-MIB", "hh3cOfpInstanceID"),
    (0, "HH3C-OFP-MIB", "hh3cOfpInstanceControllerID"),
)
if mibBuilder.loadTexts:
    hh3cOfpInstanceControllerEntry.setStatus("current")


class _Hh3cOfpInstanceID_Type(Integer32):
    """Custom type hh3cOfpInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cOfpInstanceID_Type.__name__ = "Integer32"
_Hh3cOfpInstanceID_Object = MibTableColumn
hh3cOfpInstanceID = _Hh3cOfpInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1, 1, 1),
    _Hh3cOfpInstanceID_Type()
)
hh3cOfpInstanceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cOfpInstanceID.setStatus("current")


class _Hh3cOfpInstanceControllerID_Type(Integer32):
    """Custom type hh3cOfpInstanceControllerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cOfpInstanceControllerID_Type.__name__ = "Integer32"
_Hh3cOfpInstanceControllerID_Object = MibTableColumn
hh3cOfpInstanceControllerID = _Hh3cOfpInstanceControllerID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1, 1, 2),
    _Hh3cOfpInstanceControllerID_Type()
)
hh3cOfpInstanceControllerID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cOfpInstanceControllerID.setStatus("current")


class _Hh3cOfpInstanceControllerRole_Type(Integer32):
    """Custom type hh3cOfpInstanceControllerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("master", 2),
          ("slave", 3))
    )


_Hh3cOfpInstanceControllerRole_Type.__name__ = "Integer32"
_Hh3cOfpInstanceControllerRole_Object = MibTableColumn
hh3cOfpInstanceControllerRole = _Hh3cOfpInstanceControllerRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1, 1, 3),
    _Hh3cOfpInstanceControllerRole_Type()
)
hh3cOfpInstanceControllerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOfpInstanceControllerRole.setStatus("current")


class _Hh3cOfpInstanceCtrConnectType_Type(Integer32):
    """Custom type hh3cOfpInstanceCtrConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("ssl", 2))
    )


_Hh3cOfpInstanceCtrConnectType_Type.__name__ = "Integer32"
_Hh3cOfpInstanceCtrConnectType_Object = MibTableColumn
hh3cOfpInstanceCtrConnectType = _Hh3cOfpInstanceCtrConnectType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1, 1, 4),
    _Hh3cOfpInstanceCtrConnectType_Type()
)
hh3cOfpInstanceCtrConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOfpInstanceCtrConnectType.setStatus("current")


class _Hh3cOfpInstanceCtrConnectState_Type(Integer32):
    """Custom type hh3cOfpInstanceCtrConnectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("established", 1))
    )


_Hh3cOfpInstanceCtrConnectState_Type.__name__ = "Integer32"
_Hh3cOfpInstanceCtrConnectState_Object = MibTableColumn
hh3cOfpInstanceCtrConnectState = _Hh3cOfpInstanceCtrConnectState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1, 1, 5),
    _Hh3cOfpInstanceCtrConnectState_Type()
)
hh3cOfpInstanceCtrConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOfpInstanceCtrConnectState.setStatus("current")


class _Hh3cOfpInstanceCtrSSLPolicy_Type(OctetString):
    """Custom type hh3cOfpInstanceCtrSSLPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cOfpInstanceCtrSSLPolicy_Type.__name__ = "OctetString"
_Hh3cOfpInstanceCtrSSLPolicy_Object = MibTableColumn
hh3cOfpInstanceCtrSSLPolicy = _Hh3cOfpInstanceCtrSSLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1, 1, 6),
    _Hh3cOfpInstanceCtrSSLPolicy_Type()
)
hh3cOfpInstanceCtrSSLPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOfpInstanceCtrSSLPolicy.setStatus("current")


class _Hh3cOfpInstanceCtrVRFName_Type(OctetString):
    """Custom type hh3cOfpInstanceCtrVRFName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cOfpInstanceCtrVRFName_Type.__name__ = "OctetString"
_Hh3cOfpInstanceCtrVRFName_Object = MibTableColumn
hh3cOfpInstanceCtrVRFName = _Hh3cOfpInstanceCtrVRFName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1, 1, 7),
    _Hh3cOfpInstanceCtrVRFName_Type()
)
hh3cOfpInstanceCtrVRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOfpInstanceCtrVRFName.setStatus("current")
_Hh3cOfpInstanceCtrIPType_Type = InetAddressType
_Hh3cOfpInstanceCtrIPType_Object = MibTableColumn
hh3cOfpInstanceCtrIPType = _Hh3cOfpInstanceCtrIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1, 1, 8),
    _Hh3cOfpInstanceCtrIPType_Type()
)
hh3cOfpInstanceCtrIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOfpInstanceCtrIPType.setStatus("current")
_Hh3cOfpInstanceCtrIPaddress_Type = InetAddress
_Hh3cOfpInstanceCtrIPaddress_Object = MibTableColumn
hh3cOfpInstanceCtrIPaddress = _Hh3cOfpInstanceCtrIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1, 1, 9),
    _Hh3cOfpInstanceCtrIPaddress_Type()
)
hh3cOfpInstanceCtrIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOfpInstanceCtrIPaddress.setStatus("current")


class _Hh3cOfpInstanceCtrPort_Type(Integer32):
    """Custom type hh3cOfpInstanceCtrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cOfpInstanceCtrPort_Type.__name__ = "Integer32"
_Hh3cOfpInstanceCtrPort_Object = MibTableColumn
hh3cOfpInstanceCtrPort = _Hh3cOfpInstanceCtrPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 1, 1, 10),
    _Hh3cOfpInstanceCtrPort_Type()
)
hh3cOfpInstanceCtrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOfpInstanceCtrPort.setStatus("current")
_Hh3cOfpInstanceFlowTableTable_Object = MibTable
hh3cOfpInstanceFlowTableTable = _Hh3cOfpInstanceFlowTableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cOfpInstanceFlowTableTable.setStatus("current")
_Hh3cOfpInstanceFlowTableEntry_Object = MibTableRow
hh3cOfpInstanceFlowTableEntry = _Hh3cOfpInstanceFlowTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 2, 1)
)
hh3cOfpInstanceFlowTableEntry.setIndexNames(
    (0, "HH3C-OFP-MIB", "hh3cOfpFlowTableInstanceID"),
    (0, "HH3C-OFP-MIB", "hh3cOfpInstanceTableID"),
)
if mibBuilder.loadTexts:
    hh3cOfpInstanceFlowTableEntry.setStatus("current")


class _Hh3cOfpFlowTableInstanceID_Type(Integer32):
    """Custom type hh3cOfpFlowTableInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cOfpFlowTableInstanceID_Type.__name__ = "Integer32"
_Hh3cOfpFlowTableInstanceID_Object = MibTableColumn
hh3cOfpFlowTableInstanceID = _Hh3cOfpFlowTableInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 2, 1, 1),
    _Hh3cOfpFlowTableInstanceID_Type()
)
hh3cOfpFlowTableInstanceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOfpFlowTableInstanceID.setStatus("current")


class _Hh3cOfpInstanceTableID_Type(Integer32):
    """Custom type hh3cOfpInstanceTableID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_Hh3cOfpInstanceTableID_Type.__name__ = "Integer32"
_Hh3cOfpInstanceTableID_Object = MibTableColumn
hh3cOfpInstanceTableID = _Hh3cOfpInstanceTableID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 2, 1, 2),
    _Hh3cOfpInstanceTableID_Type()
)
hh3cOfpInstanceTableID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOfpInstanceTableID.setStatus("current")
_Hh3cOfpInstanceFlowEntryNumCtrl_Type = Unsigned32
_Hh3cOfpInstanceFlowEntryNumCtrl_Object = MibTableColumn
hh3cOfpInstanceFlowEntryNumCtrl = _Hh3cOfpInstanceFlowEntryNumCtrl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 2, 1, 3),
    _Hh3cOfpInstanceFlowEntryNumCtrl_Type()
)
hh3cOfpInstanceFlowEntryNumCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOfpInstanceFlowEntryNumCtrl.setStatus("current")
_Hh3cOfpInstanceFlowEntryTotalNum_Type = Unsigned32
_Hh3cOfpInstanceFlowEntryTotalNum_Object = MibTableColumn
hh3cOfpInstanceFlowEntryTotalNum = _Hh3cOfpInstanceFlowEntryTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 2, 1, 4),
    _Hh3cOfpInstanceFlowEntryTotalNum_Type()
)
hh3cOfpInstanceFlowEntryTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOfpInstanceFlowEntryTotalNum.setStatus("current")
_Hh3cOfpInstanceFlowEntryLimit_Type = Unsigned32
_Hh3cOfpInstanceFlowEntryLimit_Object = MibTableColumn
hh3cOfpInstanceFlowEntryLimit = _Hh3cOfpInstanceFlowEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 1, 2, 1, 5),
    _Hh3cOfpInstanceFlowEntryLimit_Type()
)
hh3cOfpInstanceFlowEntryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOfpInstanceFlowEntryLimit.setStatus("current")
_Hh3cOfpMibTrap_ObjectIdentity = ObjectIdentity
hh3cOfpMibTrap = _Hh3cOfpMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 2)
)
_Hh3cOfpMibTrapOid_ObjectIdentity = ObjectIdentity
hh3cOfpMibTrapOid = _Hh3cOfpMibTrapOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 2, 1)
)


class _Hh3cOfpTrapDisconnectReason_Type(Integer32):
    """Custom type hh3cOfpTrapDisconnectReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Hh3cOfpTrapDisconnectReason_Type.__name__ = "Integer32"
_Hh3cOfpTrapDisconnectReason_Object = MibScalar
hh3cOfpTrapDisconnectReason = _Hh3cOfpTrapDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 2, 1, 1),
    _Hh3cOfpTrapDisconnectReason_Type()
)
hh3cOfpTrapDisconnectReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cOfpTrapDisconnectReason.setStatus("current")
_Hh3cOfpTraps_ObjectIdentity = ObjectIdentity
hh3cOfpTraps = _Hh3cOfpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 2, 2)
)
_Hh3cOfpTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cOfpTrapsPrefix = _Hh3cOfpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 2, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cOfpControllerDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 2, 2, 0, 1)
)
hh3cOfpControllerDisconnect.setObjects(
      *(("HH3C-OFP-MIB", "hh3cOfpInstanceID"),
        ("HH3C-OFP-MIB", "hh3cOfpInstanceControllerID"),
        ("HH3C-OFP-MIB", "hh3cOfpTrapDisconnectReason"))
)
if mibBuilder.loadTexts:
    hh3cOfpControllerDisconnect.setStatus(
        "current"
    )

hh3cOfpControllerConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 167, 2, 2, 0, 2)
)
hh3cOfpControllerConnect.setObjects(
      *(("HH3C-OFP-MIB", "hh3cOfpInstanceID"),
        ("HH3C-OFP-MIB", "hh3cOfpInstanceControllerID"))
)
if mibBuilder.loadTexts:
    hh3cOfpControllerConnect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-OFP-MIB",
    **{"hh3cOfp": hh3cOfp,
       "hh3cOfpInstanceObjects": hh3cOfpInstanceObjects,
       "hh3cOfpInstanceControllerTable": hh3cOfpInstanceControllerTable,
       "hh3cOfpInstanceControllerEntry": hh3cOfpInstanceControllerEntry,
       "hh3cOfpInstanceID": hh3cOfpInstanceID,
       "hh3cOfpInstanceControllerID": hh3cOfpInstanceControllerID,
       "hh3cOfpInstanceControllerRole": hh3cOfpInstanceControllerRole,
       "hh3cOfpInstanceCtrConnectType": hh3cOfpInstanceCtrConnectType,
       "hh3cOfpInstanceCtrConnectState": hh3cOfpInstanceCtrConnectState,
       "hh3cOfpInstanceCtrSSLPolicy": hh3cOfpInstanceCtrSSLPolicy,
       "hh3cOfpInstanceCtrVRFName": hh3cOfpInstanceCtrVRFName,
       "hh3cOfpInstanceCtrIPType": hh3cOfpInstanceCtrIPType,
       "hh3cOfpInstanceCtrIPaddress": hh3cOfpInstanceCtrIPaddress,
       "hh3cOfpInstanceCtrPort": hh3cOfpInstanceCtrPort,
       "hh3cOfpInstanceFlowTableTable": hh3cOfpInstanceFlowTableTable,
       "hh3cOfpInstanceFlowTableEntry": hh3cOfpInstanceFlowTableEntry,
       "hh3cOfpFlowTableInstanceID": hh3cOfpFlowTableInstanceID,
       "hh3cOfpInstanceTableID": hh3cOfpInstanceTableID,
       "hh3cOfpInstanceFlowEntryNumCtrl": hh3cOfpInstanceFlowEntryNumCtrl,
       "hh3cOfpInstanceFlowEntryTotalNum": hh3cOfpInstanceFlowEntryTotalNum,
       "hh3cOfpInstanceFlowEntryLimit": hh3cOfpInstanceFlowEntryLimit,
       "hh3cOfpMibTrap": hh3cOfpMibTrap,
       "hh3cOfpMibTrapOid": hh3cOfpMibTrapOid,
       "hh3cOfpTrapDisconnectReason": hh3cOfpTrapDisconnectReason,
       "hh3cOfpTraps": hh3cOfpTraps,
       "hh3cOfpTrapsPrefix": hh3cOfpTrapsPrefix,
       "hh3cOfpControllerDisconnect": hh3cOfpControllerDisconnect,
       "hh3cOfpControllerConnect": hh3cOfpControllerConnect}
)
