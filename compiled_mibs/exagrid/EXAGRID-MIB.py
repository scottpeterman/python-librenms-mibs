# SNMP MIB module (EXAGRID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\exagrid\EXAGRID-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:01 2025
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

(InternationalDisplayString,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Exagrid_ObjectIdentity = ObjectIdentity
exagrid = _Exagrid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941)
)
_ExagridTraps_ObjectIdentity = ObjectIdentity
exagridTraps = _ExagridTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 1)
)
_EgEventParams_ObjectIdentity = ObjectIdentity
egEventParams = _EgEventParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 2)
)


class _EgEventParamsName_Type(DisplayString):
    """Custom type egEventParamsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsName_Type.__name__ = "DisplayString"
_EgEventParamsName_Object = MibScalar
egEventParamsName = _EgEventParamsName_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 1),
    _EgEventParamsName_Type()
)
egEventParamsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsName.setStatus("mandatory")


class _EgEventParamsId_Type(DisplayString):
    """Custom type egEventParamsId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsId_Type.__name__ = "DisplayString"
_EgEventParamsId_Object = MibScalar
egEventParamsId = _EgEventParamsId_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 2),
    _EgEventParamsId_Type()
)
egEventParamsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsId.setStatus("mandatory")


class _EgEventParamsCreateTime_Type(DisplayString):
    """Custom type egEventParamsCreateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsCreateTime_Type.__name__ = "DisplayString"
_EgEventParamsCreateTime_Object = MibScalar
egEventParamsCreateTime = _EgEventParamsCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 3),
    _EgEventParamsCreateTime_Type()
)
egEventParamsCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsCreateTime.setStatus("mandatory")


class _EgEventParamsCreateTimeRaw_Type(DisplayString):
    """Custom type egEventParamsCreateTimeRaw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsCreateTimeRaw_Type.__name__ = "DisplayString"
_EgEventParamsCreateTimeRaw_Object = MibScalar
egEventParamsCreateTimeRaw = _EgEventParamsCreateTimeRaw_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 4),
    _EgEventParamsCreateTimeRaw_Type()
)
egEventParamsCreateTimeRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsCreateTimeRaw.setStatus("mandatory")


class _EgEventParamsGridName_Type(DisplayString):
    """Custom type egEventParamsGridName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsGridName_Type.__name__ = "DisplayString"
_EgEventParamsGridName_Object = MibScalar
egEventParamsGridName = _EgEventParamsGridName_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 5),
    _EgEventParamsGridName_Type()
)
egEventParamsGridName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsGridName.setStatus("mandatory")


class _EgEventParamsSiteName_Type(DisplayString):
    """Custom type egEventParamsSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsSiteName_Type.__name__ = "DisplayString"
_EgEventParamsSiteName_Object = MibScalar
egEventParamsSiteName = _EgEventParamsSiteName_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 6),
    _EgEventParamsSiteName_Type()
)
egEventParamsSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsSiteName.setStatus("mandatory")


class _EgEventParamsSiteId_Type(DisplayString):
    """Custom type egEventParamsSiteId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsSiteId_Type.__name__ = "DisplayString"
_EgEventParamsSiteId_Object = MibScalar
egEventParamsSiteId = _EgEventParamsSiteId_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 7),
    _EgEventParamsSiteId_Type()
)
egEventParamsSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsSiteId.setStatus("mandatory")


class _EgEventParamsSeverity_Type(DisplayString):
    """Custom type egEventParamsSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsSeverity_Type.__name__ = "DisplayString"
_EgEventParamsSeverity_Object = MibScalar
egEventParamsSeverity = _EgEventParamsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 8),
    _EgEventParamsSeverity_Type()
)
egEventParamsSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsSeverity.setStatus("mandatory")


class _EgEventParamsDeviceName_Type(DisplayString):
    """Custom type egEventParamsDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsDeviceName_Type.__name__ = "DisplayString"
_EgEventParamsDeviceName_Object = MibScalar
egEventParamsDeviceName = _EgEventParamsDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 9),
    _EgEventParamsDeviceName_Type()
)
egEventParamsDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsDeviceName.setStatus("mandatory")


class _EgEventParamsDeviceId_Type(DisplayString):
    """Custom type egEventParamsDeviceId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsDeviceId_Type.__name__ = "DisplayString"
