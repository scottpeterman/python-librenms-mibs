# SNMP MIB module (ARRIS-C3-SM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-C3-SM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:07 2025
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

(cmtsC3,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "cmtsC3")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cmtsC3SMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcxSMObjects_ObjectIdentity = ObjectIdentity
dcxSMObjects = _DcxSMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1)
)
_DcxSMBootGroup_ObjectIdentity = ObjectIdentity
dcxSMBootGroup = _DcxSMBootGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1)
)


class _DcxSMBootDevice_Type(Integer32):
    """Custom type dcxSMBootDevice based on Integer32"""
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
        *(("nfs", 1),
          ("tftp", 2),
          ("ftp", 3),
          ("diskAlternative", 4),
          ("diskCurrent", 5))
    )


_DcxSMBootDevice_Type.__name__ = "Integer32"
_DcxSMBootDevice_Object = MibScalar
dcxSMBootDevice = _DcxSMBootDevice_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 1),
    _DcxSMBootDevice_Type()
)
dcxSMBootDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMBootDevice.setStatus("current")
_DcxSMBootHostname_Type = IpAddress
_DcxSMBootHostname_Object = MibScalar
dcxSMBootHostname = _DcxSMBootHostname_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 2),
    _DcxSMBootHostname_Type()
)
dcxSMBootHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMBootHostname.setStatus("current")


class _DcxSMBootUsername_Type(OctetString):
    """Custom type dcxSMBootUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DcxSMBootUsername_Type.__name__ = "OctetString"
_DcxSMBootUsername_Object = MibScalar
dcxSMBootUsername = _DcxSMBootUsername_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 3),
    _DcxSMBootUsername_Type()
)
dcxSMBootUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMBootUsername.setStatus("current")


class _DcxSMBootPassword_Type(OctetString):
    """Custom type dcxSMBootPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcxSMBootPassword_Type.__name__ = "OctetString"
_DcxSMBootPassword_Object = MibScalar
dcxSMBootPassword = _DcxSMBootPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 4),
    _DcxSMBootPassword_Type()
)
dcxSMBootPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMBootPassword.setStatus("current")


class _DcxSMBootPath_Type(OctetString):
    """Custom type dcxSMBootPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DcxSMBootPath_Type.__name__ = "OctetString"
_DcxSMBootPath_Object = MibScalar
dcxSMBootPath = _DcxSMBootPath_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 5),
    _DcxSMBootPath_Type()
)
dcxSMBootPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMBootPath.setStatus("current")


class _DcxSMEnetMgmtInterface_Type(Integer32):
    """Custom type dcxSMEnetMgmtInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfBand", 0),
          ("inBand", 1))
    )


_DcxSMEnetMgmtInterface_Type.__name__ = "Integer32"
_DcxSMEnetMgmtInterface_Object = MibScalar
dcxSMEnetMgmtInterface = _DcxSMEnetMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 6),
    _DcxSMEnetMgmtInterface_Type()
)
dcxSMEnetMgmtInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMEnetMgmtInterface.setStatus("current")


class _DcxSMRebootAction_Type(Integer32):
    """Custom type dcxSMRebootAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nil", 1),
          ("rebootNow", 2))
    )


_DcxSMRebootAction_Type.__name__ = "Integer32"
_DcxSMRebootAction_Object = MibScalar
dcxSMRebootAction = _DcxSMRebootAction_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 7),
    _DcxSMRebootAction_Type()
)
dcxSMRebootAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMRebootAction.setStatus("current")
_DcxSMConfigFileBootGroup_ObjectIdentity = ObjectIdentity
dcxSMConfigFileBootGroup = _DcxSMConfigFileBootGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2)
)


class _DcxSMConfigFileBootDevice_Type(Integer32):
    """Custom type dcxSMConfigFileBootDevice based on Integer32"""
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
        *(("nfs", 1),
          ("tftp", 2),
          ("ftp", 3),
          ("diskAlternative", 4),
          ("diskCurrent", 5))
    )


_DcxSMConfigFileBootDevice_Type.__name__ = "Integer32"
_DcxSMConfigFileBootDevice_Object = MibScalar
dcxSMConfigFileBootDevice = _DcxSMConfigFileBootDevice_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2, 1),
    _DcxSMConfigFileBootDevice_Type()
)
dcxSMConfigFileBootDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMConfigFileBootDevice.setStatus("current")
_DcxSMConfigFileBootHostname_Type = IpAddress
_DcxSMConfigFileBootHostname_Object = MibScalar
dcxSMConfigFileBootHostname = _DcxSMConfigFileBootHostname_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2, 2),
    _DcxSMConfigFileBootHostname_Type()
)
dcxSMConfigFileBootHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMConfigFileBootHostname.setStatus("current")


class _DcxSMConfigFileBootUsername_Type(OctetString):
    """Custom type dcxSMConfigFileBootUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcxSMConfigFileBootUsername_Type.__name__ = "OctetString"
