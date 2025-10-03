# SNMP MIB module (SCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\equallogic\SCSI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:25 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

scsiModule = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 999)
)
if mibBuilder.loadTexts:
    scsiModule.setRevisions(
        ("2002-02-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ScsiLUNOrZero(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(8, 8),
    )



class ScsiIndexValue(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class ScsiPortIndexValueOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class ScsiIndexValueOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class ScsiIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(11, 11),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(256, 256),
        ValueSizeConstraint(258, 258),
        ValueSizeConstraint(262, 262),
    )



class ScsiName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(256, 256),
        ValueSizeConstraint(258, 258),
        ValueSizeConstraint(262, 262),
    )



class ScsiNameIdOrZero(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )



class ScsiDeviceOrPort(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("device", 1),
          ("port", 2),
          ("other", 3))
    )



class ScsiIdCodeSet(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class ScsiIdAssociation(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )



class ScsiIdType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class ScsiIdValue(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class HrSWInstalledIndexOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_ScsiObjects_ObjectIdentity = ObjectIdentity
scsiObjects = _ScsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1)
)
_ScsiTransportTypes_ObjectIdentity = ObjectIdentity
scsiTransportTypes = _ScsiTransportTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 1)
)
_ScsiTranportOther_ObjectIdentity = ObjectIdentity
scsiTranportOther = _ScsiTranportOther_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 1)
)
_ScsiTranportSPI_ObjectIdentity = ObjectIdentity
scsiTranportSPI = _ScsiTranportSPI_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 2)
)
_ScsiTransportFCP_ObjectIdentity = ObjectIdentity
scsiTransportFCP = _ScsiTransportFCP_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 3)
)
_ScsiTransportSRP_ObjectIdentity = ObjectIdentity
scsiTransportSRP = _ScsiTransportSRP_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 4)
)
_ScsiTransportISCSI_ObjectIdentity = ObjectIdentity
scsiTransportISCSI = _ScsiTransportISCSI_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 5)
)
_ScsiTransportSBP_ObjectIdentity = ObjectIdentity
scsiTransportSBP = _ScsiTransportSBP_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 1, 6)
)
_ScsiGeneral_ObjectIdentity = ObjectIdentity
scsiGeneral = _ScsiGeneral_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 2)
)
_ScsiInstanceTable_Object = MibTable
scsiInstanceTable = _ScsiInstanceTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1)
)
if mibBuilder.loadTexts:
    scsiInstanceTable.setStatus("current")
_ScsiInstanceEntry_Object = MibTableRow
scsiInstanceEntry = _ScsiInstanceEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1)
)
scsiInstanceEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
)
if mibBuilder.loadTexts:
    scsiInstanceEntry.setStatus("current")
_ScsiInstIndex_Type = ScsiIndexValue
_ScsiInstIndex_Object = MibTableColumn
scsiInstIndex = _ScsiInstIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 1),
    _ScsiInstIndex_Type()
)
scsiInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiInstIndex.setStatus("current")


class _ScsiInstAlias_Type(SnmpAdminString):
    """Custom type scsiInstAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ScsiInstAlias_Type.__name__ = "SnmpAdminString"
_ScsiInstAlias_Object = MibTableColumn
scsiInstAlias = _ScsiInstAlias_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 2),
    _ScsiInstAlias_Type()
)
scsiInstAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiInstAlias.setStatus("current")
_ScsiInstSoftwareIndex_Type = HrSWInstalledIndexOrZero
_ScsiInstSoftwareIndex_Object = MibTableColumn
scsiInstSoftwareIndex = _ScsiInstSoftwareIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 3),
    _ScsiInstSoftwareIndex_Type()
)
scsiInstSoftwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiInstSoftwareIndex.setStatus("current")


class _ScsiInstVendorVersion_Type(SnmpAdminString):
    """Custom type scsiInstVendorVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ScsiInstVendorVersion_Type.__name__ = "SnmpAdminString"
_ScsiInstVendorVersion_Object = MibTableColumn
scsiInstVendorVersion = _ScsiInstVendorVersion_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 4),
    _ScsiInstVendorVersion_Type()
)
scsiInstVendorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiInstVendorVersion.setStatus("current")


class _ScsiInstScsiNotificationsEnable_Type(TruthValue):
    """Custom type scsiInstScsiNotificationsEnable based on TruthValue"""
    defaultValue = 1


_ScsiInstScsiNotificationsEnable_Type.__name__ = "TruthValue"
_ScsiInstScsiNotificationsEnable_Object = MibTableColumn
scsiInstScsiNotificationsEnable = _ScsiInstScsiNotificationsEnable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 5),
    _ScsiInstScsiNotificationsEnable_Type()
)
scsiInstScsiNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiInstScsiNotificationsEnable.setStatus("current")
_ScsiDeviceTable_Object = MibTable
scsiDeviceTable = _ScsiDeviceTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 2)
)
if mibBuilder.loadTexts:
    scsiDeviceTable.setStatus("current")
_ScsiDeviceEntry_Object = MibTableRow
scsiDeviceEntry = _ScsiDeviceEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 2, 1)
)
scsiDeviceEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
)
if mibBuilder.loadTexts:
    scsiDeviceEntry.setStatus("current")
_ScsiDeviceIndex_Type = ScsiIndexValue
_ScsiDeviceIndex_Object = MibTableColumn
scsiDeviceIndex = _ScsiDeviceIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 2, 1, 1),
    _ScsiDeviceIndex_Type()
)
scsiDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiDeviceIndex.setStatus("current")


class _ScsiDeviceAlias_Type(SnmpAdminString):
    """Custom type scsiDeviceAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ScsiDeviceAlias_Type.__name__ = "SnmpAdminString"
_ScsiDeviceAlias_Object = MibTableColumn
scsiDeviceAlias = _ScsiDeviceAlias_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 2, 1, 2),
    _ScsiDeviceAlias_Type()
)
scsiDeviceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiDeviceAlias.setStatus("current")


class _ScsiDeviceRole_Type(Bits):
    """Custom type scsiDeviceRole based on Bits"""
    namedValues = NamedValues(
        *(("target", 0),
          ("initiator", 1))
    )

_ScsiDeviceRole_Type.__name__ = "Bits"
_ScsiDeviceRole_Object = MibTableColumn
scsiDeviceRole = _ScsiDeviceRole_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 2, 1, 3),
    _ScsiDeviceRole_Type()
)
scsiDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDeviceRole.setStatus("current")
_ScsiDevicePortNumber_Type = Unsigned32
_ScsiDevicePortNumber_Object = MibTableColumn
scsiDevicePortNumber = _ScsiDevicePortNumber_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 2, 1, 4),
    _ScsiDevicePortNumber_Type()
)
scsiDevicePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDevicePortNumber.setStatus("current")
_ScsiDeviceResets_Type = Counter32
_ScsiDeviceResets_Object = MibTableColumn
scsiDeviceResets = _ScsiDeviceResets_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 2, 1, 5),
    _ScsiDeviceResets_Type()
)
scsiDeviceResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDeviceResets.setStatus("current")
_ScsiPortTable_Object = MibTable
scsiPortTable = _ScsiPortTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 3)
)
if mibBuilder.loadTexts:
    scsiPortTable.setStatus("current")
_ScsiPortEntry_Object = MibTableRow
scsiPortEntry = _ScsiPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 3, 1)
)
scsiPortEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiPortIndex"),
)
if mibBuilder.loadTexts:
    scsiPortEntry.setStatus("current")
_ScsiPortIndex_Type = ScsiIndexValue
_ScsiPortIndex_Object = MibTableColumn
scsiPortIndex = _ScsiPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 3, 1, 1),
    _ScsiPortIndex_Type()
)
scsiPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiPortIndex.setStatus("current")


class _ScsiPortRole_Type(Bits):
    """Custom type scsiPortRole based on Bits"""
    namedValues = NamedValues(
        *(("target", 0),
          ("initiator", 1))
    )

_ScsiPortRole_Type.__name__ = "Bits"
_ScsiPortRole_Object = MibTableColumn
scsiPortRole = _ScsiPortRole_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 3, 1, 2),
    _ScsiPortRole_Type()
)
scsiPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiPortRole.setStatus("current")


class _ScsiPortTrnsptPtr_Type(OctetString):
    """Custom type scsiPortTrnsptPtr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ScsiPortTrnsptPtr_Type.__name__ = "OctetString"
_ScsiPortTrnsptPtr_Object = MibTableColumn
scsiPortTrnsptPtr = _ScsiPortTrnsptPtr_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 3, 1, 3),
    _ScsiPortTrnsptPtr_Type()
)
scsiPortTrnsptPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiPortTrnsptPtr.setStatus("current")
_ScsiPortBusyStatuses_Type = Counter32
_ScsiPortBusyStatuses_Object = MibTableColumn
scsiPortBusyStatuses = _ScsiPortBusyStatuses_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 3, 1, 4),
    _ScsiPortBusyStatuses_Type()
)
scsiPortBusyStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiPortBusyStatuses.setStatus("current")
_ScsiTrnsptTable_Object = MibTable
scsiTrnsptTable = _ScsiTrnsptTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 5)
)
if mibBuilder.loadTexts:
    scsiTrnsptTable.setStatus("current")