_EgEventParamsDeviceId_Object = MibScalar
egEventParamsDeviceId = _EgEventParamsDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 10),
    _EgEventParamsDeviceId_Type()
)
egEventParamsDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsDeviceId.setStatus("mandatory")


class _EgEventParamsDeviceSerialNumber_Type(DisplayString):
    """Custom type egEventParamsDeviceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsDeviceSerialNumber_Type.__name__ = "DisplayString"
_EgEventParamsDeviceSerialNumber_Object = MibScalar
egEventParamsDeviceSerialNumber = _EgEventParamsDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 11),
    _EgEventParamsDeviceSerialNumber_Type()
)
egEventParamsDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsDeviceSerialNumber.setStatus("mandatory")


class _EgEventParamsDeviceIp_Type(DisplayString):
    """Custom type egEventParamsDeviceIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsDeviceIp_Type.__name__ = "DisplayString"
_EgEventParamsDeviceIp_Object = MibScalar
egEventParamsDeviceIp = _EgEventParamsDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 12),
    _EgEventParamsDeviceIp_Type()
)
egEventParamsDeviceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsDeviceIp.setStatus("mandatory")


class _EgEventParamsDupCount_Type(DisplayString):
    """Custom type egEventParamsDupCount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsDupCount_Type.__name__ = "DisplayString"
_EgEventParamsDupCount_Object = MibScalar
egEventParamsDupCount = _EgEventParamsDupCount_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 13),
    _EgEventParamsDupCount_Type()
)
egEventParamsDupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsDupCount.setStatus("mandatory")


class _EgEventParamsText_Type(DisplayString):
    """Custom type egEventParamsText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EgEventParamsText_Type.__name__ = "DisplayString"
_EgEventParamsText_Object = MibScalar
egEventParamsText = _EgEventParamsText_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 14),
    _EgEventParamsText_Type()
)
egEventParamsText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsText.setStatus("mandatory")


