# SNMP MIB module (CIENA-WS-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-NOTIFICATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:07 2025
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

(cienaWsNotifications,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsNotifications")

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

cienaWsNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 3)
)
if mibBuilder.loadTexts:
    cienaWsNotificationMIB.setRevisions(
        ("2018-01-15 00:00",
         "2016-11-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayString32(TextualConvention, OctetString):
    status = "current"
    displayHint = "32t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_WsAlarmNotificationSiteId_Type = Unsigned32
_WsAlarmNotificationSiteId_Object = MibScalar
wsAlarmNotificationSiteId = _WsAlarmNotificationSiteId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11, 1),
    _WsAlarmNotificationSiteId_Type()
)
wsAlarmNotificationSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlarmNotificationSiteId.setStatus("current")
_WsAlarmNotificationGroupId_Type = Unsigned32
_WsAlarmNotificationGroupId_Object = MibScalar
wsAlarmNotificationGroupId = _WsAlarmNotificationGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11, 2),
    _WsAlarmNotificationGroupId_Type()
)
wsAlarmNotificationGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlarmNotificationGroupId.setStatus("current")
_WsAlarmNotificationMemberId_Type = Unsigned32
_WsAlarmNotificationMemberId_Object = MibScalar
wsAlarmNotificationMemberId = _WsAlarmNotificationMemberId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11, 3),
    _WsAlarmNotificationMemberId_Type()
)
wsAlarmNotificationMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlarmNotificationMemberId.setStatus("current")


class _WsAlarmNotificationInstanceId_Type(Unsigned32):
    """Custom type wsAlarmNotificationInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WsAlarmNotificationInstanceId_Type.__name__ = "Unsigned32"
_WsAlarmNotificationInstanceId_Object = MibScalar
wsAlarmNotificationInstanceId = _WsAlarmNotificationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11, 4),
    _WsAlarmNotificationInstanceId_Type()
)
wsAlarmNotificationInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlarmNotificationInstanceId.setStatus("current")
_WsAlarmNotificationDateAndTime_Type = DisplayString32
_WsAlarmNotificationDateAndTime_Object = MibScalar
wsAlarmNotificationDateAndTime = _WsAlarmNotificationDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11, 5),
    _WsAlarmNotificationDateAndTime_Type()
)
wsAlarmNotificationDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlarmNotificationDateAndTime.setStatus("current")
_WsAlarmNotificationTableId_Type = Unsigned32
_WsAlarmNotificationTableId_Object = MibScalar
wsAlarmNotificationTableId = _WsAlarmNotificationTableId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11, 6),
    _WsAlarmNotificationTableId_Type()
)
wsAlarmNotificationTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlarmNotificationTableId.setStatus("current")


class _WsAlarmNotificationSeverity_Type(Integer32):
    """Custom type wsAlarmNotificationSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6),
          ("info", 8))
    )


_WsAlarmNotificationSeverity_Type.__name__ = "Integer32"
_WsAlarmNotificationSeverity_Object = MibScalar
wsAlarmNotificationSeverity = _WsAlarmNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11, 7),
    _WsAlarmNotificationSeverity_Type()
)
wsAlarmNotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlarmNotificationSeverity.setStatus("current")
_WsAlarmNotificationInstance_Type = DisplayString32
_WsAlarmNotificationInstance_Object = MibScalar
wsAlarmNotificationInstance = _WsAlarmNotificationInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11, 8),
    _WsAlarmNotificationInstance_Type()
)
wsAlarmNotificationInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlarmNotificationInstance.setStatus("current")
_WsAlarmNotificationDescription_Type = DisplayString32
_WsAlarmNotificationDescription_Object = MibScalar
wsAlarmNotificationDescription = _WsAlarmNotificationDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11, 9),
    _WsAlarmNotificationDescription_Type()
)
wsAlarmNotificationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlarmNotificationDescription.setStatus("current")