_ScsiTrnsptEntry_Object = MibTableRow
scsiTrnsptEntry = _ScsiTrnsptEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 5, 1)
)
scsiTrnsptEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiTrnsptIndex"),
)
if mibBuilder.loadTexts:
    scsiTrnsptEntry.setStatus("current")
_ScsiTrnsptIndex_Type = ScsiIndexValue
_ScsiTrnsptIndex_Object = MibTableColumn
scsiTrnsptIndex = _ScsiTrnsptIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 5, 1, 1),
    _ScsiTrnsptIndex_Type()
)
scsiTrnsptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiTrnsptIndex.setStatus("current")


class _ScsiTrnsptType_Type(OctetString):
    """Custom type scsiTrnsptType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ScsiTrnsptType_Type.__name__ = "OctetString"
_ScsiTrnsptType_Object = MibTableColumn
scsiTrnsptType = _ScsiTrnsptType_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 5, 1, 2),
    _ScsiTrnsptType_Type()
)
scsiTrnsptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTrnsptType.setStatus("current")


class _ScsiTrnsptPointer_Type(OctetString):
    """Custom type scsiTrnsptPointer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ScsiTrnsptPointer_Type.__name__ = "OctetString"
_ScsiTrnsptPointer_Object = MibTableColumn
scsiTrnsptPointer = _ScsiTrnsptPointer_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 5, 1, 3),
    _ScsiTrnsptPointer_Type()
)
scsiTrnsptPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTrnsptPointer.setStatus("current")
_ScsiTrnsptDevName_Type = ScsiName
_ScsiTrnsptDevName_Object = MibTableColumn
scsiTrnsptDevName = _ScsiTrnsptDevName_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 2, 5, 1, 4),
    _ScsiTrnsptDevName_Type()
)
scsiTrnsptDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTrnsptDevName.setStatus("current")
_ScsiInitiator_ObjectIdentity = ObjectIdentity
scsiInitiator = _ScsiInitiator_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 3)
)
_ScsiIntrDevTable_Object = MibTable
scsiIntrDevTable = _ScsiIntrDevTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 1)
)
if mibBuilder.loadTexts:
    scsiIntrDevTable.setStatus("current")
_ScsiIntrDevEntry_Object = MibTableRow
scsiIntrDevEntry = _ScsiIntrDevEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1)
)
scsiIntrDevEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
)
if mibBuilder.loadTexts:
    scsiIntrDevEntry.setStatus("current")