class _EgEventParamsDetail_Type(InternationalDisplayString):
    """Custom type egEventParamsDetail based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 999),
    )


_EgEventParamsDetail_Type.__name__ = "InternationalDisplayString"
_EgEventParamsDetail_Object = MibScalar
egEventParamsDetail = _EgEventParamsDetail_Object(
    (1, 3, 6, 1, 4, 1, 14941, 2, 15),
    _EgEventParamsDetail_Type()
)
egEventParamsDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egEventParamsDetail.setStatus("mandatory")
_ExagridProductLines_ObjectIdentity = ObjectIdentity
exagridProductLines = _ExagridProductLines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3)
)
_ExagridExX000Series_ObjectIdentity = ObjectIdentity
exagridExX000Series = _ExagridExX000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1)
)
_ExagridExX000_ObjectIdentity = ObjectIdentity
exagridExX000 = _ExagridExX000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 0)
)
_ExagridEx1000_ObjectIdentity = ObjectIdentity
exagridEx1000 = _ExagridEx1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 1)
)
_ExagridEx2000_ObjectIdentity = ObjectIdentity
exagridEx2000 = _ExagridEx2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 2)
)
_ExagridEx3000_ObjectIdentity = ObjectIdentity
exagridEx3000 = _ExagridEx3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 3)
)
_ExagridEx4000_ObjectIdentity = ObjectIdentity
exagridEx4000 = _ExagridEx4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 4)
)
_ExagridEx5000_ObjectIdentity = ObjectIdentity
exagridEx5000 = _ExagridEx5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 5)
)
_ExagridExGW_ObjectIdentity = ObjectIdentity
exagridExGW = _ExagridExGW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 6)
)
_ExagridEx10000E_ObjectIdentity = ObjectIdentity
exagridEx10000E = _ExagridEx10000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 10)
)
_ExagridEx1T_ObjectIdentity = ObjectIdentity
exagridEx1T = _ExagridEx1T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 11)
)
_ExagridEx2T_ObjectIdentity = ObjectIdentity
exagridEx2T = _ExagridEx2T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 12)
)
_ExagridEx3T_ObjectIdentity = ObjectIdentity
exagridEx3T = _ExagridEx3T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 13)
)
_ExagridEx4T_ObjectIdentity = ObjectIdentity
exagridEx4T = _ExagridEx4T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 14)
)
_ExagridEx5T_ObjectIdentity = ObjectIdentity
exagridEx5T = _ExagridEx5T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 15)
)
_ExagridEx7T_ObjectIdentity = ObjectIdentity
exagridEx7T = _ExagridEx7T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 16)
)
_ExagridEx9T_ObjectIdentity = ObjectIdentity
exagridEx9T = _ExagridEx9T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 19)
)
_ExagridEx7S_ObjectIdentity = ObjectIdentity
exagridEx7S = _ExagridEx7S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 26)
)
_ExagridEx9S_ObjectIdentity = ObjectIdentity
exagridEx9S = _ExagridEx9S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 29)
)
_ExagridEx1T2012A_ObjectIdentity = ObjectIdentity
exagridEx1T2012A = _ExagridEx1T2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 31)
)
_ExagridEx2T2012A_ObjectIdentity = ObjectIdentity
exagridEx2T2012A = _ExagridEx2T2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 32)
)
_ExagridEx3T2012A_ObjectIdentity = ObjectIdentity
exagridEx3T2012A = _ExagridEx3T2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 33)
)
_ExagridEx4T2012A_ObjectIdentity = ObjectIdentity
exagridEx4T2012A = _ExagridEx4T2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 34)
)
_ExagridEx5T2012A_ObjectIdentity = ObjectIdentity
exagridEx5T2012A = _ExagridEx5T2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 35)
)
_ExagridEx7T2012A_ObjectIdentity = ObjectIdentity
exagridEx7T2012A = _ExagridEx7T2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 36)
)
_ExagridEx7S2012A_ObjectIdentity = ObjectIdentity
exagridEx7S2012A = _ExagridEx7S2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 46)
)
_ExagridEx10T_ObjectIdentity = ObjectIdentity
exagridEx10T = _ExagridEx10T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 110)
)
_ExagridEx13T_ObjectIdentity = ObjectIdentity
exagridEx13T = _ExagridEx13T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 113)
)
_ExagridEx10S_ObjectIdentity = ObjectIdentity
exagridEx10S = _ExagridEx10S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 210)
)
_ExagridEx13S_ObjectIdentity = ObjectIdentity
exagridEx13S = _ExagridEx13S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 213)
)
_ExagridEx10T2012A_ObjectIdentity = ObjectIdentity
exagridEx10T2012A = _ExagridEx10T2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 310)
)
_ExagridEx13T2012A_ObjectIdentity = ObjectIdentity
exagridEx13T2012A = _ExagridEx13T2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 313)
)
_ExagridEx21T2012A_ObjectIdentity = ObjectIdentity
exagridEx21T2012A = _ExagridEx21T2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 321)
)
_ExagridEx10S2012A_ObjectIdentity = ObjectIdentity
exagridEx10S2012A = _ExagridEx10S2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 410)
)
_ExagridEx13S2012A_ObjectIdentity = ObjectIdentity
exagridEx13S2012A = _ExagridEx13S2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 413)
)
_ExagridEx21S2012A_ObjectIdentity = ObjectIdentity
exagridEx21S2012A = _ExagridEx21S2012A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 3, 1, 421)
)
_ExagridServerData_ObjectIdentity = ObjectIdentity
exagridServerData = _ExagridServerData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 4)
)
_ExagridLandingSpace_ObjectIdentity = ObjectIdentity
exagridLandingSpace = _ExagridLandingSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 4, 1)
)
_EgLandingSpaceConfiguredWholeGigabytes_Type = Gauge32
_EgLandingSpaceConfiguredWholeGigabytes_Object = MibScalar
egLandingSpaceConfiguredWholeGigabytes = _EgLandingSpaceConfiguredWholeGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 1, 1),
    _EgLandingSpaceConfiguredWholeGigabytes_Type()
)
egLandingSpaceConfiguredWholeGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egLandingSpaceConfiguredWholeGigabytes.setStatus("mandatory")
_EgLandingSpaceConfiguredFractionalGigabytes_Type = Gauge32
_EgLandingSpaceConfiguredFractionalGigabytes_Object = MibScalar
egLandingSpaceConfiguredFractionalGigabytes = _EgLandingSpaceConfiguredFractionalGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 1, 2),
    _EgLandingSpaceConfiguredFractionalGigabytes_Type()
)
egLandingSpaceConfiguredFractionalGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egLandingSpaceConfiguredFractionalGigabytes.setStatus("mandatory")
_EgLandingSpaceAvailableWholeGigabytes_Type = Gauge32
_EgLandingSpaceAvailableWholeGigabytes_Object = MibScalar
egLandingSpaceAvailableWholeGigabytes = _EgLandingSpaceAvailableWholeGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 1, 3),
    _EgLandingSpaceAvailableWholeGigabytes_Type()
)
egLandingSpaceAvailableWholeGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egLandingSpaceAvailableWholeGigabytes.setStatus("mandatory")
_EgLandingSpaceAvailableFractionalGigabytes_Type = Gauge32
_EgLandingSpaceAvailableFractionalGigabytes_Object = MibScalar
egLandingSpaceAvailableFractionalGigabytes = _EgLandingSpaceAvailableFractionalGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 1, 4),
    _EgLandingSpaceAvailableFractionalGigabytes_Type()
)
egLandingSpaceAvailableFractionalGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egLandingSpaceAvailableFractionalGigabytes.setStatus("mandatory")
_ExagridRetentionSpace_ObjectIdentity = ObjectIdentity
exagridRetentionSpace = _ExagridRetentionSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 4, 2)
)
_EgRetentionSpaceConfiguredWholeGigabytes_Type = Gauge32
_EgRetentionSpaceConfiguredWholeGigabytes_Object = MibScalar
egRetentionSpaceConfiguredWholeGigabytes = _EgRetentionSpaceConfiguredWholeGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 2, 1),
    _EgRetentionSpaceConfiguredWholeGigabytes_Type()
)
egRetentionSpaceConfiguredWholeGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egRetentionSpaceConfiguredWholeGigabytes.setStatus("mandatory")
_EgRetentionSpaceConfiguredFractionalGigabytes_Type = Gauge32
_EgRetentionSpaceConfiguredFractionalGigabytes_Object = MibScalar
egRetentionSpaceConfiguredFractionalGigabytes = _EgRetentionSpaceConfiguredFractionalGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 2, 2),
    _EgRetentionSpaceConfiguredFractionalGigabytes_Type()
)
egRetentionSpaceConfiguredFractionalGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egRetentionSpaceConfiguredFractionalGigabytes.setStatus("mandatory")
_EgRetentionSpaceAvailableWholeGigabytes_Type = Gauge32
_EgRetentionSpaceAvailableWholeGigabytes_Object = MibScalar
egRetentionSpaceAvailableWholeGigabytes = _EgRetentionSpaceAvailableWholeGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 2, 3),
    _EgRetentionSpaceAvailableWholeGigabytes_Type()
)
egRetentionSpaceAvailableWholeGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egRetentionSpaceAvailableWholeGigabytes.setStatus("mandatory")
_EgRetentionSpaceAvailableFractionalGigabytes_Type = Gauge32
_EgRetentionSpaceAvailableFractionalGigabytes_Object = MibScalar
egRetentionSpaceAvailableFractionalGigabytes = _EgRetentionSpaceAvailableFractionalGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 2, 4),
    _EgRetentionSpaceAvailableFractionalGigabytes_Type()
)
egRetentionSpaceAvailableFractionalGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egRetentionSpaceAvailableFractionalGigabytes.setStatus("mandatory")
_ExagridDeduplicationRatio_ObjectIdentity = ObjectIdentity
exagridDeduplicationRatio = _ExagridDeduplicationRatio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 4, 3)
)
_EgBackupDataAvailableWholeGigabytes_Type = Gauge32
_EgBackupDataAvailableWholeGigabytes_Object = MibScalar
egBackupDataAvailableWholeGigabytes = _EgBackupDataAvailableWholeGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 3, 1),
    _EgBackupDataAvailableWholeGigabytes_Type()
)
egBackupDataAvailableWholeGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egBackupDataAvailableWholeGigabytes.setStatus("mandatory")
_EgBackupDataAvailableFractionalGigabytes_Type = Gauge32
_EgBackupDataAvailableFractionalGigabytes_Object = MibScalar
egBackupDataAvailableFractionalGigabytes = _EgBackupDataAvailableFractionalGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 3, 2),
    _EgBackupDataAvailableFractionalGigabytes_Type()
)
egBackupDataAvailableFractionalGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egBackupDataAvailableFractionalGigabytes.setStatus("mandatory")
_EgBackupDataSpaceConsumedWholeGigabytes_Type = Gauge32
_EgBackupDataSpaceConsumedWholeGigabytes_Object = MibScalar
egBackupDataSpaceConsumedWholeGigabytes = _EgBackupDataSpaceConsumedWholeGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 3, 3),
    _EgBackupDataSpaceConsumedWholeGigabytes_Type()
)
egBackupDataSpaceConsumedWholeGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egBackupDataSpaceConsumedWholeGigabytes.setStatus("mandatory")
_EgBackupDataSpaceConsumedFractionalGigabytes_Type = Gauge32
_EgBackupDataSpaceConsumedFractionalGigabytes_Object = MibScalar
egBackupDataSpaceConsumedFractionalGigabytes = _EgBackupDataSpaceConsumedFractionalGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 3, 4),
    _EgBackupDataSpaceConsumedFractionalGigabytes_Type()
)
egBackupDataSpaceConsumedFractionalGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egBackupDataSpaceConsumedFractionalGigabytes.setStatus("mandatory")
_ExagridPendingDeduplication_ObjectIdentity = ObjectIdentity
exagridPendingDeduplication = _ExagridPendingDeduplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 4, 4)
)
_EgPendingDeduplicationWholeGigabytes_Type = Gauge32
_EgPendingDeduplicationWholeGigabytes_Object = MibScalar
egPendingDeduplicationWholeGigabytes = _EgPendingDeduplicationWholeGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 4, 1),
    _EgPendingDeduplicationWholeGigabytes_Type()
)
egPendingDeduplicationWholeGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egPendingDeduplicationWholeGigabytes.setStatus("mandatory")
_EgPendingDeduplicationFractionalGigabytes_Type = Gauge32
_EgPendingDeduplicationFractionalGigabytes_Object = MibScalar
egPendingDeduplicationFractionalGigabytes = _EgPendingDeduplicationFractionalGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 4, 2),
    _EgPendingDeduplicationFractionalGigabytes_Type()
)
egPendingDeduplicationFractionalGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egPendingDeduplicationFractionalGigabytes.setStatus("mandatory")
_EgPendingDeduplicationAge_Type = TimeTicks
_EgPendingDeduplicationAge_Object = MibScalar
egPendingDeduplicationAge = _EgPendingDeduplicationAge_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 4, 3),
    _EgPendingDeduplicationAge_Type()
)
egPendingDeduplicationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egPendingDeduplicationAge.setStatus("mandatory")
_ExagridPendingReplication_ObjectIdentity = ObjectIdentity
exagridPendingReplication = _ExagridPendingReplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 4, 5)
)
_EgPendingReplicationWholeGigabytes_Type = Gauge32
_EgPendingReplicationWholeGigabytes_Object = MibScalar
egPendingReplicationWholeGigabytes = _EgPendingReplicationWholeGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 5, 1),
    _EgPendingReplicationWholeGigabytes_Type()
)
egPendingReplicationWholeGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egPendingReplicationWholeGigabytes.setStatus("mandatory")
_EgPendingReplicationFractionalGigabytes_Type = Gauge32
_EgPendingReplicationFractionalGigabytes_Object = MibScalar
egPendingReplicationFractionalGigabytes = _EgPendingReplicationFractionalGigabytes_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 5, 2),
    _EgPendingReplicationFractionalGigabytes_Type()
)
egPendingReplicationFractionalGigabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egPendingReplicationFractionalGigabytes.setStatus("mandatory")
_EgPendingReplicationAge_Type = TimeTicks
_EgPendingReplicationAge_Object = MibScalar
egPendingReplicationAge = _EgPendingReplicationAge_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 5, 3),
    _EgPendingReplicationAge_Type()
)
egPendingReplicationAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egPendingReplicationAge.setStatus("mandatory")
_ExagridServerStatus_ObjectIdentity = ObjectIdentity
exagridServerStatus = _ExagridServerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14941, 4, 6)
)
_EgServerAlarmState_Type = Integer32
_EgServerAlarmState_Object = MibScalar
egServerAlarmState = _EgServerAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 14941, 4, 6, 1),
    _EgServerAlarmState_Type()
)
egServerAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egServerAlarmState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

egTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14941, 1, 0, 1)
)
egTrap.setObjects(
      *(("EXAGRID-MIB", "egEventParamsName"),
        ("EXAGRID-MIB", "egEventParamsId"),
        ("EXAGRID-MIB", "egEventParamsCreateTime"),
        ("EXAGRID-MIB", "egEventParamsCreateTimeRaw"),
        ("EXAGRID-MIB", "egEventParamsGridName"),
        ("EXAGRID-MIB", "egEventParamsSiteName"),
        ("EXAGRID-MIB", "egEventParamsSiteId"),
        ("EXAGRID-MIB", "egEventParamsSeverity"),
        ("EXAGRID-MIB", "egEventParamsDeviceName"),
        ("EXAGRID-MIB", "egEventParamsDeviceId"),
        ("EXAGRID-MIB", "egEventParamsDeviceIp"),
        ("EXAGRID-MIB", "egEventParamsDeviceSerialNumber"),
        ("EXAGRID-MIB", "egEventParamsDupCount"),
        ("EXAGRID-MIB", "egEventParamsText"),
        ("EXAGRID-MIB", "egEventParamsDetail"))
)
if mibBuilder.loadTexts:
    egTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXAGRID-MIB",
    **{"exagrid": exagrid,
       "exagridTraps": exagridTraps,
       "egTrap": egTrap,
       "egEventParams": egEventParams,
       "egEventParamsName": egEventParamsName,
       "egEventParamsId": egEventParamsId,
       "egEventParamsCreateTime": egEventParamsCreateTime,
       "egEventParamsCreateTimeRaw": egEventParamsCreateTimeRaw,
       "egEventParamsGridName": egEventParamsGridName,
       "egEventParamsSiteName": egEventParamsSiteName,
       "egEventParamsSiteId": egEventParamsSiteId,
       "egEventParamsSeverity": egEventParamsSeverity,
       "egEventParamsDeviceName": egEventParamsDeviceName,
       "egEventParamsDeviceId": egEventParamsDeviceId,
       "egEventParamsDeviceSerialNumber": egEventParamsDeviceSerialNumber,
       "egEventParamsDeviceIp": egEventParamsDeviceIp,
       "egEventParamsDupCount": egEventParamsDupCount,
       "egEventParamsText": egEventParamsText,
       "egEventParamsDetail": egEventParamsDetail,
       "exagridProductLines": exagridProductLines,
       "exagridExX000Series": exagridExX000Series,
       "exagridExX000": exagridExX000,
       "exagridEx1000": exagridEx1000,
       "exagridEx2000": exagridEx2000,
       "exagridEx3000": exagridEx3000,
       "exagridEx4000": exagridEx4000,
       "exagridEx5000": exagridEx5000,
       "exagridExGW": exagridExGW,
       "exagridEx10000E": exagridEx10000E,
       "exagridEx1T": exagridEx1T,
       "exagridEx2T": exagridEx2T,
       "exagridEx3T": exagridEx3T,
       "exagridEx4T": exagridEx4T,
       "exagridEx5T": exagridEx5T,
       "exagridEx7T": exagridEx7T,
       "exagridEx9T": exagridEx9T,
       "exagridEx7S": exagridEx7S,
       "exagridEx9S": exagridEx9S,
       "exagridEx1T2012A": exagridEx1T2012A,
       "exagridEx2T2012A": exagridEx2T2012A,
       "exagridEx3T2012A": exagridEx3T2012A,
       "exagridEx4T2012A": exagridEx4T2012A,
       "exagridEx5T2012A": exagridEx5T2012A,
       "exagridEx7T2012A": exagridEx7T2012A,
       "exagridEx7S2012A": exagridEx7S2012A,
       "exagridEx10T": exagridEx10T,
       "exagridEx13T": exagridEx13T,
       "exagridEx10S": exagridEx10S,
       "exagridEx13S": exagridEx13S,
       "exagridEx10T2012A": exagridEx10T2012A,
       "exagridEx13T2012A": exagridEx13T2012A,
       "exagridEx21T2012A": exagridEx21T2012A,
       "exagridEx10S2012A": exagridEx10S2012A,
       "exagridEx13S2012A": exagridEx13S2012A,
       "exagridEx21S2012A": exagridEx21S2012A,
       "exagridServerData": exagridServerData,
       "exagridLandingSpace": exagridLandingSpace,
       "egLandingSpaceConfiguredWholeGigabytes": egLandingSpaceConfiguredWholeGigabytes,
       "egLandingSpaceConfiguredFractionalGigabytes": egLandingSpaceConfiguredFractionalGigabytes,
       "egLandingSpaceAvailableWholeGigabytes": egLandingSpaceAvailableWholeGigabytes,
       "egLandingSpaceAvailableFractionalGigabytes": egLandingSpaceAvailableFractionalGigabytes,
       "exagridRetentionSpace": exagridRetentionSpace,
       "egRetentionSpaceConfiguredWholeGigabytes": egRetentionSpaceConfiguredWholeGigabytes,
       "egRetentionSpaceConfiguredFractionalGigabytes": egRetentionSpaceConfiguredFractionalGigabytes,
       "egRetentionSpaceAvailableWholeGigabytes": egRetentionSpaceAvailableWholeGigabytes,
       "egRetentionSpaceAvailableFractionalGigabytes": egRetentionSpaceAvailableFractionalGigabytes,
       "exagridDeduplicationRatio": exagridDeduplicationRatio,
       "egBackupDataAvailableWholeGigabytes": egBackupDataAvailableWholeGigabytes,
       "egBackupDataAvailableFractionalGigabytes": egBackupDataAvailableFractionalGigabytes,
       "egBackupDataSpaceConsumedWholeGigabytes": egBackupDataSpaceConsumedWholeGigabytes,
       "egBackupDataSpaceConsumedFractionalGigabytes": egBackupDataSpaceConsumedFractionalGigabytes,
       "exagridPendingDeduplication": exagridPendingDeduplication,
       "egPendingDeduplicationWholeGigabytes": egPendingDeduplicationWholeGigabytes,
       "egPendingDeduplicationFractionalGigabytes": egPendingDeduplicationFractionalGigabytes,
       "egPendingDeduplicationAge": egPendingDeduplicationAge,
       "exagridPendingReplication": exagridPendingReplication,
       "egPendingReplicationWholeGigabytes": egPendingReplicationWholeGigabytes,
       "egPendingReplicationFractionalGigabytes": egPendingReplicationFractionalGigabytes,
       "egPendingReplicationAge": egPendingReplicationAge,
       "exagridServerStatus": exagridServerStatus,
       "egServerAlarmState": egServerAlarmState}
)
