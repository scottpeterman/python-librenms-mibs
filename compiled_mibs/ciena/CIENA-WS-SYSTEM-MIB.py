# SNMP MIB module (CIENA-WS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:16 2025
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

(EnabledDisabledEnum,
 StringMaxl128,
 StringMaxl16,
 StringMaxl256,
 StringMaxl32,
 StringMaxl64) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "EnabledDisabledEnum",
    "StringMaxl128",
    "StringMaxl16",
    "StringMaxl256",
    "StringMaxl32",
    "StringMaxl64")

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

cienaWsSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12)
)
if mibBuilder.loadTexts:
    cienaWsSystemMIB.setRevisions(
        ("2017-07-26 00:00",
         "2017-02-28 00:00",
         "2016-12-12 00:00",
         "2016-06-14 00:00",
         "2016-04-06 00:00",
         "2015-06-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BandplanEnum(TextualConvention, Integer32):
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
          ("flex12", 1),
          ("fixed44", 2),
          ("fixed88", 3),
          ("fixed96", 4))
    )



class Decimal32Len2(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4320000, 5040000),
    )



class Decimal32Len5(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-5"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-18000000, 18000000),
    )



class LampModeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("flash", 0)
    )



class LampTargetTypeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 1),
          ("port", 2))
    )



class LineProtectionEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unprotected", 0),
          ("trunkOps", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CienaWsSystemObjects_ObjectIdentity = ObjectIdentity
cienaWsSystemObjects = _CienaWsSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 1)
)
_CienaWsSystemConformance_ObjectIdentity = ObjectIdentity
cienaWsSystemConformance = _CienaWsSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 2)
)
_CienaWsSystemGroups_ObjectIdentity = ObjectIdentity
cienaWsSystemGroups = _CienaWsSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 2, 1)
)
_CienaWsSystemCompliances_ObjectIdentity = ObjectIdentity
cienaWsSystemCompliances = _CienaWsSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 2, 2)
)
_CwsSystemSiteTable_Object = MibTable
cwsSystemSiteTable = _CwsSystemSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 3)
)
if mibBuilder.loadTexts:
    cwsSystemSiteTable.setStatus("current")
_CwsSystemSiteEntry_Object = MibTableRow
cwsSystemSiteEntry = _CwsSystemSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 3, 1)
)
cwsSystemSiteEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemSiteTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemSiteEntry.setStatus("current")


class _CwsSystemSiteTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemSiteTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemSiteTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemSiteTableSnmpKey_Object = MibTableColumn
cwsSystemSiteTableSnmpKey = _CwsSystemSiteTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 3, 1, 1),
    _CwsSystemSiteTableSnmpKey_Type()
)
cwsSystemSiteTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemSiteTableSnmpKey.setStatus("current")
_CwsSystemSiteId_Type = Unsigned32
_CwsSystemSiteId_Object = MibTableColumn
cwsSystemSiteId = _CwsSystemSiteId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 3, 1, 2),
    _CwsSystemSiteId_Type()
)
cwsSystemSiteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemSiteId.setStatus("current")


class _CwsSystemSiteName_Type(OctetString):
    """Custom type cwsSystemSiteName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CwsSystemSiteName_Type.__name__ = "OctetString"
_CwsSystemSiteName_Object = MibTableColumn
cwsSystemSiteName = _CwsSystemSiteName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 3, 1, 3),
    _CwsSystemSiteName_Type()
)
cwsSystemSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemSiteName.setStatus("current")


class _CwsSystemSiteDescription_Type(OctetString):
    """Custom type cwsSystemSiteDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CwsSystemSiteDescription_Type.__name__ = "OctetString"
_CwsSystemSiteDescription_Object = MibTableColumn
cwsSystemSiteDescription = _CwsSystemSiteDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 3, 1, 4),
    _CwsSystemSiteDescription_Type()
)
cwsSystemSiteDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemSiteDescription.setStatus("current")
_CwsSystemSiteLatitude_Type = Decimal32Len5
_CwsSystemSiteLatitude_Object = MibTableColumn
cwsSystemSiteLatitude = _CwsSystemSiteLatitude_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 3, 1, 5),
    _CwsSystemSiteLatitude_Type()
)
cwsSystemSiteLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemSiteLatitude.setStatus("current")
_CwsSystemSiteLongitude_Type = Decimal32Len5
_CwsSystemSiteLongitude_Object = MibTableColumn
cwsSystemSiteLongitude = _CwsSystemSiteLongitude_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 3, 1, 6),
    _CwsSystemSiteLongitude_Type()
)
cwsSystemSiteLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemSiteLongitude.setStatus("current")


class _CwsSystemSiteAddress_Type(OctetString):
    """Custom type cwsSystemSiteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CwsSystemSiteAddress_Type.__name__ = "OctetString"
_CwsSystemSiteAddress_Object = MibTableColumn
cwsSystemSiteAddress = _CwsSystemSiteAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 3, 1, 7),
    _CwsSystemSiteAddress_Type()
)
cwsSystemSiteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemSiteAddress.setStatus("current")
_CwsSystemGroupTable_Object = MibTable
cwsSystemGroupTable = _CwsSystemGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 4)
)
if mibBuilder.loadTexts:
    cwsSystemGroupTable.setStatus("current")
_CwsSystemGroupEntry_Object = MibTableRow
cwsSystemGroupEntry = _CwsSystemGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 4, 1)
)
cwsSystemGroupEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemGroupTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemGroupEntry.setStatus("current")


class _CwsSystemGroupTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemGroupTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemGroupTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemGroupTableSnmpKey_Object = MibTableColumn
cwsSystemGroupTableSnmpKey = _CwsSystemGroupTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 4, 1, 1),
    _CwsSystemGroupTableSnmpKey_Type()
)
cwsSystemGroupTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemGroupTableSnmpKey.setStatus("current")
_CwsSystemGroupId_Type = Unsigned32
_CwsSystemGroupId_Object = MibTableColumn
cwsSystemGroupId = _CwsSystemGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 4, 1, 2),
    _CwsSystemGroupId_Type()
)
cwsSystemGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemGroupId.setStatus("current")


class _CwsSystemGroupName_Type(OctetString):
    """Custom type cwsSystemGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CwsSystemGroupName_Type.__name__ = "OctetString"
_CwsSystemGroupName_Object = MibTableColumn
cwsSystemGroupName = _CwsSystemGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 4, 1, 3),
    _CwsSystemGroupName_Type()
)
cwsSystemGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemGroupName.setStatus("current")


