# SNMP MIB module (SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\brocade\SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:00 2025
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

(SwPortIndex,
 SwSensorIndex) = mibBuilder.importSymbols(
    "Brocade-TC",
    "SwPortIndex",
    "SwSensorIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(sw,) = mibBuilder.importSymbols(
    "SWBASE-MIB",
    "sw")


# MODULE-IDENTITY

swSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    swSystem.setRevisions(
        ("1911-04-15 18:30",
         "1912-04-30 18:00")
    )


# Types definitions



class SwFwEvent(Integer32):
    """Custom type SwFwEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("started", 1),
          ("changed", 2),
          ("exceeded", 3),
          ("below", 4),
          ("above", 5),
          ("inBetween", 6),
          ("lowBufferCrsd", 7))
    )




# TEXTUAL-CONVENTIONS



class FcPortFlag(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("physical", 0),
          ("virtual", 1))
    )


# MIB Managed Objects in the order of their OIDs

_SwTrapsV2_ObjectIdentity = ObjectIdentity
swTrapsV2 = _SwTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0)
)
if mibBuilder.loadTexts:
    swTrapsV2.setStatus("current")


class _SwCurrentDate_Type(DisplayString):
    """Custom type swCurrentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwCurrentDate_Type.__name__ = "DisplayString"
_SwCurrentDate_Object = MibScalar
swCurrentDate = _SwCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 1),
    _SwCurrentDate_Type()
)
swCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCurrentDate.setStatus("current")


class _SwBootDate_Type(DisplayString):
    """Custom type swBootDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwBootDate_Type.__name__ = "DisplayString"
_SwBootDate_Object = MibScalar
swBootDate = _SwBootDate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 2),
    _SwBootDate_Type()
)
swBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootDate.setStatus("current")


class _SwFWLastUpdated_Type(DisplayString):
    """Custom type swFWLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFWLastUpdated_Type.__name__ = "DisplayString"
_SwFWLastUpdated_Object = MibScalar
swFWLastUpdated = _SwFWLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 3),
    _SwFWLastUpdated_Type()
)
swFWLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFWLastUpdated.setStatus("current")


class _SwFlashLastUpdated_Type(DisplayString):
    """Custom type swFlashLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFlashLastUpdated_Type.__name__ = "DisplayString"
_SwFlashLastUpdated_Object = MibScalar
swFlashLastUpdated = _SwFlashLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 4),
    _SwFlashLastUpdated_Type()
)
swFlashLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFlashLastUpdated.setStatus("current")


class _SwBootPromLastUpdated_Type(DisplayString):
    """Custom type swBootPromLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwBootPromLastUpdated_Type.__name__ = "DisplayString"
_SwBootPromLastUpdated_Object = MibScalar
swBootPromLastUpdated = _SwBootPromLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 5),
    _SwBootPromLastUpdated_Type()
)
swBootPromLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootPromLastUpdated.setStatus("current")


class _SwFirmwareVersion_Type(DisplayString):
    """Custom type swFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SwFirmwareVersion_Type.__name__ = "DisplayString"
_SwFirmwareVersion_Object = MibScalar
swFirmwareVersion = _SwFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 6),
    _SwFirmwareVersion_Type()
)
swFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwareVersion.setStatus("current")


class _SwOperStatus_Type(Integer32):
    """Custom type swOperStatus based on Integer32"""
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
        *(("online", 1),
          ("offline", 2),
          ("testing", 3),
          ("faulty", 4))
    )


_SwOperStatus_Type.__name__ = "Integer32"
_SwOperStatus_Object = MibScalar
swOperStatus = _SwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 7),
    _SwOperStatus_Type()
)
swOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOperStatus.setStatus("current")


class _SwSsn_Type(DisplayString):
    """Custom type swSsn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwSsn_Type.__name__ = "DisplayString"
_SwSsn_Object = MibScalar
swSsn = _SwSsn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 10),
    _SwSsn_Type()
)
swSsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSsn.setStatus("current")