class _ScsiIntrDevTgtAccessMode_Type(Integer32):
    """Custom type scsiIntrDevTgtAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("autoEnable", 2),
          ("manualEnable", 3))
    )


_ScsiIntrDevTgtAccessMode_Type.__name__ = "Integer32"
_ScsiIntrDevTgtAccessMode_Object = MibTableColumn
scsiIntrDevTgtAccessMode = _ScsiIntrDevTgtAccessMode_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 1),
    _ScsiIntrDevTgtAccessMode_Type()
)
scsiIntrDevTgtAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scsiIntrDevTgtAccessMode.setStatus("current")
_ScsiIntrDevOutResets_Type = Counter32
_ScsiIntrDevOutResets_Object = MibTableColumn
scsiIntrDevOutResets = _ScsiIntrDevOutResets_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 2),
    _ScsiIntrDevOutResets_Type()
)
scsiIntrDevOutResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrDevOutResets.setStatus("current")
_ScsiIntrPrtTable_Object = MibTable
scsiIntrPrtTable = _ScsiIntrPrtTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 3)
)
if mibBuilder.loadTexts:
    scsiIntrPrtTable.setStatus("current")
_ScsiIntrPrtEntry_Object = MibTableRow
scsiIntrPrtEntry = _ScsiIntrPrtEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 3, 1)
)
scsiIntrPrtEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiPortIndex"),
)
if mibBuilder.loadTexts:
    scsiIntrPrtEntry.setStatus("current")
_ScsiIntrPrtName_Type = ScsiName
_ScsiIntrPrtName_Object = MibTableColumn
scsiIntrPrtName = _ScsiIntrPrtName_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 3, 1, 1),
    _ScsiIntrPrtName_Type()
)
scsiIntrPrtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPrtName.setStatus("current")
_ScsiIntrPrtIdentifier_Type = ScsiIdentifier
_ScsiIntrPrtIdentifier_Object = MibTableColumn
scsiIntrPrtIdentifier = _ScsiIntrPrtIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 3, 1, 2),
    _ScsiIntrPrtIdentifier_Type()
)
scsiIntrPrtIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPrtIdentifier.setStatus("current")
_ScsiIntrPrtOutCommands_Type = Counter32
_ScsiIntrPrtOutCommands_Object = MibTableColumn
scsiIntrPrtOutCommands = _ScsiIntrPrtOutCommands_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 3, 1, 3),
    _ScsiIntrPrtOutCommands_Type()
)
scsiIntrPrtOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPrtOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiIntrPrtOutCommands.setUnits("commands")
_ScsiIntrPrtWrittenMegaBytes_Type = Counter32
_ScsiIntrPrtWrittenMegaBytes_Object = MibTableColumn
scsiIntrPrtWrittenMegaBytes = _ScsiIntrPrtWrittenMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 3, 1, 4),
    _ScsiIntrPrtWrittenMegaBytes_Type()
)
scsiIntrPrtWrittenMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPrtWrittenMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiIntrPrtWrittenMegaBytes.setUnits("Megabytes")
_ScsiIntrPrtReadMegaBytes_Type = Counter32
_ScsiIntrPrtReadMegaBytes_Object = MibTableColumn
scsiIntrPrtReadMegaBytes = _ScsiIntrPrtReadMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 3, 1, 5),
    _ScsiIntrPrtReadMegaBytes_Type()
)
scsiIntrPrtReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPrtReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiIntrPrtReadMegaBytes.setUnits("Megabytes")
_ScsiIntrPrtHSOutCommands_Type = Counter64
_ScsiIntrPrtHSOutCommands_Object = MibTableColumn
scsiIntrPrtHSOutCommands = _ScsiIntrPrtHSOutCommands_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 3, 1, 6),
    _ScsiIntrPrtHSOutCommands_Type()
)
scsiIntrPrtHSOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiIntrPrtHSOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiIntrPrtHSOutCommands.setUnits("commands")
_ScsiRemoteTarget_ObjectIdentity = ObjectIdentity
scsiRemoteTarget = _ScsiRemoteTarget_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4)
)
_ScsiDscTgtTable_Object = MibTable
scsiDscTgtTable = _ScsiDscTgtTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    scsiDscTgtTable.setStatus("current")
_ScsiDscTgtEntry_Object = MibTableRow
scsiDscTgtEntry = _ScsiDscTgtEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1)
)
scsiDscTgtEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIntrPortIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIndex"),
)
if mibBuilder.loadTexts:
    scsiDscTgtEntry.setStatus("current")
_ScsiDscTgtIntrPortIndex_Type = ScsiPortIndexValueOrZero
_ScsiDscTgtIntrPortIndex_Object = MibTableColumn
scsiDscTgtIntrPortIndex = _ScsiDscTgtIntrPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 1),
    _ScsiDscTgtIntrPortIndex_Type()
)
scsiDscTgtIntrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiDscTgtIntrPortIndex.setStatus("current")
_ScsiDscTgtIndex_Type = ScsiIndexValue
_ScsiDscTgtIndex_Object = MibTableColumn
scsiDscTgtIndex = _ScsiDscTgtIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 2),
    _ScsiDscTgtIndex_Type()
)
scsiDscTgtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiDscTgtIndex.setStatus("current")
_ScsiDscTgtDevOrPort_Type = ScsiDeviceOrPort
_ScsiDscTgtDevOrPort_Object = MibTableColumn
scsiDscTgtDevOrPort = _ScsiDscTgtDevOrPort_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 3),
    _ScsiDscTgtDevOrPort_Type()
)
scsiDscTgtDevOrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiDscTgtDevOrPort.setStatus("current")
_ScsiDscTgtName_Type = ScsiName
_ScsiDscTgtName_Object = MibTableColumn
scsiDscTgtName = _ScsiDscTgtName_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 4),
    _ScsiDscTgtName_Type()
)
scsiDscTgtName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiDscTgtName.setStatus("current")


class _ScsiDscTgtConfigured_Type(TruthValue):
    """Custom type scsiDscTgtConfigured based on TruthValue"""
    defaultValue = 1


_ScsiDscTgtConfigured_Type.__name__ = "TruthValue"
_ScsiDscTgtConfigured_Object = MibTableColumn
scsiDscTgtConfigured = _ScsiDscTgtConfigured_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 5),
    _ScsiDscTgtConfigured_Type()
)
scsiDscTgtConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiDscTgtConfigured.setStatus("current")
_ScsiDscTgtDiscovered_Type = TruthValue
_ScsiDscTgtDiscovered_Object = MibTableColumn
scsiDscTgtDiscovered = _ScsiDscTgtDiscovered_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 6),
    _ScsiDscTgtDiscovered_Type()
)
scsiDscTgtDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtDiscovered.setStatus("current")
_ScsiDscTgtInCommands_Type = Counter32
_ScsiDscTgtInCommands_Object = MibTableColumn
scsiDscTgtInCommands = _ScsiDscTgtInCommands_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 7),
    _ScsiDscTgtInCommands_Type()
)
scsiDscTgtInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiDscTgtInCommands.setUnits("commands")
_ScsiDscTgtWrittenMegaBytes_Type = Counter32
_ScsiDscTgtWrittenMegaBytes_Object = MibTableColumn
scsiDscTgtWrittenMegaBytes = _ScsiDscTgtWrittenMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 8),
    _ScsiDscTgtWrittenMegaBytes_Type()
)
scsiDscTgtWrittenMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtWrittenMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiDscTgtWrittenMegaBytes.setUnits("Megabytes")
_ScsiDscTgtReadMegaBytes_Type = Counter32
_ScsiDscTgtReadMegaBytes_Object = MibTableColumn
scsiDscTgtReadMegaBytes = _ScsiDscTgtReadMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 9),
    _ScsiDscTgtReadMegaBytes_Type()
)
scsiDscTgtReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiDscTgtReadMegaBytes.setUnits("Megabytes")
_ScsiDscTgtHSInCommands_Type = Counter64
_ScsiDscTgtHSInCommands_Object = MibTableColumn
scsiDscTgtHSInCommands = _ScsiDscTgtHSInCommands_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 10),
    _ScsiDscTgtHSInCommands_Type()
)
scsiDscTgtHSInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtHSInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiDscTgtHSInCommands.setUnits("commands")
_ScsiDscTgtLastCreation_Type = TimeStamp
_ScsiDscTgtLastCreation_Object = MibTableColumn
scsiDscTgtLastCreation = _ScsiDscTgtLastCreation_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 11),
    _ScsiDscTgtLastCreation_Type()
)
scsiDscTgtLastCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscTgtLastCreation.setStatus("current")
_ScsiDscTgtRowStatus_Type = RowStatus
_ScsiDscTgtRowStatus_Object = MibTableColumn
scsiDscTgtRowStatus = _ScsiDscTgtRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 1, 1, 12),
    _ScsiDscTgtRowStatus_Type()
)
scsiDscTgtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiDscTgtRowStatus.setStatus("current")
_ScsiDscLunTable_Object = MibTable
scsiDscLunTable = _ScsiDscLunTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    scsiDscLunTable.setStatus("current")
_ScsiDscLunEntry_Object = MibTableRow
scsiDscLunEntry = _ScsiDscLunEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 2, 1)
)
scsiDscLunEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIntrPortIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIndex"),
    (0, "SCSI-MIB", "scsiDscLunIndex"),
)
if mibBuilder.loadTexts:
    scsiDscLunEntry.setStatus("current")
_ScsiDscLunIndex_Type = ScsiIndexValue
_ScsiDscLunIndex_Object = MibTableColumn
scsiDscLunIndex = _ScsiDscLunIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 2, 1, 1),
    _ScsiDscLunIndex_Type()
)
scsiDscLunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiDscLunIndex.setStatus("current")
_ScsiDscLunLun_Type = ScsiLUNOrZero
_ScsiDscLunLun_Object = MibTableColumn
scsiDscLunLun = _ScsiDscLunLun_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 2, 1, 2),
    _ScsiDscLunLun_Type()
)
scsiDscLunLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscLunLun.setStatus("current")
_ScsiDscLunIdTable_Object = MibTable
scsiDscLunIdTable = _ScsiDscLunIdTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    scsiDscLunIdTable.setStatus("current")
_ScsiDscLunIdEntry_Object = MibTableRow
scsiDscLunIdEntry = _ScsiDscLunIdEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 3, 1)
)
scsiDscLunIdEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIntrPortIndex"),
    (0, "SCSI-MIB", "scsiDscTgtIndex"),
    (0, "SCSI-MIB", "scsiDscLunIndex"),
    (0, "SCSI-MIB", "scsiDscLunIdIndex"),
)
if mibBuilder.loadTexts:
    scsiDscLunIdEntry.setStatus("current")
_ScsiDscLunIdIndex_Type = ScsiIndexValue
_ScsiDscLunIdIndex_Object = MibTableColumn
scsiDscLunIdIndex = _ScsiDscLunIdIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 3, 1, 1),
    _ScsiDscLunIdIndex_Type()
)
scsiDscLunIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiDscLunIdIndex.setStatus("current")
_ScsiDscLunIdCodeSet_Type = ScsiIdCodeSet
_ScsiDscLunIdCodeSet_Object = MibTableColumn
scsiDscLunIdCodeSet = _ScsiDscLunIdCodeSet_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 3, 1, 2),
    _ScsiDscLunIdCodeSet_Type()
)
scsiDscLunIdCodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscLunIdCodeSet.setStatus("current")
_ScsiDscLunIdAssociation_Type = ScsiIdAssociation
_ScsiDscLunIdAssociation_Object = MibTableColumn
scsiDscLunIdAssociation = _ScsiDscLunIdAssociation_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 3, 1, 3),
    _ScsiDscLunIdAssociation_Type()
)
scsiDscLunIdAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscLunIdAssociation.setStatus("current")
_ScsiDscLunIdType_Type = ScsiIdType
_ScsiDscLunIdType_Object = MibTableColumn
scsiDscLunIdType = _ScsiDscLunIdType_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 3, 1, 4),
    _ScsiDscLunIdType_Type()
)
scsiDscLunIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscLunIdType.setStatus("current")
_ScsiDscLunIdValue_Type = ScsiIdValue
_ScsiDscLunIdValue_Object = MibTableColumn
scsiDscLunIdValue = _ScsiDscLunIdValue_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 3, 1, 5),
    _ScsiDscLunIdValue_Type()
)
scsiDscLunIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiDscLunIdValue.setStatus("current")
_ScsiAttTgtPortTable_Object = MibTable
scsiAttTgtPortTable = _ScsiAttTgtPortTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 6)
)
if mibBuilder.loadTexts:
    scsiAttTgtPortTable.setStatus("current")
_ScsiAttTgtPortEntry_Object = MibTableRow
scsiAttTgtPortEntry = _ScsiAttTgtPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 6, 1)
)
scsiAttTgtPortEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiPortIndex"),
    (0, "SCSI-MIB", "scsiAttTgtPortIndex"),
)
if mibBuilder.loadTexts:
    scsiAttTgtPortEntry.setStatus("current")
_ScsiAttTgtPortIndex_Type = ScsiIndexValue
_ScsiAttTgtPortIndex_Object = MibTableColumn
scsiAttTgtPortIndex = _ScsiAttTgtPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 6, 1, 1),
    _ScsiAttTgtPortIndex_Type()
)
scsiAttTgtPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiAttTgtPortIndex.setStatus("current")
_ScsiAttTgtPortDscTgtIdx_Type = ScsiIndexValueOrZero
_ScsiAttTgtPortDscTgtIdx_Object = MibTableColumn
scsiAttTgtPortDscTgtIdx = _ScsiAttTgtPortDscTgtIdx_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 6, 1, 2),
    _ScsiAttTgtPortDscTgtIdx_Type()
)
scsiAttTgtPortDscTgtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttTgtPortDscTgtIdx.setStatus("current")
_ScsiAttTgtPortName_Type = ScsiName
_ScsiAttTgtPortName_Object = MibTableColumn
scsiAttTgtPortName = _ScsiAttTgtPortName_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 6, 1, 3),
    _ScsiAttTgtPortName_Type()
)
scsiAttTgtPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttTgtPortName.setStatus("current")
_ScsiAttTgtPortIdentifier_Type = ScsiIdentifier
_ScsiAttTgtPortIdentifier_Object = MibTableColumn
scsiAttTgtPortIdentifier = _ScsiAttTgtPortIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 3, 4, 6, 1, 4),
    _ScsiAttTgtPortIdentifier_Type()
)
scsiAttTgtPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttTgtPortIdentifier.setStatus("current")
_ScsiTarget_ObjectIdentity = ObjectIdentity
scsiTarget = _ScsiTarget_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 4)
)
_ScsiTgtDevTable_Object = MibTable
scsiTgtDevTable = _ScsiTgtDevTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 1)
)
if mibBuilder.loadTexts:
    scsiTgtDevTable.setStatus("current")
_ScsiTgtDevEntry_Object = MibTableRow
scsiTgtDevEntry = _ScsiTgtDevEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1)
)
scsiTgtDevEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
)
if mibBuilder.loadTexts:
    scsiTgtDevEntry.setStatus("current")
_ScsiTgtDevNumberOfLUs_Type = Gauge32
_ScsiTgtDevNumberOfLUs_Object = MibTableColumn
scsiTgtDevNumberOfLUs = _ScsiTgtDevNumberOfLUs_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 1),
    _ScsiTgtDevNumberOfLUs_Type()
)
scsiTgtDevNumberOfLUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtDevNumberOfLUs.setStatus("current")


class _ScsiTgtDeviceStatus_Type(Integer32):
    """Custom type scsiTgtDeviceStatus based on Integer32"""
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
        *(("unknown", 1),
          ("available", 2),
          ("broken", 3),
          ("readying", 4),
          ("abnormal", 5),
          ("nonAddrFailure", 6),
          ("nonAddrFailReadying", 7),
          ("nonAddrFailAbnormal", 8))
    )


_ScsiTgtDeviceStatus_Type.__name__ = "Integer32"
_ScsiTgtDeviceStatus_Object = MibTableColumn
scsiTgtDeviceStatus = _ScsiTgtDeviceStatus_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 2),
    _ScsiTgtDeviceStatus_Type()
)
scsiTgtDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtDeviceStatus.setStatus("current")
_ScsiTgtDevNonAccessibleLUs_Type = Gauge32
_ScsiTgtDevNonAccessibleLUs_Object = MibTableColumn
scsiTgtDevNonAccessibleLUs = _ScsiTgtDevNonAccessibleLUs_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 3),
    _ScsiTgtDevNonAccessibleLUs_Type()
)
scsiTgtDevNonAccessibleLUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtDevNonAccessibleLUs.setStatus("current")
_ScsiTgtPortTable_Object = MibTable
scsiTgtPortTable = _ScsiTgtPortTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 2)
)
if mibBuilder.loadTexts:
    scsiTgtPortTable.setStatus("current")
_ScsiTgtPortEntry_Object = MibTableRow
scsiTgtPortEntry = _ScsiTgtPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 2, 1)
)
scsiTgtPortEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiPortIndex"),
)
if mibBuilder.loadTexts:
    scsiTgtPortEntry.setStatus("current")
_ScsiTgtPortName_Type = ScsiName
_ScsiTgtPortName_Object = MibTableColumn
scsiTgtPortName = _ScsiTgtPortName_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 2, 1, 1),
    _ScsiTgtPortName_Type()
)
scsiTgtPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortName.setStatus("current")
_ScsiTgtPortIdentifier_Type = ScsiIdentifier
_ScsiTgtPortIdentifier_Object = MibTableColumn
scsiTgtPortIdentifier = _ScsiTgtPortIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 2, 1, 2),
    _ScsiTgtPortIdentifier_Type()
)
scsiTgtPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortIdentifier.setStatus("current")
_ScsiTgtPortInCommands_Type = Counter32
_ScsiTgtPortInCommands_Object = MibTableColumn
scsiTgtPortInCommands = _ScsiTgtPortInCommands_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 2, 1, 3),
    _ScsiTgtPortInCommands_Type()
)
scsiTgtPortInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiTgtPortInCommands.setUnits("commands")
_ScsiTgtPortWrittenMegaBytes_Type = Counter32
_ScsiTgtPortWrittenMegaBytes_Object = MibTableColumn
scsiTgtPortWrittenMegaBytes = _ScsiTgtPortWrittenMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 2, 1, 4),
    _ScsiTgtPortWrittenMegaBytes_Type()
)
scsiTgtPortWrittenMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortWrittenMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiTgtPortWrittenMegaBytes.setUnits("Megabytes")
_ScsiTgtPortReadMegaBytes_Type = Counter32
_ScsiTgtPortReadMegaBytes_Object = MibTableColumn
scsiTgtPortReadMegaBytes = _ScsiTgtPortReadMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 2, 1, 5),
    _ScsiTgtPortReadMegaBytes_Type()
)
scsiTgtPortReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiTgtPortReadMegaBytes.setUnits("Megabytes")
_ScsiTgtPortHSInCommands_Type = Counter64
_ScsiTgtPortHSInCommands_Object = MibTableColumn
scsiTgtPortHSInCommands = _ScsiTgtPortHSInCommands_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 2, 1, 6),
    _ScsiTgtPortHSInCommands_Type()
)
scsiTgtPortHSInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTgtPortHSInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiTgtPortHSInCommands.setUnits("commands")
_ScsiRemoteInitiators_ObjectIdentity = ObjectIdentity
scsiRemoteInitiators = _ScsiRemoteInitiators_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3)
)
_ScsiAuthorizedIntrTable_Object = MibTable
scsiAuthorizedIntrTable = _ScsiAuthorizedIntrTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    scsiAuthorizedIntrTable.setStatus("current")
_ScsiAuthorizedIntrEntry_Object = MibTableRow
scsiAuthorizedIntrEntry = _ScsiAuthorizedIntrEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1)
)
scsiAuthorizedIntrEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiAuthIntrTgtPortIndex"),
    (0, "SCSI-MIB", "scsiAuthIntrIndex"),
)
if mibBuilder.loadTexts:
    scsiAuthorizedIntrEntry.setStatus("current")
_ScsiAuthIntrTgtPortIndex_Type = ScsiPortIndexValueOrZero
_ScsiAuthIntrTgtPortIndex_Object = MibTableColumn
scsiAuthIntrTgtPortIndex = _ScsiAuthIntrTgtPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 1),
    _ScsiAuthIntrTgtPortIndex_Type()
)
scsiAuthIntrTgtPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiAuthIntrTgtPortIndex.setStatus("current")
_ScsiAuthIntrIndex_Type = ScsiIndexValue
_ScsiAuthIntrIndex_Object = MibTableColumn
scsiAuthIntrIndex = _ScsiAuthIntrIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 2),
    _ScsiAuthIntrIndex_Type()
)
scsiAuthIntrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiAuthIntrIndex.setStatus("current")
_ScsiAuthIntrDevOrPort_Type = ScsiDeviceOrPort
_ScsiAuthIntrDevOrPort_Object = MibTableColumn
scsiAuthIntrDevOrPort = _ScsiAuthIntrDevOrPort_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 3),
    _ScsiAuthIntrDevOrPort_Type()
)
scsiAuthIntrDevOrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiAuthIntrDevOrPort.setStatus("current")
_ScsiAuthIntrName_Type = ScsiName
_ScsiAuthIntrName_Object = MibTableColumn
scsiAuthIntrName = _ScsiAuthIntrName_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 4),
    _ScsiAuthIntrName_Type()
)
scsiAuthIntrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiAuthIntrName.setStatus("current")
_ScsiAuthIntrLunMapIndex_Type = ScsiIndexValueOrZero
_ScsiAuthIntrLunMapIndex_Object = MibTableColumn
scsiAuthIntrLunMapIndex = _ScsiAuthIntrLunMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 5),
    _ScsiAuthIntrLunMapIndex_Type()
)
scsiAuthIntrLunMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiAuthIntrLunMapIndex.setStatus("current")
_ScsiAuthIntrAttachedTimes_Type = Counter32
_ScsiAuthIntrAttachedTimes_Object = MibTableColumn
scsiAuthIntrAttachedTimes = _ScsiAuthIntrAttachedTimes_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 6),
    _ScsiAuthIntrAttachedTimes_Type()
)
scsiAuthIntrAttachedTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrAttachedTimes.setStatus("current")
if mibBuilder.loadTexts:
    scsiAuthIntrAttachedTimes.setUnits("Times")
_ScsiAuthIntrOutCommands_Type = Counter32
_ScsiAuthIntrOutCommands_Object = MibTableColumn
scsiAuthIntrOutCommands = _ScsiAuthIntrOutCommands_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 7),
    _ScsiAuthIntrOutCommands_Type()
)
scsiAuthIntrOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiAuthIntrOutCommands.setUnits("commands")
_ScsiAuthIntrReadMegaBytes_Type = Counter32
_ScsiAuthIntrReadMegaBytes_Object = MibTableColumn
scsiAuthIntrReadMegaBytes = _ScsiAuthIntrReadMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 8),
    _ScsiAuthIntrReadMegaBytes_Type()
)
scsiAuthIntrReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiAuthIntrReadMegaBytes.setUnits("Megabytes")
_ScsiAuthIntrWrittenMegaBytes_Type = Counter32
_ScsiAuthIntrWrittenMegaBytes_Object = MibTableColumn
scsiAuthIntrWrittenMegaBytes = _ScsiAuthIntrWrittenMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 9),
    _ScsiAuthIntrWrittenMegaBytes_Type()
)
scsiAuthIntrWrittenMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrWrittenMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiAuthIntrWrittenMegaBytes.setUnits("Megabytes")
_ScsiAuthIntrHSOutCommands_Type = Counter64
_ScsiAuthIntrHSOutCommands_Object = MibTableColumn
scsiAuthIntrHSOutCommands = _ScsiAuthIntrHSOutCommands_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 10),
    _ScsiAuthIntrHSOutCommands_Type()
)
scsiAuthIntrHSOutCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrHSOutCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiAuthIntrHSOutCommands.setUnits("commands")
_ScsiAuthIntrLastCreation_Type = TimeStamp
_ScsiAuthIntrLastCreation_Object = MibTableColumn
scsiAuthIntrLastCreation = _ScsiAuthIntrLastCreation_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 11),
    _ScsiAuthIntrLastCreation_Type()
)
scsiAuthIntrLastCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAuthIntrLastCreation.setStatus("current")
_ScsiAuthIntrRowStatus_Type = RowStatus
_ScsiAuthIntrRowStatus_Object = MibTableColumn
scsiAuthIntrRowStatus = _ScsiAuthIntrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 1, 1, 12),
    _ScsiAuthIntrRowStatus_Type()
)
scsiAuthIntrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiAuthIntrRowStatus.setStatus("current")
_ScsiAttIntrPrtTable_Object = MibTable
scsiAttIntrPrtTable = _ScsiAttIntrPrtTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    scsiAttIntrPrtTable.setStatus("current")
_ScsiAttIntrPrtEntry_Object = MibTableRow
scsiAttIntrPrtEntry = _ScsiAttIntrPrtEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 2, 1)
)
scsiAttIntrPrtEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiPortIndex"),
    (0, "SCSI-MIB", "scsiAttIntrPrtIdx"),
)
if mibBuilder.loadTexts:
    scsiAttIntrPrtEntry.setStatus("current")
_ScsiAttIntrPrtIdx_Type = ScsiIndexValue
_ScsiAttIntrPrtIdx_Object = MibTableColumn
scsiAttIntrPrtIdx = _ScsiAttIntrPrtIdx_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 2, 1, 1),
    _ScsiAttIntrPrtIdx_Type()
)
scsiAttIntrPrtIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiAttIntrPrtIdx.setStatus("current")
_ScsiAttIntrPrtAuthIntrIdx_Type = ScsiIndexValueOrZero
_ScsiAttIntrPrtAuthIntrIdx_Object = MibTableColumn
scsiAttIntrPrtAuthIntrIdx = _ScsiAttIntrPrtAuthIntrIdx_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 2, 1, 2),
    _ScsiAttIntrPrtAuthIntrIdx_Type()
)
scsiAttIntrPrtAuthIntrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttIntrPrtAuthIntrIdx.setStatus("current")
_ScsiAttIntrPrtName_Type = ScsiName
_ScsiAttIntrPrtName_Object = MibTableColumn
scsiAttIntrPrtName = _ScsiAttIntrPrtName_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 2, 1, 3),
    _ScsiAttIntrPrtName_Type()
)
scsiAttIntrPrtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttIntrPrtName.setStatus("current")
_ScsiAttIntrPrtId_Type = ScsiIdentifier
_ScsiAttIntrPrtId_Object = MibTableColumn
scsiAttIntrPrtId = _ScsiAttIntrPrtId_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 4, 3, 2, 1, 4),
    _ScsiAttIntrPrtId_Type()
)
scsiAttIntrPrtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiAttIntrPrtId.setStatus("current")
_ScsiLogicalUnit_ObjectIdentity = ObjectIdentity
scsiLogicalUnit = _ScsiLogicalUnit_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1, 5)
)
_ScsiLuTable_Object = MibTable
scsiLuTable = _ScsiLuTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1)
)
if mibBuilder.loadTexts:
    scsiLuTable.setStatus("current")
_ScsiLuEntry_Object = MibTableRow
scsiLuEntry = _ScsiLuEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1)
)
scsiLuEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiLuIndex"),
)
if mibBuilder.loadTexts:
    scsiLuEntry.setStatus("current")
_ScsiLuIndex_Type = ScsiIndexValue
_ScsiLuIndex_Object = MibTableColumn
scsiLuIndex = _ScsiLuIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 1),
    _ScsiLuIndex_Type()
)
scsiLuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiLuIndex.setStatus("current")
_ScsiLuDefaultLun_Type = ScsiLUNOrZero
_ScsiLuDefaultLun_Object = MibTableColumn
scsiLuDefaultLun = _ScsiLuDefaultLun_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 2),
    _ScsiLuDefaultLun_Type()
)
scsiLuDefaultLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuDefaultLun.setStatus("current")
_ScsiLuWwnName_Type = ScsiNameIdOrZero
_ScsiLuWwnName_Object = MibTableColumn
scsiLuWwnName = _ScsiLuWwnName_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 3),
    _ScsiLuWwnName_Type()
)
scsiLuWwnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuWwnName.setStatus("current")


class _ScsiLuVendorId_Type(SnmpAdminString):
    """Custom type scsiLuVendorId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ScsiLuVendorId_Type.__name__ = "SnmpAdminString"