class _CwsSystemGroupDescription_Type(OctetString):
    """Custom type cwsSystemGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CwsSystemGroupDescription_Type.__name__ = "OctetString"
_CwsSystemGroupDescription_Object = MibTableColumn
cwsSystemGroupDescription = _CwsSystemGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 4, 1, 4),
    _CwsSystemGroupDescription_Type()
)
cwsSystemGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemGroupDescription.setStatus("current")
_CwsSystemMemberTable_Object = MibTable
cwsSystemMemberTable = _CwsSystemMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 5)
)
if mibBuilder.loadTexts:
    cwsSystemMemberTable.setStatus("current")
_CwsSystemMemberEntry_Object = MibTableRow
cwsSystemMemberEntry = _CwsSystemMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 5, 1)
)
cwsSystemMemberEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemMemberTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemMemberEntry.setStatus("current")


class _CwsSystemMemberTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemMemberTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemMemberTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemMemberTableSnmpKey_Object = MibTableColumn
cwsSystemMemberTableSnmpKey = _CwsSystemMemberTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 5, 1, 1),
    _CwsSystemMemberTableSnmpKey_Type()
)
cwsSystemMemberTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemMemberTableSnmpKey.setStatus("current")
_CwsSystemMemberId_Type = Unsigned32
_CwsSystemMemberId_Object = MibTableColumn
cwsSystemMemberId = _CwsSystemMemberId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 5, 1, 2),
    _CwsSystemMemberId_Type()
)
cwsSystemMemberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemMemberId.setStatus("current")


class _CwsSystemMemberName_Type(OctetString):
    """Custom type cwsSystemMemberName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CwsSystemMemberName_Type.__name__ = "OctetString"
_CwsSystemMemberName_Object = MibTableColumn
cwsSystemMemberName = _CwsSystemMemberName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 5, 1, 3),
    _CwsSystemMemberName_Type()
)
cwsSystemMemberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemMemberName.setStatus("current")


class _CwsSystemMemberDescription_Type(OctetString):
    """Custom type cwsSystemMemberDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CwsSystemMemberDescription_Type.__name__ = "OctetString"
_CwsSystemMemberDescription_Object = MibTableColumn
cwsSystemMemberDescription = _CwsSystemMemberDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 5, 1, 4),
    _CwsSystemMemberDescription_Type()
)
cwsSystemMemberDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemMemberDescription.setStatus("current")


class _CwsSystemMemberFrameIdentification_Type(OctetString):
    """Custom type cwsSystemMemberFrameIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CwsSystemMemberFrameIdentification_Type.__name__ = "OctetString"
_CwsSystemMemberFrameIdentification_Object = MibTableColumn
cwsSystemMemberFrameIdentification = _CwsSystemMemberFrameIdentification_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 5, 1, 5),
    _CwsSystemMemberFrameIdentification_Type()
)
cwsSystemMemberFrameIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemMemberFrameIdentification.setStatus("current")
_CwsSystemMemberRackUnitNumber_Type = Unsigned32
_CwsSystemMemberRackUnitNumber_Object = MibTableColumn
cwsSystemMemberRackUnitNumber = _CwsSystemMemberRackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 5, 1, 6),
    _CwsSystemMemberRackUnitNumber_Type()
)
cwsSystemMemberRackUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemMemberRackUnitNumber.setStatus("current")
_CwsSystemHostNameTable_Object = MibTable
cwsSystemHostNameTable = _CwsSystemHostNameTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 6)
)
if mibBuilder.loadTexts:
    cwsSystemHostNameTable.setStatus("current")
_CwsSystemHostNameEntry_Object = MibTableRow
cwsSystemHostNameEntry = _CwsSystemHostNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 6, 1)
)
cwsSystemHostNameEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemHostNameTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemHostNameEntry.setStatus("current")


class _CwsSystemHostNameTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemHostNameTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemHostNameTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemHostNameTableSnmpKey_Object = MibTableColumn
cwsSystemHostNameTableSnmpKey = _CwsSystemHostNameTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 6, 1, 1),
    _CwsSystemHostNameTableSnmpKey_Type()
)
cwsSystemHostNameTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemHostNameTableSnmpKey.setStatus("current")
_CwsSystemHostNameCurrentHostName_Type = StringMaxl64
_CwsSystemHostNameCurrentHostName_Object = MibTableColumn
cwsSystemHostNameCurrentHostName = _CwsSystemHostNameCurrentHostName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 6, 1, 2),
    _CwsSystemHostNameCurrentHostName_Type()
)
cwsSystemHostNameCurrentHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSystemHostNameCurrentHostName.setStatus("current")
_CwsSystemHostNameConfigHostName_Type = StringMaxl64
_CwsSystemHostNameConfigHostName_Object = MibTableColumn
cwsSystemHostNameConfigHostName = _CwsSystemHostNameConfigHostName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 6, 1, 3),
    _CwsSystemHostNameConfigHostName_Type()
)
cwsSystemHostNameConfigHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemHostNameConfigHostName.setStatus("current")
_CwsSystemHostNameDhcpHostName_Type = StringMaxl64
_CwsSystemHostNameDhcpHostName_Object = MibTableColumn
cwsSystemHostNameDhcpHostName = _CwsSystemHostNameDhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 6, 1, 4),
    _CwsSystemHostNameDhcpHostName_Type()
)
cwsSystemHostNameDhcpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSystemHostNameDhcpHostName.setStatus("current")
_CwsSystemTimeConfigTable_Object = MibTable
cwsSystemTimeConfigTable = _CwsSystemTimeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 7)
)
if mibBuilder.loadTexts:
    cwsSystemTimeConfigTable.setStatus("current")
_CwsSystemTimeConfigEntry_Object = MibTableRow
cwsSystemTimeConfigEntry = _CwsSystemTimeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 7, 1)
)
cwsSystemTimeConfigEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemTimeConfigTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemTimeConfigEntry.setStatus("current")


class _CwsSystemTimeConfigTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemTimeConfigTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemTimeConfigTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemTimeConfigTableSnmpKey_Object = MibTableColumn
cwsSystemTimeConfigTableSnmpKey = _CwsSystemTimeConfigTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 7, 1, 1),
    _CwsSystemTimeConfigTableSnmpKey_Type()
)
cwsSystemTimeConfigTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemTimeConfigTableSnmpKey.setStatus("current")


class _CwsSystemTimeConfigDate_Type(OctetString):
    """Custom type cwsSystemTimeConfigDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_CwsSystemTimeConfigDate_Type.__name__ = "OctetString"
_CwsSystemTimeConfigDate_Object = MibTableColumn
cwsSystemTimeConfigDate = _CwsSystemTimeConfigDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 7, 1, 2),
    _CwsSystemTimeConfigDate_Type()
)
cwsSystemTimeConfigDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemTimeConfigDate.setStatus("current")


class _CwsSystemTimeConfigTime_Type(OctetString):
    """Custom type cwsSystemTimeConfigTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_CwsSystemTimeConfigTime_Type.__name__ = "OctetString"
_CwsSystemTimeConfigTime_Object = MibTableColumn
cwsSystemTimeConfigTime = _CwsSystemTimeConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 7, 1, 3),
    _CwsSystemTimeConfigTime_Type()
)
cwsSystemTimeConfigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemTimeConfigTime.setStatus("current")
_CwsSystemTimeConfigTimeOffset_Type = Decimal32Len2
_CwsSystemTimeConfigTimeOffset_Object = MibTableColumn
cwsSystemTimeConfigTimeOffset = _CwsSystemTimeConfigTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 7, 1, 4),
    _CwsSystemTimeConfigTimeOffset_Type()
)
cwsSystemTimeConfigTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemTimeConfigTimeOffset.setStatus("current")


