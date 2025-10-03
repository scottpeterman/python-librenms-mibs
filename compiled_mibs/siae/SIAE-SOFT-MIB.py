# SNMP MIB module (SIAE-SOFT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-SOFT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:44 2025
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

(alarmTrap,) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "alarmTrap")

(equipIpSnmpAgentAddress,) = mibBuilder.importSymbols(
    "SIAE-EQUIP-MIB",
    "equipIpSnmpAgentAddress")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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

software = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7)
)
if mibBuilder.loadTexts:
    software.setRevisions(
        ("2015-03-23 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SoftwareMibVersion_Type(Integer32):
    """Custom type softwareMibVersion based on Integer32"""
    defaultValue = 1


_SoftwareMibVersion_Type.__name__ = "Integer32"
_SoftwareMibVersion_Object = MibScalar
softwareMibVersion = _SoftwareMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 1),
    _SoftwareMibVersion_Type()
)
softwareMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMibVersion.setStatus("current")


class _SoftwareEquipmentReleaseBench1_Type(DisplayString):
    """Custom type softwareEquipmentReleaseBench1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SoftwareEquipmentReleaseBench1_Type.__name__ = "DisplayString"
_SoftwareEquipmentReleaseBench1_Object = MibScalar
softwareEquipmentReleaseBench1 = _SoftwareEquipmentReleaseBench1_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 2),
    _SoftwareEquipmentReleaseBench1_Type()
)
softwareEquipmentReleaseBench1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareEquipmentReleaseBench1.setStatus("current")


class _SoftwareEquipmentReleaseBench1Status_Type(Integer32):
    """Custom type softwareEquipmentReleaseBench1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notLoaded", 1),
          ("loaded", 2),
          ("running", 3))
    )


_SoftwareEquipmentReleaseBench1Status_Type.__name__ = "Integer32"
_SoftwareEquipmentReleaseBench1Status_Object = MibScalar
softwareEquipmentReleaseBench1Status = _SoftwareEquipmentReleaseBench1Status_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 3),
    _SoftwareEquipmentReleaseBench1Status_Type()
)
softwareEquipmentReleaseBench1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareEquipmentReleaseBench1Status.setStatus("current")


class _SoftwareEquipmentReleaseBench2_Type(DisplayString):
    """Custom type softwareEquipmentReleaseBench2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SoftwareEquipmentReleaseBench2_Type.__name__ = "DisplayString"
_SoftwareEquipmentReleaseBench2_Object = MibScalar
softwareEquipmentReleaseBench2 = _SoftwareEquipmentReleaseBench2_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 4),
    _SoftwareEquipmentReleaseBench2_Type()
)
softwareEquipmentReleaseBench2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareEquipmentReleaseBench2.setStatus("current")


class _SoftwareEquipmentReleaseBench2Status_Type(Integer32):
    """Custom type softwareEquipmentReleaseBench2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notLoaded", 1),
          ("loaded", 2),
          ("running", 3))
    )


_SoftwareEquipmentReleaseBench2Status_Type.__name__ = "Integer32"
_SoftwareEquipmentReleaseBench2Status_Object = MibScalar
softwareEquipmentReleaseBench2Status = _SoftwareEquipmentReleaseBench2Status_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 5),
    _SoftwareEquipmentReleaseBench2Status_Type()
)
softwareEquipmentReleaseBench2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareEquipmentReleaseBench2Status.setStatus("current")
_SoftwareIpAddressDwlServer_Type = IpAddress
_SoftwareIpAddressDwlServer_Object = MibScalar
softwareIpAddressDwlServer = _SoftwareIpAddressDwlServer_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 6),
    _SoftwareIpAddressDwlServer_Type()
)
softwareIpAddressDwlServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareIpAddressDwlServer.setStatus("current")


class _SoftwareGosipAddressDwlServer_Type(OctetString):
    """Custom type softwareGosipAddressDwlServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SoftwareGosipAddressDwlServer_Type.__name__ = "OctetString"
_SoftwareGosipAddressDwlServer_Object = MibScalar
softwareGosipAddressDwlServer = _SoftwareGosipAddressDwlServer_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 7),
    _SoftwareGosipAddressDwlServer_Type()
)
softwareGosipAddressDwlServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareGosipAddressDwlServer.setStatus("current")


class _SoftwareDownloadfile_Type(DisplayString):
    """Custom type softwareDownloadfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareDownloadfile_Type.__name__ = "DisplayString"
_SoftwareDownloadfile_Object = MibScalar
softwareDownloadfile = _SoftwareDownloadfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 8),
    _SoftwareDownloadfile_Type()
)
softwareDownloadfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareDownloadfile.setStatus("current")
_SoftwareActionRequest_Type = Integer32
_SoftwareActionRequest_Object = MibScalar
softwareActionRequest = _SoftwareActionRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 9),
    _SoftwareActionRequest_Type()
)
softwareActionRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareActionRequest.setStatus("current")


class _SoftwareDownloadStatus_Type(Integer32):
    """Custom type softwareDownloadStatus based on Integer32"""
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
        *(("downloading", 1),
          ("completed", 2),
          ("interrupted", 3),
          ("perifDownloading", 4),
          ("configurationDownloading", 5))
    )


_SoftwareDownloadStatus_Type.__name__ = "Integer32"
_SoftwareDownloadStatus_Object = MibScalar
softwareDownloadStatus = _SoftwareDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 10),
    _SoftwareDownloadStatus_Type()
)
softwareDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareDownloadStatus.setStatus("current")
_SoftwareUnitTable_Object = MibTable
softwareUnitTable = _SoftwareUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11)
)
if mibBuilder.loadTexts:
    softwareUnitTable.setStatus("current")