_DcxSMConfigFileBootUsername_Object = MibScalar
dcxSMConfigFileBootUsername = _DcxSMConfigFileBootUsername_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2, 3),
    _DcxSMConfigFileBootUsername_Type()
)
dcxSMConfigFileBootUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMConfigFileBootUsername.setStatus("current")


class _DcxSMConfigFileBootPassword_Type(OctetString):
    """Custom type dcxSMConfigFileBootPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcxSMConfigFileBootPassword_Type.__name__ = "OctetString"
_DcxSMConfigFileBootPassword_Object = MibScalar
dcxSMConfigFileBootPassword = _DcxSMConfigFileBootPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2, 4),
    _DcxSMConfigFileBootPassword_Type()
)
dcxSMConfigFileBootPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMConfigFileBootPassword.setStatus("current")


class _DcxSMConfigFileBootPath_Type(OctetString):
    """Custom type dcxSMConfigFileBootPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DcxSMConfigFileBootPath_Type.__name__ = "OctetString"
_DcxSMConfigFileBootPath_Object = MibScalar
dcxSMConfigFileBootPath = _DcxSMConfigFileBootPath_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2, 5),
    _DcxSMConfigFileBootPath_Type()
)
dcxSMConfigFileBootPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMConfigFileBootPath.setStatus("current")
_DcxSMDownloadGroup_ObjectIdentity = ObjectIdentity
dcxSMDownloadGroup = _DcxSMDownloadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3)
)


class _DcxSMDownloadDevice_Type(Integer32):
    """Custom type dcxSMDownloadDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nfs", 1),
          ("tftp", 2),
          ("ftp", 3))
    )


_DcxSMDownloadDevice_Type.__name__ = "Integer32"
_DcxSMDownloadDevice_Object = MibScalar
dcxSMDownloadDevice = _DcxSMDownloadDevice_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 1),
    _DcxSMDownloadDevice_Type()
)
dcxSMDownloadDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMDownloadDevice.setStatus("current")
_DcxSMDownloadHostname_Type = IpAddress
_DcxSMDownloadHostname_Object = MibScalar
dcxSMDownloadHostname = _DcxSMDownloadHostname_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 2),
    _DcxSMDownloadHostname_Type()
)
dcxSMDownloadHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMDownloadHostname.setStatus("current")


class _DcxSMDownloadUsername_Type(OctetString):
    """Custom type dcxSMDownloadUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcxSMDownloadUsername_Type.__name__ = "OctetString"
_DcxSMDownloadUsername_Object = MibScalar
dcxSMDownloadUsername = _DcxSMDownloadUsername_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 3),
    _DcxSMDownloadUsername_Type()
)
dcxSMDownloadUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMDownloadUsername.setStatus("current")


class _DcxSMDownloadPassword_Type(OctetString):
    """Custom type dcxSMDownloadPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcxSMDownloadPassword_Type.__name__ = "OctetString"
_DcxSMDownloadPassword_Object = MibScalar
dcxSMDownloadPassword = _DcxSMDownloadPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 4),
    _DcxSMDownloadPassword_Type()
)
dcxSMDownloadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMDownloadPassword.setStatus("current")


class _DcxSMDownloadPath_Type(OctetString):
    """Custom type dcxSMDownloadPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DcxSMDownloadPath_Type.__name__ = "OctetString"
_DcxSMDownloadPath_Object = MibScalar
dcxSMDownloadPath = _DcxSMDownloadPath_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 5),
    _DcxSMDownloadPath_Type()
)
dcxSMDownloadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMDownloadPath.setStatus("current")


class _DcxSMDownloadControl_Type(Integer32):
    """Custom type dcxSMDownloadControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("abort", 2))
    )


_DcxSMDownloadControl_Type.__name__ = "Integer32"
_DcxSMDownloadControl_Object = MibScalar
dcxSMDownloadControl = _DcxSMDownloadControl_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 6),
    _DcxSMDownloadControl_Type()
)
dcxSMDownloadControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMDownloadControl.setStatus("current")


class _DcxSMDownloadStatus_Type(Integer32):
    """Custom type dcxSMDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inprogress", 2),
          ("finished", 3))
    )