class _WsAlarmNotificationActiveStatus_Type(Integer32):
    """Custom type wsAlarmNotificationActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("intermittent", 3))
    )


_WsAlarmNotificationActiveStatus_Type.__name__ = "Integer32"
_WsAlarmNotificationActiveStatus_Object = MibScalar
wsAlarmNotificationActiveStatus = _WsAlarmNotificationActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11, 10),
    _WsAlarmNotificationActiveStatus_Type()
)
wsAlarmNotificationActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlarmNotificationActiveStatus.setStatus("current")


class _WsAlarmNotificationEntityType_Type(Integer32):
    """Custom type wsAlarmNotificationEntityType based on Integer32"""
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
        *(("notApplicable", 0),
          ("other", 1),
          ("clientPort", 2),
          ("linePort", 3))
    )


_WsAlarmNotificationEntityType_Type.__name__ = "Integer32"
_WsAlarmNotificationEntityType_Object = MibScalar
wsAlarmNotificationEntityType = _WsAlarmNotificationEntityType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11, 11),
    _WsAlarmNotificationEntityType_Type()
)
wsAlarmNotificationEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlarmNotificationEntityType.setStatus("current")
_WsLinkStateAlarmNotificationSiteId_Type = Unsigned32
_WsLinkStateAlarmNotificationSiteId_Object = MibScalar
wsLinkStateAlarmNotificationSiteId = _WsLinkStateAlarmNotificationSiteId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 1),
    _WsLinkStateAlarmNotificationSiteId_Type()
)
wsLinkStateAlarmNotificationSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationSiteId.setStatus("current")
_WsLinkStateAlarmNotificationGroupId_Type = Unsigned32
_WsLinkStateAlarmNotificationGroupId_Object = MibScalar
wsLinkStateAlarmNotificationGroupId = _WsLinkStateAlarmNotificationGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 2),
    _WsLinkStateAlarmNotificationGroupId_Type()
)
wsLinkStateAlarmNotificationGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationGroupId.setStatus("current")
_WsLinkStateAlarmNotificationMemberId_Type = Unsigned32
_WsLinkStateAlarmNotificationMemberId_Object = MibScalar
wsLinkStateAlarmNotificationMemberId = _WsLinkStateAlarmNotificationMemberId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 3),
    _WsLinkStateAlarmNotificationMemberId_Type()
)
wsLinkStateAlarmNotificationMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationMemberId.setStatus("current")


class _WsLinkStateAlarmNotificationInstanceId_Type(Unsigned32):
    """Custom type wsLinkStateAlarmNotificationInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WsLinkStateAlarmNotificationInstanceId_Type.__name__ = "Unsigned32"
_WsLinkStateAlarmNotificationInstanceId_Object = MibScalar
wsLinkStateAlarmNotificationInstanceId = _WsLinkStateAlarmNotificationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 4),
    _WsLinkStateAlarmNotificationInstanceId_Type()
)
wsLinkStateAlarmNotificationInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationInstanceId.setStatus("current")
_WsLinkStateAlarmNotificationDateAndTime_Type = DisplayString32
_WsLinkStateAlarmNotificationDateAndTime_Object = MibScalar
wsLinkStateAlarmNotificationDateAndTime = _WsLinkStateAlarmNotificationDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 5),
    _WsLinkStateAlarmNotificationDateAndTime_Type()
)
wsLinkStateAlarmNotificationDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationDateAndTime.setStatus("current")


class _WsLinkStateAlarmNotificationSeverity_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6),
          ("info", 8))
    )


_WsLinkStateAlarmNotificationSeverity_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationSeverity_Object = MibScalar
wsLinkStateAlarmNotificationSeverity = _WsLinkStateAlarmNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 7),
    _WsLinkStateAlarmNotificationSeverity_Type()
)
wsLinkStateAlarmNotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationSeverity.setStatus("current")
_WsLinkStateAlarmNotificationInstance_Type = DisplayString32
_WsLinkStateAlarmNotificationInstance_Object = MibScalar
wsLinkStateAlarmNotificationInstance = _WsLinkStateAlarmNotificationInstance_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 8),
    _WsLinkStateAlarmNotificationInstance_Type()
)
wsLinkStateAlarmNotificationInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationInstance.setStatus("current")
_WsLinkStateAlarmNotificationDescription_Type = DisplayString32
_WsLinkStateAlarmNotificationDescription_Object = MibScalar
wsLinkStateAlarmNotificationDescription = _WsLinkStateAlarmNotificationDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 9),
    _WsLinkStateAlarmNotificationDescription_Type()
)
wsLinkStateAlarmNotificationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationDescription.setStatus("current")
_WsLinkStateAlarmNotificationPtpDefects_ObjectIdentity = ObjectIdentity
wsLinkStateAlarmNotificationPtpDefects = _WsLinkStateAlarmNotificationPtpDefects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 10)
)
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationPtpDefects.setStatus("current")