class _SwFlashDLOperStatus_Type(Integer32):
    """Custom type swFlashDLOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("swCurrent", 1),
          ("swFwUpgraded", 2),
          ("swCfUploaded", 3),
          ("swCfDownloaded", 4),
          ("swFwCorrupted", 5))
    )


_SwFlashDLOperStatus_Type.__name__ = "Integer32"
_SwFlashDLOperStatus_Object = MibScalar
swFlashDLOperStatus = _SwFlashDLOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 11),
    _SwFlashDLOperStatus_Type()
)
swFlashDLOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFlashDLOperStatus.setStatus("current")


class _SwFlashDLAdmStatus_Type(Integer32):
    """Custom type swFlashDLAdmStatus based on Integer32"""
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
        *(("swCurrent", 1),
          ("swFwUpgrade", 2),
          ("swCfUpload", 3),
          ("swCfDownload", 4),
          ("swFwCorrupted", 5))
    )


_SwFlashDLAdmStatus_Type.__name__ = "Integer32"
_SwFlashDLAdmStatus_Object = MibScalar
swFlashDLAdmStatus = _SwFlashDLAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 12),
    _SwFlashDLAdmStatus_Type()
)
swFlashDLAdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFlashDLAdmStatus.setStatus("current")


class _SwBeaconOperStatus_Type(Integer32):
    """Custom type swBeaconOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SwBeaconOperStatus_Type.__name__ = "Integer32"
_SwBeaconOperStatus_Object = MibScalar
swBeaconOperStatus = _SwBeaconOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 18),
    _SwBeaconOperStatus_Type()
)
swBeaconOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBeaconOperStatus.setStatus("current")


class _SwBeaconAdmStatus_Type(Integer32):
    """Custom type swBeaconAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SwBeaconAdmStatus_Type.__name__ = "Integer32"
_SwBeaconAdmStatus_Object = MibScalar
swBeaconAdmStatus = _SwBeaconAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 19),
    _SwBeaconAdmStatus_Type()
)
swBeaconAdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBeaconAdmStatus.setStatus("current")


class _SwDiagResult_Type(Integer32):
    """Custom type swDiagResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sw-ok", 1),
          ("sw-faulty", 2),
          ("sw-embedded-port-fault", 3))
    )


_SwDiagResult_Type.__name__ = "Integer32"
_SwDiagResult_Object = MibScalar
swDiagResult = _SwDiagResult_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 20),
    _SwDiagResult_Type()
)
swDiagResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDiagResult.setStatus("current")


class _SwNumSensors_Type(Integer32):
    """Custom type swNumSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNumSensors_Type.__name__ = "Integer32"
_SwNumSensors_Object = MibScalar
swNumSensors = _SwNumSensors_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 21),
    _SwNumSensors_Type()
)
swNumSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNumSensors.setStatus("current")
_SwSensorTable_Object = MibTable
swSensorTable = _SwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22)
)
if mibBuilder.loadTexts:
    swSensorTable.setStatus("current")
_SwSensorEntry_Object = MibTableRow
swSensorEntry = _SwSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1)
)
swSensorEntry.setIndexNames(
    (0, "SYSTEM-MIB", "swSensorIndex"),
)
if mibBuilder.loadTexts:
    swSensorEntry.setStatus("current")
_SwSensorIndex_Type = SwSensorIndex
_SwSensorIndex_Object = MibTableColumn
swSensorIndex = _SwSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 1),
    _SwSensorIndex_Type()
)
swSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorIndex.setStatus("current")


class _SwSensorType_Type(Integer32):
    """Custom type swSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("temperature", 1),
          ("fan", 2),
          ("power-supply", 3))
    )


_SwSensorType_Type.__name__ = "Integer32"
_SwSensorType_Object = MibTableColumn
swSensorType = _SwSensorType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 2),
    _SwSensorType_Type()
)
swSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorType.setStatus("current")


class _SwSensorStatus_Type(Integer32):
    """Custom type swSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("faulty", 2),
          ("below-min", 3),
          ("nominal", 4),
          ("above-max", 5),
          ("absent", 6))
    )


_SwSensorStatus_Type.__name__ = "Integer32"
_SwSensorStatus_Object = MibTableColumn
swSensorStatus = _SwSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 3),
    _SwSensorStatus_Type()
)
swSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorStatus.setStatus("current")
_SwSensorValue_Type = Integer32
_SwSensorValue_Object = MibTableColumn
swSensorValue = _SwSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 4),
    _SwSensorValue_Type()
)
swSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorValue.setStatus("current")


class _SwSensorInfo_Type(DisplayString):
    """Custom type swSensorInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwSensorInfo_Type.__name__ = "DisplayString"
