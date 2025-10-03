# SNMP MIB module (RUCKUS-SZ-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruckus\RUCKUS-SZ-WLAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:51 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ruckusSZWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusSZWLANModule")

(RuckusAdminStatus,
 RuckusRadioMode,
 RuckusRateLimiting,
 RuckusSSID,
 RuckusdB) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusAdminStatus",
    "RuckusRadioMode",
    "RuckusRateLimiting",
    "RuckusSSID",
    "RuckusdB")

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


# MODULE-IDENTITY

ruckusSZWLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusSZWLANObjects_ObjectIdentity = ObjectIdentity
ruckusSZWLANObjects = _RuckusSZWLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1)
)
_RuckusSZWLANInfo_ObjectIdentity = ObjectIdentity
ruckusSZWLANInfo = _RuckusSZWLANInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 1)
)
_RuckusSZWLANTable_Object = MibTable
ruckusSZWLANTable = _RuckusSZWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruckusSZWLANTable.setStatus("current")
_RuckusSZWLANEntry_Object = MibTableRow
ruckusSZWLANEntry = _RuckusSZWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 1, 2, 1)
)
ruckusSZWLANEntry.setIndexNames(
    (0, "RUCKUS-SZ-WLAN-MIB", "ruckusSZWLANIndex"),
)
if mibBuilder.loadTexts:
    ruckusSZWLANEntry.setStatus("current")
_RuckusSZWLANSSID_Type = RuckusSSID
_RuckusSZWLANSSID_Object = MibTableColumn
ruckusSZWLANSSID = _RuckusSZWLANSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 1, 2, 1, 1),
    _RuckusSZWLANSSID_Type()
)
ruckusSZWLANSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZWLANSSID.setStatus("current")
_RuckusSZWLANNumSta_Type = Unsigned32
_RuckusSZWLANNumSta_Object = MibTableColumn
ruckusSZWLANNumSta = _RuckusSZWLANNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 1, 2, 1, 12),
    _RuckusSZWLANNumSta_Type()
)
ruckusSZWLANNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZWLANNumSta.setStatus("current")
_RuckusSZWLANRxBytes_Type = Counter64
_RuckusSZWLANRxBytes_Object = MibTableColumn
ruckusSZWLANRxBytes = _RuckusSZWLANRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 1, 2, 1, 14),
    _RuckusSZWLANRxBytes_Type()
)
ruckusSZWLANRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZWLANRxBytes.setStatus("current")
_RuckusSZWLANTxBytes_Type = Counter64
_RuckusSZWLANTxBytes_Object = MibTableColumn
ruckusSZWLANTxBytes = _RuckusSZWLANTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 1, 2, 1, 16),
    _RuckusSZWLANTxBytes_Type()
)
ruckusSZWLANTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZWLANTxBytes.setStatus("current")
_RuckusSZWLANAuthType_Type = DisplayString
_RuckusSZWLANAuthType_Object = MibTableColumn
ruckusSZWLANAuthType = _RuckusSZWLANAuthType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 1, 2, 1, 17),
    _RuckusSZWLANAuthType_Type()
)
ruckusSZWLANAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZWLANAuthType.setStatus("current")