class _CwsSystemTimeConfigTimeStamp_Type(Integer32):
    """Custom type cwsSystemTimeConfigTimeStamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("utc", 0),
          ("local", 1))
    )


_CwsSystemTimeConfigTimeStamp_Type.__name__ = "Integer32"
_CwsSystemTimeConfigTimeStamp_Object = MibTableColumn
cwsSystemTimeConfigTimeStamp = _CwsSystemTimeConfigTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 7, 1, 5),
    _CwsSystemTimeConfigTimeStamp_Type()
)
cwsSystemTimeConfigTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemTimeConfigTimeStamp.setStatus("current")


class _CwsSystemTimeConfigLocalDateTime_Type(OctetString):
    """Custom type cwsSystemTimeConfigLocalDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 41),
    )


_CwsSystemTimeConfigLocalDateTime_Type.__name__ = "OctetString"
_CwsSystemTimeConfigLocalDateTime_Object = MibTableColumn
cwsSystemTimeConfigLocalDateTime = _CwsSystemTimeConfigLocalDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 7, 1, 6),
    _CwsSystemTimeConfigLocalDateTime_Type()
)
cwsSystemTimeConfigLocalDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSystemTimeConfigLocalDateTime.setStatus("current")


class _CwsSystemTimeConfigCoordinatedUniversalTime_Type(OctetString):
    """Custom type cwsSystemTimeConfigCoordinatedUniversalTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 41),
    )


_CwsSystemTimeConfigCoordinatedUniversalTime_Type.__name__ = "OctetString"
_CwsSystemTimeConfigCoordinatedUniversalTime_Object = MibTableColumn
cwsSystemTimeConfigCoordinatedUniversalTime = _CwsSystemTimeConfigCoordinatedUniversalTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 7, 1, 7),
    _CwsSystemTimeConfigCoordinatedUniversalTime_Type()
)
cwsSystemTimeConfigCoordinatedUniversalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSystemTimeConfigCoordinatedUniversalTime.setStatus("current")


class _CwsSystemTimeConfigSystemUptime_Type(OctetString):
    """Custom type cwsSystemTimeConfigSystemUptime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_CwsSystemTimeConfigSystemUptime_Type.__name__ = "OctetString"
_CwsSystemTimeConfigSystemUptime_Object = MibTableColumn
cwsSystemTimeConfigSystemUptime = _CwsSystemTimeConfigSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 7, 1, 8),
    _CwsSystemTimeConfigSystemUptime_Type()
)
cwsSystemTimeConfigSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSystemTimeConfigSystemUptime.setStatus("current")
_CwsSystemServerConfigTable_Object = MibTable
cwsSystemServerConfigTable = _CwsSystemServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 8)
)
if mibBuilder.loadTexts:
    cwsSystemServerConfigTable.setStatus("current")
_CwsSystemServerConfigEntry_Object = MibTableRow
cwsSystemServerConfigEntry = _CwsSystemServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 8, 1)
)
cwsSystemServerConfigEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemServerConfigTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemServerConfigEntry.setStatus("current")


class _CwsSystemServerConfigTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemServerConfigTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemServerConfigTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemServerConfigTableSnmpKey_Object = MibTableColumn
cwsSystemServerConfigTableSnmpKey = _CwsSystemServerConfigTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 8, 1, 1),
    _CwsSystemServerConfigTableSnmpKey_Type()
)
cwsSystemServerConfigTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemServerConfigTableSnmpKey.setStatus("current")
_CwsSystemServerConfigSftpServerState_Type = EnabledDisabledEnum
_CwsSystemServerConfigSftpServerState_Object = MibTableColumn
cwsSystemServerConfigSftpServerState = _CwsSystemServerConfigSftpServerState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 8, 1, 2),
    _CwsSystemServerConfigSftpServerState_Type()
)
cwsSystemServerConfigSftpServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemServerConfigSftpServerState.setStatus("current")
_CwsSystemServerConfigWebServerState_Type = EnabledDisabledEnum
_CwsSystemServerConfigWebServerState_Object = MibTableColumn
cwsSystemServerConfigWebServerState = _CwsSystemServerConfigWebServerState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 8, 1, 3),
    _CwsSystemServerConfigWebServerState_Type()
)
cwsSystemServerConfigWebServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemServerConfigWebServerState.setStatus("current")
_CwsSystemServerConfigNetconfServerState_Type = EnabledDisabledEnum
_CwsSystemServerConfigNetconfServerState_Object = MibTableColumn
cwsSystemServerConfigNetconfServerState = _CwsSystemServerConfigNetconfServerState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 8, 1, 4),
    _CwsSystemServerConfigNetconfServerState_Type()
)
cwsSystemServerConfigNetconfServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemServerConfigNetconfServerState.setStatus("current")
_CwsSystemServerConfigRestconfServerState_Type = EnabledDisabledEnum
_CwsSystemServerConfigRestconfServerState_Object = MibTableColumn
cwsSystemServerConfigRestconfServerState = _CwsSystemServerConfigRestconfServerState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 8, 1, 5),
    _CwsSystemServerConfigRestconfServerState_Type()
)
cwsSystemServerConfigRestconfServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemServerConfigRestconfServerState.setStatus("current")
_CwsSystemXftpConfigTable_Object = MibTable
cwsSystemXftpConfigTable = _CwsSystemXftpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 9)
)
if mibBuilder.loadTexts:
    cwsSystemXftpConfigTable.setStatus("current")
_CwsSystemXftpConfigEntry_Object = MibTableRow
cwsSystemXftpConfigEntry = _CwsSystemXftpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 9, 1)
)
cwsSystemXftpConfigEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemXftpConfigTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemXftpConfigEntry.setStatus("current")


class _CwsSystemXftpConfigTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemXftpConfigTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemXftpConfigTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemXftpConfigTableSnmpKey_Object = MibTableColumn
cwsSystemXftpConfigTableSnmpKey = _CwsSystemXftpConfigTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 9, 1, 1),
    _CwsSystemXftpConfigTableSnmpKey_Type()
)
cwsSystemXftpConfigTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemXftpConfigTableSnmpKey.setStatus("current")


class _CwsSystemXftpConfigMode_Type(Integer32):
    """Custom type cwsSystemXftpConfigMode based on Integer32"""
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
          ("tftp", 1),
          ("ftp", 2),
          ("sftp", 3),
          ("scp", 4))
    )


_CwsSystemXftpConfigMode_Type.__name__ = "Integer32"
_CwsSystemXftpConfigMode_Object = MibTableColumn
cwsSystemXftpConfigMode = _CwsSystemXftpConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 9, 1, 2),
    _CwsSystemXftpConfigMode_Type()
)
cwsSystemXftpConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSystemXftpConfigMode.setStatus("current")
_CwsSystemTftpTable_Object = MibTable
cwsSystemTftpTable = _CwsSystemTftpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 10)
)
if mibBuilder.loadTexts:
    cwsSystemTftpTable.setStatus("current")
_CwsSystemTftpEntry_Object = MibTableRow
cwsSystemTftpEntry = _CwsSystemTftpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 10, 1)
)
cwsSystemTftpEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemTftpTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemTftpEntry.setStatus("current")