_SwSensorInfo_Object = MibTableColumn
swSensorInfo = _SwSensorInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 5),
    _SwSensorInfo_Type()
)
swSensorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorInfo.setStatus("current")
_SwID_Type = Integer32
_SwID_Object = MibScalar
swID = _SwID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 24),
    _SwID_Type()
)
swID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swID.setStatus("current")
_SwEtherIPAddress_Type = IpAddress
_SwEtherIPAddress_Object = MibScalar
swEtherIPAddress = _SwEtherIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 25),
    _SwEtherIPAddress_Type()
)
swEtherIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherIPAddress.setStatus("current")
_SwEtherIPMask_Type = IpAddress
_SwEtherIPMask_Object = MibScalar
swEtherIPMask = _SwEtherIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 26),
    _SwEtherIPMask_Type()
)
swEtherIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherIPMask.setStatus("current")
_SwIPv6Address_Type = DisplayString
_SwIPv6Address_Object = MibScalar
swIPv6Address = _SwIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 29),
    _SwIPv6Address_Type()
)
swIPv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIPv6Address.setStatus("current")


class _SwIPv6Status_Type(Integer32):
    """Custom type swIPv6Status based on Integer32"""
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
        *(("tentative", 1),
          ("preferred", 2),
          ("ipdeprecated", 3),
          ("inactive", 4))
    )


_SwIPv6Status_Type.__name__ = "Integer32"
_SwIPv6Status_Object = MibScalar
swIPv6Status = _SwIPv6Status_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 30),
    _SwIPv6Status_Type()
)
swIPv6Status.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIPv6Status.setStatus("current")
_SwFabric_ObjectIdentity = ObjectIdentity
swFabric = _SwFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    swFabric.setStatus("current")


class _SwVfId_Type(Integer32):
    """Custom type swVfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwVfId_Type.__name__ = "Integer32"
_SwVfId_Object = MibScalar
swVfId = _SwVfId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 15),
    _SwVfId_Type()
)
swVfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVfId.setStatus("current")
_SwFCport_ObjectIdentity = ObjectIdentity
swFCport = _SwFCport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    swFCport.setStatus("current")
_SwFCPortTable_Object = MibTable
swFCPortTable = _SwFCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    swFCPortTable.setStatus("current")
_SwFCPortEntry_Object = MibTableRow
swFCPortEntry = _SwFCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1)
)
swFCPortEntry.setIndexNames(
    (0, "SYSTEM-MIB", "swFCPortIndex"),
)
if mibBuilder.loadTexts:
    swFCPortEntry.setStatus("current")
_SwFCPortIndex_Type = SwPortIndex
_SwFCPortIndex_Object = MibTableColumn
swFCPortIndex = _SwFCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 1),
    _SwFCPortIndex_Type()
)
swFCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortIndex.setStatus("current")


class _SwFCPortType_Type(Integer32):
    """Custom type swFCPortType based on Integer32"""
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
        *(("stitch", 1),
          ("flannel", 2),
          ("loom", 3),
          ("bloom", 4),
          ("rdbloom", 5),
          ("wormhole", 6),
          ("other", 7),
          ("unknown", 8))
    )


_SwFCPortType_Type.__name__ = "Integer32"
_SwFCPortType_Object = MibTableColumn
swFCPortType = _SwFCPortType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 2),
    _SwFCPortType_Type()
)
swFCPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortType.setStatus("current")


class _SwFCPortPhyState_Type(Integer32):
    """Custom type swFCPortPhyState based on Integer32"""
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
              8,
              9,
              10,
              11,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noCard", 1),
          ("noTransceiver", 2),
          ("laserFault", 3),
          ("noLight", 4),
          ("noSync", 5),
          ("inSync", 6),
          ("portFault", 7),
          ("diagFault", 8),
          ("lockRef", 9),
          ("validating", 10),
          ("invalidModule", 11),
          ("unknown", 255))
    )


_SwFCPortPhyState_Type.__name__ = "Integer32"
_SwFCPortPhyState_Object = MibTableColumn
swFCPortPhyState = _SwFCPortPhyState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 3),
    _SwFCPortPhyState_Type()
)
swFCPortPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortPhyState.setStatus("current")


class _SwFCPortOpStatus_Type(Integer32):
    """Custom type swFCPortOpStatus based on Integer32"""
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
        *(("unknown", 0),
          ("online", 1),
          ("offline", 2),
          ("testing", 3),
          ("faulty", 4))
    )


_SwFCPortOpStatus_Type.__name__ = "Integer32"
_SwFCPortOpStatus_Object = MibTableColumn
swFCPortOpStatus = _SwFCPortOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 4),
    _SwFCPortOpStatus_Type()
)
swFCPortOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortOpStatus.setStatus("current")


class _SwFCPortAdmStatus_Type(Integer32):
    """Custom type swFCPortAdmStatus based on Integer32"""
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
        *(("online", 1),
          ("offline", 2),
          ("testing", 3),
          ("faulty", 4))
    )


_SwFCPortAdmStatus_Type.__name__ = "Integer32"
_SwFCPortAdmStatus_Object = MibTableColumn
swFCPortAdmStatus = _SwFCPortAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 5),
    _SwFCPortAdmStatus_Type()
)
swFCPortAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFCPortAdmStatus.setStatus("current")


class _SwFCPortLinkState_Type(Integer32):
    """Custom type swFCPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("loopback", 3))
    )