_DcxSMDownloadStatus_Type.__name__ = "Integer32"
_DcxSMDownloadStatus_Object = MibScalar
dcxSMDownloadStatus = _DcxSMDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 7),
    _DcxSMDownloadStatus_Type()
)
dcxSMDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxSMDownloadStatus.setStatus("current")
_DcxSMTrapGroup_ObjectIdentity = ObjectIdentity
dcxSMTrapGroup = _DcxSMTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4)
)
_DcxSMConfigFileGroup_ObjectIdentity = ObjectIdentity
dcxSMConfigFileGroup = _DcxSMConfigFileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5)
)
_DcxSMConfigFileTable_Object = MibTable
dcxSMConfigFileTable = _DcxSMConfigFileTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dcxSMConfigFileTable.setStatus("current")
_DcxSMConfigFileEntry_Object = MibTableRow
dcxSMConfigFileEntry = _DcxSMConfigFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1)
)
dcxSMConfigFileEntry.setIndexNames(
    (0, "ARRIS-C3-SM-MIB", "dcxSMConfigFileIndex"),
)
if mibBuilder.loadTexts:
    dcxSMConfigFileEntry.setStatus("current")


class _DcxSMConfigFileIndex_Type(Unsigned32):
    """Custom type dcxSMConfigFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_DcxSMConfigFileIndex_Type.__name__ = "Unsigned32"
_DcxSMConfigFileIndex_Object = MibTableColumn
dcxSMConfigFileIndex = _DcxSMConfigFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 1),
    _DcxSMConfigFileIndex_Type()
)
dcxSMConfigFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxSMConfigFileIndex.setStatus("current")
_DcxSMConfigFileDate_Type = DateAndTime
_DcxSMConfigFileDate_Object = MibTableColumn
dcxSMConfigFileDate = _DcxSMConfigFileDate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 2),
    _DcxSMConfigFileDate_Type()
)
dcxSMConfigFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxSMConfigFileDate.setStatus("current")


class _DcxSMConfigFileDesc_Type(OctetString):
    """Custom type dcxSMConfigFileDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DcxSMConfigFileDesc_Type.__name__ = "OctetString"
_DcxSMConfigFileDesc_Object = MibTableColumn
dcxSMConfigFileDesc = _DcxSMConfigFileDesc_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 3),
    _DcxSMConfigFileDesc_Type()
)
dcxSMConfigFileDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMConfigFileDesc.setStatus("current")
_DcxSMConfigFileChecksum_Type = Integer32
_DcxSMConfigFileChecksum_Object = MibTableColumn
dcxSMConfigFileChecksum = _DcxSMConfigFileChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 4),
    _DcxSMConfigFileChecksum_Type()
)
dcxSMConfigFileChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxSMConfigFileChecksum.setStatus("current")
_DcxSMConfigFileSize_Type = Integer32
_DcxSMConfigFileSize_Object = MibTableColumn
dcxSMConfigFileSize = _DcxSMConfigFileSize_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 5),
    _DcxSMConfigFileSize_Type()
)
dcxSMConfigFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxSMConfigFileSize.setStatus("current")


class _DcxSMConfigFileStatus_Type(Integer32):
    """Custom type dcxSMConfigFileStatus based on Integer32"""
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
        *(("curconfig", 1),
          ("alt", 2),
          ("inactive", 3),
          ("deleted", 4))
    )


_DcxSMConfigFileStatus_Type.__name__ = "Integer32"
_DcxSMConfigFileStatus_Object = MibTableColumn
dcxSMConfigFileStatus = _DcxSMConfigFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 6),
    _DcxSMConfigFileStatus_Type()
)
dcxSMConfigFileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMConfigFileStatus.setStatus("current")
_DcxSMSoftwareListGroup_ObjectIdentity = ObjectIdentity
dcxSMSoftwareListGroup = _DcxSMSoftwareListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6)
)
_DcxSMSoftwareListTable_Object = MibTable
dcxSMSoftwareListTable = _DcxSMSoftwareListTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dcxSMSoftwareListTable.setStatus("current")
_DcxSMSoftwareListEntry_Object = MibTableRow
dcxSMSoftwareListEntry = _DcxSMSoftwareListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1)
)
dcxSMSoftwareListEntry.setIndexNames(
    (0, "ARRIS-C3-SM-MIB", "dcxSMSoftwareIndex"),
)
if mibBuilder.loadTexts:
    dcxSMSoftwareListEntry.setStatus("current")