class _CwsSystemTftpTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemTftpTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemTftpTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemTftpTableSnmpKey_Object = MibTableColumn
cwsSystemTftpTableSnmpKey = _CwsSystemTftpTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 10, 1, 1),
    _CwsSystemTftpTableSnmpKey_Type()
)
cwsSystemTftpTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemTftpTableSnmpKey.setStatus("current")
_CwsSystemTftpConfigHostName_Type = StringMaxl64
_CwsSystemTftpConfigHostName_Object = MibTableColumn
cwsSystemTftpConfigHostName = _CwsSystemTftpConfigHostName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 10, 1, 2),
    _CwsSystemTftpConfigHostName_Type()
)
cwsSystemTftpConfigHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemTftpConfigHostName.setStatus("current")
_CwsSystemTftpDhcpHostName_Type = StringMaxl64
_CwsSystemTftpDhcpHostName_Object = MibTableColumn
cwsSystemTftpDhcpHostName = _CwsSystemTftpDhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 10, 1, 3),
    _CwsSystemTftpDhcpHostName_Type()
)
cwsSystemTftpDhcpHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemTftpDhcpHostName.setStatus("current")
_CwsSystemTftpCurrentHostName_Type = StringMaxl64
_CwsSystemTftpCurrentHostName_Object = MibTableColumn
cwsSystemTftpCurrentHostName = _CwsSystemTftpCurrentHostName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 10, 1, 4),
    _CwsSystemTftpCurrentHostName_Type()
)
cwsSystemTftpCurrentHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemTftpCurrentHostName.setStatus("current")
_CwsSystemFtpTable_Object = MibTable
cwsSystemFtpTable = _CwsSystemFtpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 11)
)
if mibBuilder.loadTexts:
    cwsSystemFtpTable.setStatus("current")
_CwsSystemFtpEntry_Object = MibTableRow
cwsSystemFtpEntry = _CwsSystemFtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 11, 1)
)
cwsSystemFtpEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemFtpTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemFtpEntry.setStatus("current")


class _CwsSystemFtpTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemFtpTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemFtpTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemFtpTableSnmpKey_Object = MibTableColumn
cwsSystemFtpTableSnmpKey = _CwsSystemFtpTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 11, 1, 1),
    _CwsSystemFtpTableSnmpKey_Type()
)
cwsSystemFtpTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemFtpTableSnmpKey.setStatus("current")
_CwsSystemFtpHostName_Type = StringMaxl64
_CwsSystemFtpHostName_Object = MibTableColumn
cwsSystemFtpHostName = _CwsSystemFtpHostName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 11, 1, 2),
    _CwsSystemFtpHostName_Type()
)
cwsSystemFtpHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemFtpHostName.setStatus("current")
_CwsSystemFtpUserName_Type = StringMaxl32
_CwsSystemFtpUserName_Object = MibTableColumn
cwsSystemFtpUserName = _CwsSystemFtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 11, 1, 3),
    _CwsSystemFtpUserName_Type()
)
cwsSystemFtpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemFtpUserName.setStatus("current")
_CwsSystemFtpPassword_Type = StringMaxl128
_CwsSystemFtpPassword_Object = MibTableColumn
cwsSystemFtpPassword = _CwsSystemFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 11, 1, 4),
    _CwsSystemFtpPassword_Type()
)
cwsSystemFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemFtpPassword.setStatus("current")
_CwsSystemFtpSecret_Type = StringMaxl256
_CwsSystemFtpSecret_Object = MibTableColumn
cwsSystemFtpSecret = _CwsSystemFtpSecret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 11, 1, 5),
    _CwsSystemFtpSecret_Type()
)
cwsSystemFtpSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemFtpSecret.setStatus("current")
_CwsSystemSftpTable_Object = MibTable
cwsSystemSftpTable = _CwsSystemSftpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 12)
)
if mibBuilder.loadTexts:
    cwsSystemSftpTable.setStatus("current")
_CwsSystemSftpEntry_Object = MibTableRow
cwsSystemSftpEntry = _CwsSystemSftpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 12, 1)
)
cwsSystemSftpEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemSftpTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemSftpEntry.setStatus("current")


class _CwsSystemSftpTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemSftpTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemSftpTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemSftpTableSnmpKey_Object = MibTableColumn
cwsSystemSftpTableSnmpKey = _CwsSystemSftpTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 12, 1, 1),
    _CwsSystemSftpTableSnmpKey_Type()
)
cwsSystemSftpTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemSftpTableSnmpKey.setStatus("current")
_CwsSystemSftpHostName_Type = StringMaxl64
_CwsSystemSftpHostName_Object = MibTableColumn
cwsSystemSftpHostName = _CwsSystemSftpHostName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 12, 1, 2),
    _CwsSystemSftpHostName_Type()
)
cwsSystemSftpHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemSftpHostName.setStatus("current")
_CwsSystemSftpUserName_Type = StringMaxl32
_CwsSystemSftpUserName_Object = MibTableColumn
cwsSystemSftpUserName = _CwsSystemSftpUserName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 12, 1, 3),
    _CwsSystemSftpUserName_Type()
)
cwsSystemSftpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemSftpUserName.setStatus("current")
_CwsSystemSftpPassword_Type = StringMaxl128
_CwsSystemSftpPassword_Object = MibTableColumn
cwsSystemSftpPassword = _CwsSystemSftpPassword_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 12, 1, 4),
    _CwsSystemSftpPassword_Type()
)
cwsSystemSftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemSftpPassword.setStatus("current")
_CwsSystemSftpSecret_Type = StringMaxl256
_CwsSystemSftpSecret_Object = MibTableColumn
cwsSystemSftpSecret = _CwsSystemSftpSecret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 12, 1, 5),
    _CwsSystemSftpSecret_Type()
)
cwsSystemSftpSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemSftpSecret.setStatus("current")
_CwsSystemGlobalProvisioningTable_Object = MibTable
cwsSystemGlobalProvisioningTable = _CwsSystemGlobalProvisioningTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 13)
)
if mibBuilder.loadTexts:
    cwsSystemGlobalProvisioningTable.setStatus("current")
_CwsSystemGlobalProvisioningEntry_Object = MibTableRow
cwsSystemGlobalProvisioningEntry = _CwsSystemGlobalProvisioningEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 13, 1)
)
cwsSystemGlobalProvisioningEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemGlobalProvisioningTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemGlobalProvisioningEntry.setStatus("current")


class _CwsSystemGlobalProvisioningTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemGlobalProvisioningTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemGlobalProvisioningTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemGlobalProvisioningTableSnmpKey_Object = MibTableColumn
cwsSystemGlobalProvisioningTableSnmpKey = _CwsSystemGlobalProvisioningTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 13, 1, 1),
    _CwsSystemGlobalProvisioningTableSnmpKey_Type()
)
cwsSystemGlobalProvisioningTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemGlobalProvisioningTableSnmpKey.setStatus("current")
_CwsSystemGlobalProvisioningLowPowerMode_Type = EnabledDisabledEnum
_CwsSystemGlobalProvisioningLowPowerMode_Object = MibTableColumn
cwsSystemGlobalProvisioningLowPowerMode = _CwsSystemGlobalProvisioningLowPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 13, 1, 2),
    _CwsSystemGlobalProvisioningLowPowerMode_Type()
)
cwsSystemGlobalProvisioningLowPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemGlobalProvisioningLowPowerMode.setStatus("current")
_CwsSystemGlobalProvisioningLampTest_Type = EnabledDisabledEnum
_CwsSystemGlobalProvisioningLampTest_Object = MibTableColumn
cwsSystemGlobalProvisioningLampTest = _CwsSystemGlobalProvisioningLampTest_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 13, 1, 3),
    _CwsSystemGlobalProvisioningLampTest_Type()
)
cwsSystemGlobalProvisioningLampTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemGlobalProvisioningLampTest.setStatus("obsolete")
_CwsSystemGlobalProvisioningResetToFactoryDefaultButton_Type = EnabledDisabledEnum
_CwsSystemGlobalProvisioningResetToFactoryDefaultButton_Object = MibTableColumn
cwsSystemGlobalProvisioningResetToFactoryDefaultButton = _CwsSystemGlobalProvisioningResetToFactoryDefaultButton_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 13, 1, 4),
    _CwsSystemGlobalProvisioningResetToFactoryDefaultButton_Type()
)
cwsSystemGlobalProvisioningResetToFactoryDefaultButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemGlobalProvisioningResetToFactoryDefaultButton.setStatus("obsolete")
_CwsSystemGlobalProvisioningFcsErrorForwarding_Type = TruthValue
_CwsSystemGlobalProvisioningFcsErrorForwarding_Object = MibTableColumn
cwsSystemGlobalProvisioningFcsErrorForwarding = _CwsSystemGlobalProvisioningFcsErrorForwarding_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 13, 1, 5),
    _CwsSystemGlobalProvisioningFcsErrorForwarding_Type()
)
cwsSystemGlobalProvisioningFcsErrorForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemGlobalProvisioningFcsErrorForwarding.setStatus("current")
_CwsSystemGlobalProvisioningChassisFunctionality_Type = StringMaxl16
_CwsSystemGlobalProvisioningChassisFunctionality_Object = MibTableColumn
cwsSystemGlobalProvisioningChassisFunctionality = _CwsSystemGlobalProvisioningChassisFunctionality_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 13, 1, 6),
    _CwsSystemGlobalProvisioningChassisFunctionality_Type()
)
cwsSystemGlobalProvisioningChassisFunctionality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemGlobalProvisioningChassisFunctionality.setStatus("current")
_CwsSystemFrontDisplayTable_Object = MibTable
cwsSystemFrontDisplayTable = _CwsSystemFrontDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 14)
)
if mibBuilder.loadTexts:
    cwsSystemFrontDisplayTable.setStatus("current")
_CwsSystemFrontDisplayEntry_Object = MibTableRow
cwsSystemFrontDisplayEntry = _CwsSystemFrontDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 14, 1)
)
cwsSystemFrontDisplayEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemFrontDisplayTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemFrontDisplayEntry.setStatus("current")


class _CwsSystemFrontDisplayTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemFrontDisplayTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemFrontDisplayTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemFrontDisplayTableSnmpKey_Object = MibTableColumn
cwsSystemFrontDisplayTableSnmpKey = _CwsSystemFrontDisplayTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 14, 1, 1),
    _CwsSystemFrontDisplayTableSnmpKey_Type()
)
cwsSystemFrontDisplayTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemFrontDisplayTableSnmpKey.setStatus("current")
_CwsSystemFrontDisplayAdminState_Type = EnabledDisabledEnum
_CwsSystemFrontDisplayAdminState_Object = MibTableColumn
cwsSystemFrontDisplayAdminState = _CwsSystemFrontDisplayAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 14, 1, 2),
    _CwsSystemFrontDisplayAdminState_Type()
)
cwsSystemFrontDisplayAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemFrontDisplayAdminState.setStatus("current")
_CwsSystemFrontDisplayScreensaverState_Type = EnabledDisabledEnum
_CwsSystemFrontDisplayScreensaverState_Object = MibTableColumn
cwsSystemFrontDisplayScreensaverState = _CwsSystemFrontDisplayScreensaverState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 14, 1, 3),
    _CwsSystemFrontDisplayScreensaverState_Type()
)
cwsSystemFrontDisplayScreensaverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemFrontDisplayScreensaverState.setStatus("current")
_CwsSystemFrontDisplayScreensaverTimeout_Type = Unsigned32
_CwsSystemFrontDisplayScreensaverTimeout_Object = MibTableColumn
cwsSystemFrontDisplayScreensaverTimeout = _CwsSystemFrontDisplayScreensaverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 14, 1, 4),
    _CwsSystemFrontDisplayScreensaverTimeout_Type()
)
cwsSystemFrontDisplayScreensaverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemFrontDisplayScreensaverTimeout.setStatus("current")
_CwsSystemFrontDisplayInputButtonState_Type = EnabledDisabledEnum
_CwsSystemFrontDisplayInputButtonState_Object = MibTableColumn
cwsSystemFrontDisplayInputButtonState = _CwsSystemFrontDisplayInputButtonState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 14, 1, 5),
    _CwsSystemFrontDisplayInputButtonState_Type()
)
cwsSystemFrontDisplayInputButtonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemFrontDisplayInputButtonState.setStatus("current")
_CwsSystemFrontDisplayUserMessageState_Type = EnabledDisabledEnum
_CwsSystemFrontDisplayUserMessageState_Object = MibTableColumn
cwsSystemFrontDisplayUserMessageState = _CwsSystemFrontDisplayUserMessageState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 14, 1, 6),
    _CwsSystemFrontDisplayUserMessageState_Type()
)
cwsSystemFrontDisplayUserMessageState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemFrontDisplayUserMessageState.setStatus("obsolete")