_SwFCPortLinkState_Type.__name__ = "Integer32"
_SwFCPortLinkState_Object = MibTableColumn
swFCPortLinkState = _SwFCPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 6),
    _SwFCPortLinkState_Type()
)
swFCPortLinkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFCPortLinkState.setStatus("current")


class _SwFCPortTxType_Type(Integer32):
    """Custom type swFCPortTxType based on Integer32"""
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
          ("lw", 2),
          ("sw", 3),
          ("ld", 4),
          ("cu", 5))
    )


_SwFCPortTxType_Type.__name__ = "Integer32"
_SwFCPortTxType_Object = MibTableColumn
swFCPortTxType = _SwFCPortTxType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 7),
    _SwFCPortTxType_Type()
)
swFCPortTxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxType.setStatus("current")
_SwFCPortTxWords_Type = Counter32
_SwFCPortTxWords_Object = MibTableColumn
swFCPortTxWords = _SwFCPortTxWords_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 11),
    _SwFCPortTxWords_Type()
)
swFCPortTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxWords.setStatus("current")
_SwFCPortRxWords_Type = Counter32
_SwFCPortRxWords_Object = MibTableColumn
swFCPortRxWords = _SwFCPortRxWords_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 12),
    _SwFCPortRxWords_Type()
)
swFCPortRxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxWords.setStatus("current")
_SwFCPortTxFrames_Type = Counter32
_SwFCPortTxFrames_Object = MibTableColumn
swFCPortTxFrames = _SwFCPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 13),
    _SwFCPortTxFrames_Type()
)
swFCPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxFrames.setStatus("current")
_SwFCPortRxFrames_Type = Counter32
_SwFCPortRxFrames_Object = MibTableColumn
swFCPortRxFrames = _SwFCPortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 14),
    _SwFCPortRxFrames_Type()
)
swFCPortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxFrames.setStatus("current")
_SwFCPortRxC2Frames_Type = Counter32
_SwFCPortRxC2Frames_Object = MibTableColumn
swFCPortRxC2Frames = _SwFCPortRxC2Frames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 15),
    _SwFCPortRxC2Frames_Type()
)
swFCPortRxC2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxC2Frames.setStatus("current")
_SwFCPortRxC3Frames_Type = Counter32
_SwFCPortRxC3Frames_Object = MibTableColumn
swFCPortRxC3Frames = _SwFCPortRxC3Frames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 16),
    _SwFCPortRxC3Frames_Type()
)
swFCPortRxC3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxC3Frames.setStatus("current")
_SwFCPortRxLCs_Type = Counter32
_SwFCPortRxLCs_Object = MibTableColumn
swFCPortRxLCs = _SwFCPortRxLCs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 17),
    _SwFCPortRxLCs_Type()
)
swFCPortRxLCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxLCs.setStatus("current")
_SwFCPortRxMcasts_Type = Counter32
_SwFCPortRxMcasts_Object = MibTableColumn
swFCPortRxMcasts = _SwFCPortRxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 18),
    _SwFCPortRxMcasts_Type()
)
swFCPortRxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxMcasts.setStatus("current")
_SwFCPortTooManyRdys_Type = Counter32
_SwFCPortTooManyRdys_Object = MibTableColumn
swFCPortTooManyRdys = _SwFCPortTooManyRdys_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 19),
    _SwFCPortTooManyRdys_Type()
)
swFCPortTooManyRdys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTooManyRdys.setStatus("current")
_SwFCPortNoTxCredits_Type = Counter32
_SwFCPortNoTxCredits_Object = MibTableColumn
swFCPortNoTxCredits = _SwFCPortNoTxCredits_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 20),
    _SwFCPortNoTxCredits_Type()
)
swFCPortNoTxCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortNoTxCredits.setStatus("current")
_SwFCPortRxEncInFrs_Type = Counter32
_SwFCPortRxEncInFrs_Object = MibTableColumn
swFCPortRxEncInFrs = _SwFCPortRxEncInFrs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 21),
    _SwFCPortRxEncInFrs_Type()
)
swFCPortRxEncInFrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxEncInFrs.setStatus("current")
_SwFCPortRxCrcs_Type = Counter32
_SwFCPortRxCrcs_Object = MibTableColumn
swFCPortRxCrcs = _SwFCPortRxCrcs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 22),
    _SwFCPortRxCrcs_Type()
)
swFCPortRxCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxCrcs.setStatus("current")
_SwFCPortRxTruncs_Type = Counter32
_SwFCPortRxTruncs_Object = MibTableColumn
swFCPortRxTruncs = _SwFCPortRxTruncs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 23),
    _SwFCPortRxTruncs_Type()
)
swFCPortRxTruncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxTruncs.setStatus("current")
_SwFCPortRxTooLongs_Type = Counter32
_SwFCPortRxTooLongs_Object = MibTableColumn
swFCPortRxTooLongs = _SwFCPortRxTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 24),
    _SwFCPortRxTooLongs_Type()
)
swFCPortRxTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxTooLongs.setStatus("current")
_SwFCPortRxBadEofs_Type = Counter32
_SwFCPortRxBadEofs_Object = MibTableColumn
swFCPortRxBadEofs = _SwFCPortRxBadEofs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 25),
    _SwFCPortRxBadEofs_Type()
)
swFCPortRxBadEofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxBadEofs.setStatus("current")
_SwFCPortRxEncOutFrs_Type = Counter32
_SwFCPortRxEncOutFrs_Object = MibTableColumn
swFCPortRxEncOutFrs = _SwFCPortRxEncOutFrs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 26),
    _SwFCPortRxEncOutFrs_Type()
)
swFCPortRxEncOutFrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxEncOutFrs.setStatus("current")
_SwFCPortRxBadOs_Type = Counter32
_SwFCPortRxBadOs_Object = MibTableColumn
swFCPortRxBadOs = _SwFCPortRxBadOs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 27),
    _SwFCPortRxBadOs_Type()
)
swFCPortRxBadOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxBadOs.setStatus("current")
_SwFCPortC3Discards_Type = Counter32
_SwFCPortC3Discards_Object = MibTableColumn
swFCPortC3Discards = _SwFCPortC3Discards_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 28),
    _SwFCPortC3Discards_Type()
)
swFCPortC3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortC3Discards.setStatus("current")
_SwFCPortMcastTimedOuts_Type = Counter32
_SwFCPortMcastTimedOuts_Object = MibTableColumn
swFCPortMcastTimedOuts = _SwFCPortMcastTimedOuts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 29),
    _SwFCPortMcastTimedOuts_Type()
)
swFCPortMcastTimedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortMcastTimedOuts.setStatus("current")
_SwFCPortTxMcasts_Type = Counter32
_SwFCPortTxMcasts_Object = MibTableColumn
swFCPortTxMcasts = _SwFCPortTxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 30),
    _SwFCPortTxMcasts_Type()
)
swFCPortTxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxMcasts.setStatus("current")
_SwFCPortLipIns_Type = Counter32
_SwFCPortLipIns_Object = MibTableColumn
swFCPortLipIns = _SwFCPortLipIns_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 31),
    _SwFCPortLipIns_Type()
)
swFCPortLipIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortLipIns.setStatus("current")
_SwFCPortLipOuts_Type = Counter32
_SwFCPortLipOuts_Object = MibTableColumn
swFCPortLipOuts = _SwFCPortLipOuts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 32),
    _SwFCPortLipOuts_Type()
)
swFCPortLipOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortLipOuts.setStatus("current")