_ScsiLuVendorId_Object = MibTableColumn
scsiLuVendorId = _ScsiLuVendorId_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 4),
    _ScsiLuVendorId_Type()
)
scsiLuVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuVendorId.setStatus("current")


class _ScsiLuProductId_Type(SnmpAdminString):
    """Custom type scsiLuProductId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ScsiLuProductId_Type.__name__ = "SnmpAdminString"
_ScsiLuProductId_Object = MibTableColumn
scsiLuProductId = _ScsiLuProductId_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 5),
    _ScsiLuProductId_Type()
)
scsiLuProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuProductId.setStatus("current")


class _ScsiLuRevisionId_Type(SnmpAdminString):
    """Custom type scsiLuRevisionId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ScsiLuRevisionId_Type.__name__ = "SnmpAdminString"
_ScsiLuRevisionId_Object = MibTableColumn
scsiLuRevisionId = _ScsiLuRevisionId_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 6),
    _ScsiLuRevisionId_Type()
)
scsiLuRevisionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuRevisionId.setStatus("current")
_ScsiLuPeripheralType_Type = Unsigned32
_ScsiLuPeripheralType_Object = MibTableColumn
scsiLuPeripheralType = _ScsiLuPeripheralType_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 7),
    _ScsiLuPeripheralType_Type()
)
scsiLuPeripheralType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuPeripheralType.setStatus("current")