class _DcxSMSoftwareIndex_Type(Unsigned32):
    """Custom type dcxSMSoftwareIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_DcxSMSoftwareIndex_Type.__name__ = "Unsigned32"
_DcxSMSoftwareIndex_Object = MibTableColumn
dcxSMSoftwareIndex = _DcxSMSoftwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 1),
    _DcxSMSoftwareIndex_Type()
)
dcxSMSoftwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxSMSoftwareIndex.setStatus("current")


class _DcxSMSoftwareVersion_Type(OctetString):
    """Custom type dcxSMSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcxSMSoftwareVersion_Type.__name__ = "OctetString"
_DcxSMSoftwareVersion_Object = MibTableColumn
dcxSMSoftwareVersion = _DcxSMSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 2),
    _DcxSMSoftwareVersion_Type()
)
dcxSMSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxSMSoftwareVersion.setStatus("current")
_DcxSMSoftwareDate_Type = DateAndTime
_DcxSMSoftwareDate_Object = MibTableColumn
dcxSMSoftwareDate = _DcxSMSoftwareDate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 3),
    _DcxSMSoftwareDate_Type()
)
dcxSMSoftwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxSMSoftwareDate.setStatus("current")


class _DcxSMSoftwareDesc_Type(OctetString):
    """Custom type dcxSMSoftwareDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DcxSMSoftwareDesc_Type.__name__ = "OctetString"
_DcxSMSoftwareDesc_Object = MibTableColumn
dcxSMSoftwareDesc = _DcxSMSoftwareDesc_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 4),
    _DcxSMSoftwareDesc_Type()
)
dcxSMSoftwareDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMSoftwareDesc.setStatus("current")
_DcxSMSoftwareChecksum_Type = Integer32
_DcxSMSoftwareChecksum_Object = MibTableColumn
dcxSMSoftwareChecksum = _DcxSMSoftwareChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 5),
    _DcxSMSoftwareChecksum_Type()
)
dcxSMSoftwareChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxSMSoftwareChecksum.setStatus("current")
_DcxSMSoftwareSize_Type = Integer32
_DcxSMSoftwareSize_Object = MibTableColumn
dcxSMSoftwareSize = _DcxSMSoftwareSize_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 6),
    _DcxSMSoftwareSize_Type()
)
dcxSMSoftwareSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxSMSoftwareSize.setStatus("current")


class _DcxSMSoftwareStatus_Type(Integer32):
    """Custom type dcxSMSoftwareStatus based on Integer32"""
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
        *(("curimage", 1),
          ("alt", 2),
          ("inactive", 3),
          ("deleted", 4))
    )


_DcxSMSoftwareStatus_Type.__name__ = "Integer32"
_DcxSMSoftwareStatus_Object = MibTableColumn
dcxSMSoftwareStatus = _DcxSMSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 7),
    _DcxSMSoftwareStatus_Type()
)
dcxSMSoftwareStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMSoftwareStatus.setStatus("current")
_DcxSMMiscUserManagementGroup_ObjectIdentity = ObjectIdentity
dcxSMMiscUserManagementGroup = _DcxSMMiscUserManagementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7)
)
_DcxSMMiscUserTable_Object = MibTable
dcxSMMiscUserTable = _DcxSMMiscUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    dcxSMMiscUserTable.setStatus("current")
_DcxSMMiscUserListEntry_Object = MibTableRow
dcxSMMiscUserListEntry = _DcxSMMiscUserListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1)
)
dcxSMMiscUserListEntry.setIndexNames(
    (0, "ARRIS-C3-SM-MIB", "dcxSMMiscUserIndex"),
)
if mibBuilder.loadTexts:
    dcxSMMiscUserListEntry.setStatus("current")


class _DcxSMMiscUserIndex_Type(Unsigned32):
    """Custom type dcxSMMiscUserIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DcxSMMiscUserIndex_Type.__name__ = "Unsigned32"
_DcxSMMiscUserIndex_Object = MibTableColumn
dcxSMMiscUserIndex = _DcxSMMiscUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 1),
    _DcxSMMiscUserIndex_Type()
)
dcxSMMiscUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxSMMiscUserIndex.setStatus("current")


class _DcxSMMiscUserLoginName_Type(OctetString):
    """Custom type dcxSMMiscUserLoginName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcxSMMiscUserLoginName_Type.__name__ = "OctetString"
_DcxSMMiscUserLoginName_Object = MibTableColumn
dcxSMMiscUserLoginName = _DcxSMMiscUserLoginName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 2),
    _DcxSMMiscUserLoginName_Type()
)
dcxSMMiscUserLoginName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMMiscUserLoginName.setStatus("current")


class _DcxSMMiscUserLoginPwd_Type(OctetString):
    """Custom type dcxSMMiscUserLoginPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcxSMMiscUserLoginPwd_Type.__name__ = "OctetString"