class _SwFCPortLipLastAlpa_Type(OctetString):
    """Custom type swFCPortLipLastAlpa based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_SwFCPortLipLastAlpa_Type.__name__ = "OctetString"
_SwFCPortLipLastAlpa_Object = MibTableColumn
swFCPortLipLastAlpa = _SwFCPortLipLastAlpa_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 33),
    _SwFCPortLipLastAlpa_Type()
)
swFCPortLipLastAlpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortLipLastAlpa.setStatus("current")


class _SwFCPortWwn_Type(OctetString):
    """Custom type swFCPortWwn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwFCPortWwn_Type.__name__ = "OctetString"
_SwFCPortWwn_Object = MibTableColumn
swFCPortWwn = _SwFCPortWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 34),
    _SwFCPortWwn_Type()
)
swFCPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortWwn.setStatus("current")


class _SwFCPortSpeed_Type(Integer32):
    """Custom type swFCPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("one-GB", 1),
          ("two-GB", 2),
          ("auto-Negotiate", 3),
          ("four-GB", 4),
          ("eight-GB", 5),
          ("ten-GB", 6),
          ("unknown", 7))
    )


_SwFCPortSpeed_Type.__name__ = "Integer32"
_SwFCPortSpeed_Object = MibTableColumn
swFCPortSpeed = _SwFCPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 35),
    _SwFCPortSpeed_Type()
)
swFCPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFCPortSpeed.setStatus("current")


class _SwFCPortName_Type(DisplayString):
    """Custom type swFCPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFCPortName_Type.__name__ = "DisplayString"