class _WsLinkStateAlarmNotificationPtpRxLos_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationPtpRxLos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationPtpRxLos_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationPtpRxLos_Object = MibScalar
wsLinkStateAlarmNotificationPtpRxLos = _WsLinkStateAlarmNotificationPtpRxLos_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 10, 1),
    _WsLinkStateAlarmNotificationPtpRxLos_Type()
)
wsLinkStateAlarmNotificationPtpRxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationPtpRxLos.setStatus("current")


class _WsLinkStateAlarmNotificationPtpRxLol_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationPtpRxLol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationPtpRxLol_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationPtpRxLol_Object = MibScalar
wsLinkStateAlarmNotificationPtpRxLol = _WsLinkStateAlarmNotificationPtpRxLol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 10, 2),
    _WsLinkStateAlarmNotificationPtpRxLol_Type()
)
wsLinkStateAlarmNotificationPtpRxLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationPtpRxLol.setStatus("current")


class _WsLinkStateAlarmNotificationPtpTxLos_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationPtpTxLos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationPtpTxLos_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationPtpTxLos_Object = MibScalar
wsLinkStateAlarmNotificationPtpTxLos = _WsLinkStateAlarmNotificationPtpTxLos_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 10, 3),
    _WsLinkStateAlarmNotificationPtpTxLos_Type()
)
wsLinkStateAlarmNotificationPtpTxLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationPtpTxLos.setStatus("current")


class _WsLinkStateAlarmNotificationPtpTxLol_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationPtpTxLol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationPtpTxLol_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationPtpTxLol_Object = MibScalar
wsLinkStateAlarmNotificationPtpTxLol = _WsLinkStateAlarmNotificationPtpTxLol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 10, 4),
    _WsLinkStateAlarmNotificationPtpTxLol_Type()
)
wsLinkStateAlarmNotificationPtpTxLol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationPtpTxLol.setStatus("current")
_WsLinkStateAlarmNotificationEthDefects_ObjectIdentity = ObjectIdentity
wsLinkStateAlarmNotificationEthDefects = _WsLinkStateAlarmNotificationEthDefects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 11)
)
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationEthDefects.setStatus("current")


class _WsLinkStateAlarmNotificationEthPcsHighBer_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationEthPcsHighBer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationEthPcsHighBer_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationEthPcsHighBer_Object = MibScalar
wsLinkStateAlarmNotificationEthPcsHighBer = _WsLinkStateAlarmNotificationEthPcsHighBer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 11, 1),
    _WsLinkStateAlarmNotificationEthPcsHighBer_Type()
)
wsLinkStateAlarmNotificationEthPcsHighBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationEthPcsHighBer.setStatus("current")


class _WsLinkStateAlarmNotificationEthPcsLoam_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationEthPcsLoam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationEthPcsLoam_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationEthPcsLoam_Object = MibScalar
wsLinkStateAlarmNotificationEthPcsLoam = _WsLinkStateAlarmNotificationEthPcsLoam_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 11, 2),
    _WsLinkStateAlarmNotificationEthPcsLoam_Type()
)
wsLinkStateAlarmNotificationEthPcsLoam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationEthPcsLoam.setStatus("current")