class _ScsiLuStatus_Type(Integer32):
    """Custom type scsiLuStatus based on Integer32"""
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
          ("available", 2),
          ("notAvailable", 3),
          ("broken", 4),
          ("readying", 5),
          ("abnormal", 6))
    )


_ScsiLuStatus_Type.__name__ = "Integer32"
_ScsiLuStatus_Object = MibTableColumn
scsiLuStatus = _ScsiLuStatus_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 8),
    _ScsiLuStatus_Type()
)
scsiLuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuStatus.setStatus("current")


class _ScsiLuState_Type(Bits):
    """Custom type scsiLuState based on Bits"""
    namedValues = NamedValues(
        *(("dataLost", 0),
          ("dynamicReconfigurationInProgress", 1),
          ("exposed", 2),
          ("fractionallyExposed", 3),
          ("partiallyExposed", 4),
          ("protectedRebuild", 5),
          ("protectionDisabled", 6),
          ("rebuild", 7),
          ("recalculate", 8),
          ("spareInUse", 9),
          ("verifyInProgress", 10))
    )

_ScsiLuState_Type.__name__ = "Bits"
_ScsiLuState_Object = MibTableColumn
scsiLuState = _ScsiLuState_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 9),
    _ScsiLuState_Type()
)
scsiLuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuState.setStatus("current")
_ScsiLuInCommands_Type = Counter32
_ScsiLuInCommands_Object = MibTableColumn
scsiLuInCommands = _ScsiLuInCommands_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 10),
    _ScsiLuInCommands_Type()
)
scsiLuInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiLuInCommands.setUnits("commands")
_ScsiLuReadMegaBytes_Type = Counter32
_ScsiLuReadMegaBytes_Object = MibTableColumn
scsiLuReadMegaBytes = _ScsiLuReadMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 11),
    _ScsiLuReadMegaBytes_Type()
)
scsiLuReadMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuReadMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiLuReadMegaBytes.setUnits("Megabytes")
_ScsiLuWrittenMegaBytes_Type = Counter32
_ScsiLuWrittenMegaBytes_Object = MibTableColumn
scsiLuWrittenMegaBytes = _ScsiLuWrittenMegaBytes_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 12),
    _ScsiLuWrittenMegaBytes_Type()
)
scsiLuWrittenMegaBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuWrittenMegaBytes.setStatus("current")
if mibBuilder.loadTexts:
    scsiLuWrittenMegaBytes.setUnits("Megabytes")
_ScsiLuInResets_Type = Counter32
_ScsiLuInResets_Object = MibTableColumn
scsiLuInResets = _ScsiLuInResets_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 13),
    _ScsiLuInResets_Type()
)
scsiLuInResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuInResets.setStatus("current")
if mibBuilder.loadTexts:
    scsiLuInResets.setUnits("resets")
_ScsiLuOutQueueFullStatus_Type = Counter32
_ScsiLuOutQueueFullStatus_Object = MibTableColumn
scsiLuOutQueueFullStatus = _ScsiLuOutQueueFullStatus_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 14),
    _ScsiLuOutQueueFullStatus_Type()
)
scsiLuOutQueueFullStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuOutQueueFullStatus.setStatus("current")
_ScsiLuHSInCommands_Type = Counter64
_ScsiLuHSInCommands_Object = MibTableColumn
scsiLuHSInCommands = _ScsiLuHSInCommands_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 1, 1, 15),
    _ScsiLuHSInCommands_Type()
)
scsiLuHSInCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuHSInCommands.setStatus("current")
if mibBuilder.loadTexts:
    scsiLuHSInCommands.setUnits("commands")