class _CwsSystemFrontDisplayUserMessage_Type(OctetString):
    """Custom type cwsSystemFrontDisplayUserMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 144),
    )


_CwsSystemFrontDisplayUserMessage_Type.__name__ = "OctetString"
_CwsSystemFrontDisplayUserMessage_Object = MibTableColumn
cwsSystemFrontDisplayUserMessage = _CwsSystemFrontDisplayUserMessage_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 14, 1, 7),
    _CwsSystemFrontDisplayUserMessage_Type()
)
cwsSystemFrontDisplayUserMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemFrontDisplayUserMessage.setStatus("current")
_CwsSystemLineConfigTable_Object = MibTable
cwsSystemLineConfigTable = _CwsSystemLineConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 15)
)
if mibBuilder.loadTexts:
    cwsSystemLineConfigTable.setStatus("current")
_CwsSystemLineConfigEntry_Object = MibTableRow
cwsSystemLineConfigEntry = _CwsSystemLineConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 15, 1)
)
cwsSystemLineConfigEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemLineConfigTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemLineConfigEntry.setStatus("current")


class _CwsSystemLineConfigTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemLineConfigTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemLineConfigTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemLineConfigTableSnmpKey_Object = MibTableColumn
cwsSystemLineConfigTableSnmpKey = _CwsSystemLineConfigTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 15, 1, 1),
    _CwsSystemLineConfigTableSnmpKey_Type()
)
cwsSystemLineConfigTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemLineConfigTableSnmpKey.setStatus("current")
_CwsSystemLineConfigBandPlan_Type = BandplanEnum
_CwsSystemLineConfigBandPlan_Object = MibTableColumn
cwsSystemLineConfigBandPlan = _CwsSystemLineConfigBandPlan_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 15, 1, 2),
    _CwsSystemLineConfigBandPlan_Type()
)
cwsSystemLineConfigBandPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemLineConfigBandPlan.setStatus("current")
_CwsSystemLineConfigLineProtection_Type = LineProtectionEnum
_CwsSystemLineConfigLineProtection_Object = MibTableColumn
cwsSystemLineConfigLineProtection = _CwsSystemLineConfigLineProtection_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 15, 1, 3),
    _CwsSystemLineConfigLineProtection_Type()
)
cwsSystemLineConfigLineProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemLineConfigLineProtection.setStatus("current")
_CwsSystemLampFlashTestTable_Object = MibTable
cwsSystemLampFlashTestTable = _CwsSystemLampFlashTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 16)
)
if mibBuilder.loadTexts:
    cwsSystemLampFlashTestTable.setStatus("current")
_CwsSystemLampFlashTestEntry_Object = MibTableRow
cwsSystemLampFlashTestEntry = _CwsSystemLampFlashTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 16, 1)
)
cwsSystemLampFlashTestEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemLampFlashTestTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemLampFlashTestEntry.setStatus("current")


class _CwsSystemLampFlashTestTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemLampFlashTestTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemLampFlashTestTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemLampFlashTestTableSnmpKey_Object = MibTableColumn
cwsSystemLampFlashTestTableSnmpKey = _CwsSystemLampFlashTestTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 16, 1, 1),
    _CwsSystemLampFlashTestTableSnmpKey_Type()
)
cwsSystemLampFlashTestTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemLampFlashTestTableSnmpKey.setStatus("current")
_CwsSystemLampFlashTestOperationalState_Type = EnabledDisabledEnum
_CwsSystemLampFlashTestOperationalState_Object = MibTableColumn
cwsSystemLampFlashTestOperationalState = _CwsSystemLampFlashTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 16, 1, 2),
    _CwsSystemLampFlashTestOperationalState_Type()
)
cwsSystemLampFlashTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSystemLampFlashTestOperationalState.setStatus("current")
_CwsSystemLampFlashTestMode_Type = LampModeEnum
_CwsSystemLampFlashTestMode_Object = MibTableColumn
cwsSystemLampFlashTestMode = _CwsSystemLampFlashTestMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 16, 1, 3),
    _CwsSystemLampFlashTestMode_Type()
)
cwsSystemLampFlashTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSystemLampFlashTestMode.setStatus("current")
_CwsSystemLampFlashTestTargetType_Type = LampTargetTypeEnum
_CwsSystemLampFlashTestTargetType_Object = MibTableColumn
cwsSystemLampFlashTestTargetType = _CwsSystemLampFlashTestTargetType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 16, 1, 4),
    _CwsSystemLampFlashTestTargetType_Type()
)
cwsSystemLampFlashTestTargetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemLampFlashTestTargetType.setStatus("current")
_CwsSystemLampFlashTestTimeout_Type = Unsigned32
_CwsSystemLampFlashTestTimeout_Object = MibTableColumn
cwsSystemLampFlashTestTimeout = _CwsSystemLampFlashTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 16, 1, 5),
    _CwsSystemLampFlashTestTimeout_Type()
)
cwsSystemLampFlashTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemLampFlashTestTimeout.setStatus("current")


class _CwsSystemLampFlashTestPorts_Type(Bits):
    """Custom type cwsSystemLampFlashTestPorts based on Bits"""
    namedValues = NamedValues(
        *(("port1", 0),
          ("port2", 1),
          ("port3", 2),
          ("port4", 3),
          ("port5", 4),
          ("port6", 5),
          ("port7", 6),
          ("port8", 7),
          ("port9", 8),
          ("port10", 9),
          ("port11", 10),
          ("port12", 11))
    )

_CwsSystemLampFlashTestPorts_Type.__name__ = "Bits"
_CwsSystemLampFlashTestPorts_Object = MibTableColumn
cwsSystemLampFlashTestPorts = _CwsSystemLampFlashTestPorts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 16, 1, 6),
    _CwsSystemLampFlashTestPorts_Type()
)
cwsSystemLampFlashTestPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemLampFlashTestPorts.setStatus("current")
_CwsSystemRootTable_Object = MibTable
cwsSystemRootTable = _CwsSystemRootTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 18)
)
if mibBuilder.loadTexts:
    cwsSystemRootTable.setStatus("current")
_CwsSystemRootEntry_Object = MibTableRow
cwsSystemRootEntry = _CwsSystemRootEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 18, 1)
)
cwsSystemRootEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemRootTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemRootEntry.setStatus("current")


class _CwsSystemRootTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemRootTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemRootTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemRootTableSnmpKey_Object = MibTableColumn
cwsSystemRootTableSnmpKey = _CwsSystemRootTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 18, 1, 1),
    _CwsSystemRootTableSnmpKey_Type()
)
cwsSystemRootTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemRootTableSnmpKey.setStatus("current")
_CwsSystemRootPassword_Type = StringMaxl128
_CwsSystemRootPassword_Object = MibTableColumn
cwsSystemRootPassword = _CwsSystemRootPassword_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 18, 1, 2),
    _CwsSystemRootPassword_Type()
)
cwsSystemRootPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSystemRootPassword.setStatus("current")
_CwsSystemScpTable_Object = MibTable
cwsSystemScpTable = _CwsSystemScpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 19)
)
if mibBuilder.loadTexts:
    cwsSystemScpTable.setStatus("current")
_CwsSystemScpEntry_Object = MibTableRow
cwsSystemScpEntry = _CwsSystemScpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 19, 1)
)
cwsSystemScpEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemScpTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemScpEntry.setStatus("current")


class _CwsSystemScpTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemScpTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemScpTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemScpTableSnmpKey_Object = MibTableColumn
cwsSystemScpTableSnmpKey = _CwsSystemScpTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 19, 1, 1),
    _CwsSystemScpTableSnmpKey_Type()
)
cwsSystemScpTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemScpTableSnmpKey.setStatus("current")
_CwsSystemScpHostName_Type = StringMaxl64
_CwsSystemScpHostName_Object = MibTableColumn
cwsSystemScpHostName = _CwsSystemScpHostName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 19, 1, 2),
    _CwsSystemScpHostName_Type()
)
cwsSystemScpHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemScpHostName.setStatus("current")
_CwsSystemScpUserName_Type = StringMaxl32
_CwsSystemScpUserName_Object = MibTableColumn
cwsSystemScpUserName = _CwsSystemScpUserName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 19, 1, 3),
    _CwsSystemScpUserName_Type()
)
cwsSystemScpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemScpUserName.setStatus("current")
_CwsSystemScpPassword_Type = StringMaxl128
_CwsSystemScpPassword_Object = MibTableColumn
cwsSystemScpPassword = _CwsSystemScpPassword_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 19, 1, 4),
    _CwsSystemScpPassword_Type()
)
cwsSystemScpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemScpPassword.setStatus("current")
_CwsSystemScpSecret_Type = StringMaxl256
_CwsSystemScpSecret_Object = MibTableColumn
cwsSystemScpSecret = _CwsSystemScpSecret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 19, 1, 5),
    _CwsSystemScpSecret_Type()
)
cwsSystemScpSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSystemScpSecret.setStatus("current")
_CwsSystemDhcpTable_Object = MibTable
cwsSystemDhcpTable = _CwsSystemDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 21)
)
if mibBuilder.loadTexts:
    cwsSystemDhcpTable.setStatus("current")
_CwsSystemDhcpEntry_Object = MibTableRow
cwsSystemDhcpEntry = _CwsSystemDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 21, 1)
)
cwsSystemDhcpEntry.setIndexNames(
    (0, "CIENA-WS-SYSTEM-MIB", "cwsSystemDhcpTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSystemDhcpEntry.setStatus("current")


class _CwsSystemDhcpTableSnmpKey_Type(Integer32):
    """Custom type cwsSystemDhcpTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSystemDhcpTableSnmpKey_Type.__name__ = "Integer32"