class _WsLinkStateAlarmNotificationEthPcsLobl_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationEthPcsLobl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationEthPcsLobl_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationEthPcsLobl_Object = MibScalar
wsLinkStateAlarmNotificationEthPcsLobl = _WsLinkStateAlarmNotificationEthPcsLobl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 11, 3),
    _WsLinkStateAlarmNotificationEthPcsLobl_Type()
)
wsLinkStateAlarmNotificationEthPcsLobl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationEthPcsLobl.setStatus("current")


class _WsLinkStateAlarmNotificationEthRsLinkDown_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationEthRsLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationEthRsLinkDown_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationEthRsLinkDown_Object = MibScalar
wsLinkStateAlarmNotificationEthRsLinkDown = _WsLinkStateAlarmNotificationEthRsLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 11, 4),
    _WsLinkStateAlarmNotificationEthRsLinkDown_Type()
)
wsLinkStateAlarmNotificationEthRsLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationEthRsLinkDown.setStatus("current")


class _WsLinkStateAlarmNotificationEthRsLf_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationEthRsLf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationEthRsLf_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationEthRsLf_Object = MibScalar
wsLinkStateAlarmNotificationEthRsLf = _WsLinkStateAlarmNotificationEthRsLf_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 11, 5),
    _WsLinkStateAlarmNotificationEthRsLf_Type()
)
wsLinkStateAlarmNotificationEthRsLf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationEthRsLf.setStatus("current")


class _WsLinkStateAlarmNotificationEthRsRf_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationEthRsRf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationEthRsRf_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationEthRsRf_Object = MibScalar
wsLinkStateAlarmNotificationEthRsRf = _WsLinkStateAlarmNotificationEthRsRf_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 11, 6),
    _WsLinkStateAlarmNotificationEthRsRf_Type()
)
wsLinkStateAlarmNotificationEthRsRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationEthRsRf.setStatus("current")


class _WsLinkStateAlarmNotificationEthFecLossSync_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationEthFecLossSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationEthFecLossSync_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationEthFecLossSync_Object = MibScalar
wsLinkStateAlarmNotificationEthFecLossSync = _WsLinkStateAlarmNotificationEthFecLossSync_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 11, 7),
    _WsLinkStateAlarmNotificationEthFecLossSync_Type()
)
wsLinkStateAlarmNotificationEthFecLossSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationEthFecLossSync.setStatus("current")


class _WsLinkStateAlarmNotificationEthPmaSool_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationEthPmaSool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationEthPmaSool_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationEthPmaSool_Object = MibScalar
wsLinkStateAlarmNotificationEthPmaSool = _WsLinkStateAlarmNotificationEthPmaSool_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 11, 8),
    _WsLinkStateAlarmNotificationEthPmaSool_Type()
)
wsLinkStateAlarmNotificationEthPmaSool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationEthPmaSool.setStatus("current")
_WsLinkStateAlarmNotificationOtuDefects_ObjectIdentity = ObjectIdentity
wsLinkStateAlarmNotificationOtuDefects = _WsLinkStateAlarmNotificationOtuDefects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 12)
)
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOtuDefects.setStatus("current")


class _WsLinkStateAlarmNotificationOtuLoc_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOtuLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOtuLoc_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOtuLoc_Object = MibScalar
wsLinkStateAlarmNotificationOtuLoc = _WsLinkStateAlarmNotificationOtuLoc_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 12, 1),
    _WsLinkStateAlarmNotificationOtuLoc_Type()
)
wsLinkStateAlarmNotificationOtuLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOtuLoc.setStatus("current")


class _WsLinkStateAlarmNotificationOtuFreqOor_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOtuFreqOor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOtuFreqOor_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOtuFreqOor_Object = MibScalar
wsLinkStateAlarmNotificationOtuFreqOor = _WsLinkStateAlarmNotificationOtuFreqOor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 12, 2),
    _WsLinkStateAlarmNotificationOtuFreqOor_Type()
)
wsLinkStateAlarmNotificationOtuFreqOor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOtuFreqOor.setStatus("current")