_DcxSMMiscUserLoginPwd_Object = MibTableColumn
dcxSMMiscUserLoginPwd = _DcxSMMiscUserLoginPwd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 3),
    _DcxSMMiscUserLoginPwd_Type()
)
dcxSMMiscUserLoginPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMMiscUserLoginPwd.setStatus("current")


class _DcxSMMiscUserEnablePwd_Type(OctetString):
    """Custom type dcxSMMiscUserEnablePwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcxSMMiscUserEnablePwd_Type.__name__ = "OctetString"
_DcxSMMiscUserEnablePwd_Object = MibTableColumn
dcxSMMiscUserEnablePwd = _DcxSMMiscUserEnablePwd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 4),
    _DcxSMMiscUserEnablePwd_Type()
)
dcxSMMiscUserEnablePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMMiscUserEnablePwd.setStatus("current")


class _DcxSMMiscUserEnableSecretePwd_Type(OctetString):
    """Custom type dcxSMMiscUserEnableSecretePwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcxSMMiscUserEnableSecretePwd_Type.__name__ = "OctetString"
_DcxSMMiscUserEnableSecretePwd_Object = MibTableColumn
dcxSMMiscUserEnableSecretePwd = _DcxSMMiscUserEnableSecretePwd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 5),
    _DcxSMMiscUserEnableSecretePwd_Type()
)
dcxSMMiscUserEnableSecretePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMMiscUserEnableSecretePwd.setStatus("current")


class _DcxSMMiscUserWorkMode_Type(Integer32):
    """Custom type dcxSMMiscUserWorkMode based on Integer32"""
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
        *(("usermode", 1),
          ("priviledgedmode", 2),
          ("globalconfiguremode", 3),
          ("lineconfmode", 4),
          ("ethernetconfmode", 5),
          ("cableconfmode", 6))
    )


_DcxSMMiscUserWorkMode_Type.__name__ = "Integer32"
_DcxSMMiscUserWorkMode_Object = MibTableColumn
dcxSMMiscUserWorkMode = _DcxSMMiscUserWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 6),
    _DcxSMMiscUserWorkMode_Type()
)
dcxSMMiscUserWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxSMMiscUserWorkMode.setStatus("current")
_DcxIpdrGroup_ObjectIdentity = ObjectIdentity
dcxIpdrGroup = _DcxIpdrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 8)
)
_DcxIpdrEnable_Type = TruthValue
_DcxIpdrEnable_Object = MibScalar
dcxIpdrEnable = _DcxIpdrEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 8, 1),
    _DcxIpdrEnable_Type()
)
dcxIpdrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxIpdrEnable.setStatus("current")


class _DcxIpdrFileName_Type(OctetString):
    """Custom type dcxIpdrFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_DcxIpdrFileName_Type.__name__ = "OctetString"
_DcxIpdrFileName_Object = MibScalar
dcxIpdrFileName = _DcxIpdrFileName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 8, 2),
    _DcxIpdrFileName_Type()
)
dcxIpdrFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxIpdrFileName.setStatus("current")


class _DcxIpdrUserLoginName_Type(OctetString):
    """Custom type dcxIpdrUserLoginName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 31),
    )


_DcxIpdrUserLoginName_Type.__name__ = "OctetString"
_DcxIpdrUserLoginName_Object = MibScalar
dcxIpdrUserLoginName = _DcxIpdrUserLoginName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 8, 3),
    _DcxIpdrUserLoginName_Type()
)
dcxIpdrUserLoginName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxIpdrUserLoginName.setStatus("current")


class _DcxIpdrUserLoginPwd_Type(OctetString):
    """Custom type dcxIpdrUserLoginPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 31),
    )


_DcxIpdrUserLoginPwd_Type.__name__ = "OctetString"
_DcxIpdrUserLoginPwd_Object = MibScalar
dcxIpdrUserLoginPwd = _DcxIpdrUserLoginPwd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 8, 4),
    _DcxIpdrUserLoginPwd_Type()
)
dcxIpdrUserLoginPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxIpdrUserLoginPwd.setStatus("current")
_DcxDxmObjects_ObjectIdentity = ObjectIdentity
dcxDxmObjects = _DcxDxmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2)
)
_DcxDxmStatusGroup_ObjectIdentity = ObjectIdentity
dcxDxmStatusGroup = _DcxDxmStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1)
)
_DcxDxmStatusIpAddress_Type = IpAddress
_DcxDxmStatusIpAddress_Object = MibScalar
dcxDxmStatusIpAddress = _DcxDxmStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 1),
    _DcxDxmStatusIpAddress_Type()
)
dcxDxmStatusIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxDxmStatusIpAddress.setStatus("current")
_DcxDxmStatusPort_Type = Unsigned32
_DcxDxmStatusPort_Object = MibScalar
dcxDxmStatusPort = _DcxDxmStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 2),
    _DcxDxmStatusPort_Type()
)
dcxDxmStatusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxDxmStatusPort.setStatus("current")
_DcxDxmStatusEnable_Type = TruthValue
_DcxDxmStatusEnable_Object = MibScalar
dcxDxmStatusEnable = _DcxDxmStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 3),
    _DcxDxmStatusEnable_Type()
)
dcxDxmStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxDxmStatusEnable.setStatus("current")


class _DcxDxmStatusCmtsId_Type(Integer32):
    """Custom type dcxDxmStatusCmtsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_DcxDxmStatusCmtsId_Type.__name__ = "Integer32"