_SwFCPortName_Object = MibTableColumn
swFCPortName = _SwFCPortName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 36),
    _SwFCPortName_Type()
)
swFCPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortName.setStatus("current")
_SwFCPortSpecifier_Type = DisplayString
_SwFCPortSpecifier_Object = MibTableColumn
swFCPortSpecifier = _SwFCPortSpecifier_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 37),
    _SwFCPortSpecifier_Type()
)
swFCPortSpecifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortSpecifier.setStatus("current")
_SwFCPortFlag_Type = FcPortFlag
_SwFCPortFlag_Object = MibTableColumn
swFCPortFlag = _SwFCPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 38),
    _SwFCPortFlag_Type()
)
swFCPortFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortFlag.setStatus("current")


class _SwFCPortBrcdType_Type(Integer32):
    """Custom type swFCPortBrcdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("fl-port", 3),
          ("f-port", 4),
          ("e-port", 5),
          ("g-port", 6),
          ("ex-port", 7))
    )


_SwFCPortBrcdType_Type.__name__ = "Integer32"
_SwFCPortBrcdType_Object = MibTableColumn
swFCPortBrcdType = _SwFCPortBrcdType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 39),
    _SwFCPortBrcdType_Type()
)
swFCPortBrcdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortBrcdType.setStatus("current")
_SwEvent_ObjectIdentity = ObjectIdentity
swEvent = _SwEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    swEvent.setStatus("current")
_SwEventTable_Object = MibTable
swEventTable = _SwEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    swEventTable.setStatus("current")
_SwEventEntry_Object = MibTableRow
swEventEntry = _SwEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1)
)
swEventEntry.setIndexNames(
    (0, "SYSTEM-MIB", "swEventIndex"),
)
if mibBuilder.loadTexts:
    swEventEntry.setStatus("current")


class _SwEventIndex_Type(Integer32):
    """Custom type swEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEventIndex_Type.__name__ = "Integer32"