_ScsiLuIdTable_Object = MibTable
scsiLuIdTable = _ScsiLuIdTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 2)
)
if mibBuilder.loadTexts:
    scsiLuIdTable.setStatus("current")
_ScsiLuIdEntry_Object = MibTableRow
scsiLuIdEntry = _ScsiLuIdEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 2, 1)
)
scsiLuIdEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiLuIndex"),
    (0, "SCSI-MIB", "scsiLuIdIndex"),
)
if mibBuilder.loadTexts:
    scsiLuIdEntry.setStatus("current")
_ScsiLuIdIndex_Type = ScsiIndexValue
_ScsiLuIdIndex_Object = MibTableColumn
scsiLuIdIndex = _ScsiLuIdIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 2, 1, 1),
    _ScsiLuIdIndex_Type()
)
scsiLuIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiLuIdIndex.setStatus("current")
_ScsiLuIdCodeSet_Type = ScsiIdCodeSet
_ScsiLuIdCodeSet_Object = MibTableColumn
scsiLuIdCodeSet = _ScsiLuIdCodeSet_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 2, 1, 2),
    _ScsiLuIdCodeSet_Type()
)
scsiLuIdCodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuIdCodeSet.setStatus("current")
_ScsiLuIdAssociation_Type = ScsiIdAssociation
_ScsiLuIdAssociation_Object = MibTableColumn
scsiLuIdAssociation = _ScsiLuIdAssociation_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 2, 1, 3),
    _ScsiLuIdAssociation_Type()
)
scsiLuIdAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuIdAssociation.setStatus("current")
_ScsiLuIdType_Type = ScsiIdType
_ScsiLuIdType_Object = MibTableColumn
scsiLuIdType = _ScsiLuIdType_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 2, 1, 4),
    _ScsiLuIdType_Type()
)
scsiLuIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuIdType.setStatus("current")
_ScsiLuIdValue_Type = ScsiIdValue
_ScsiLuIdValue_Object = MibTableColumn
scsiLuIdValue = _ScsiLuIdValue_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 2, 1, 5),
    _ScsiLuIdValue_Type()
)
scsiLuIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLuIdValue.setStatus("current")
_ScsiLunMapTable_Object = MibTable
scsiLunMapTable = _ScsiLunMapTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 3)
)
if mibBuilder.loadTexts:
    scsiLunMapTable.setStatus("current")
_ScsiLunMapEntry_Object = MibTableRow
scsiLunMapEntry = _ScsiLunMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 3, 1)
)
scsiLunMapEntry.setIndexNames(
    (0, "SCSI-MIB", "scsiInstIndex"),
    (0, "SCSI-MIB", "scsiDeviceIndex"),
    (0, "SCSI-MIB", "scsiLunMapIndex"),
    (0, "SCSI-MIB", "scsiLunMapLun"),
)
if mibBuilder.loadTexts:
    scsiLunMapEntry.setStatus("current")
_ScsiLunMapIndex_Type = ScsiIndexValue
_ScsiLunMapIndex_Object = MibTableColumn
scsiLunMapIndex = _ScsiLunMapIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 3, 1, 1),
    _ScsiLunMapIndex_Type()
)
scsiLunMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiLunMapIndex.setStatus("current")
_ScsiLunMapLun_Type = ScsiLUNOrZero
_ScsiLunMapLun_Object = MibTableColumn
scsiLunMapLun = _ScsiLunMapLun_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 3, 1, 2),
    _ScsiLunMapLun_Type()
)
scsiLunMapLun.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scsiLunMapLun.setStatus("current")
_ScsiLunMapLuIndex_Type = ScsiIndexValue
_ScsiLunMapLuIndex_Object = MibTableColumn
scsiLunMapLuIndex = _ScsiLunMapLuIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 3, 1, 3),
    _ScsiLunMapLuIndex_Type()
)
scsiLunMapLuIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiLunMapLuIndex.setStatus("current")
_ScsiLunMapRowStatus_Type = RowStatus
_ScsiLunMapRowStatus_Object = MibTableColumn
scsiLunMapRowStatus = _ScsiLunMapRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 999, 1, 5, 3, 1, 4),
    _ScsiLunMapRowStatus_Type()
)
scsiLunMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scsiLunMapRowStatus.setStatus("current")
_ScsiNotifications_ObjectIdentity = ObjectIdentity
scsiNotifications = _ScsiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 2)
)
_ScsiNotificationsPrefix_ObjectIdentity = ObjectIdentity
scsiNotificationsPrefix = _ScsiNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 2, 0)
)
_ScsiConformance_ObjectIdentity = ObjectIdentity
scsiConformance = _ScsiConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 3)
)
_ScsiCompliances_ObjectIdentity = ObjectIdentity
scsiCompliances = _ScsiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 3, 1)
)
_ScsiGroups_ObjectIdentity = ObjectIdentity
scsiGroups = _ScsiGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 3, 2)
)

# Managed Objects groups

scsiDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 1)
)
scsiDeviceGroup.setObjects(
      *(("SCSI-MIB", "scsiInstAlias"),
        ("SCSI-MIB", "scsiInstSoftwareIndex"),
        ("SCSI-MIB", "scsiInstVendorVersion"),
        ("SCSI-MIB", "scsiInstScsiNotificationsEnable"),
        ("SCSI-MIB", "scsiDeviceAlias"),
        ("SCSI-MIB", "scsiDeviceRole"),
        ("SCSI-MIB", "scsiDevicePortNumber"),
        ("SCSI-MIB", "scsiPortRole"),
        ("SCSI-MIB", "scsiPortTrnsptPtr"),
        ("SCSI-MIB", "scsiTrnsptType"),
        ("SCSI-MIB", "scsiTrnsptPointer"),
        ("SCSI-MIB", "scsiTrnsptDevName"))
)
if mibBuilder.loadTexts:
    scsiDeviceGroup.setStatus("current")

scsiInitiatorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 2)
)
scsiInitiatorGroup.setObjects(
      *(("SCSI-MIB", "scsiIntrDevTgtAccessMode"),
        ("SCSI-MIB", "scsiIntrPrtName"),
        ("SCSI-MIB", "scsiIntrPrtIdentifier"),
        ("SCSI-MIB", "scsiAttTgtPortDscTgtIdx"),
        ("SCSI-MIB", "scsiAttTgtPortName"),
        ("SCSI-MIB", "scsiAttTgtPortIdentifier"))
)
if mibBuilder.loadTexts:
    scsiInitiatorGroup.setStatus("current")

scsiDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 3)
)
scsiDiscoveryGroup.setObjects(
      *(("SCSI-MIB", "scsiDscTgtDevOrPort"),
        ("SCSI-MIB", "scsiDscTgtName"),
        ("SCSI-MIB", "scsiDscTgtConfigured"),
        ("SCSI-MIB", "scsiDscTgtDiscovered"),
        ("SCSI-MIB", "scsiDscTgtRowStatus"),
        ("SCSI-MIB", "scsiDscTgtLastCreation"),
        ("SCSI-MIB", "scsiDscLunLun"),
        ("SCSI-MIB", "scsiDscLunIdCodeSet"),
        ("SCSI-MIB", "scsiDscLunIdAssociation"),
        ("SCSI-MIB", "scsiDscLunIdType"),
        ("SCSI-MIB", "scsiDscLunIdValue"))
)
if mibBuilder.loadTexts:
    scsiDiscoveryGroup.setStatus("current")

scsiTargetGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 4)
)
scsiTargetGroup.setObjects(
      *(("SCSI-MIB", "scsiTgtDevNumberOfLUs"),
        ("SCSI-MIB", "scsiTgtDeviceStatus"),
        ("SCSI-MIB", "scsiTgtDevNonAccessibleLUs"),
        ("SCSI-MIB", "scsiTgtPortName"),
        ("SCSI-MIB", "scsiTgtPortIdentifier"),
        ("SCSI-MIB", "scsiAttIntrPrtAuthIntrIdx"),
        ("SCSI-MIB", "scsiAttIntrPrtName"),
        ("SCSI-MIB", "scsiAttIntrPrtId"),
        ("SCSI-MIB", "scsiLuDefaultLun"),
        ("SCSI-MIB", "scsiLuWwnName"),
        ("SCSI-MIB", "scsiLuVendorId"),
        ("SCSI-MIB", "scsiLuProductId"),
        ("SCSI-MIB", "scsiLuRevisionId"),
        ("SCSI-MIB", "scsiLuPeripheralType"),
        ("SCSI-MIB", "scsiLuStatus"),
        ("SCSI-MIB", "scsiLuState"),
        ("SCSI-MIB", "scsiLuIdCodeSet"),
        ("SCSI-MIB", "scsiLuIdAssociation"),
        ("SCSI-MIB", "scsiLuIdType"),
        ("SCSI-MIB", "scsiLuIdValue"))
)
if mibBuilder.loadTexts:
    scsiTargetGroup.setStatus("current")

scsiLunMapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 5)
)
scsiLunMapGroup.setObjects(
      *(("SCSI-MIB", "scsiLunMapLuIndex"),
        ("SCSI-MIB", "scsiLunMapRowStatus"),
        ("SCSI-MIB", "scsiAuthIntrDevOrPort"),
        ("SCSI-MIB", "scsiAuthIntrName"),
        ("SCSI-MIB", "scsiAuthIntrLunMapIndex"),
        ("SCSI-MIB", "scsiAuthIntrLastCreation"),
        ("SCSI-MIB", "scsiAuthIntrRowStatus"))
)
if mibBuilder.loadTexts:
    scsiLunMapGroup.setStatus("current")

scsiTargetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 6)
)
scsiTargetStatsGroup.setObjects(
      *(("SCSI-MIB", "scsiTgtPortInCommands"),
        ("SCSI-MIB", "scsiTgtPortWrittenMegaBytes"),
        ("SCSI-MIB", "scsiTgtPortReadMegaBytes"),
        ("SCSI-MIB", "scsiLuInCommands"),
        ("SCSI-MIB", "scsiLuReadMegaBytes"),
        ("SCSI-MIB", "scsiLuWrittenMegaBytes"),
        ("SCSI-MIB", "scsiLuInResets"),
        ("SCSI-MIB", "scsiLuOutQueueFullStatus"))
)
if mibBuilder.loadTexts:
    scsiTargetStatsGroup.setStatus("current")

scsiTargetHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 7)
)
scsiTargetHSStatsGroup.setObjects(
      *(("SCSI-MIB", "scsiTgtPortHSInCommands"),
        ("SCSI-MIB", "scsiLuHSInCommands"))
)
if mibBuilder.loadTexts:
    scsiTargetHSStatsGroup.setStatus("current")

scsiLunMapStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 8)
)
scsiLunMapStatsGroup.setObjects(
      *(("SCSI-MIB", "scsiAuthIntrAttachedTimes"),
        ("SCSI-MIB", "scsiAuthIntrOutCommands"),
        ("SCSI-MIB", "scsiAuthIntrReadMegaBytes"),
        ("SCSI-MIB", "scsiAuthIntrWrittenMegaBytes"))
)
if mibBuilder.loadTexts:
    scsiLunMapStatsGroup.setStatus("current")

scsiLunMapHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 9)
)
scsiLunMapHSStatsGroup.setObjects(
    ("SCSI-MIB", "scsiAuthIntrHSOutCommands")
)
if mibBuilder.loadTexts:
    scsiLunMapHSStatsGroup.setStatus("current")

scsiInitiatorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 10)
)
scsiInitiatorStatsGroup.setObjects(
      *(("SCSI-MIB", "scsiIntrDevOutResets"),
        ("SCSI-MIB", "scsiIntrPrtOutCommands"),
        ("SCSI-MIB", "scsiIntrPrtWrittenMegaBytes"),
        ("SCSI-MIB", "scsiIntrPrtReadMegaBytes"))
)
if mibBuilder.loadTexts:
    scsiInitiatorStatsGroup.setStatus("current")

scsiInitiatorHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 11)
)
scsiInitiatorHSStatsGroup.setObjects(
    ("SCSI-MIB", "scsiIntrPrtHSOutCommands")
)
if mibBuilder.loadTexts:
    scsiInitiatorHSStatsGroup.setStatus("current")

scsiDiscoveryStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 12)
)
scsiDiscoveryStatsGroup.setObjects(
      *(("SCSI-MIB", "scsiDscTgtInCommands"),
        ("SCSI-MIB", "scsiDscTgtReadMegaBytes"),
        ("SCSI-MIB", "scsiDscTgtWrittenMegaBytes"))
)
if mibBuilder.loadTexts:
    scsiDiscoveryStatsGroup.setStatus("current")

scsiDiscoveryHSStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 13)
)
scsiDiscoveryHSStatsGroup.setObjects(
    ("SCSI-MIB", "scsiDscTgtHSInCommands")
)
if mibBuilder.loadTexts:
    scsiDiscoveryHSStatsGroup.setStatus("current")

scsiDeviceStatGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 3, 2, 14)
)
scsiDeviceStatGroup.setObjects(
      *(("SCSI-MIB", "scsiDeviceResets"),
        ("SCSI-MIB", "scsiPortBusyStatuses"))
)
if mibBuilder.loadTexts:
    scsiDeviceStatGroup.setStatus("current")


# Notification objects

scsiTgtDeviceStatusChanged = NotificationType(
    (1, 3, 6, 1, 2, 1, 999, 2, 0, 1)
)
scsiTgtDeviceStatusChanged.setObjects(
    ("SCSI-MIB", "scsiTgtDeviceStatus")
)
if mibBuilder.loadTexts:
    scsiTgtDeviceStatusChanged.setStatus(
        "current"
    )

scsiLuStatusChanged = NotificationType(
    (1, 3, 6, 1, 2, 1, 999, 2, 0, 2)
)
scsiLuStatusChanged.setObjects(
    ("SCSI-MIB", "scsiLuStatus")
)
if mibBuilder.loadTexts:
    scsiLuStatusChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

scsiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 999, 3, 1, 1)
)
scsiCompliance.setObjects(
    ("SCSI-MIB", "scsiDeviceGroup")
)
if mibBuilder.loadTexts:
    scsiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCSI-MIB",
    **{"ScsiLUNOrZero": ScsiLUNOrZero,
       "ScsiIndexValue": ScsiIndexValue,
       "ScsiPortIndexValueOrZero": ScsiPortIndexValueOrZero,
       "ScsiIndexValueOrZero": ScsiIndexValueOrZero,
       "ScsiIdentifier": ScsiIdentifier,
       "ScsiName": ScsiName,
       "ScsiNameIdOrZero": ScsiNameIdOrZero,
       "ScsiDeviceOrPort": ScsiDeviceOrPort,
       "ScsiIdCodeSet": ScsiIdCodeSet,
       "ScsiIdAssociation": ScsiIdAssociation,
       "ScsiIdType": ScsiIdType,
       "ScsiIdValue": ScsiIdValue,
       "HrSWInstalledIndexOrZero": HrSWInstalledIndexOrZero,
       "scsiModule": scsiModule,
       "scsiObjects": scsiObjects,
       "scsiTransportTypes": scsiTransportTypes,
       "scsiTranportOther": scsiTranportOther,
       "scsiTranportSPI": scsiTranportSPI,
       "scsiTransportFCP": scsiTransportFCP,
       "scsiTransportSRP": scsiTransportSRP,
       "scsiTransportISCSI": scsiTransportISCSI,
       "scsiTransportSBP": scsiTransportSBP,
       "scsiGeneral": scsiGeneral,
       "scsiInstanceTable": scsiInstanceTable,
       "scsiInstanceEntry": scsiInstanceEntry,
       "scsiInstIndex": scsiInstIndex,
       "scsiInstAlias": scsiInstAlias,
       "scsiInstSoftwareIndex": scsiInstSoftwareIndex,
       "scsiInstVendorVersion": scsiInstVendorVersion,
       "scsiInstScsiNotificationsEnable": scsiInstScsiNotificationsEnable,
       "scsiDeviceTable": scsiDeviceTable,
       "scsiDeviceEntry": scsiDeviceEntry,
       "scsiDeviceIndex": scsiDeviceIndex,
       "scsiDeviceAlias": scsiDeviceAlias,
       "scsiDeviceRole": scsiDeviceRole,
       "scsiDevicePortNumber": scsiDevicePortNumber,
       "scsiDeviceResets": scsiDeviceResets,
       "scsiPortTable": scsiPortTable,
       "scsiPortEntry": scsiPortEntry,
       "scsiPortIndex": scsiPortIndex,
       "scsiPortRole": scsiPortRole,
       "scsiPortTrnsptPtr": scsiPortTrnsptPtr,
       "scsiPortBusyStatuses": scsiPortBusyStatuses,
       "scsiTrnsptTable": scsiTrnsptTable,
       "scsiTrnsptEntry": scsiTrnsptEntry,
       "scsiTrnsptIndex": scsiTrnsptIndex,
       "scsiTrnsptType": scsiTrnsptType,
       "scsiTrnsptPointer": scsiTrnsptPointer,
       "scsiTrnsptDevName": scsiTrnsptDevName,
       "scsiInitiator": scsiInitiator,
       "scsiIntrDevTable": scsiIntrDevTable,
       "scsiIntrDevEntry": scsiIntrDevEntry,
       "scsiIntrDevTgtAccessMode": scsiIntrDevTgtAccessMode,
       "scsiIntrDevOutResets": scsiIntrDevOutResets,
       "scsiIntrPrtTable": scsiIntrPrtTable,
       "scsiIntrPrtEntry": scsiIntrPrtEntry,
       "scsiIntrPrtName": scsiIntrPrtName,
       "scsiIntrPrtIdentifier": scsiIntrPrtIdentifier,
       "scsiIntrPrtOutCommands": scsiIntrPrtOutCommands,
       "scsiIntrPrtWrittenMegaBytes": scsiIntrPrtWrittenMegaBytes,
       "scsiIntrPrtReadMegaBytes": scsiIntrPrtReadMegaBytes,
       "scsiIntrPrtHSOutCommands": scsiIntrPrtHSOutCommands,
       "scsiRemoteTarget": scsiRemoteTarget,
       "scsiDscTgtTable": scsiDscTgtTable,
       "scsiDscTgtEntry": scsiDscTgtEntry,
       "scsiDscTgtIntrPortIndex": scsiDscTgtIntrPortIndex,
       "scsiDscTgtIndex": scsiDscTgtIndex,
       "scsiDscTgtDevOrPort": scsiDscTgtDevOrPort,
       "scsiDscTgtName": scsiDscTgtName,
       "scsiDscTgtConfigured": scsiDscTgtConfigured,
       "scsiDscTgtDiscovered": scsiDscTgtDiscovered,
       "scsiDscTgtInCommands": scsiDscTgtInCommands,
       "scsiDscTgtWrittenMegaBytes": scsiDscTgtWrittenMegaBytes,
       "scsiDscTgtReadMegaBytes": scsiDscTgtReadMegaBytes,
       "scsiDscTgtHSInCommands": scsiDscTgtHSInCommands,
       "scsiDscTgtLastCreation": scsiDscTgtLastCreation,
       "scsiDscTgtRowStatus": scsiDscTgtRowStatus,
       "scsiDscLunTable": scsiDscLunTable,
       "scsiDscLunEntry": scsiDscLunEntry,
       "scsiDscLunIndex": scsiDscLunIndex,
       "scsiDscLunLun": scsiDscLunLun,
       "scsiDscLunIdTable": scsiDscLunIdTable,
       "scsiDscLunIdEntry": scsiDscLunIdEntry,
       "scsiDscLunIdIndex": scsiDscLunIdIndex,
       "scsiDscLunIdCodeSet": scsiDscLunIdCodeSet,
       "scsiDscLunIdAssociation": scsiDscLunIdAssociation,
       "scsiDscLunIdType": scsiDscLunIdType,
       "scsiDscLunIdValue": scsiDscLunIdValue,
       "scsiAttTgtPortTable": scsiAttTgtPortTable,
       "scsiAttTgtPortEntry": scsiAttTgtPortEntry,
       "scsiAttTgtPortIndex": scsiAttTgtPortIndex,
       "scsiAttTgtPortDscTgtIdx": scsiAttTgtPortDscTgtIdx,
       "scsiAttTgtPortName": scsiAttTgtPortName,
       "scsiAttTgtPortIdentifier": scsiAttTgtPortIdentifier,
       "scsiTarget": scsiTarget,
       "scsiTgtDevTable": scsiTgtDevTable,
       "scsiTgtDevEntry": scsiTgtDevEntry,
       "scsiTgtDevNumberOfLUs": scsiTgtDevNumberOfLUs,
       "scsiTgtDeviceStatus": scsiTgtDeviceStatus,
       "scsiTgtDevNonAccessibleLUs": scsiTgtDevNonAccessibleLUs,
       "scsiTgtPortTable": scsiTgtPortTable,
       "scsiTgtPortEntry": scsiTgtPortEntry,
       "scsiTgtPortName": scsiTgtPortName,
       "scsiTgtPortIdentifier": scsiTgtPortIdentifier,
       "scsiTgtPortInCommands": scsiTgtPortInCommands,
       "scsiTgtPortWrittenMegaBytes": scsiTgtPortWrittenMegaBytes,
       "scsiTgtPortReadMegaBytes": scsiTgtPortReadMegaBytes,
       "scsiTgtPortHSInCommands": scsiTgtPortHSInCommands,
       "scsiRemoteInitiators": scsiRemoteInitiators,
       "scsiAuthorizedIntrTable": scsiAuthorizedIntrTable,
       "scsiAuthorizedIntrEntry": scsiAuthorizedIntrEntry,
       "scsiAuthIntrTgtPortIndex": scsiAuthIntrTgtPortIndex,
       "scsiAuthIntrIndex": scsiAuthIntrIndex,
       "scsiAuthIntrDevOrPort": scsiAuthIntrDevOrPort,
       "scsiAuthIntrName": scsiAuthIntrName,
       "scsiAuthIntrLunMapIndex": scsiAuthIntrLunMapIndex,
       "scsiAuthIntrAttachedTimes": scsiAuthIntrAttachedTimes,
       "scsiAuthIntrOutCommands": scsiAuthIntrOutCommands,
       "scsiAuthIntrReadMegaBytes": scsiAuthIntrReadMegaBytes,
       "scsiAuthIntrWrittenMegaBytes": scsiAuthIntrWrittenMegaBytes,
       "scsiAuthIntrHSOutCommands": scsiAuthIntrHSOutCommands,
       "scsiAuthIntrLastCreation": scsiAuthIntrLastCreation,
       "scsiAuthIntrRowStatus": scsiAuthIntrRowStatus,
       "scsiAttIntrPrtTable": scsiAttIntrPrtTable,
       "scsiAttIntrPrtEntry": scsiAttIntrPrtEntry,
       "scsiAttIntrPrtIdx": scsiAttIntrPrtIdx,
       "scsiAttIntrPrtAuthIntrIdx": scsiAttIntrPrtAuthIntrIdx,
       "scsiAttIntrPrtName": scsiAttIntrPrtName,
       "scsiAttIntrPrtId": scsiAttIntrPrtId,
       "scsiLogicalUnit": scsiLogicalUnit,
       "scsiLuTable": scsiLuTable,
       "scsiLuEntry": scsiLuEntry,
       "scsiLuIndex": scsiLuIndex,
       "scsiLuDefaultLun": scsiLuDefaultLun,
       "scsiLuWwnName": scsiLuWwnName,
       "scsiLuVendorId": scsiLuVendorId,
       "scsiLuProductId": scsiLuProductId,
       "scsiLuRevisionId": scsiLuRevisionId,
       "scsiLuPeripheralType": scsiLuPeripheralType,
       "scsiLuStatus": scsiLuStatus,
       "scsiLuState": scsiLuState,
       "scsiLuInCommands": scsiLuInCommands,
       "scsiLuReadMegaBytes": scsiLuReadMegaBytes,
       "scsiLuWrittenMegaBytes": scsiLuWrittenMegaBytes,
       "scsiLuInResets": scsiLuInResets,
       "scsiLuOutQueueFullStatus": scsiLuOutQueueFullStatus,
       "scsiLuHSInCommands": scsiLuHSInCommands,
       "scsiLuIdTable": scsiLuIdTable,
       "scsiLuIdEntry": scsiLuIdEntry,
       "scsiLuIdIndex": scsiLuIdIndex,
       "scsiLuIdCodeSet": scsiLuIdCodeSet,
       "scsiLuIdAssociation": scsiLuIdAssociation,
       "scsiLuIdType": scsiLuIdType,
       "scsiLuIdValue": scsiLuIdValue,
       "scsiLunMapTable": scsiLunMapTable,
       "scsiLunMapEntry": scsiLunMapEntry,
       "scsiLunMapIndex": scsiLunMapIndex,
       "scsiLunMapLun": scsiLunMapLun,
       "scsiLunMapLuIndex": scsiLunMapLuIndex,
       "scsiLunMapRowStatus": scsiLunMapRowStatus,
       "scsiNotifications": scsiNotifications,
       "scsiNotificationsPrefix": scsiNotificationsPrefix,
       "scsiTgtDeviceStatusChanged": scsiTgtDeviceStatusChanged,
       "scsiLuStatusChanged": scsiLuStatusChanged,
       "scsiConformance": scsiConformance,
       "scsiCompliances": scsiCompliances,
       "scsiCompliance": scsiCompliance,
       "scsiGroups": scsiGroups,
       "scsiDeviceGroup": scsiDeviceGroup,
       "scsiInitiatorGroup": scsiInitiatorGroup,
       "scsiDiscoveryGroup": scsiDiscoveryGroup,
       "scsiTargetGroup": scsiTargetGroup,
       "scsiLunMapGroup": scsiLunMapGroup,
       "scsiTargetStatsGroup": scsiTargetStatsGroup,
       "scsiTargetHSStatsGroup": scsiTargetHSStatsGroup,
       "scsiLunMapStatsGroup": scsiLunMapStatsGroup,
       "scsiLunMapHSStatsGroup": scsiLunMapHSStatsGroup,
       "scsiInitiatorStatsGroup": scsiInitiatorStatsGroup,
       "scsiInitiatorHSStatsGroup": scsiInitiatorHSStatsGroup,
       "scsiDiscoveryStatsGroup": scsiDiscoveryStatsGroup,
       "scsiDiscoveryHSStatsGroup": scsiDiscoveryHSStatsGroup,
       "scsiDeviceStatGroup": scsiDeviceStatGroup}
)