_CwsSystemDhcpTableSnmpKey_Object = MibTableColumn
cwsSystemDhcpTableSnmpKey = _CwsSystemDhcpTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 21, 1, 1),
    _CwsSystemDhcpTableSnmpKey_Type()
)
cwsSystemDhcpTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSystemDhcpTableSnmpKey.setStatus("current")
_CwsSystemDhcpAdminState_Type = EnabledDisabledEnum
_CwsSystemDhcpAdminState_Object = MibTableColumn
cwsSystemDhcpAdminState = _CwsSystemDhcpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 21, 1, 2),
    _CwsSystemDhcpAdminState_Type()
)
cwsSystemDhcpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSystemDhcpAdminState.setStatus("current")

# Managed Objects groups

cienaWsSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 2, 1, 1)
)
cienaWsSystemGroup.setObjects(
      *(("CIENA-WS-SYSTEM-MIB", "cwsSystemSiteId"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemSiteName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemSiteDescription"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemSiteLatitude"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemSiteLongitude"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemSiteAddress"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemGroupId"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemGroupName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemGroupDescription"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemMemberId"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemMemberName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemMemberDescription"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemMemberFrameIdentification"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemMemberRackUnitNumber"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemHostNameCurrentHostName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemHostNameConfigHostName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemHostNameDhcpHostName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemTimeConfigDate"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemTimeConfigTime"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemTimeConfigTimeOffset"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemTimeConfigTimeStamp"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemTimeConfigLocalDateTime"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemTimeConfigCoordinatedUniversalTime"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemTimeConfigSystemUptime"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemServerConfigSftpServerState"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemServerConfigWebServerState"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemServerConfigNetconfServerState"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemServerConfigRestconfServerState"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemDhcpAdminState"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemXftpConfigMode"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemTftpConfigHostName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemTftpDhcpHostName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemTftpCurrentHostName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemFtpHostName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemFtpUserName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemFtpPassword"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemFtpSecret"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemSftpHostName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemSftpUserName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemSftpPassword"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemSftpSecret"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemScpHostName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemScpUserName"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemScpPassword"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemScpSecret"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemGlobalProvisioningLowPowerMode"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemGlobalProvisioningLampTest"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemGlobalProvisioningResetToFactoryDefaultButton"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemGlobalProvisioningFcsErrorForwarding"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemGlobalProvisioningChassisFunctionality"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemFrontDisplayAdminState"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemFrontDisplayScreensaverState"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemFrontDisplayScreensaverTimeout"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemFrontDisplayInputButtonState"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemFrontDisplayUserMessageState"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemFrontDisplayUserMessage"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemLineConfigBandPlan"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemLineConfigLineProtection"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemLampFlashTestOperationalState"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemLampFlashTestMode"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemLampFlashTestTargetType"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemLampFlashTestTimeout"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemLampFlashTestPorts"),
        ("CIENA-WS-SYSTEM-MIB", "cwsSystemRootPassword"))
)
if mibBuilder.loadTexts:
    cienaWsSystemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 12, 2, 2, 1)
)
cienaWsSystemCompliance.setObjects(
    ("CIENA-WS-SYSTEM-MIB", "cienaWsSystemGroup")
)
if mibBuilder.loadTexts:
    cienaWsSystemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-SYSTEM-MIB",
    **{"BandplanEnum": BandplanEnum,
       "Decimal32Len2": Decimal32Len2,
       "Decimal32Len5": Decimal32Len5,
       "LampModeEnum": LampModeEnum,
       "LampTargetTypeEnum": LampTargetTypeEnum,
       "LineProtectionEnum": LineProtectionEnum,
       "cienaWsSystemMIB": cienaWsSystemMIB,
       "cienaWsSystemObjects": cienaWsSystemObjects,
       "cienaWsSystemConformance": cienaWsSystemConformance,
       "cienaWsSystemGroups": cienaWsSystemGroups,
       "cienaWsSystemGroup": cienaWsSystemGroup,
       "cienaWsSystemCompliances": cienaWsSystemCompliances,
       "cienaWsSystemCompliance": cienaWsSystemCompliance,
       "cwsSystemSiteTable": cwsSystemSiteTable,
       "cwsSystemSiteEntry": cwsSystemSiteEntry,
       "cwsSystemSiteTableSnmpKey": cwsSystemSiteTableSnmpKey,
       "cwsSystemSiteId": cwsSystemSiteId,
       "cwsSystemSiteName": cwsSystemSiteName,
       "cwsSystemSiteDescription": cwsSystemSiteDescription,
       "cwsSystemSiteLatitude": cwsSystemSiteLatitude,
       "cwsSystemSiteLongitude": cwsSystemSiteLongitude,
       "cwsSystemSiteAddress": cwsSystemSiteAddress,
       "cwsSystemGroupTable": cwsSystemGroupTable,
       "cwsSystemGroupEntry": cwsSystemGroupEntry,
       "cwsSystemGroupTableSnmpKey": cwsSystemGroupTableSnmpKey,
       "cwsSystemGroupId": cwsSystemGroupId,
       "cwsSystemGroupName": cwsSystemGroupName,
       "cwsSystemGroupDescription": cwsSystemGroupDescription,
       "cwsSystemMemberTable": cwsSystemMemberTable,
       "cwsSystemMemberEntry": cwsSystemMemberEntry,
       "cwsSystemMemberTableSnmpKey": cwsSystemMemberTableSnmpKey,
       "cwsSystemMemberId": cwsSystemMemberId,
       "cwsSystemMemberName": cwsSystemMemberName,
       "cwsSystemMemberDescription": cwsSystemMemberDescription,
       "cwsSystemMemberFrameIdentification": cwsSystemMemberFrameIdentification,
       "cwsSystemMemberRackUnitNumber": cwsSystemMemberRackUnitNumber,
       "cwsSystemHostNameTable": cwsSystemHostNameTable,
       "cwsSystemHostNameEntry": cwsSystemHostNameEntry,
       "cwsSystemHostNameTableSnmpKey": cwsSystemHostNameTableSnmpKey,
       "cwsSystemHostNameCurrentHostName": cwsSystemHostNameCurrentHostName,
       "cwsSystemHostNameConfigHostName": cwsSystemHostNameConfigHostName,
       "cwsSystemHostNameDhcpHostName": cwsSystemHostNameDhcpHostName,
       "cwsSystemTimeConfigTable": cwsSystemTimeConfigTable,
       "cwsSystemTimeConfigEntry": cwsSystemTimeConfigEntry,
       "cwsSystemTimeConfigTableSnmpKey": cwsSystemTimeConfigTableSnmpKey,
       "cwsSystemTimeConfigDate": cwsSystemTimeConfigDate,
       "cwsSystemTimeConfigTime": cwsSystemTimeConfigTime,
       "cwsSystemTimeConfigTimeOffset": cwsSystemTimeConfigTimeOffset,
       "cwsSystemTimeConfigTimeStamp": cwsSystemTimeConfigTimeStamp,
       "cwsSystemTimeConfigLocalDateTime": cwsSystemTimeConfigLocalDateTime,
       "cwsSystemTimeConfigCoordinatedUniversalTime": cwsSystemTimeConfigCoordinatedUniversalTime,
       "cwsSystemTimeConfigSystemUptime": cwsSystemTimeConfigSystemUptime,
       "cwsSystemServerConfigTable": cwsSystemServerConfigTable,
       "cwsSystemServerConfigEntry": cwsSystemServerConfigEntry,
       "cwsSystemServerConfigTableSnmpKey": cwsSystemServerConfigTableSnmpKey,
       "cwsSystemServerConfigSftpServerState": cwsSystemServerConfigSftpServerState,
       "cwsSystemServerConfigWebServerState": cwsSystemServerConfigWebServerState,
       "cwsSystemServerConfigNetconfServerState": cwsSystemServerConfigNetconfServerState,
       "cwsSystemServerConfigRestconfServerState": cwsSystemServerConfigRestconfServerState,
       "cwsSystemXftpConfigTable": cwsSystemXftpConfigTable,
       "cwsSystemXftpConfigEntry": cwsSystemXftpConfigEntry,
       "cwsSystemXftpConfigTableSnmpKey": cwsSystemXftpConfigTableSnmpKey,
       "cwsSystemXftpConfigMode": cwsSystemXftpConfigMode,
       "cwsSystemTftpTable": cwsSystemTftpTable,
       "cwsSystemTftpEntry": cwsSystemTftpEntry,
       "cwsSystemTftpTableSnmpKey": cwsSystemTftpTableSnmpKey,
       "cwsSystemTftpConfigHostName": cwsSystemTftpConfigHostName,
       "cwsSystemTftpDhcpHostName": cwsSystemTftpDhcpHostName,
       "cwsSystemTftpCurrentHostName": cwsSystemTftpCurrentHostName,
       "cwsSystemFtpTable": cwsSystemFtpTable,
       "cwsSystemFtpEntry": cwsSystemFtpEntry,
       "cwsSystemFtpTableSnmpKey": cwsSystemFtpTableSnmpKey,
       "cwsSystemFtpHostName": cwsSystemFtpHostName,
       "cwsSystemFtpUserName": cwsSystemFtpUserName,
       "cwsSystemFtpPassword": cwsSystemFtpPassword,
       "cwsSystemFtpSecret": cwsSystemFtpSecret,
       "cwsSystemSftpTable": cwsSystemSftpTable,
       "cwsSystemSftpEntry": cwsSystemSftpEntry,
       "cwsSystemSftpTableSnmpKey": cwsSystemSftpTableSnmpKey,
       "cwsSystemSftpHostName": cwsSystemSftpHostName,
       "cwsSystemSftpUserName": cwsSystemSftpUserName,
       "cwsSystemSftpPassword": cwsSystemSftpPassword,
       "cwsSystemSftpSecret": cwsSystemSftpSecret,
       "cwsSystemGlobalProvisioningTable": cwsSystemGlobalProvisioningTable,
       "cwsSystemGlobalProvisioningEntry": cwsSystemGlobalProvisioningEntry,
       "cwsSystemGlobalProvisioningTableSnmpKey": cwsSystemGlobalProvisioningTableSnmpKey,
       "cwsSystemGlobalProvisioningLowPowerMode": cwsSystemGlobalProvisioningLowPowerMode,
       "cwsSystemGlobalProvisioningLampTest": cwsSystemGlobalProvisioningLampTest,
       "cwsSystemGlobalProvisioningResetToFactoryDefaultButton": cwsSystemGlobalProvisioningResetToFactoryDefaultButton,
       "cwsSystemGlobalProvisioningFcsErrorForwarding": cwsSystemGlobalProvisioningFcsErrorForwarding,
       "cwsSystemGlobalProvisioningChassisFunctionality": cwsSystemGlobalProvisioningChassisFunctionality,
       "cwsSystemFrontDisplayTable": cwsSystemFrontDisplayTable,
       "cwsSystemFrontDisplayEntry": cwsSystemFrontDisplayEntry,
       "cwsSystemFrontDisplayTableSnmpKey": cwsSystemFrontDisplayTableSnmpKey,
       "cwsSystemFrontDisplayAdminState": cwsSystemFrontDisplayAdminState,
       "cwsSystemFrontDisplayScreensaverState": cwsSystemFrontDisplayScreensaverState,
       "cwsSystemFrontDisplayScreensaverTimeout": cwsSystemFrontDisplayScreensaverTimeout,
       "cwsSystemFrontDisplayInputButtonState": cwsSystemFrontDisplayInputButtonState,
       "cwsSystemFrontDisplayUserMessageState": cwsSystemFrontDisplayUserMessageState,
       "cwsSystemFrontDisplayUserMessage": cwsSystemFrontDisplayUserMessage,
       "cwsSystemLineConfigTable": cwsSystemLineConfigTable,
       "cwsSystemLineConfigEntry": cwsSystemLineConfigEntry,
       "cwsSystemLineConfigTableSnmpKey": cwsSystemLineConfigTableSnmpKey,
       "cwsSystemLineConfigBandPlan": cwsSystemLineConfigBandPlan,
       "cwsSystemLineConfigLineProtection": cwsSystemLineConfigLineProtection,
       "cwsSystemLampFlashTestTable": cwsSystemLampFlashTestTable,
       "cwsSystemLampFlashTestEntry": cwsSystemLampFlashTestEntry,
       "cwsSystemLampFlashTestTableSnmpKey": cwsSystemLampFlashTestTableSnmpKey,
       "cwsSystemLampFlashTestOperationalState": cwsSystemLampFlashTestOperationalState,
       "cwsSystemLampFlashTestMode": cwsSystemLampFlashTestMode,
       "cwsSystemLampFlashTestTargetType": cwsSystemLampFlashTestTargetType,
       "cwsSystemLampFlashTestTimeout": cwsSystemLampFlashTestTimeout,
       "cwsSystemLampFlashTestPorts": cwsSystemLampFlashTestPorts,
       "cwsSystemRootTable": cwsSystemRootTable,
       "cwsSystemRootEntry": cwsSystemRootEntry,
       "cwsSystemRootTableSnmpKey": cwsSystemRootTableSnmpKey,
       "cwsSystemRootPassword": cwsSystemRootPassword,
       "cwsSystemScpTable": cwsSystemScpTable,
       "cwsSystemScpEntry": cwsSystemScpEntry,
       "cwsSystemScpTableSnmpKey": cwsSystemScpTableSnmpKey,
       "cwsSystemScpHostName": cwsSystemScpHostName,
       "cwsSystemScpUserName": cwsSystemScpUserName,
       "cwsSystemScpPassword": cwsSystemScpPassword,
       "cwsSystemScpSecret": cwsSystemScpSecret,
       "cwsSystemDhcpTable": cwsSystemDhcpTable,
       "cwsSystemDhcpEntry": cwsSystemDhcpEntry,
       "cwsSystemDhcpTableSnmpKey": cwsSystemDhcpTableSnmpKey,
       "cwsSystemDhcpAdminState": cwsSystemDhcpAdminState}
)