_DcxDxmStatusCmtsId_Object = MibScalar
dcxDxmStatusCmtsId = _DcxDxmStatusCmtsId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 4),
    _DcxDxmStatusCmtsId_Type()
)
dcxDxmStatusCmtsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxDxmStatusCmtsId.setStatus("current")


class _DcxDxmStatusRole_Type(Integer32):
    """Custom type dcxDxmStatusRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("primary", 2),
          ("standby", 3))
    )


_DcxDxmStatusRole_Type.__name__ = "Integer32"
_DcxDxmStatusRole_Object = MibScalar
dcxDxmStatusRole = _DcxDxmStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 5),
    _DcxDxmStatusRole_Type()
)
dcxDxmStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxDxmStatusRole.setStatus("current")


class _DcxDxmStatusState_Type(Integer32):
    """Custom type dcxDxmStatusState based on Integer32"""
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
        *(("standalone", 1),
          ("active", 2),
          ("inactive", 3),
          ("passive", 4),
          ("restored", 5),
          ("failed", 6),
          ("replacement", 7),
          ("restoring", 8))
    )


_DcxDxmStatusState_Type.__name__ = "Integer32"
_DcxDxmStatusState_Object = MibScalar
dcxDxmStatusState = _DcxDxmStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 6),
    _DcxDxmStatusState_Type()
)
dcxDxmStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxDxmStatusState.setStatus("current")
_DcxDxmStatusLastConfigRetrieval_Type = DateAndTime
_DcxDxmStatusLastConfigRetrieval_Object = MibScalar
dcxDxmStatusLastConfigRetrieval = _DcxDxmStatusLastConfigRetrieval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 7),
    _DcxDxmStatusLastConfigRetrieval_Type()
)
dcxDxmStatusLastConfigRetrieval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxDxmStatusLastConfigRetrieval.setStatus("current")
_DcxDxmStatusLastConfigChange_Type = DateAndTime
_DcxDxmStatusLastConfigChange_Object = MibScalar
dcxDxmStatusLastConfigChange = _DcxDxmStatusLastConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 8),
    _DcxDxmStatusLastConfigChange_Type()
)
dcxDxmStatusLastConfigChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxDxmStatusLastConfigChange.setStatus("current")
_DcxDxmStatusConfigRetrievalCount_Type = Unsigned32
_DcxDxmStatusConfigRetrievalCount_Object = MibScalar
dcxDxmStatusConfigRetrievalCount = _DcxDxmStatusConfigRetrievalCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 9),
    _DcxDxmStatusConfigRetrievalCount_Type()
)
dcxDxmStatusConfigRetrievalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxDxmStatusConfigRetrievalCount.setStatus("current")
_DcxDxmStatusHeartbeatCount_Type = Unsigned32
_DcxDxmStatusHeartbeatCount_Object = MibScalar
dcxDxmStatusHeartbeatCount = _DcxDxmStatusHeartbeatCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 10),
    _DcxDxmStatusHeartbeatCount_Type()
)
dcxDxmStatusHeartbeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxDxmStatusHeartbeatCount.setStatus("current")
_DcxDxmStatusNotifAddCmCount_Type = Unsigned32
_DcxDxmStatusNotifAddCmCount_Object = MibScalar
dcxDxmStatusNotifAddCmCount = _DcxDxmStatusNotifAddCmCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 11),
    _DcxDxmStatusNotifAddCmCount_Type()
)
dcxDxmStatusNotifAddCmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxDxmStatusNotifAddCmCount.setStatus("current")
_DcxDxmStatusNotifDelCmCount_Type = Unsigned32
_DcxDxmStatusNotifDelCmCount_Object = MibScalar
dcxDxmStatusNotifDelCmCount = _DcxDxmStatusNotifDelCmCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 12),
    _DcxDxmStatusNotifDelCmCount_Type()
)
dcxDxmStatusNotifDelCmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxDxmStatusNotifDelCmCount.setStatus("current")
_DcxDxmStatusNotifAddCpeCount_Type = Unsigned32
_DcxDxmStatusNotifAddCpeCount_Object = MibScalar
dcxDxmStatusNotifAddCpeCount = _DcxDxmStatusNotifAddCpeCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 13),
    _DcxDxmStatusNotifAddCpeCount_Type()
)
dcxDxmStatusNotifAddCpeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxDxmStatusNotifAddCpeCount.setStatus("current")
_DcxDxmStatusNotifDelCpeCount_Type = Unsigned32
_DcxDxmStatusNotifDelCpeCount_Object = MibScalar
dcxDxmStatusNotifDelCpeCount = _DcxDxmStatusNotifDelCpeCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 14),
    _DcxDxmStatusNotifDelCpeCount_Type()
)
dcxDxmStatusNotifDelCpeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxDxmStatusNotifDelCpeCount.setStatus("current")

# Managed Objects groups


# Notification objects

dcxSMDiskInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 1)
)
dcxSMDiskInserted.setObjects(
    ("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion")
)
if mibBuilder.loadTexts:
    dcxSMDiskInserted.setStatus(
        "current"
    )

dcxSMDiskRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 2)
)
dcxSMDiskRemoved.setObjects(
    ("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion")
)
if mibBuilder.loadTexts:
    dcxSMDiskRemoved.setStatus(
        "current"
    )

dcxSMDiskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 3)
)
dcxSMDiskFailed.setObjects(
    ("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion")
)
if mibBuilder.loadTexts:
    dcxSMDiskFailed.setStatus(
        "current"
    )

dcxSMConfigChecksumChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 4)
)
dcxSMConfigChecksumChanged.setObjects(
    ("ARRIS-C3-SM-MIB", "dcxSMConfigFileDesc")
)
if mibBuilder.loadTexts:
    dcxSMConfigChecksumChanged.setStatus(
        "current"
    )

dcxSMImageChecksumChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 5)
)
dcxSMImageChecksumChanged.setObjects(
    ("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion")
)
if mibBuilder.loadTexts:
    dcxSMImageChecksumChanged.setStatus(
        "current"
    )

dcxSMImageDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 6)
)
dcxSMImageDownloadFailed.setObjects(
    ("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion")
)
if mibBuilder.loadTexts:
    dcxSMImageDownloadFailed.setStatus(
        "current"
    )

dcxSMImageBootFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 7)
)
dcxSMImageBootFailed.setObjects(
    ("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion")
)
if mibBuilder.loadTexts:
    dcxSMImageBootFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-C3-SM-MIB",
    **{"cmtsC3SMMIB": cmtsC3SMMIB,
       "dcxSMObjects": dcxSMObjects,
       "dcxSMBootGroup": dcxSMBootGroup,
       "dcxSMBootDevice": dcxSMBootDevice,
       "dcxSMBootHostname": dcxSMBootHostname,
       "dcxSMBootUsername": dcxSMBootUsername,
       "dcxSMBootPassword": dcxSMBootPassword,
       "dcxSMBootPath": dcxSMBootPath,
       "dcxSMEnetMgmtInterface": dcxSMEnetMgmtInterface,
       "dcxSMRebootAction": dcxSMRebootAction,
       "dcxSMConfigFileBootGroup": dcxSMConfigFileBootGroup,
       "dcxSMConfigFileBootDevice": dcxSMConfigFileBootDevice,
       "dcxSMConfigFileBootHostname": dcxSMConfigFileBootHostname,
       "dcxSMConfigFileBootUsername": dcxSMConfigFileBootUsername,
       "dcxSMConfigFileBootPassword": dcxSMConfigFileBootPassword,
       "dcxSMConfigFileBootPath": dcxSMConfigFileBootPath,
       "dcxSMDownloadGroup": dcxSMDownloadGroup,
       "dcxSMDownloadDevice": dcxSMDownloadDevice,
       "dcxSMDownloadHostname": dcxSMDownloadHostname,
       "dcxSMDownloadUsername": dcxSMDownloadUsername,
       "dcxSMDownloadPassword": dcxSMDownloadPassword,
       "dcxSMDownloadPath": dcxSMDownloadPath,
       "dcxSMDownloadControl": dcxSMDownloadControl,
       "dcxSMDownloadStatus": dcxSMDownloadStatus,
       "dcxSMTrapGroup": dcxSMTrapGroup,
       "dcxSMDiskInserted": dcxSMDiskInserted,
       "dcxSMDiskRemoved": dcxSMDiskRemoved,
       "dcxSMDiskFailed": dcxSMDiskFailed,
       "dcxSMConfigChecksumChanged": dcxSMConfigChecksumChanged,
       "dcxSMImageChecksumChanged": dcxSMImageChecksumChanged,
       "dcxSMImageDownloadFailed": dcxSMImageDownloadFailed,
       "dcxSMImageBootFailed": dcxSMImageBootFailed,
       "dcxSMConfigFileGroup": dcxSMConfigFileGroup,
       "dcxSMConfigFileTable": dcxSMConfigFileTable,
       "dcxSMConfigFileEntry": dcxSMConfigFileEntry,
       "dcxSMConfigFileIndex": dcxSMConfigFileIndex,
       "dcxSMConfigFileDate": dcxSMConfigFileDate,
       "dcxSMConfigFileDesc": dcxSMConfigFileDesc,
       "dcxSMConfigFileChecksum": dcxSMConfigFileChecksum,
       "dcxSMConfigFileSize": dcxSMConfigFileSize,
       "dcxSMConfigFileStatus": dcxSMConfigFileStatus,
       "dcxSMSoftwareListGroup": dcxSMSoftwareListGroup,
       "dcxSMSoftwareListTable": dcxSMSoftwareListTable,
       "dcxSMSoftwareListEntry": dcxSMSoftwareListEntry,
       "dcxSMSoftwareIndex": dcxSMSoftwareIndex,
       "dcxSMSoftwareVersion": dcxSMSoftwareVersion,
       "dcxSMSoftwareDate": dcxSMSoftwareDate,
       "dcxSMSoftwareDesc": dcxSMSoftwareDesc,
       "dcxSMSoftwareChecksum": dcxSMSoftwareChecksum,
       "dcxSMSoftwareSize": dcxSMSoftwareSize,
       "dcxSMSoftwareStatus": dcxSMSoftwareStatus,
       "dcxSMMiscUserManagementGroup": dcxSMMiscUserManagementGroup,
       "dcxSMMiscUserTable": dcxSMMiscUserTable,
       "dcxSMMiscUserListEntry": dcxSMMiscUserListEntry,
       "dcxSMMiscUserIndex": dcxSMMiscUserIndex,
       "dcxSMMiscUserLoginName": dcxSMMiscUserLoginName,
       "dcxSMMiscUserLoginPwd": dcxSMMiscUserLoginPwd,
       "dcxSMMiscUserEnablePwd": dcxSMMiscUserEnablePwd,
       "dcxSMMiscUserEnableSecretePwd": dcxSMMiscUserEnableSecretePwd,
       "dcxSMMiscUserWorkMode": dcxSMMiscUserWorkMode,
       "dcxIpdrGroup": dcxIpdrGroup,
       "dcxIpdrEnable": dcxIpdrEnable,
       "dcxIpdrFileName": dcxIpdrFileName,
       "dcxIpdrUserLoginName": dcxIpdrUserLoginName,
       "dcxIpdrUserLoginPwd": dcxIpdrUserLoginPwd,
       "dcxDxmObjects": dcxDxmObjects,
       "dcxDxmStatusGroup": dcxDxmStatusGroup,
       "dcxDxmStatusIpAddress": dcxDxmStatusIpAddress,
       "dcxDxmStatusPort": dcxDxmStatusPort,
       "dcxDxmStatusEnable": dcxDxmStatusEnable,
       "dcxDxmStatusCmtsId": dcxDxmStatusCmtsId,
       "dcxDxmStatusRole": dcxDxmStatusRole,
       "dcxDxmStatusState": dcxDxmStatusState,
       "dcxDxmStatusLastConfigRetrieval": dcxDxmStatusLastConfigRetrieval,
       "dcxDxmStatusLastConfigChange": dcxDxmStatusLastConfigChange,
       "dcxDxmStatusConfigRetrievalCount": dcxDxmStatusConfigRetrievalCount,
       "dcxDxmStatusHeartbeatCount": dcxDxmStatusHeartbeatCount,
       "dcxDxmStatusNotifAddCmCount": dcxDxmStatusNotifAddCmCount,
       "dcxDxmStatusNotifDelCmCount": dcxDxmStatusNotifDelCmCount,
       "dcxDxmStatusNotifAddCpeCount": dcxDxmStatusNotifAddCpeCount,
       "dcxDxmStatusNotifDelCpeCount": dcxDxmStatusNotifDelCpeCount}
)