class _WsLinkStateAlarmNotificationOtuLof_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOtuLof based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOtuLof_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOtuLof_Object = MibScalar
wsLinkStateAlarmNotificationOtuLof = _WsLinkStateAlarmNotificationOtuLof_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 12, 3),
    _WsLinkStateAlarmNotificationOtuLof_Type()
)
wsLinkStateAlarmNotificationOtuLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOtuLof.setStatus("current")


class _WsLinkStateAlarmNotificationOtuPreFecSf_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOtuPreFecSf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOtuPreFecSf_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOtuPreFecSf_Object = MibScalar
wsLinkStateAlarmNotificationOtuPreFecSf = _WsLinkStateAlarmNotificationOtuPreFecSf_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 12, 4),
    _WsLinkStateAlarmNotificationOtuPreFecSf_Type()
)
wsLinkStateAlarmNotificationOtuPreFecSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOtuPreFecSf.setStatus("current")


class _WsLinkStateAlarmNotificationOtuPreFecSd_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOtuPreFecSd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOtuPreFecSd_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOtuPreFecSd_Object = MibScalar
wsLinkStateAlarmNotificationOtuPreFecSd = _WsLinkStateAlarmNotificationOtuPreFecSd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 12, 5),
    _WsLinkStateAlarmNotificationOtuPreFecSd_Type()
)
wsLinkStateAlarmNotificationOtuPreFecSd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOtuPreFecSd.setStatus("current")


class _WsLinkStateAlarmNotificationOtuLom_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOtuLom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOtuLom_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOtuLom_Object = MibScalar
wsLinkStateAlarmNotificationOtuLom = _WsLinkStateAlarmNotificationOtuLom_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 12, 6),
    _WsLinkStateAlarmNotificationOtuLom_Type()
)
wsLinkStateAlarmNotificationOtuLom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOtuLom.setStatus("current")


class _WsLinkStateAlarmNotificationOtuBdi_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOtuBdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOtuBdi_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOtuBdi_Object = MibScalar
wsLinkStateAlarmNotificationOtuBdi = _WsLinkStateAlarmNotificationOtuBdi_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 12, 7),
    _WsLinkStateAlarmNotificationOtuBdi_Type()
)
wsLinkStateAlarmNotificationOtuBdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOtuBdi.setStatus("current")


class _WsLinkStateAlarmNotificationOtuTtiMismatch_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOtuTtiMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOtuTtiMismatch_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOtuTtiMismatch_Object = MibScalar
wsLinkStateAlarmNotificationOtuTtiMismatch = _WsLinkStateAlarmNotificationOtuTtiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 12, 8),
    _WsLinkStateAlarmNotificationOtuTtiMismatch_Type()
)
wsLinkStateAlarmNotificationOtuTtiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOtuTtiMismatch.setStatus("current")
_WsLinkStateAlarmNotificationOduDefects_ObjectIdentity = ObjectIdentity
wsLinkStateAlarmNotificationOduDefects = _WsLinkStateAlarmNotificationOduDefects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 13)
)
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOduDefects.setStatus("current")


class _WsLinkStateAlarmNotificationOduOci_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOduOci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOduOci_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOduOci_Object = MibScalar
wsLinkStateAlarmNotificationOduOci = _WsLinkStateAlarmNotificationOduOci_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 13, 1),
    _WsLinkStateAlarmNotificationOduOci_Type()
)
wsLinkStateAlarmNotificationOduOci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOduOci.setStatus("current")


class _WsLinkStateAlarmNotificationOduAis_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOduAis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOduAis_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOduAis_Object = MibScalar
wsLinkStateAlarmNotificationOduAis = _WsLinkStateAlarmNotificationOduAis_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 13, 2),
    _WsLinkStateAlarmNotificationOduAis_Type()
)
wsLinkStateAlarmNotificationOduAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOduAis.setStatus("current")


class _WsLinkStateAlarmNotificationOduLck_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOduLck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOduLck_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOduLck_Object = MibScalar
wsLinkStateAlarmNotificationOduLck = _WsLinkStateAlarmNotificationOduLck_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 13, 3),
    _WsLinkStateAlarmNotificationOduLck_Type()
)
wsLinkStateAlarmNotificationOduLck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOduLck.setStatus("current")