_SwEventIndex_Object = MibTableColumn
swEventIndex = _SwEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 1),
    _SwEventIndex_Type()
)
swEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventIndex.setStatus("current")


class _SwEventTimeInfo_Type(DisplayString):
    """Custom type swEventTimeInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwEventTimeInfo_Type.__name__ = "DisplayString"
_SwEventTimeInfo_Object = MibTableColumn
swEventTimeInfo = _SwEventTimeInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 2),
    _SwEventTimeInfo_Type()
)
swEventTimeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventTimeInfo.setStatus("current")


class _SwEventLevel_Type(Integer32):
    """Custom type swEventLevel based on Integer32"""
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
        *(("critical", 1),
          ("error", 2),
          ("warning", 3),
          ("informational", 4),
          ("debug", 5))
    )


_SwEventLevel_Type.__name__ = "Integer32"
_SwEventLevel_Object = MibTableColumn
swEventLevel = _SwEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 3),
    _SwEventLevel_Type()
)
swEventLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventLevel.setStatus("current")


class _SwEventRepeatCount_Type(Integer32):
    """Custom type swEventRepeatCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEventRepeatCount_Type.__name__ = "Integer32"
_SwEventRepeatCount_Object = MibTableColumn
swEventRepeatCount = _SwEventRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 4),
    _SwEventRepeatCount_Type()
)
swEventRepeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventRepeatCount.setStatus("current")
_SwEventDescr_Type = DisplayString
_SwEventDescr_Object = MibTableColumn
swEventDescr = _SwEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 5),
    _SwEventDescr_Type()
)
swEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventDescr.setStatus("current")