class _RuckusSZWLANIndex_Type(Integer32):
    """Custom type ruckusSZWLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuckusSZWLANIndex_Type.__name__ = "Integer32"
_RuckusSZWLANIndex_Object = MibTableColumn
ruckusSZWLANIndex = _RuckusSZWLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 1, 2, 1, 99),
    _RuckusSZWLANIndex_Type()
)
ruckusSZWLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZWLANIndex.setStatus("current")
_RuckusSZWLANAPInfo_ObjectIdentity = ObjectIdentity
ruckusSZWLANAPInfo = _RuckusSZWLANAPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2)
)
_RuckusSZAPTable_Object = MibTable
ruckusSZAPTable = _RuckusSZAPTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruckusSZAPTable.setStatus("current")
_RuckusSZAPEntry_Object = MibTableRow
ruckusSZAPEntry = _RuckusSZAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1)
)
ruckusSZAPEntry.setIndexNames(
    (0, "RUCKUS-SZ-WLAN-MIB", "ruckusSZAPMac"),
)
if mibBuilder.loadTexts:
    ruckusSZAPEntry.setStatus("current")
_RuckusSZAPMac_Type = MacAddress
_RuckusSZAPMac_Object = MibTableColumn
ruckusSZAPMac = _RuckusSZAPMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 1),
    _RuckusSZAPMac_Type()
)
ruckusSZAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPMac.setStatus("current")
_RuckusSZAPGroup_Type = DisplayString
_RuckusSZAPGroup_Object = MibTableColumn
ruckusSZAPGroup = _RuckusSZAPGroup_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 2),
    _RuckusSZAPGroup_Type()
)
ruckusSZAPGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPGroup.setStatus("current")
_RuckusSZAPName_Type = DisplayString
_RuckusSZAPName_Object = MibTableColumn
ruckusSZAPName = _RuckusSZAPName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 5),
    _RuckusSZAPName_Type()
)
ruckusSZAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPName.setStatus("current")
_RuckusSZAPUptime_Type = TimeTicks
_RuckusSZAPUptime_Object = MibTableColumn
ruckusSZAPUptime = _RuckusSZAPUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 6),
    _RuckusSZAPUptime_Type()
)
ruckusSZAPUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPUptime.setStatus("current")
_RuckusSZAPFWversion_Type = DisplayString
_RuckusSZAPFWversion_Object = MibTableColumn
ruckusSZAPFWversion = _RuckusSZAPFWversion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 7),
    _RuckusSZAPFWversion_Type()
)
ruckusSZAPFWversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPFWversion.setStatus("current")
_RuckusSZAPModel_Type = DisplayString
_RuckusSZAPModel_Object = MibTableColumn
ruckusSZAPModel = _RuckusSZAPModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 8),
    _RuckusSZAPModel_Type()
)
ruckusSZAPModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPModel.setStatus("current")
_RuckusSZAPSerial_Type = DisplayString
_RuckusSZAPSerial_Object = MibTableColumn
ruckusSZAPSerial = _RuckusSZAPSerial_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 9),
    _RuckusSZAPSerial_Type()
)
ruckusSZAPSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPSerial.setStatus("current")
_RuckusSZAPIp_Type = IpAddress
_RuckusSZAPIp_Object = MibTableColumn
ruckusSZAPIp = _RuckusSZAPIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 10),
    _RuckusSZAPIp_Type()
)
ruckusSZAPIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPIp.setStatus("current")
_RuckusSZAPIPType_Type = DisplayString
_RuckusSZAPIPType_Object = MibTableColumn
ruckusSZAPIPType = _RuckusSZAPIPType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 11),
    _RuckusSZAPIPType_Type()
)
ruckusSZAPIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPIPType.setStatus("current")
_RuckusSZAPExtIp_Type = IpAddress
_RuckusSZAPExtIp_Object = MibTableColumn
ruckusSZAPExtIp = _RuckusSZAPExtIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 12),
    _RuckusSZAPExtIp_Type()
)
ruckusSZAPExtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPExtIp.setStatus("current")
_RuckusSZAPExtPort_Type = Unsigned32
_RuckusSZAPExtPort_Object = MibTableColumn
ruckusSZAPExtPort = _RuckusSZAPExtPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 13),
    _RuckusSZAPExtPort_Type()
)
ruckusSZAPExtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPExtPort.setStatus("current")
_RuckusSZAPNumSta_Type = Unsigned32
_RuckusSZAPNumSta_Object = MibTableColumn
ruckusSZAPNumSta = _RuckusSZAPNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 15),
    _RuckusSZAPNumSta_Type()
)
ruckusSZAPNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPNumSta.setStatus("current")
_RuckusSZAPConnStatus_Type = DisplayString
_RuckusSZAPConnStatus_Object = MibTableColumn
ruckusSZAPConnStatus = _RuckusSZAPConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 16),
    _RuckusSZAPConnStatus_Type()
)
ruckusSZAPConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPConnStatus.setStatus("current")
_RuckusSZAPRegStatus_Type = DisplayString
_RuckusSZAPRegStatus_Object = MibTableColumn
ruckusSZAPRegStatus = _RuckusSZAPRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 17),
    _RuckusSZAPRegStatus_Type()
)
ruckusSZAPRegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPRegStatus.setStatus("current")
_RuckusSZAPConfigStatus_Type = DisplayString
_RuckusSZAPConfigStatus_Object = MibTableColumn
ruckusSZAPConfigStatus = _RuckusSZAPConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 18),
    _RuckusSZAPConfigStatus_Type()
)
ruckusSZAPConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPConfigStatus.setStatus("current")
_RuckusSZAPLocation_Type = DisplayString
_RuckusSZAPLocation_Object = MibTableColumn
ruckusSZAPLocation = _RuckusSZAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 19),
    _RuckusSZAPLocation_Type()
)
ruckusSZAPLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPLocation.setStatus("current")
_RuckusSZAPGPSInfo_Type = DisplayString
_RuckusSZAPGPSInfo_Object = MibTableColumn
ruckusSZAPGPSInfo = _RuckusSZAPGPSInfo_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 20),
    _RuckusSZAPGPSInfo_Type()
)
ruckusSZAPGPSInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPGPSInfo.setStatus("current")
_RuckusSZAPMeshRole_Type = DisplayString
_RuckusSZAPMeshRole_Object = MibTableColumn
ruckusSZAPMeshRole = _RuckusSZAPMeshRole_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 21),
    _RuckusSZAPMeshRole_Type()
)
ruckusSZAPMeshRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPMeshRole.setStatus("current")
_RuckusSZAPDescription_Type = DisplayString
_RuckusSZAPDescription_Object = MibTableColumn
ruckusSZAPDescription = _RuckusSZAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 22),
    _RuckusSZAPDescription_Type()
)
ruckusSZAPDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPDescription.setStatus("current")
_RuckusSZAPRXBytes_Type = Counter64
_RuckusSZAPRXBytes_Object = MibTableColumn
ruckusSZAPRXBytes = _RuckusSZAPRXBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 30),
    _RuckusSZAPRXBytes_Type()
)
ruckusSZAPRXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPRXBytes.setStatus("current")
_RuckusSZAPTXBytes_Type = Counter64
_RuckusSZAPTXBytes_Object = MibTableColumn
ruckusSZAPTXBytes = _RuckusSZAPTXBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 31),
    _RuckusSZAPTXBytes_Type()
)
ruckusSZAPTXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPTXBytes.setStatus("current")
_RuckusSZAPIpsecSessionTime_Type = Unsigned32
_RuckusSZAPIpsecSessionTime_Object = MibTableColumn
ruckusSZAPIpsecSessionTime = _RuckusSZAPIpsecSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 50),
    _RuckusSZAPIpsecSessionTime_Type()
)
ruckusSZAPIpsecSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPIpsecSessionTime.setStatus("current")
_RuckusSZAPIpsecTXPkts_Type = Counter64
_RuckusSZAPIpsecTXPkts_Object = MibTableColumn
ruckusSZAPIpsecTXPkts = _RuckusSZAPIpsecTXPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 55),
    _RuckusSZAPIpsecTXPkts_Type()
)
ruckusSZAPIpsecTXPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPIpsecTXPkts.setStatus("current")
_RuckusSZAPIpsecRXPkts_Type = Counter64
_RuckusSZAPIpsecRXPkts_Object = MibTableColumn
ruckusSZAPIpsecRXPkts = _RuckusSZAPIpsecRXPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 56),
    _RuckusSZAPIpsecRXPkts_Type()
)
ruckusSZAPIpsecRXPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPIpsecRXPkts.setStatus("current")
_RuckusSZAPIpsecTXBytes_Type = Counter64
_RuckusSZAPIpsecTXBytes_Object = MibTableColumn
ruckusSZAPIpsecTXBytes = _RuckusSZAPIpsecTXBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 57),
    _RuckusSZAPIpsecTXBytes_Type()
)
ruckusSZAPIpsecTXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPIpsecTXBytes.setStatus("current")
_RuckusSZAPIpsecRXBytes_Type = Counter64
_RuckusSZAPIpsecRXBytes_Object = MibTableColumn
ruckusSZAPIpsecRXBytes = _RuckusSZAPIpsecRXBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 58),
    _RuckusSZAPIpsecRXBytes_Type()
)
ruckusSZAPIpsecRXBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPIpsecRXBytes.setStatus("current")
_RuckusSZAPIpsecTXPktsDropped_Type = Counter64
_RuckusSZAPIpsecTXPktsDropped_Object = MibTableColumn
ruckusSZAPIpsecTXPktsDropped = _RuckusSZAPIpsecTXPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 59),
    _RuckusSZAPIpsecTXPktsDropped_Type()
)
ruckusSZAPIpsecTXPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPIpsecTXPktsDropped.setStatus("current")
_RuckusSZAPIpsecRXPktsDropped_Type = Counter64
_RuckusSZAPIpsecRXPktsDropped_Object = MibTableColumn
ruckusSZAPIpsecRXPktsDropped = _RuckusSZAPIpsecRXPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 60),
    _RuckusSZAPIpsecRXPktsDropped_Type()
)
ruckusSZAPIpsecRXPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPIpsecRXPktsDropped.setStatus("current")
_RuckusSZAPIpsecTXIdleTime_Type = Unsigned32
_RuckusSZAPIpsecTXIdleTime_Object = MibTableColumn
ruckusSZAPIpsecTXIdleTime = _RuckusSZAPIpsecTXIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 65),
    _RuckusSZAPIpsecTXIdleTime_Type()
)
ruckusSZAPIpsecTXIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPIpsecTXIdleTime.setStatus("current")
_RuckusSZAPIpsecRXIdleTime_Type = Unsigned32
_RuckusSZAPIpsecRXIdleTime_Object = MibTableColumn
ruckusSZAPIpsecRXIdleTime = _RuckusSZAPIpsecRXIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 2, 1, 1, 2, 2, 1, 66),
    _RuckusSZAPIpsecRXIdleTime_Type()
)
ruckusSZAPIpsecRXIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZAPIpsecRXIdleTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-SZ-WLAN-MIB",
    **{"ruckusSZWLANMIB": ruckusSZWLANMIB,
       "ruckusSZWLANObjects": ruckusSZWLANObjects,
       "ruckusSZWLANInfo": ruckusSZWLANInfo,
       "ruckusSZWLANTable": ruckusSZWLANTable,
       "ruckusSZWLANEntry": ruckusSZWLANEntry,
       "ruckusSZWLANSSID": ruckusSZWLANSSID,
       "ruckusSZWLANNumSta": ruckusSZWLANNumSta,
       "ruckusSZWLANRxBytes": ruckusSZWLANRxBytes,
       "ruckusSZWLANTxBytes": ruckusSZWLANTxBytes,
       "ruckusSZWLANAuthType": ruckusSZWLANAuthType,
       "ruckusSZWLANIndex": ruckusSZWLANIndex,
       "ruckusSZWLANAPInfo": ruckusSZWLANAPInfo,
       "ruckusSZAPTable": ruckusSZAPTable,
       "ruckusSZAPEntry": ruckusSZAPEntry,
       "ruckusSZAPMac": ruckusSZAPMac,
       "ruckusSZAPGroup": ruckusSZAPGroup,
       "ruckusSZAPName": ruckusSZAPName,
       "ruckusSZAPUptime": ruckusSZAPUptime,
       "ruckusSZAPFWversion": ruckusSZAPFWversion,
       "ruckusSZAPModel": ruckusSZAPModel,
       "ruckusSZAPSerial": ruckusSZAPSerial,
       "ruckusSZAPIp": ruckusSZAPIp,
       "ruckusSZAPIPType": ruckusSZAPIPType,
       "ruckusSZAPExtIp": ruckusSZAPExtIp,
       "ruckusSZAPExtPort": ruckusSZAPExtPort,
       "ruckusSZAPNumSta": ruckusSZAPNumSta,
       "ruckusSZAPConnStatus": ruckusSZAPConnStatus,
       "ruckusSZAPRegStatus": ruckusSZAPRegStatus,
       "ruckusSZAPConfigStatus": ruckusSZAPConfigStatus,
       "ruckusSZAPLocation": ruckusSZAPLocation,
       "ruckusSZAPGPSInfo": ruckusSZAPGPSInfo,
       "ruckusSZAPMeshRole": ruckusSZAPMeshRole,
       "ruckusSZAPDescription": ruckusSZAPDescription,
       "ruckusSZAPRXBytes": ruckusSZAPRXBytes,
       "ruckusSZAPTXBytes": ruckusSZAPTXBytes,
       "ruckusSZAPIpsecSessionTime": ruckusSZAPIpsecSessionTime,
       "ruckusSZAPIpsecTXPkts": ruckusSZAPIpsecTXPkts,
       "ruckusSZAPIpsecRXPkts": ruckusSZAPIpsecRXPkts,
       "ruckusSZAPIpsecTXBytes": ruckusSZAPIpsecTXBytes,
       "ruckusSZAPIpsecRXBytes": ruckusSZAPIpsecRXBytes,
       "ruckusSZAPIpsecTXPktsDropped": ruckusSZAPIpsecTXPktsDropped,
       "ruckusSZAPIpsecRXPktsDropped": ruckusSZAPIpsecRXPktsDropped,
       "ruckusSZAPIpsecTXIdleTime": ruckusSZAPIpsecTXIdleTime,
       "ruckusSZAPIpsecRXIdleTime": ruckusSZAPIpsecRXIdleTime}
)