class _WsLinkStateAlarmNotificationOduSf_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOduSf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOduSf_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOduSf_Object = MibScalar
wsLinkStateAlarmNotificationOduSf = _WsLinkStateAlarmNotificationOduSf_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 13, 4),
    _WsLinkStateAlarmNotificationOduSf_Type()
)
wsLinkStateAlarmNotificationOduSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOduSf.setStatus("current")


class _WsLinkStateAlarmNotificationOduSd_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOduSd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOduSd_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOduSd_Object = MibScalar
wsLinkStateAlarmNotificationOduSd = _WsLinkStateAlarmNotificationOduSd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 13, 5),
    _WsLinkStateAlarmNotificationOduSd_Type()
)
wsLinkStateAlarmNotificationOduSd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOduSd.setStatus("current")


class _WsLinkStateAlarmNotificationOduTtiMismatch_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOduTtiMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOduTtiMismatch_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOduTtiMismatch_Object = MibScalar
wsLinkStateAlarmNotificationOduTtiMismatch = _WsLinkStateAlarmNotificationOduTtiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 13, 6),
    _WsLinkStateAlarmNotificationOduTtiMismatch_Type()
)
wsLinkStateAlarmNotificationOduTtiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOduTtiMismatch.setStatus("current")


class _WsLinkStateAlarmNotificationOduBdi_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOduBdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOduBdi_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOduBdi_Object = MibScalar
wsLinkStateAlarmNotificationOduBdi = _WsLinkStateAlarmNotificationOduBdi_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 13, 7),
    _WsLinkStateAlarmNotificationOduBdi_Type()
)
wsLinkStateAlarmNotificationOduBdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOduBdi.setStatus("current")


class _WsLinkStateAlarmNotificationOduPtiMismatch_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOduPtiMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOduPtiMismatch_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOduPtiMismatch_Object = MibScalar
wsLinkStateAlarmNotificationOduPtiMismatch = _WsLinkStateAlarmNotificationOduPtiMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 13, 8),
    _WsLinkStateAlarmNotificationOduPtiMismatch_Type()
)
wsLinkStateAlarmNotificationOduPtiMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOduPtiMismatch.setStatus("current")


class _WsLinkStateAlarmNotificationOduFeClientSf_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOduFeClientSf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOduFeClientSf_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOduFeClientSf_Object = MibScalar
wsLinkStateAlarmNotificationOduFeClientSf = _WsLinkStateAlarmNotificationOduFeClientSf_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 13, 9),
    _WsLinkStateAlarmNotificationOduFeClientSf_Type()
)
wsLinkStateAlarmNotificationOduFeClientSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOduFeClientSf.setStatus("current")


class _WsLinkStateAlarmNotificationOduSkewOor_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationOduSkewOor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_WsLinkStateAlarmNotificationOduSkewOor_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationOduSkewOor_Object = MibScalar
wsLinkStateAlarmNotificationOduSkewOor = _WsLinkStateAlarmNotificationOduSkewOor_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 13, 10),
    _WsLinkStateAlarmNotificationOduSkewOor_Type()
)
wsLinkStateAlarmNotificationOduSkewOor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationOduSkewOor.setStatus("current")


class _WsLinkStateAlarmNotificationEntityType_Type(Integer32):
    """Custom type wsLinkStateAlarmNotificationEntityType based on Integer32"""
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
        *(("notApplicable", 0),
          ("other", 1),
          ("clientPort", 2),
          ("linePort", 3))
    )


_WsLinkStateAlarmNotificationEntityType_Type.__name__ = "Integer32"
_WsLinkStateAlarmNotificationEntityType_Object = MibScalar
wsLinkStateAlarmNotificationEntityType = _WsLinkStateAlarmNotificationEntityType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12, 14),
    _WsLinkStateAlarmNotificationEntityType_Type()
)
wsLinkStateAlarmNotificationEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotificationEntityType.setStatus("current")

# Managed Objects groups


# Notification objects

wsAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 11)
)
wsAlarmNotification.setObjects(
      *(("CIENA-WS-NOTIFICATION-MIB", "wsAlarmNotificationSiteId"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsAlarmNotificationGroupId"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsAlarmNotificationMemberId"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsAlarmNotificationInstanceId"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsAlarmNotificationDateAndTime"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsAlarmNotificationTableId"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsAlarmNotificationSeverity"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsAlarmNotificationInstance"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsAlarmNotificationDescription"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsAlarmNotificationActiveStatus"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsAlarmNotificationEntityType"))
)
if mibBuilder.loadTexts:
    wsAlarmNotification.setStatus(
        "current"
    )

wsLinkStateAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 12)
)
wsLinkStateAlarmNotification.setObjects(
      *(("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationSiteId"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationGroupId"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationMemberId"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationInstanceId"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationDateAndTime"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationSeverity"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationInstance"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationDescription"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationPtpRxLos"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationPtpRxLol"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationPtpTxLos"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationPtpTxLol"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationEthFecLossSync"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationEthEBer"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationEthRsLf"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationEthRsRf"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationEthPcsLobl"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationEthPcsLoam"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationEthPcsLol"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationEthRsLinkDown"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOtuLoc"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOtuFreqOor"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOtuLof"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOtuPreFecSf"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOtuPreFecSd"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOtuLom"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOtuBdi"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOtuTtiMismatch"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOduOci"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOduAis"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOduLck"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOduSf"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOduSd"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOduTtiMismatch"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOduBdi"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOduPtiMismatch"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOduFeClientSf"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationOduSkewOor"),
        ("CIENA-WS-NOTIFICATION-MIB", "wsLinkStateAlarmNotificationEntityType"))
)
if mibBuilder.loadTexts:
    wsLinkStateAlarmNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-NOTIFICATION-MIB",
    **{"DisplayString32": DisplayString32,
       "cienaWsNotificationMIB": cienaWsNotificationMIB,
       "wsAlarmNotification": wsAlarmNotification,
       "wsAlarmNotificationSiteId": wsAlarmNotificationSiteId,
       "wsAlarmNotificationGroupId": wsAlarmNotificationGroupId,
       "wsAlarmNotificationMemberId": wsAlarmNotificationMemberId,
       "wsAlarmNotificationInstanceId": wsAlarmNotificationInstanceId,
       "wsAlarmNotificationDateAndTime": wsAlarmNotificationDateAndTime,
       "wsAlarmNotificationTableId": wsAlarmNotificationTableId,
       "wsAlarmNotificationSeverity": wsAlarmNotificationSeverity,
       "wsAlarmNotificationInstance": wsAlarmNotificationInstance,
       "wsAlarmNotificationDescription": wsAlarmNotificationDescription,
       "wsAlarmNotificationActiveStatus": wsAlarmNotificationActiveStatus,
       "wsAlarmNotificationEntityType": wsAlarmNotificationEntityType,
       "wsLinkStateAlarmNotification": wsLinkStateAlarmNotification,
       "wsLinkStateAlarmNotificationSiteId": wsLinkStateAlarmNotificationSiteId,
       "wsLinkStateAlarmNotificationGroupId": wsLinkStateAlarmNotificationGroupId,
       "wsLinkStateAlarmNotificationMemberId": wsLinkStateAlarmNotificationMemberId,
       "wsLinkStateAlarmNotificationInstanceId": wsLinkStateAlarmNotificationInstanceId,
       "wsLinkStateAlarmNotificationDateAndTime": wsLinkStateAlarmNotificationDateAndTime,
       "wsLinkStateAlarmNotificationSeverity": wsLinkStateAlarmNotificationSeverity,
       "wsLinkStateAlarmNotificationInstance": wsLinkStateAlarmNotificationInstance,
       "wsLinkStateAlarmNotificationDescription": wsLinkStateAlarmNotificationDescription,
       "wsLinkStateAlarmNotificationPtpDefects": wsLinkStateAlarmNotificationPtpDefects,
       "wsLinkStateAlarmNotificationPtpRxLos": wsLinkStateAlarmNotificationPtpRxLos,
       "wsLinkStateAlarmNotificationPtpRxLol": wsLinkStateAlarmNotificationPtpRxLol,
       "wsLinkStateAlarmNotificationPtpTxLos": wsLinkStateAlarmNotificationPtpTxLos,
       "wsLinkStateAlarmNotificationPtpTxLol": wsLinkStateAlarmNotificationPtpTxLol,
       "wsLinkStateAlarmNotificationEthDefects": wsLinkStateAlarmNotificationEthDefects,
       "wsLinkStateAlarmNotificationEthPcsHighBer": wsLinkStateAlarmNotificationEthPcsHighBer,
       "wsLinkStateAlarmNotificationEthPcsLoam": wsLinkStateAlarmNotificationEthPcsLoam,
       "wsLinkStateAlarmNotificationEthPcsLobl": wsLinkStateAlarmNotificationEthPcsLobl,
       "wsLinkStateAlarmNotificationEthRsLinkDown": wsLinkStateAlarmNotificationEthRsLinkDown,
       "wsLinkStateAlarmNotificationEthRsLf": wsLinkStateAlarmNotificationEthRsLf,
       "wsLinkStateAlarmNotificationEthRsRf": wsLinkStateAlarmNotificationEthRsRf,
       "wsLinkStateAlarmNotificationEthFecLossSync": wsLinkStateAlarmNotificationEthFecLossSync,
       "wsLinkStateAlarmNotificationEthPmaSool": wsLinkStateAlarmNotificationEthPmaSool,
       "wsLinkStateAlarmNotificationOtuDefects": wsLinkStateAlarmNotificationOtuDefects,
       "wsLinkStateAlarmNotificationOtuLoc": wsLinkStateAlarmNotificationOtuLoc,
       "wsLinkStateAlarmNotificationOtuFreqOor": wsLinkStateAlarmNotificationOtuFreqOor,
       "wsLinkStateAlarmNotificationOtuLof": wsLinkStateAlarmNotificationOtuLof,
       "wsLinkStateAlarmNotificationOtuPreFecSf": wsLinkStateAlarmNotificationOtuPreFecSf,
       "wsLinkStateAlarmNotificationOtuPreFecSd": wsLinkStateAlarmNotificationOtuPreFecSd,
       "wsLinkStateAlarmNotificationOtuLom": wsLinkStateAlarmNotificationOtuLom,
       "wsLinkStateAlarmNotificationOtuBdi": wsLinkStateAlarmNotificationOtuBdi,
       "wsLinkStateAlarmNotificationOtuTtiMismatch": wsLinkStateAlarmNotificationOtuTtiMismatch,
       "wsLinkStateAlarmNotificationOduDefects": wsLinkStateAlarmNotificationOduDefects,
       "wsLinkStateAlarmNotificationOduOci": wsLinkStateAlarmNotificationOduOci,
       "wsLinkStateAlarmNotificationOduAis": wsLinkStateAlarmNotificationOduAis,
       "wsLinkStateAlarmNotificationOduLck": wsLinkStateAlarmNotificationOduLck,
       "wsLinkStateAlarmNotificationOduSf": wsLinkStateAlarmNotificationOduSf,
       "wsLinkStateAlarmNotificationOduSd": wsLinkStateAlarmNotificationOduSd,
       "wsLinkStateAlarmNotificationOduTtiMismatch": wsLinkStateAlarmNotificationOduTtiMismatch,
       "wsLinkStateAlarmNotificationOduBdi": wsLinkStateAlarmNotificationOduBdi,
       "wsLinkStateAlarmNotificationOduPtiMismatch": wsLinkStateAlarmNotificationOduPtiMismatch,
       "wsLinkStateAlarmNotificationOduFeClientSf": wsLinkStateAlarmNotificationOduFeClientSf,
       "wsLinkStateAlarmNotificationOduSkewOor": wsLinkStateAlarmNotificationOduSkewOor,
       "wsLinkStateAlarmNotificationEntityType": wsLinkStateAlarmNotificationEntityType}
)