_SoftwareUnitRecord_Object = MibTableRow
softwareUnitRecord = _SoftwareUnitRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1)
)
softwareUnitRecord.setIndexNames(
    (0, "SIAE-SOFT-MIB", "softwareUnitId"),
    (0, "SIAE-SOFT-MIB", "softwareElementId"),
)
if mibBuilder.loadTexts:
    softwareUnitRecord.setStatus("current")
_SoftwareUnitId_Type = Integer32
_SoftwareUnitId_Object = MibTableColumn
softwareUnitId = _SoftwareUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 1),
    _SoftwareUnitId_Type()
)
softwareUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareUnitId.setStatus("current")
_SoftwareElementId_Type = Integer32
_SoftwareElementId_Object = MibTableColumn
softwareElementId = _SoftwareElementId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 2),
    _SoftwareElementId_Type()
)
softwareElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareElementId.setStatus("current")


class _SoftwareType_Type(Integer32):
    """Custom type softwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("s-record", 1),
          ("image-FPGA", 2),
          ("volatile", 3))
    )


_SoftwareType_Type.__name__ = "Integer32"
_SoftwareType_Object = MibTableColumn
softwareType = _SoftwareType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 3),
    _SoftwareType_Type()
)
softwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareType.setStatus("current")


class _SoftwareUnitReleaseBench1_Type(DisplayString):
    """Custom type softwareUnitReleaseBench1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SoftwareUnitReleaseBench1_Type.__name__ = "DisplayString"
_SoftwareUnitReleaseBench1_Object = MibTableColumn
softwareUnitReleaseBench1 = _SoftwareUnitReleaseBench1_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 4),
    _SoftwareUnitReleaseBench1_Type()
)
softwareUnitReleaseBench1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareUnitReleaseBench1.setStatus("current")


class _SoftwareUnitReleaseBench2_Type(DisplayString):
    """Custom type softwareUnitReleaseBench2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SoftwareUnitReleaseBench2_Type.__name__ = "DisplayString"
_SoftwareUnitReleaseBench2_Object = MibTableColumn
softwareUnitReleaseBench2 = _SoftwareUnitReleaseBench2_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 5),
    _SoftwareUnitReleaseBench2_Type()
)
softwareUnitReleaseBench2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareUnitReleaseBench2.setStatus("current")


class _SoftwareUnitActualRelease_Type(DisplayString):
    """Custom type softwareUnitActualRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_SoftwareUnitActualRelease_Type.__name__ = "DisplayString"
_SoftwareUnitActualRelease_Object = MibTableColumn
softwareUnitActualRelease = _SoftwareUnitActualRelease_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 11, 1, 6),
    _SoftwareUnitActualRelease_Type()
)
softwareUnitActualRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareUnitActualRelease.setStatus("current")


class _SoftwareDownloadStatusTrapNotification_Type(Integer32):
    """Custom type softwareDownloadStatusTrapNotification based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              34)
        )
    )
    namedValues = NamedValues(
        *(("trapDisable", 1),
          ("trapEnable", 2),
          ("trapEnableWithACK", 34))
    )


_SoftwareDownloadStatusTrapNotification_Type.__name__ = "Integer32"
_SoftwareDownloadStatusTrapNotification_Object = MibScalar
softwareDownloadStatusTrapNotification = _SoftwareDownloadStatusTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 12),
    _SoftwareDownloadStatusTrapNotification_Type()
)
softwareDownloadStatusTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareDownloadStatusTrapNotification.setStatus("current")
_SoftwareRemoteIpAddressDwlServer_Type = IpAddress
_SoftwareRemoteIpAddressDwlServer_Object = MibScalar
softwareRemoteIpAddressDwlServer = _SoftwareRemoteIpAddressDwlServer_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 7, 13),
    _SoftwareRemoteIpAddressDwlServer_Type()
)
softwareRemoteIpAddressDwlServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareRemoteIpAddressDwlServer.setStatus("current")

# Managed Objects groups


# Notification objects

softwareDownloadStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 0, 701)
)
softwareDownloadStatusTrap.setObjects(
      *(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"),
        ("SIAE-SOFT-MIB", "softwareDownloadStatus"))
)
if mibBuilder.loadTexts:
    softwareDownloadStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-SOFT-MIB",
    **{"softwareDownloadStatusTrap": softwareDownloadStatusTrap,
       "software": software,
       "softwareMibVersion": softwareMibVersion,
       "softwareEquipmentReleaseBench1": softwareEquipmentReleaseBench1,
       "softwareEquipmentReleaseBench1Status": softwareEquipmentReleaseBench1Status,
       "softwareEquipmentReleaseBench2": softwareEquipmentReleaseBench2,
       "softwareEquipmentReleaseBench2Status": softwareEquipmentReleaseBench2Status,
       "softwareIpAddressDwlServer": softwareIpAddressDwlServer,
       "softwareGosipAddressDwlServer": softwareGosipAddressDwlServer,
       "softwareDownloadfile": softwareDownloadfile,
       "softwareActionRequest": softwareActionRequest,
       "softwareDownloadStatus": softwareDownloadStatus,
       "softwareUnitTable": softwareUnitTable,
       "softwareUnitRecord": softwareUnitRecord,
       "softwareUnitId": softwareUnitId,
       "softwareElementId": softwareElementId,
       "softwareType": softwareType,
       "softwareUnitReleaseBench1": softwareUnitReleaseBench1,
       "softwareUnitReleaseBench2": softwareUnitReleaseBench2,
       "softwareUnitActualRelease": softwareUnitActualRelease,
       "softwareDownloadStatusTrapNotification": softwareDownloadStatusTrapNotification,
       "softwareRemoteIpAddressDwlServer": softwareRemoteIpAddressDwlServer}
)