class _SwEventVfId_Type(Integer32):
    """Custom type swEventVfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwEventVfId_Type.__name__ = "Integer32"
_SwEventVfId_Object = MibTableColumn
swEventVfId = _SwEventVfId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 6),
    _SwEventVfId_Type()
)
swEventVfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventVfId.setStatus("current")

# Managed Objects groups


# Notification objects

swFCPortScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 3)
)
swFCPortScn.setObjects(
      *(("SYSTEM-MIB", "swFCPortOpStatus"),
        ("SYSTEM-MIB", "swFCPortIndex"),
        ("SYSTEM-MIB", "swFCPortName"),
        ("SYSTEM-MIB", "swSsn"),
        ("SYSTEM-MIB", "swFCPortFlag"),
        ("SYSTEM-MIB", "swVfId"))
)
if mibBuilder.loadTexts:
    swFCPortScn.setStatus(
        "current"
    )

swEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 4)
)
swEventTrap.setObjects(
      *(("SYSTEM-MIB", "swEventIndex"),
        ("SYSTEM-MIB", "swEventTimeInfo"),
        ("SYSTEM-MIB", "swEventLevel"),
        ("SYSTEM-MIB", "swEventRepeatCount"),
        ("SYSTEM-MIB", "swEventDescr"),
        ("SYSTEM-MIB", "swSsn"),
        ("SYSTEM-MIB", "swVfId"))
)
if mibBuilder.loadTexts:
    swEventTrap.setStatus(
        "current"
    )

swStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 12)
)
swStateChangeTrap.setObjects(
      *(("SYSTEM-MIB", "swOperStatus"),
        ("SYSTEM-MIB", "swVfId"))
)
if mibBuilder.loadTexts:
    swStateChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYSTEM-MIB",
    **{"FcPortFlag": FcPortFlag,
       "SwFwEvent": SwFwEvent,
       "swTrapsV2": swTrapsV2,
       "swFCPortScn": swFCPortScn,
       "swEventTrap": swEventTrap,
       "swStateChangeTrap": swStateChangeTrap,
       "swSystem": swSystem,
       "swCurrentDate": swCurrentDate,
       "swBootDate": swBootDate,
       "swFWLastUpdated": swFWLastUpdated,
       "swFlashLastUpdated": swFlashLastUpdated,
       "swBootPromLastUpdated": swBootPromLastUpdated,
       "swFirmwareVersion": swFirmwareVersion,
       "swOperStatus": swOperStatus,
       "swSsn": swSsn,
       "swFlashDLOperStatus": swFlashDLOperStatus,
       "swFlashDLAdmStatus": swFlashDLAdmStatus,
       "swBeaconOperStatus": swBeaconOperStatus,
       "swBeaconAdmStatus": swBeaconAdmStatus,
       "swDiagResult": swDiagResult,
       "swNumSensors": swNumSensors,
       "swSensorTable": swSensorTable,
       "swSensorEntry": swSensorEntry,
       "swSensorIndex": swSensorIndex,
       "swSensorType": swSensorType,
       "swSensorStatus": swSensorStatus,
       "swSensorValue": swSensorValue,
       "swSensorInfo": swSensorInfo,
       "swID": swID,
       "swEtherIPAddress": swEtherIPAddress,
       "swEtherIPMask": swEtherIPMask,
       "swIPv6Address": swIPv6Address,
       "swIPv6Status": swIPv6Status,
       "swFabric": swFabric,
       "swVfId": swVfId,
       "swFCport": swFCport,
       "swFCPortTable": swFCPortTable,
       "swFCPortEntry": swFCPortEntry,
       "swFCPortIndex": swFCPortIndex,
       "swFCPortType": swFCPortType,
       "swFCPortPhyState": swFCPortPhyState,
       "swFCPortOpStatus": swFCPortOpStatus,
       "swFCPortAdmStatus": swFCPortAdmStatus,
       "swFCPortLinkState": swFCPortLinkState,
       "swFCPortTxType": swFCPortTxType,
       "swFCPortTxWords": swFCPortTxWords,
       "swFCPortRxWords": swFCPortRxWords,
       "swFCPortTxFrames": swFCPortTxFrames,
       "swFCPortRxFrames": swFCPortRxFrames,
       "swFCPortRxC2Frames": swFCPortRxC2Frames,
       "swFCPortRxC3Frames": swFCPortRxC3Frames,
       "swFCPortRxLCs": swFCPortRxLCs,
       "swFCPortRxMcasts": swFCPortRxMcasts,
       "swFCPortTooManyRdys": swFCPortTooManyRdys,
       "swFCPortNoTxCredits": swFCPortNoTxCredits,
       "swFCPortRxEncInFrs": swFCPortRxEncInFrs,
       "swFCPortRxCrcs": swFCPortRxCrcs,
       "swFCPortRxTruncs": swFCPortRxTruncs,
       "swFCPortRxTooLongs": swFCPortRxTooLongs,
       "swFCPortRxBadEofs": swFCPortRxBadEofs,
       "swFCPortRxEncOutFrs": swFCPortRxEncOutFrs,
       "swFCPortRxBadOs": swFCPortRxBadOs,
       "swFCPortC3Discards": swFCPortC3Discards,
       "swFCPortMcastTimedOuts": swFCPortMcastTimedOuts,
       "swFCPortTxMcasts": swFCPortTxMcasts,
       "swFCPortLipIns": swFCPortLipIns,
       "swFCPortLipOuts": swFCPortLipOuts,
       "swFCPortLipLastAlpa": swFCPortLipLastAlpa,
       "swFCPortWwn": swFCPortWwn,
       "swFCPortSpeed": swFCPortSpeed,
       "swFCPortName": swFCPortName,
       "swFCPortSpecifier": swFCPortSpecifier,
       "swFCPortFlag": swFCPortFlag,
       "swFCPortBrcdType": swFCPortBrcdType,
       "swEvent": swEvent,
       "swEventTable": swEventTable,
       "swEventEntry": swEventEntry,
       "swEventIndex": swEventIndex,
       "swEventTimeInfo": swEventTimeInfo,
       "swEventLevel": swEventLevel,
       "swEventRepeatCount": swEventRepeatCount,
       "swEventDescr": swEventDescr,
       "swEventVfId": swEventVfId}
)
